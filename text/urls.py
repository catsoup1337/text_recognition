from django.urls import path

from . import views

urlpatterns = [
    path('tag/<str:tag_slug>/', views.tag, name='tag'),
    path('', views.image_upload_view, name='index'),
]