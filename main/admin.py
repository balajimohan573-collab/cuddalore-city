from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'area', 'status', 'created_at', 'is_pinned')
    list_editable = ('status', 'is_pinned')
    list_filter = ('status', 'area')
    search_fields = ('title', 'description')