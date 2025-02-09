from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class NTTFEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()

        # Ensure username is valid and ends with '@nttf.co.in'
        if not username or not username.endswith('@nttf.co.in'):
            return None  # Return None instead of raising an exception

        # Fetch the user by email safely using filter().first() to avoid MultipleObjectsReturned
        user = User.objects.filter(email=username).first()

        if user and user.check_password(password):
            return user  # Return authenticated user

        return None  # Return None if authentication fails
