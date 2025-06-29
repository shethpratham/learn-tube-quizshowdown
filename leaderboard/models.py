from django.db import models
from django.contrib.auth.models import User

class LeaderboardEntry(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  total_score = models.IntegerField(default=0)
  global_rank = models.IntegerField(null=True, blank=True)
  country = models.CharField(max_length=100)
  country_rank = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return f"{self.user.username} - {self.total_score} pts"
