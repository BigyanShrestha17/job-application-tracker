from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSet, SignupView

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'applications', ApplicationViewSet, basename='application')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('', include(router.urls)),
]
