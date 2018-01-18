from django.db import models

# Create your models here.


class Song(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)
    title = models.CharField(max_length=64)
    tuning = models.CharField(max_length=2)
    starting_note = models.CharField(max_length=2)
    ending_note = models.CharField(max_length=2)
    starting_fifth = models.CharField(max_length=2)
    actual_tuning = models.CharField(max_length=2)
    active = models.BooleanField()

    def __str__(self):
        return self.title
