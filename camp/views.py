from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.utils import timezone
from .models import Place, Comment, Family, Rating, Visited, Add, Phoneno
from .forms import PlaceForm, CommentForm, FamilyForm, RatingForm, VisitedForm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
import smtplib


from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AboutView(TemplateView):
    template_name = 'camp/about.html'
   
class PlaceListView(ListView):
    model = Place

    def get_queryset(self):
        return Place.objects.all()

class PlaceDetailView(DetailView):
    model = Place

class CreatePlaceView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'camp/place_detail.html'
 
    form_class = PlaceForm

    model = Place

class PlaceUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'camp/place_detail.html'

    form_class = PlaceForm

    model = Place

class PlaceDeleteView(LoginRequiredMixin,DeleteView):
    model = Place
    success_url = reverse_lazy('place_list')

class RecommendListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'camp/place_recommend_list.html'
    template_name = 'camp/place_recommend_list.html'
    model = Place
    
    def inspect(self,results):
        lhs         = [tuple(result[2][0][0])[0] for result in results]
        rhs         = [tuple(result[2][0][1])[0] for result in results]
        supports    = [result[1] for result in results]
        confidences = [result[2][0][2] for result in results]
        lifts       = [result[2][0][3] for result in results]
        return list(zip(lhs, rhs, supports, confidences, lifts))

    def get_queryset(self):
        dataset = pd.read_csv('E:\VCODE\HTML_LEVEL_ONE\DJANGO_COURSE_2.xx\dbd\camp\campground_places.csv', header = None)
        transactions = []
        for i in range(0, 7501):
            transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

        rules = apriori(transactions = transactions, min_support = 0.001, min_confidence = 0.1, min_lift = 2, min_length = 2, max_length = 2)

        results = list(rules)

        resultsinDataFrame = pd.DataFrame(self.inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

        res = []
        res.append(list(resultsinDataFrame.nlargest(n=5,columns='Lift').values[i] for i in range(4)))
 
        ans=[] 
        for i in range(len(res[0])):
            ans.append(res[0][i][0])
            ans.append(res[0][i][1])

        ans=list(set(ans))
        for obj in Place.objects.all():
            obj.isSelected=False
            obj.save()

        for i in range(len(ans)-4):
            if Place.objects.filter(name=ans[i]).exists():
                place = Place.objects.get(name=ans[i])
                place.isSelected = True
                place.save()
            
        return Place.objects.filter(isSelected=True)

def index(request):
    return render(request,"camp/index.html")

@login_required
def add_comment_to_place(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.place = place
            comment.author = request.user
            comment.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = CommentForm()
    return render(request, 'camp/comment_form.html', {'form': form})

@login_required
def rate_place(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            if(rate.star_rating<=0 or rate.star_rating>5):
                messages.info(request,'Rating must be between 1 and 5')
                return redirect('rate_place')
            rate.user = user
            rate.save()
            return redirect('place_detail', pk=rate.place.pk)
    else:
        form = RatingForm()
    return render(request, 'camp/rating_form.html', {'form': form})

@login_required
def visited_place(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        form = VisitedForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.user = user 
            visit.save()
            return redirect('place_detail', pk=visit.place.pk)
    else:
        form = VisitedForm()
    return render(request, 'camp/visited_form.html', {'form': form})

@login_required
def family(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        form = FamilyForm(request.POST)
        if form.is_valid():
            family = form.save(commit=False)
            family.head = user
            family.save()
            return redirect('place_list')
    else:
        form = FamilyForm()
    return render(request, 'camp/family_form.html', {'form': form})


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        phoneno = request.POST['phoneno']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email =  request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                v1 = Phoneno.objects.create(user=user,phone_no=phoneno)
                v1.save()
                my_email = "campgroundsite@gmail.com"
                his_email = user.email
                password = "*****"
                message = "hi "+user.first_name+" "+user.last_name+" welcome to campground!!!" 

                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(my_email,password)
                print("Login success")
                server.sendmail(my_email,his_email,message)
        else:
            messages.info(request,'passwords do not much')
            return redirect('register')
        return redirect('place_list')

    else:
        return render(request,'registration/register.html')

def logout(request):
    auth.logout(request)
    return redirect('place_list')

def confirm_save(request,pk):
    place = get_object_or_404(Place,pk=pk)
    a = Add.objects.create(user=request.user, place=place)
    place.add()
    a.save() 
    return redirect('place_detail', pk=pk)
