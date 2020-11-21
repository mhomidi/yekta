from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from accounts.apps import CustomJWTSerializer

urlpatterns = [
    # Your URLs...
    path('token/', jwt_views.TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(serializer_class=CustomJWTSerializer), name='token_refresh'),
]