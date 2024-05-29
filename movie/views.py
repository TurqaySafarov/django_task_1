from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Movie

# Create your views here.

def movie_list(request):
    search_query = request.GET.get('q', '')
    if search_query:
        movies = Movie.objects.filter(title__icontains=search_query)
    else:
        movies = Movie.objects.all()

    paginator = Paginator(movies, 10)  # Show 10 movies per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'movie_reviews/movie_list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
    })
