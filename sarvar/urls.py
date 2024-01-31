from django.urls import path

from sarvar.views import HomeView, PostDetailView

appname = "blog"
urlpatterns = [
    path('', HomeView.as_view(), name="homepage"),

    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
]
