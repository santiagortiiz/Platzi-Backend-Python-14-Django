from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    """
    Proxy model that extends from base User Info
    """

    # class OneToOneField(to, on_delete, parent_link=False, **options)
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Relation with User of django.contrib.auth.models.User

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username