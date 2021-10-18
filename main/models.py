from django.db import models

class website(models.Model):
    website_name = models.CharField(max_length = 30)
    website_url = models.URLField(max_length = 1000)
    id = models.IntegerField(max_length = 120)
    website_description = models.CharField(max_length = 1500)