from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView, DeleteView, UpdateView, ListView

from sarvar.models import Post


class HomeView(View):
    def get(self, request):
        posts_for_homepage = Post.objects.order_by('-created_at')[:10]
        context = {
            "posts": posts_for_homepage,
        }

        return render(request, 'home.html', context=context)


class PostDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post
    context_object_name = "post"
