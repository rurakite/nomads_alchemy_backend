from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("review", views.ReviewViewSet)

app_name = "api"

urlpatterns = [
    # country
    path("countries/", views.CountryList.as_view()),
    path("country/<int:pk>/", views.CountryDetail.as_view()),
    # visa
    path("visas/", views.VisaList.as_view()),
    path("visa/<int:pk>/", views.VisaDetail.as_view()),
    # acivity
    path("activities/", views.ActivityList.as_view()),
    path("activity/<int:pk>/", views.ActivityDetail.as_view()),
    # costumer
    path("costumers/", views.CostumerList.as_view()),
    path("costumer/<int:pk>/", views.CostumerDetail.as_view()),
    # reviews
    path("", include(router.urls)),
]
