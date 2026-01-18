from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    """
    Administration interface for Application model.
    """
    # Fields to display in the list view
    list_display = ('company_name', 'role', 'status', 'user', 'applied_date', 'created_at')
    
    # Enable filtering by status and date
    list_filter = ('status', 'applied_date', 'created_at')
    
    # Search functionality for company and role
    search_fields = ('company_name', 'role', 'user__username')
    
    # Date hierarchy for easier navigation
    date_hierarchy = 'applied_date'
