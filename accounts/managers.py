from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Manager for custom user model"""

    def create_user(self, username, email, password=None):
        """Create a new user"""
        if not email:
            raise ValueError("User must have an email adress")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """Create new superuser"""
        user = self.create_user(username=username, email=email, password=password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user