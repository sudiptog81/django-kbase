
from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('register/', views.register, name='register'),
    path('article/new/', views.create_article, name='create_article'),
    path('article/update/<str:slug>/',
         views.update_article, name='update_article'),
    path('article/delete/<str:slug>/',
         views.delete_article, name='delete_article'),
    path('category/new/', views.create_category, name='create_category'),
    path('article/<str:slug>/', views.article, name='article'),
    path('category/<str:name>/', views.category, name='category'),
    path('articles/', views.articles, name='articles'),
    path('categories/', views.categories, name='categories'),
    path('search/', views.search, name='search'),
]

handler404 = views.not_found
