from django.shortcuts import render
from datetime import datetime
from dateutil.relativedelta import relativedelta


def calculate_time_passed():
    # Jara's birthdate
    birthdate = datetime(1994, 12, 24)

    # Current date
    current_date = datetime.now()

    age_delta = relativedelta(current_date, birthdate)

    return age_delta
def index(request):
    age_delta = calculate_time_passed()
    context = {
        'age_years': age_delta.years,
        'age_months': age_delta.months,
        'age_days': age_delta.days,
    }

    return render(request, 'index.html', context)