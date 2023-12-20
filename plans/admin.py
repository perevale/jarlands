
from django.contrib import admin
from .models import TravelPlan

@admin.register(TravelPlan)
class TravelPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'comfortability', 'travel_time', 'price', 'activities', 'length', 'restrictions', 'plan_type', 'total_score', 'image')