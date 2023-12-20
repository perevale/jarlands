from django.db import models

class TravelPlan(models.Model):
    title = models.CharField(max_length=255, default="Super Plan")
    description = models.TextField(blank=True)
    difficulty = models.IntegerField()
    comfortability = models.IntegerField()
    travel_time = models.IntegerField()
    price = models.CharField(max_length=50)
    activities = models.TextField()
    length = models.IntegerField()
    restrictions = models.TextField()
    plan_type = models.CharField(max_length=50)
    total_score = models.FloatField()
    image = models.ImageField(upload_to='plan_images/', blank=True, null=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title
