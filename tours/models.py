from django.db import models

class Tour(models.Model):
    CATEGORY_CHOICES = [
        ('Popular', 'Popular'),
        ('Featured', 'Featured'),
        ('More Visited', 'More Visited'),
        ('Europe', 'Europe'),
        ('Asia', 'Asia'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=100)
    description = models.TextField()
    recommended = models.BooleanField(default=False)    

    def __str__(self):
        return self.title

     
class Review(models.Model):
    tour = models.ForeignKey(Tour, related_name='reviews', on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    user_image = models.ImageField(blank=True, null=True)
    comment = models.TextField()

    def __str__(self):
        return f'Review for {self.tour.title} by {self.name}'


class Application(models.Model):
    tour = models.ForeignKey(Tour, related_name='applications', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'Application for {self.tour.title} by {self.name}'