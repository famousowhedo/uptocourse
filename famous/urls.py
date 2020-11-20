from django.urls import path
from .import views
from .views import PostListView, PostDetailView


urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('blog/', PostListView.as_view() ,name='blog'),
    path('post/<int:pk>/', PostDetailView.as_view() ,name='post-detail'),
    path('contact/', views.contact,name='contact')
]
