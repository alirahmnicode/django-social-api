from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

from .managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
    )
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self) -> str:
        return self.username


class Profile(models.Model):
    """User profile model"""
    
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(_("First Name"), max_length=250, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=250, blank=True)
    avatar = models.ImageField(_("User Profile Image"), upload_to="avatar")
    following = models.ManyToManyField(
        CustomUser, verbose_name=_("following"), related_name="following"
    )
    followers = models.ManyToManyField(
        CustomUser, verbose_name=_("followers"), related_name="followers"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
