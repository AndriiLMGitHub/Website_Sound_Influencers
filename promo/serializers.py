from rest_framework import serializers
from .models import Promo, CampaignResult, CampaignResultScreenshot


class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = "__all__"


class CampaignResultScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignResultScreenshot
        fields = "__all__"


class CampaignResultSerializer(serializers.ModelSerializer):
    campaign_images = CampaignResultScreenshotSerializer(read_only=True, many=True)

    class Meta:
        model = CampaignResult
        fields = (
            "id",
            "user",
            "instagram_post_link",
            "reach",
            "likes",
            "campaign_images",
        )
