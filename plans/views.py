# plans/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import TravelPlan
from .forms import TravelPlanForm, TravelPlanCheckForm
from django.contrib.auth.decorators import login_required


@login_required
def plans(request):
    completed_filter = request.GET.get('completed')
    if completed_filter:
        plans = TravelPlan.objects.filter(completed=False)
    else:
        plans = TravelPlan.objects.all()

    return render(request, 'plans.html', {'plans': plans, 'completed_filter': completed_filter})

@login_required
def plan_detail(request, plan_id):
    plan = get_object_or_404(TravelPlan, pk=plan_id)
    return render(request, "plan_detail.html", {"plan": plan})


@login_required
def add_plan(request):
    if request.method == "POST":
        form = TravelPlanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("plans")
    else:
        form = TravelPlanForm()

    return render(request, "add_plan.html", {"form": form})


@login_required
def toggle_completion(request, plan_id):
    plan = TravelPlan.objects.get(pk=plan_id)
    if request.method == "POST":
        form = TravelPlanCheckForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect("plan_detail", plan_id=plan_id)
    else:
        form = TravelPlanCheckForm(instance=plan)

    return render(request, "plan_detail.html", {"plan": plan, "form": form})
