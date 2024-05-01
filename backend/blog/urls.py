from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('list', views.ListView.as_view()),
    path('<slug:slug>', views.BlogDetailsView.as_view()),
    path('mail/<slug:slug>', views.SendEmailView.as_view())
]