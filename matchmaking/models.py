from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):
  SUBJECT_CHOICES = [
    ('science', 'Science'),
    ('history', 'History'),
    ('math', 'Math'),
  ]

  subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
  start_time = models.DateTimeField(auto_now_add=True)
  end_time = models.DateTimeField(null=True, blank=True)
  winning_team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL, related_name='won_matches')

  def __str__(self):
    return f"Match {self.id} - {self.subject}"
    

class Team(models.Model):
  match = models.ForeignKey(Match, on_delete=models.CASCADE)
  players = models.ManyToManyField(User)

  def __str__(self):
    return f"Team {self.id} in Match {self.match.id}"
