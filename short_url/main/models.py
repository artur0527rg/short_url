from django.db import models

# Create your models here.
class LinksModel(models.Model):
    # Generate link
    gen_link = models.CharField(max_length=300, unique=True)
    # User link
    cl_link = models.CharField(max_length=600)