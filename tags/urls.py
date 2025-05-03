from django.urls import path
from .views import TagListCreateView, TagRetrieveDestroyView

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<uuid:id>/', TagRetrieveDestroyView.as_view(), name='tag-retrieve-destroy'),
]