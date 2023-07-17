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
            'class': 'form-control',
        })
    )

    subtitle1 = forms.CharField(
        label = "sous-titre 1", 
        max_length = 200,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder':'Ajouter un sous-titre',
            'style':'text-transform: capitalize; font-size:1rem',
            'class': 'form-control',
        })
    )
    
    subtitle2 = forms.CharField(
        label = "sous-titre 2", 
        max_length = 200,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder':'Ajouter un sous-titre',
            'style':'text-transform: capitalize; font-size:1rem',
            'class': 'form-control',
        })
    )
    
    subtitle3 = forms.CharField(
        label = "sous-titre 3", 
        max_length = 200,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder':'Ajouter un sous-titre',
            'style':'text-transform: capitalize; font-size:1rem',
            'class': 'form-control',
        })
    )
    
    subtitle4 = forms.CharField(
        label = "sous-titre 4", 
        max_length = 200,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder':'Ajouter un sous-titre',
            'style':'text-transform: capitalize; font-size:1rem',
            'class': 'form-control',
        })
    )
    
    subtitle5 = forms.CharField(
        label = "sous-titre 5", 
        max_length = 200,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder':'Ajouter un sous-titre',
            'style':'text-transform: capitalize; font-size:1rem',
            'class': 'form-control',
        })
    )

    subtitle6 = forms.CharField(
        label = "sous-titre 6", 
        max_length = 200,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder':'Ajouter un sous-titre',
            'style':'text-transform: capitalize; font-size:1rem',
            'class': 'form-control',
        })
    )
    
    conclusiontile = forms.CharField(
        label = "Titre de la conclusion", 
        max_length = 200,
        validators = [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$', 
        message = "Only letters is allowd !")],
        required = True,
        widget = forms.TextInput(attrs = {
            'placeholder':'Titre de la conclusion',
            'class':'form-control',
            'style':'text-transform: capitalize; font-size:1rem',
        })
    )

    

    class Meta:
        model = Article
        exclude =['created_at']

        labels = {
            'category' : 'Categorie',
            'introduction' : 'Introduction',
            'paragraphe1':'Paragraphe1',
            'paragraphe2':'Paragraphe2',
            'paragraphe3':'Paragraphe3',
            'paragraphe4':'Paragraphe4',
            'paragraphe5':'Paragraphe5',
            'paragraphe6':'Paragraphe6',
            'conclusion':'Conclusion',
        }

        CATEGORY = (
            ('BUSINESS','Business'),
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
            'introduction': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),
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
            
            'conclusion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                }
            ),

        }
        