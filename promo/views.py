from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework import status
from .models import Promo, CampaignResult, CampaignResultScreenshot
from .serializers import PromoSerializer, CampaignResultSerializer, CampaignResultScreenshotSerializer


# Get all promos and create one
@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated, ])
@parser_classes([JSONParser, ])
def promo(request):
    if request.method == "GET":
        promos = Promo.objects.all()
        serializer = PromoSerializer(promos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PromoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated, ])
@parser_classes([JSONParser, ])
def promo_detail(request, id):
    promo = get_object_or_404(Promo, id=id)

    if request.method == "GET":
        serializer = PromoSerializer(promo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PromoSerializer(promo, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        promo.delete()
        return Response({"message": "Deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated, ])
@parser_classes([JSONParser, ])
def campaign_results(request):
    if request.method == "GET":
        camp_results = CampaignResult.objects.all()
        serializer = CampaignResultSerializer(camp_results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CampaignResultSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["GET", ])
@permission_classes([IsAuthenticated, ])
@parser_classes([JSONParser, ])
def campaign_results_detail(request, id):
    camp_result = get_object_or_404(CampaignResult, id=id)
    serializer = CampaignResultSerializer(camp_result)
    return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated, ])
@parser_classes([MultiPartParser, FormParser])
def upload_screenshots(request):
    if request.method == "POST":
        serializer = CampaignResultScreenshotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Files has been uploaded successfully!"},
                status=status.HTTP_204_NO_CONTENT
            )
        return Response(
            {"message": "Files has not been uploaded successfully!"},
            status=status.HTTP_400_BAD_REQUEST
        )
    elif request.method == "GET":
        screenshots = CampaignResultScreenshot.objects.all()
        serializer = CampaignResultScreenshotSerializer(screenshots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




