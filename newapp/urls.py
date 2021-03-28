from django.urls import path
from .views import IndexView,BookFormView,TestView,listfunc,detailfunc

app_name = 'store'

urlpatterns = [
    path('index/',IndexView.as_view(),name="index"),
    path('book_form/', BookFormView.as_view(), name='book_form'),
    path('', TestView.as_view(), name='index2'),
    path('list/', listfunc, name='listfunc'),
    path('detail/<int:pk>/', detailfunc, name='detail'),
#    path('test/', 'newapp/aaa.html', name='test'),
]