# from django.contrib import admin
# from .models import CustomUser, Attendance  # Import only once
# from .models import Attendance

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ("email", "username", "is_staff", "is_active")

# @admin.register(Attendance)  # ✅ Ensure it's only registered once
# class AttendanceAdmin(admin.ModelAdmin):
#     list_display = ('user', 'date', 'status')

# # class Attendance(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User model
# #     date = models.DateField()  # Make sure date exists in the model
# #     status = models.CharField(max_length=10)  # Example: 'Present', 'Absent'
    
# #     def __str__(self):
# #         return f"{self.user} - {self.date} - {self.status}"

# from django.contrib import admin
# from .models import CustomUser, Attendance  # ✅ Import only once

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ("email", "username", "is_staff", "is_active")

# @admin.register(Attendance)  # ✅ Ensure it's only registered once
# class AttendanceAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'date', 'status')  # ✅ Ensure these fields exist in Attendance
#     search_fields = ('user__email', 'date', 'status')  # Optional: Add search functionality

# # ✅ Remove duplicate registration check






from django.contrib import admin
from .models import Attendance

# ✅ Make sure you're not registering Attendance twice
if not admin.site.is_registered(Attendance):
    admin.site.register(Attendance)
