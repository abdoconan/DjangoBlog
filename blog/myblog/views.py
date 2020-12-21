from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

#Posts
# posts = [
#     {
#         'author':'Youstina Nagy',
#         'title':'First post',
#         'contant':'this is my first post',
#         'date_posted': 'Augest 1st, 2019'
#     },
#     {
#         'author':'Abdo Conan',
#         'title':'Second post',
#         'contant':'this is my second post',
#         'date_posted': 'September 23th, 2019'
#     },

# ]


# Create your views here.
def home(request):
    context = {
        'posts': Posts.objects.all(),
    }
    return render(request, 'myblog/home.html', context)

def about(request):
    return render(request, "myblog/about.html", {"title": "About"})