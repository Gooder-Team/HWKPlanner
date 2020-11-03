import datetime

from django.db import models
import django.utils


class Assignment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="DESCRIPTION OF ASSIGNMENT!")
    teacher = models.CharField(max_length=20, default="YOUR NAME HERE!")
    subject = models.CharField(max_length=20, default="SUBJECT HERE!")
    pub_date = models.DateTimeField('date published', default=django.utils.timezone.now)
    due_date = models.DateTimeField('date due', default=django.utils.timezone.now)
    students = models.ManyToManyField('app.Student', blank=True)
    # student1 = models.BooleanField()
    # student2 = models.BooleanField()
    # student3 = models.BooleanField()
    # student4 = models.BooleanField()
    def __str__(self):
        return self.name
    def was_published_recently(self):
        now = django.utils.timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'
    def is_due(self):
        now = django.utils.timezone.now()


class Student(models.Model):
    # assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    # assignment = models.ManyToManyField(Assignment)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
