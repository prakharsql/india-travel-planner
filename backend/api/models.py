from django.db import models


class City(models.Model):
    name = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    description = models.TextField(blank=True, default='')
    best_time_to_visit = models.CharField(max_length=255, blank=True, default='')
    image = models.URLField(max_length=500, blank=True, default='')
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    travel_tips = models.TextField(blank=True, default='')

    class Meta:
        verbose_name_plural = 'cities'
        ordering = ['name']

    def __str__(self):
        return self.name


class Place(models.Model):
    CATEGORY_CHOICES = [
        ('historical', 'Historical'),
        ('nature', 'Nature'),
        ('adventure', 'Adventure'),
        ('religious', 'Religious'),
        ('beach', 'Beach'),
        ('cultural', 'Cultural'),
    ]

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='places')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='historical')
    timing = models.CharField(max_length=100, blank=True, default='')
    entry_fee = models.CharField(max_length=100, blank=True, default='Free')
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    image = models.URLField(max_length=500, blank=True, default='')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.city.name})"


class Food(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='foods')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.city.name})"
