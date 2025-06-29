from django.db import models
from django.contrib.auth.models import User
from matchmaking.models import Match, Team

class Question(models.Model):
  subject = models.CharField(max_length=50)
  text = models.TextField()
  choices = models.JSONField()  # e.g., {"A": "Option1", "B": "Option2"}
  correct_choice = models.CharField(max_length=1)  # e.g., 'A'
  created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  approved = models.BooleanField(default=False)

  def __str__(self):
    return f"Q{self.id} - {self.subject}"


class PlayerScore(models.Model):
  player = models.ForeignKey(User, on_delete=models.CASCADE)
  match = models.ForeignKey(Match, on_delete=models.CASCADE)
  team = models.ForeignKey(Team, on_delete=models.CASCADE)
  score = models.IntegerField(default=0)
  answers = models.JSONField(default=dict)  # e.g., {"q1": {"choice": "B", "correct": True, "time": 2.1}}

  def __str__(self):
    return f"{self.player.username} - {self.score} pts in Match {self.match.id}"
