from django.db import models
from django.conf import settings


class Promo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="promos"
    )
    video_link = models.URLField()
    description = models.TextField()
    story_tag = models.CharField(max_length=256)
    swipe_up_link = models.URLField()
    date_request = models.DateTimeField()
    special_wishes = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.description[:10]


class CampaignResult(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="campaign_results"
    )
    instagram_post_link = models.URLField()
    reach = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()


class CampaignResultScreenshot(models.Model):
    campaign = models.ForeignKey(
        CampaignResult,
        on_delete=models.CASCADE,
        related_name="campaign_images"
    )
    screenshots = models.FileField(upload_to="screenshots/")
