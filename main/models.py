import uuid
from django.db import models
from django.utils import timezone

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(default=timezone.now())
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Skill(models.Model):
    SKILL_LEVEL = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('upper-intermediate', 'Upper-Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=SKILL_LEVEL, default='intermediate')
    certification = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def prioritize(self):
        return self.level == 'upper-intermediate' 

    @property
    def highlight(self):
        return self.level == 'advanced' or self.level == 'expert'

    @property
    def certif_available(self):
        return self.certification is not None

class Projects(models.Model):
    PROJECT_STATUS = [
        ('ongoing', 'Ongoing'),
        ('finished', 'Finished'),
    ]

    PROJECT_TYPE = [
        ('solo', 'Solo'),
        ('team', 'Team'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=PROJECT_STATUS)
    type = models.CharField(max_length=20, choices=PROJECT_TYPE)
    link = models.URLField(blank=True, null=True)

    @property
    def is_solo(self):
        return self.type == 'solo'

    @property
    def link_available(self):
        return self.link is not None
