from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailBackend(ModelBackend):
    """Custom authentication backend that uses email instead of username"""

    def authenticate(self, request, username=None, password=None, email=None, **kwargs):
        """
        Authenticate user using email and password
        """
        # Allow both 'username' and 'email' parameters
        email = email or username

        if email is None or password is None:
            return None

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        # Check the password
        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        """
        Get user by ID
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
