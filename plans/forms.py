from django import forms
from .models import TravelPlan

class TravelPlanForm(forms.ModelForm):
    class Meta:
        model = TravelPlan
        fields = ['title', 'description', 'difficulty', 'comfortability', 'travel_time', 'price', 'activities', 'length', 'restrictions', 'plan_type', 'total_score', 'image']

class TravelPlanCheckForm(forms.ModelForm):
    class Meta:
        model = TravelPlan
        fields = ['completed']