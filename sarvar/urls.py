from django.urls import path

from sarvar.views import HomePageView, AboutView, PostFormView, PostDetailView, PostConfirmDeleteView, \
    UserPostsView, RegisterView, UserLoginView, UserLogoutView

app_name = "blog"
urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('about/', AboutView.as_view(), name='about-page'),
    path('register/', RegisterView.as_view(), name='register-page'),
    path('login/', UserLoginView.as_view(), name='login-page'),
    path('logout/', UserLogoutView.as_view(), name='logout-page'),
    path('postdetail/<int:pk>', PostDetailView.as_view(), name='post-detail-page'),
    path('post/confirm/', PostConfirmDeleteView.as_view(), name='post-confirm-delete-page'),
    path('new-post/', PostFormView.as_view(), name='post-form-page'),
    path('user/posts/', UserPostsView.as_view(), name='user-posts-page'),
]
