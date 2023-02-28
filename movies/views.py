from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *


def home(request):
    search_term = request.GET.get('search_movie')
    if search_term:
        movies_data = Movie.objects.filter(title__icontains=search_term)
    else:
        movies_data = Movie.objects.all()
    return render(request, 'home.html', {'search_term': search_term, 'movies': movies_data,
                                         'title': 'Movies', 'logo': '/static/logos/movie-logo.jpg'})


def movie_detail(request, movie_id):
    movie_data = get_object_or_404(Movie, pk=movie_id)
    reviews_data = Review.objects.filter(movie=movie_data)
    return render(request, 'detail.html', {'movie': movie_data, 'reviews': reviews_data, 'logo': '/static/logos/movie-logo.jpg'})


@login_required
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'review_create.html',
                      {'form': ReviewForm, 'movie': movie})
    else:
        try:
            form = ReviewForm(request.POST)
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.movie = movie
            new_review.save()
            return redirect('detail',
                            new_review.movie.id)
        except ValueError:
            return render(request,
                          'review_create.html',
                          {'form': ReviewForm, 'error': 'bad data passed in '})


@login_required
def update_review(request, review_id):
    review_data = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review_data)
        return render(request, 'review_update.html', {'review': review_data, 'form': form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review_data)
            form.save()
            return redirect('detail', review_data.movie.id)
        except ValueError:
            return render(request, 'review_update.html',
                          {'review': review_data,
                           'form': form, 'error': 'Bad data in form'})


@login_required
def delete_review(request, review_id):
    review_data = get_object_or_404(Review, pk=review_id, user=request.user)
    review_data.delete()
    return redirect('detail', review_data.id)


