from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('followers/', views.FollowerListView.as_view()),
    path('following/', views.FollowingListView.as_view()),
    path('posts/<int:pk>', views.PostListView.as_view()),
    path('likes/<int:pk>', views.PostLikesListView.as_view()),
    path('comments/<int:pk>', views.PostCommentsListView.as_view()),
    path('posts/', views.MyPostListView.as_view()),
    path('post/', views.PostView.as_view()),
]

# login http://localhost:8000/auth/token/login
# register http://localhost:8000/auth/users
