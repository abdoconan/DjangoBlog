from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class PostListView(ListView):
    model = Posts
    template_name = 'myblog/home.html' # defult route for class base view <app>/<model>_<viewtype>.html  
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class UserPostListView(ListView):
    model = Posts
    template_name = 'myblog/user_posts.html' # defult route for class base view <app>/<model>_<viewtype>.html  
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Posts

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Posts
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeletelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def about(request):
    return render(request, "myblog/about.html", {"title": "About"})