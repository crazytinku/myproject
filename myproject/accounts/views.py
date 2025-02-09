from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Rename login to avoid conflicts
from django.contrib import messages
from django.utils.timezone import now
from django.conf import settings
from django.contrib.auth.decorators import login_required
from pymongo import MongoClient
from django.contrib.auth.views import LoginView
from datetime import datetime
from .models import Attendance

# Safely retrieve MongoDB connection details
client_settings = settings.DATABASES['default'].get('CLIENT', {})
mongo_host = client_settings.get('host', 'mongodb://localhost:27017/')

# Connect to MongoDB
client = MongoClient(mongo_host)
db = client[settings.DATABASES['default']['NAME']]
users_collection = db['USERS']  # Change 'USERS' if your collection name is different

def custom_login(request):
    """Handles user login and stores user details in MongoDB."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Log in the user
            messages.success(request, "Login successful!")

            # Store user details in MongoDB
            user_data = {
                "username": user.username,
                "email": user.email,
                "last_login": now(),
            }
            users_collection.update_one(
                {"username": user.username},  # Find user by username
                {"$set": user_data},  # Update user data
                upsert=True  # Insert if not exists
            )

            return redirect('/dashboard/')  # Redirect to dashboard
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'registration/login.html')  # Ensure this template exists

@login_required
def dashboard(request):
    """Renders the dashboard for the logged-in user."""
    return render(request, 'registration/dashboard.html')  # Ensure this template exists

# @login_required
# def profile(request):
#     """Renders the user profile page."""
#     return render(request, 'registration/profile.html')  # Ensure this template exists

# from datetime import datetime



# @login_required
# def todays_attendance(request):
#     """Displays today's attendance records."""
#     today = datetime.today().date()  # Get today's date
#     Attendance.objects.filter(time__date=today)  # ✅ Correct lookup
#     return render(request, 'registration/todays_attendance.html', {'attendance_records': attendance_records})

from datetime import datetime
from django.shortcuts import render
from .models import Attendance

def todays_attendance(request):
    today = datetime.today().date()  # Get today's date

    # Fix: Fetch records and manually compare the date
    attendance_records = [
        record for record in Attendance.objects.all()
        if record.time.date() == today
    ]

    return render(request, 'registration/todays_attendance.html', {'attendance_records': attendance_records})
