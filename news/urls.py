from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('news/',views.base,name='base'),
    path('<int:id>/', views.news_detail, name='news_detail'),
    path('<int:news_id>/comment/', views.news_comment, name='news_comment'),
    path('news_list/',views.news_list,name='news_list'),
    path('<slug:category_slug>/', views.news_list,
         name='news_list_by_category'),
]
