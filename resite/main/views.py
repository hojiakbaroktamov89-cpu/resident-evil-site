from django.shortcuts import render, get_object_or_404
from .models import Game, Character, Movie, History


def home(request):
    context = {
        'games': Game.objects.all(),
        'characters': Character.objects.all(),
        'movies': Movie.objects.all(),
        'histories': History.objects.all(),
    }
    return render(request, 'main/index.html', context)


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'main/game_detail.html', {'game': game})


def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'main/character_detail.html', {'character': character})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'main/movie_detail.html', {'movie': movie})


def history_detail(request, pk):
    history = get_object_or_404(History, pk=pk)
    return render(request, 'main/history_detail.html', {'history': history})
