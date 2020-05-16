from django.urls import path 
from . import views 

app_name = 'dev'

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('review/<int:pk>', views.review_detail, name='review_detail'),
    path('tip/', views.tip_list, name='tip_list'),
    path('tip/<int:pk>/', views.tip_detail, name='tip_detail'),
    path('add_review/<int:pk>/', views.add_review, name='add_review'),
]

