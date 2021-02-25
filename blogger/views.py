from django.shortcuts import render
from .models import Article
# Create your views here.
def show(request):
    context = {
        "articles": Article.objects.all()
    }
    return render(request, 'blogger/home.html', context)
