from django.db import models

# Create your models here.

# Song file fields:
# - ID – (mandatory, integer, unique)
# - Name of the song – (mandatory, string, cannot be larger than 100
# characters)
# - Duration in number of seconds – (mandatory, integer, positive)
# - Uploaded time – (mandatory, Datetime, cannot be in the past)
# Podcast file fields:
# - ID – (mandatory, integer, unique)
# - Name of the podcast – (mandatory, string, cannot be larger than 100
# characters)
# - Duration in number of seconds – (mandatory, integer, positive)
# - Uploaded time – (mandatory, Datetime, cannot be in the past)
# - Host – (mandatory, string, cannot be larger than 100 characters)
# - Participants – (optional, list of strings, each string cannot be larger than
# 100 characters, maximum of 10 participants possible)
# Audiobook file fields:
# - ID – (mandatory, integer, unique)
# - Title of the audiobook – (mandatory, string, cannot be larger than 100
# characters)
# - Author of the title (mandatory, string, cannot be larger than 100
# characters)
# - Narrator - (mandatory, string, cannot be larger than 100 characters)
# - Duration in number of seconds – (mandatory, integer, positive)
# - Uploaded time – (mandatory, Datetime, cannot be in the past)

class Audio(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=False)
    
    class Meta:
        abstract = True

class Song(Audio):
    
    def __str__(self):
        return self.name

class Podcast(Audio):
    host = models.CharField(max_length=100)
    participants = models.JSONField(null=True)

    def __str__(self):
        return self.name

    

class Audiobook(Audio):
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)

    def __str__(self):
        return self.name