from django.urls import path
from core import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('index_class/', views.ClassBasedIndex.as_view(), name='index_class'),

    path('animal/', views.AnimalList.as_view(), name='animals'),
    path('animal/<int:pk>/', views.AnimalDetail.as_view(), name='animal_detail'),
    path('redirect/', views.Redirect.as_view(), name='redirect'),
    path('form_example/', views.SimpleForm.as_view(), name='form_example'),
]