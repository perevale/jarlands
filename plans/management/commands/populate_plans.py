# plans/management/commands/populate_plans.py
from django.core.management.base import BaseCommand
from plans.models import TravelPlan

class Command(BaseCommand):
    help = 'Populate the database with sample travel plans'

    def handle(self, *args, **options):
        # Your sample data goes here
        plans_data = [
            {'difficulty': 5, 'comfortability': 8, 'travel_time': 10, 'price': 200, 'activities': 'Hiking', 'length': 3, 'restrictions': 'None', 'plan_type': 'Adventure', 'total_score': 7.5},
            # Add more sample data as needed
        ]

        for data in plans_data:
            TravelPlan.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample travel plans'))
