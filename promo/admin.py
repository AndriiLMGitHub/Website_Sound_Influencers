from django.contrib import admin
from .models import Promo, CampaignResult, CampaignResultScreenshot


class PromoAdmin(admin.ModelAdmin):
    pass


class CampaignResultAdmin(admin.ModelAdmin):
    pass


class CampaignResultScreenshotAdmin(admin.ModelAdmin):
    pass


admin.site.register(Promo, PromoAdmin)
admin.site.register(CampaignResult, CampaignResultAdmin)
admin.site.register(CampaignResultScreenshot, CampaignResultScreenshotAdmin)
