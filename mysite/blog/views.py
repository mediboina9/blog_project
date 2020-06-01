from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from . import models
from . import forms
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class PostCreateView(CreateView):
    fields = ('author','title','text')
    model = models.Post

class PostUpdateView(UpdateView):
    fields = ('author','title')
    model = models.Post

class PostDeleteView(DeleteView):
    #context_object_name='post'
    model = models.Post
    success_url = reverse_lazy('blog:list')

class CommCreateView(CreateView):
    fields = ['text']
    model = models.Comments

    """def post_add_tags(request):
    #post= get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = CommentsForm(request.POST)
            if form.is_valid():
                tag = form.save(commit=False)
                tag.post= post
                tag.save()
                return redirect("single_post_view", pk=post.pk)
        else:
            form = CommentsForm()
            return render(request, "comments_form.html", {"form": form})"""


class PostDetailView(DetailView):
    context_object_name='post_detail'
    model = models.Post
    template_name = 'blog/post_detail.html'

class PostListView(ListView):
    context_object_name = 'post_list'
    model = models.Post
    template_name = 'blog/post_list.html'
