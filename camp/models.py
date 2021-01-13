from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
# Create your models here.



class Place(models.Model):
    added_by = models.ManyToManyField(User,through='Add',related_name='added_place')
    visited_by = models.ManyToManyField(User,through='Visited',related_name='visited_place')
    rated_by = models.ManyToManyField(User,through='Rating',related_name='rated_place')
    name = models.CharField(max_length=100,primary_key=True)
    place_url = models.URLField(blank=True)
    description = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=7)
    isSelected = models.BooleanField(default=False)

    class Meta:
        db_table = "places"

    def get_absolute_url(self):
        return reverse("place_detail",kwargs={'pk':self.pk})

    def get_count(self):
        return self.places.all()

    def get_access(self):
        add = Add.objects.get(place=self)
        return add

    def add(self):
        self.places.added_date = timezone.now()

    def __str__(self):
        return self.name

class Add(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    place = models.ForeignKey(Place,related_name="places",on_delete=models.CASCADE)
    added_date =  models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "add"

class Phoneno(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=10)

    class Meta:
        db_table = "Phone_Number"

class Visited(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    visited_date =  models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "visited"

class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    star_rating =  models.IntegerField(default=0)

    class Meta:
        db_table = "rating"
        constraints = [
            models.CheckConstraint(
                check=models.Q(star_rating__gte=1) & models.Q(star_rating__lte=5),
                name="rate between 1 and 5",
            )
        ]


class Comment(models.Model):
    author = models.ForeignKey(User,related_name='my_comments',on_delete=models.CASCADE,null=True)
    text = models.TextField()
    commented_date = models.DateTimeField(default=timezone.now)
    place = models.ForeignKey(Place, related_name='comments',on_delete=models.CASCADE)
    
    class Meta:
        db_table = "comment"
    
    def __str__(self):
        return self.text

class Family(models.Model):
    class Meta:
        unique_together = (('head','name'),)
        db_table = "familyandfriends"

    head = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    relation = models.CharField(max_length=100)