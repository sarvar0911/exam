from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from sarvar.forms import UserLoginForm, UserRegisterModelForm, PostCreateForm
from sarvar.models import About, Post


class HomePageView(ListView):
    model = Post
    template_name = "sarvar/home.html"
    context_object_name = "posts"


class AboutView(ListView):
    model = About
    template_name = "sarvar/about.html"
    context_object_name = "abouts"


class CustomLoginRequiredMixin(LoginRequiredMixin):

    def get_permission_denied_message(self):
        messages.set_level()
        return super().get_permission_denied_message()


class PostFormView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "sarvar/post_form.html"
    model = Post
    form = PostCreateForm
    fields = ["title", "content"]
    success_message = 'Post successfully created'


class PostDetailView(DetailView):
    model = Post
    template_name = "sarvar/post_detail.html"
    context_object_name = "post"


class PostConfirmDeleteView(DeleteView):
    model = Post
    template_name = "sarvar/post_confirm_delete.html"
    success_message = 'deleted successfully'


class RegisterView(View):
    def get(self, request):
        form = UserRegisterModelForm()
        return render(request, "sarvar/register.html", {"form": form})

    def post(self, request):
        form = UserRegisterModelForm(data=request.POST)
        if form.is_valid():
            messages.success(request, "User successfully registered")
            form.save()
            return redirect("blog:login-page")
        else:
            return render(request, "sarvar/register.html", {"form": form})


class UserPostsView(ListView):
    model = Post
    template_name = "sarvar/user_posts.html"
    context_object_name = "userposts"


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "sarvar/login.html", {"form": form})

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.COOKIES)
                messages.success(request, "user successfully logged in")
                return redirect("blog:home-page")
            else:
                messages.error(request, "Username or password wrong")
                return redirect("blog:login-page")

        else:
            return render(request, "sarvar/login.html", {"form": form})


class UserLogoutView(View):
    def get(self, request):
        return render(request, "sarvar/logout.html")

    def post(self, request):
        logout(request)
        messages.info(request, "User successfully logged out")
        return redirect("blog:login-page")
