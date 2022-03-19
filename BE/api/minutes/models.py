from django.db import models
from community.models import Member


class Minute(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    conclusion = models.TextField(max_length=300)
    is_closed = models.BooleanField(default=False)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reference_file = models.FileField(upload_to='', null=True)

    def __str__(self):
        return self.title


class Participant(models.Model):
    minute = models.ForeignKey(Minute, on_delete=models.CASCADE)
    is_assignee = models.BooleanField(default=False)


class Speech(models.Model):
    minute = models.ForeignKey(Minute, on_delete=models.CASCADE)
    participant = models.OneToOneField(Participant, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    summary = models.TextField(max_length=400)
    cloud_keyword = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    record_file = models.FileField(upload_to='', null=True)
    reference_file = models.FileField(upload_to='', null=True)
    
    def __str__(self):
        return self.title


class SpeechComment(models.Model):
    speech = models.ForeignKey(Speech, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content