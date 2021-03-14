from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .form import MovieForm
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

def index(request):
    Movies = Movie.objects.all()
    return render(request,'index.html', {'Movies':Movies}) 
    
@login_required
def CreateMovie(request):    
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
        
    return render(request,'create.html',{'form':form})

def ShowMovie(request,name):
    movie = Movie.objects.get(name=name)
    categories = movie.categories.all()
    return render(request,'show.html', {'movie':movie, 'categories':categories}) 

@login_required
def EditMovie(request,id):
    movie = Movie.objects.get(pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'update.html', {'movie':movie,'form':form})

@login_required
# @permission_required('netflix.delete_movie')
def DeleteMovie(request,id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect('index')
