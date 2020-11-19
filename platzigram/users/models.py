""" User models """
# Django
from django.contrib.auth.models import User
from django.db import models

# Models
class Profile(models.Model):
    """ Profile models

    proxy model extends the base data with other information.
    """
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    
    """ The model extended """
    website = models.URLField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    """ return object username"""

    def __str__(self):
        return self.user.username

