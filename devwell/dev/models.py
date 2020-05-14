from django.conf import settings
from django.db import models
from django.utils import timezone



class Rating(models.Model): 
    work = models.TextChoices('Awesome', 'Good')
    food = models.TextChoices('Plant Based options', 'Gluten Free')
    environment = models.TextChoices('Quiet', 'Fun')
    food_choices = models.CharField(blank=True, choices=work.choices, max_length=10)
    
class Dev(models.Model): 
    name = models.CharField(max_length=100)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name



    
