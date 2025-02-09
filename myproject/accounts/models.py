from django.db import models

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)  # ✅ Add this if missing
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)
