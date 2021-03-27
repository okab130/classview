from django.urls import path
from .views import IndexView,BookFormView,TestView

app_name = 'store'

urlpatterns = [
    path('index/',IndexView.as_view(),name="index"),
    path('book_form/', BookFormView.as_view(), name='book_form'),
    path('', TestView.as_view(), name='index2'),
]