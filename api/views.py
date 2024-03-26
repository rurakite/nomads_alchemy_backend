from rest_framework import generics, permissions, viewsets

import api.pagination
from . import models
from . import serializers


class CountryList(generics.ListCreateAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    pagination_class = api.pagination.CustomPagination


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountryDetailSerializer


class VisaList(generics.ListCreateAPIView):
    queryset = models.Visa.objects.all()
    serializer_class = serializers.VisaSerializer
    pagination_class = api.pagination.CustomPagination


class VisaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Visa.objects.all()
    serializer_class = serializers.VisaDetailSerializer


class ActivityList(generics.ListCreateAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer


class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivityDetailSerializer


class CostumerList(generics.ListCreateAPIView):
    queryset = models.Costumer.objects.all()
    serializer_class = serializers.CostumerSerializer


class CostumerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Costumer.objects.all()
    serializer_class = serializers.CostumerDetailSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
