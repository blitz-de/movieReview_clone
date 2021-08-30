from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from .forms import *
# main login of the website

def home(request):
    # print("This was executed successfully.")
    # 
    allMovies = Movie.objects.all() # select * from movie
    print(allMovies)

    context = {
        'movies': allMovies,
    }
    return render(request, 'main/index.html', context)

def details(request, id):
    movie = Movie.objects.get(id=id) # select * from movie where id=id

    context = {
        'movie': movie
    }
        
    if id <= len(Movie.objects.all()):
        return render(request, 'main/details.html', context)
    else:
        return HttpResponse("<h1>This page doesn't exist</h1>")

# add movies to the database
def add_movies(request):
    if request.method == "POST":
        form = MovieForm(request.POST or None)

        # check if te form is valid
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:home")
    else:
        form = MovieForm()
    return render(request, 'main/addmovies.html', {"form": form,
                                                    "controller": "Add Movies"})

# edit the movie
def edit_movies(request, id):
    # get the movie linked with id
    movie = Movie.objects.get(id=id)

    # form check
    if request.method == "POST":
        form = MovieForm(request.POST or None, instance=movie)
        # check if form is valid
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect ("main:detail", id)
    
    else: 
        form = MovieForm(instance=movie)
    return render(request, 'main/addmovies.html', {"form": form, "controller": "Edit Movies"})