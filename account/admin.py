from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["email", "date_joined", 'last_login', "is_active", "id"]
    list_filter = [
        "is_sponsor",
        "is_influence",
        "date_joined",
        "date_joined",
        "last_login",
        "is_active",
    ]
    fields = [
        (
            "user_name",
            "email",
            "password"
        ),
        (
            "first_name",
            "last_name"
        ),
        ('address', 'phone_number',),
        (
            "is_active",
        ),
        "instagram_link",
        "referal_code",
        "company",
        "company_type",
        "influencer_name",
        "music_styles",
        "followers_number",
        "price",
        "is_sponsor",
        "is_influence",
        "date_joined",
        'last_login',
        "is_staff",
        "is_superuser",
    ]
    search_fields = ['email', "id"]
    date_hierarchy = "date_joined"


admin.site.register(CustomUser, CustomUserAdmin)
