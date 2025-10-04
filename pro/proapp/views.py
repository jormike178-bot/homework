from django.shortcuts import render
from .models import News,NewCotegory

# Create your views here.
def home_page(request):
    news = News.objects.all()
    cotegory = NewCotegory.objects.all()

    context = {
        'news' : news,
        'cotegory' : cotegory
    }

    return render(request, 'home.html', context)