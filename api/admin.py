from django.contrib import admin
from .models import Post, Profile, Comment
from django.contrib.auth.admin import UserAdmin


class AdminConfig(UserAdmin):
    ordering = ("-date_created",)
    list_display = ("user_name", "email", "is_staff", "is_active")
    search_fields = ("user_name", "email")
    fieldsets = [
        (None, {"fields": ["email", "user_name"]}),
        ("Personal info", {"fields": ["profile_picture"]}),
        ("Permissions", {"fields": ["is_staff", "is_active"]}),
    ]


@admin.register(Post)
class PersonAdmin(admin.ModelAdmin):
    autocomplete_fields = ["likes"]


admin.site.register(Comment)
admin.site.register(Profile, AdminConfig)
