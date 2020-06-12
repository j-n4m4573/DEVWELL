from django.urls import path 
from . import views 

app_name = 'dev'

urlpatterns = [
    path('', views.IndexView.as_view(), name='review_list'),
    path('review/<int:pk>', views.DetailView.as_view(), name='review_detail'),
    path('tip/', views.tip_list, name='tip_list'),
    path('tip/<int:pk>/', views.tip_detail, name='tip_detail'),
    path('add_review/<int:pk>/', views.add_review, name='add_review'),
]

