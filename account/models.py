from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


# User Model
class CustomUser(AbstractUser):
    COMPANY_TYPES = [
        ("Artist", "Artist"),
        ("Promoter", "Promoter"),
        ("PR Agent", "PR Agent"),
        ("Label", "Label"),
        ("Other", "Other")
    ]
    MUSIC_STYLES = [
        ("Techno", "Techno"),
        ("EDM", "EDM"),
        ("House", "House"),
        ("Other", "Other")
    ]
    username = None
    email = models.EmailField(_("Email address"), unique=True)
    user_name = models.CharField(_("Username"), max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    referal_code = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    company_type = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=COMPANY_TYPES
    )
    influencer_name = models.CharField(max_length=255, null=True, blank=True)
    music_styles = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=MUSIC_STYLES
    )
    followers_number = models.PositiveIntegerField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    is_sponsor = models.BooleanField(default=False)
    is_influence = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "address",
        "phone_number",
        "user_name",
        "instagram_link",
        "referal_code",
        "company",
        "company_type",
        "influencer_name",
        "music_styles",
        "followers_number",
        "price",
        "is_sponsor",
        "is_influence"
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

