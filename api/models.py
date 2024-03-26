from django.db import models
from django.contrib.auth.models import User


class Costumer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    cover_photo = models.ImageField(upload_to="profile_photo/")

    def __str__(self):
        return self.user.username


class Country(models.Model):
    class ContinentChoices(models.TextChoices):
        AFRICA = "Africa"
        ASIA = "Asia"
        EUROPE = "Europe"
        NORTH_AMERICA = "North America"
        SOUTH_AMERICA = "South America"
        OCEANIA = "Oceania"

    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    continent = models.CharField(max_length=100, choices=ContinentChoices.choices)
    climate_zone = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    flag_url = models.CharField(max_length=200, blank=True, null=True)

    safety_index = models.DecimalField(
        max_digits=5, decimal_places=3, blank=True, null=True
    )
    safety_and_security = models.TextField(blank=True, null=True)
    temperature = models.IntegerField(blank=True, null=True)
    humidity = models.IntegerField(blank=True, null=True)
    uv_index = models.IntegerField(blank=True, null=True)
    broadband_speed = models.IntegerField(blank=True, null=True)
    mobile_speed = models.IntegerField(blank=True, null=True)
    internet_accessibility = models.TextField(blank=True, null=True)
    cost_of_living = models.IntegerField(blank=True, null=True)
    avg_rent_cost = models.IntegerField(blank=True, null=True)
    healthcare_index = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True
    )
    cultural_and_recreational_opportunities = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Countries"


class CountryImage(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="countries/")

    class Meta:
        verbose_name_plural = "Country Images"


class Visa(models.Model):
    title = models.CharField(max_length=255, default="Digital Nomad Visa")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="visas")
    visa_cost = models.CharField(max_length=255, blank=True, null=True)
    income_requirements = models.TextField(blank=True, null=True)
    visa_length = models.TextField(blank=True, null=True)
    citizens_that_qualify = models.CharField(max_length=255, blank=True, null=True)
    apply_remotely = models.CharField(max_length=255, blank=True, null=True)
    bonus = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.country} - {self.title}"

    class Meta:
        ordering = ["country"]
        verbose_name_plural = "Visas"


class Review(models.Model):
    class RatingChoices(models.TextChoices):
        ONE_STAR = "★☆☆☆☆"
        TWO_STARS = "★★☆☆☆"
        THREE_STARS = "★★★☆☆"
        FOUR_STARS = "★★★★☆"
        FIVE_STARS = "★★★★★"

    user = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name="reviews")
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="reviews",
        related_query_name="review",
    )
    rating = models.CharField(max_length=10, choices=RatingChoices.choices)
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.rating} - {self.review_text}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Reviews"


class ActivityCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Activity Categories"


class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        ActivityCategory, on_delete=models.CASCADE, related_name="activities"
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="activities"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Activities"


class ActivityImage(models.Model):
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="activities/")

    def __str__(self):
        return f"Image for {self.activity.name}"

    class Meta:
        verbose_name_plural = "Activity Images"
