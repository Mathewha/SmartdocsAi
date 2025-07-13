from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_documents, name='search_documents'),
    path('semantic/', views.semantic_search_documents, name='semantic_search_documents'),
    path('api/search-options/', views.get_search_options, name='search_options_api'),
    path('conversational/', views.conversational_search_documents, name='conversational_search_documents'),
]