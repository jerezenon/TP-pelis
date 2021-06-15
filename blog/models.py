from django.db import models
from django.utils import timezone

class pelis(model.model)
    Original name = models.CharField(max_length = 100)
    NameInSpain = models.CharField(max_length = 100)
    Year = models.CharField(max_length=8)
    Director = models.CharField( max_length=50)
    Duration = models.PositiveSmallIntegerField()
    Genres = models.CharField()
    RATE_CHOICES = (
        (1,"1"),
        (2,"2"),
        (3,"3"),
        (4,"5")
        (5,"5")
    )
    rate = models.PositiveSmallIntegerField(choices = RATE_CHOICES, default = 0)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title 

   



