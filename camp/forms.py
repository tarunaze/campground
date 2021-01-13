from django import forms
from .models import Place,Add,Visited,Rating,Comment,Family

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name','place_url','description','country','state','city','zip_code')

        widgets = {
                'name': forms.TextInput(attrs={'class': 'textinputclass'}),
                'country': forms.TextInput(attrs={'class': 'textinputclass'}),
                'state': forms.TextInput(attrs={'class': 'textinputclass'}),
                'city': forms.TextInput(attrs={'class': 'textinputclass'}),
                'description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
            }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ('name','age','relation')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'age': forms.TextInput(attrs={'class': 'textinputclass'}),
            'relation': forms.TextInput(attrs={'class': 'textinputclass'}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('place','star_rating')

class VisitedForm(forms.ModelForm):
    class Meta:
        model = Visited
        fields = ('place','visited_date')