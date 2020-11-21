from django.urls import path

from models.URL import views

urlpatterns = [
    # Your URLs...
    path('<slug:short_addr>', views.RedirectView.as_view()),
    path('create/', views.CreateShortLink.as_view()),
]