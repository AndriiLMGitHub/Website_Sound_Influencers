from django.urls import path
from . import views

urlpatterns = [
    path('', views.promo),
    path('<int:id>/', views.promo_detail),
    path('invoice/', views.campaign_results),
    path('invoice/<int:id>/', views.campaign_results_detail),
    path('invoice/upload/screenshots/', views.upload_screenshots)
] 