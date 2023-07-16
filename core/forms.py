from django import forms
from django.core.validators import RegexValidator


from .models import Article



class FormArticle(forms.ModelForm):
    title = forms.CharField(
        label = 'Titre', min_length=3, max_length=200,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = True, 
        widget=forms.TextInput(attrs={
            'placeholder':'Le titre de l\'article',
            'style':'text-transform: capitalize; font-size:1rem',
        })
    )
    title = forms.CharField(
        label = 'Titre', min_length=3, max_length=200,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = True, 
        widget=forms.TextInput(attrs={
            'placeholder':'Le titre de l\'article',
            'style':'text-transform: capitalize; font-size:1rem',
        })
    )

    subtitle1 = forms.CharField(
        label = "sous-titre1", 
        min_length = 20,
        max_length = 20,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder':'Ajouter un sous-titre',
            'style':'text-transform: capitalize; font-size:1rem',
        })
    )
    
    subtitle2 = forms.CharField(
        label = "sous-titre1", 
        min_length = 20,
        max_length = 20,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder':'Ajouter un sous-titre',
            'style':'text-transform: capitalize; font-size:1rem',
        })
    )
    
    subtitle3 = forms.CharField(
        label = "sous-titre1", 
        min_length = 20,
        max_length = 20,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder':'Ajouter un sous-titre',
            'style':'text-transform: capitalize; font-size:1rem',
        })
    )
    
    subtitle4 = forms.CharField(
        label = "sous-titre1", 
        min_length = 20,
        max_length = 20,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder':'Ajouter un sous-titre',
            'style':'text-transform: capitalize; font-size:1rem',
        })
    )
    
    subtitle5 = forms.CharField(
        label = "sous-titre1", 
        min_length = 20,
        max_length = 20,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder':'Ajouter un sous-titre',
            'style':'text-transform: capitalize; font-size:1rem',
        })
    )

    subtitle6 = forms.CharField(
        label = "sous-titre1", 
        min_length = 20,
        max_length = 20,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder':'Ajouter un sous-titre',
            'style':'text-transform: capitalize; font-size:1rem',
        })
    )
    
    conclusion = forms.CharField(
        label = "Conclusion", 
        min_length = 20,
        max_length = 20,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = True,
        widget = forms.Textarea(attrs = {
            'placeholder':'Titre de la conclusion',
            'style':'text-transform: capitalize; font-size:1rem',
        })
    )

    

    class Meta:
        model = Article
        exclude =['created_at']

        labels = {
            'category' : 'Categorie',
            'paragraphe1':'paragraphe1',
            'paragraphe2':'paragraphe2',
            'paragraphe3':'paragraphe3',
            'paragraphe4':'paragraphe4',
            'paragraphe5':'paragraphe5',
            'paragraphe6':'paragraphe6',
        }

        CATEGORY = (
            ('', 'Choisissez une categorie'),
            ('BUSINESS','BUSINESS'),
            ('Culture','Culture'),
            ('Sport','Sport'),
            ('Alimentation','Alimentation'),
            ('Politique','Politique'),
            ('Celebrite','Celebrite'),
            ('Startup','Startup'),
            ('Voyage','Voyage'),
        )

        widgets = {
            'category': forms.Select(
                choices = CATEGORY,
                attrs = {
                    'class': 'form-control',
            }),
            'paragraphe1': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),
            
            'paragraphe2': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),
            
            'paragraphe3': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),
            
            'paragraphe4': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),
            
            'paragraphe5': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),
            
            'paragraphe6': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),

        }
        