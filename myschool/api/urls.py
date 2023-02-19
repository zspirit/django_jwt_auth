from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
        )

urlpatterns = [
    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]