from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .form import MovieForm

# Create your views here.
def index(request):
    Movies = Movie.objects.all()
    # return HttpResponse('Hello From Index Page')
    return render(request,'index.html', {'Movies':Movies}) 
    
def CreateMovie(request):
    # return HttpResponse('Hello From Create Page')
    
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
        
    return render(request,'create.html',{'form':form})
    # return HttpResponse('Hello From Create Page')

def ShowMovie(request,name):
    movie = Movie.objects.get(name=name)
    categories = movie.categories.all()
    # movie = Movie.objects.get(pk=id)
    return render(request,'show.html', {'movie':movie, 'categories':categories}) 


def EditMovie(request,id):
    # return HttpResponse('Hello From Edit Page')
    movie = Movie.objects.get(pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'update.html', {'movie':movie,'form':form})

def DeleteMovie(request,id):
    # return HttpResponse('Hello From Delete Page')
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect('index')
