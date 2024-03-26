from rest_framework import serializers
from . import models


class VisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visa
        fields = (
            "id",
            "title",
            "country",
            "visa_cost",
            "income_requirements",
            "visa_length",
            "citizens_that_qualify",
            "apply_remotely",
            "bonus",
        )


class VisaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visa
        fields = (
            "id",
            "title",
            "country",
            "visa_cost",
            "income_requirements",
            "visa_length",
            "citizens_that_qualify",
            "apply_remotely",
            "bonus",
        )

    def __init__(self, *args, **kwargs):
        super(VisaDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class CountryImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CountryImage
        fields = ("id", "country", "image")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = (
            "id",
            "name",
            "capital",
            "description",
            "continent",
            "climate_zone",
            "language",
            "flag_url",
            "safety_index",
            "broadband_speed",
            "mobile_speed",
            "internet_accessibility",
            "cost_of_living",
            "avg_rent_cost",
            "healthcare_index",
            "cultural_and_recreational_opportunities",
            "images",
        )

    # def __init__(self, *args, **kwargs):
    #     super(CountrySerializer, self).__init__(*args, **kwargs)
    #     self.Meta.depth = 1


class CountryDetailSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Country
        fields = (
            "id",
            "name",
            "capital",
            "description",
            "continent",
            "climate_zone",
            "language",
            "flag_url",
            "safety_index",
            "broadband_speed",
            "mobile_speed",
            "internet_accessibility",
            "cost_of_living",
            "avg_rent_cost",
            "healthcare_index",
            "cultural_and_recreational_opportunities",
            "images",
            "reviews",
            "activities",
        )

    def __init__(self, *args, **kwargs):
        super(CountryDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Costumer
        fields = ("id", "user", "bio", "cover_photo")

    def __init__(self, *args, **kwargs):
        super(CostumerSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class CostumerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Costumer
        fields = ("id", "user", "bio", "cover_photo")

    def __init__(self, *args, **kwargs):
        super(CostumerDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ("id", "user", "country", "rating", "review_text", "created_at")

    def __init__(self, *args, **kwargs):
        super(ReviewSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class ActivityImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ActivityImage
        fields = ("id", "activity", "image")


class ActivityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ActivityCategory
        fields = ("id", "name")


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = ("id", "name", "description", "category", "country")

    # def __init__(self, *args, **kwargs):
    #     super(ActivitySerializer, self).__init__(*args, **kwargs)
    #     self.Meta.depth = 1


class ActivityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = ("id", "name", "description", "category", "country")

    def __init__(self, *args, **kwargs):
        super(ActivityDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1
