from django.urls import path
from .views import plans, plan_detail, add_plan, toggle_completion

urlpatterns = [
    path('', plans, name='plans'),
    path('add_plan/', add_plan, name='add_plan'),
    path('<int:plan_id>/', plan_detail, name='plan_detail'),
    path('toggle_completion/<int:plan_id>/', toggle_completion, name='toggle_completion'),

]
