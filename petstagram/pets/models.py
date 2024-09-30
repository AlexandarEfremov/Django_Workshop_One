from django.db import models
from django.template.defaultfilters import slugify


class Pet(models.Model):
    name = models.CharField(
        max_length=30,
    )
    personal_photo = models.URLField()
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )
    #we need to override the save() and pass it to our super()
    #as the slug model can be blank, we need to give it the parameters as per
    #the problem description: name - id
    #then we call the super() so the changes can be pushe dto our DB
    #if we call it earlier then it will save the current changes and bypass the rest
    #of the logic
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(f"{self.name}-{self.id}")
        super().save(*args, **kwargs)