from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return self.name