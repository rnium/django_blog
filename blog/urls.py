from django.urls import path
from .views import homepage, add_new, post_update, post_detail

urlpatterns = [
    path('', homepage, name='homepage'),
    path('add/', add_new, name="add_new"),
    path('blog/<int:pk>/', post_detail, name='post_detail'),
    path('blog/<int:pk>/update', post_update, name='update')
]