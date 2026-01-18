from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    """
    Model representing a job application tracking record.
    """
    # Choices for the application status
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected'),
    ]

    # Reference to the user who created this application
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='applications'
    )
    
    # Details of the job application
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    
    # Status of the application with predefined choices
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='Applied'
    )
    
    # Date when the application was submitted
    applied_date = models.DateField(null=True, blank=True)
    
    # Source where the job was found (e.g., LinkedIn, Company Website)
    source = models.CharField(max_length=255, null=True, blank=True)
    
    # Additional notes about the application
    notes = models.TextField(null=True, blank=True)
    
    # Date for a follow-up reminder
    follow_up_date = models.DateField(null=True, blank=True)
    
    # Automatically recording when the record was created
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.company_name} - {self.role} ({self.user.username})"
