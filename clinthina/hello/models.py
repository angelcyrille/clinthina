from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    year_level = models.IntegerField()

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"