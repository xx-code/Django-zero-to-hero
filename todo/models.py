from django.db import models

INDICATOR_TASK = [
    ('Urgent', 'Urgently '),
    ('Normal', 'Normal'),
    ('Low', 'Lower')
]

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=500)
    due_date = models.DateTimeField('due date')
    detail = models.TextField()
    indicator = models.CharField(choices=INDICATOR_TASK, max_length=10)

    def __str__(self):
        return self.title
    
    @property
    def sort_description(self):
        raise('Methode not implemented')


