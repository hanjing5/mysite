from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# each of these represent a database  field

class Poll(models.Model):
    # we extend a model method 
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
        
class Choice(models.Model):
    # relations, one to many
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.choice
        
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # this field is required.
    user = models.OneToOneField(User)
    
    # Other fields here
    accepted_eula = models.BooleanField()
    favorite_animal = models.CharField(max_length=20, default="Dragons.")   