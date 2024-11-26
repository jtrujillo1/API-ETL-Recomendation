from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('email', 'username')