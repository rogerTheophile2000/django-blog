from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Article
from .forms import FormArticle
# Create your views here.

def home(request):
    articles = Article.objects.all()
    return render(request, "index.html", {'articles': articles})

def addArticle(request):
    if request.method == "POST":
        form =FormArticle(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully !")
            return HttpResponseRedirect('/')
        else:
            return render(request, "article/add.html", {"form": form})
    else:
        form = FormArticle()
        return render(request, "article/add.html", {"form": form})
    