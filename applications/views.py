from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.http import HttpResponse
import csv
from .models import Application
from .serializers import ApplicationSerializer, UserSerializer
from .permissions import IsOwner

class SignupView(APIView):
    """
    API View to handle user registration.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing job applications.
    Coordinates API endpoints for List, Retrieve, Create, Update, Delete.
    """
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        Override to ensure users can only see their own applications.
        """
        # Filter applications by the currently authenticated user
        return Application.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Override to automatically associate the current user with a new application.
        """
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def export_csv(self, request):
        """
        Export all user's applications to CSV format.
        """
        applications = self.get_queryset()
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="job_applications.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Company', 'Role', 'Status', 'Applied Date', 'Source', 'Notes', 'Follow-up Date'])
        
        for app in applications:
            writer.writerow([
                app.company_name,
                app.role,
                app.status,
                app.applied_date or '',
                app.source or '',
                app.notes or '',
                app.follow_up_date or '',
            ])
        
        return response
