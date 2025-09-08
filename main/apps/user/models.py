from django.db import models

from main.apps.user.manager import UserManager
from ..common.models import BaseModel, BaseMeta
from django.contrib.auth.models import User 
from django.utils.translation import gettext as _

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _




class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    username = models.CharField(max_length=100, unique=True, null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site.",
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting account."
        ),
    )
    is_moderator = models.BooleanField(_("moderator status"), default=False)
    is_superuser = models.BooleanField(_("superuser status"), default=False)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    # role = models.CharField(max_length=10, choices=RoleChoices.choices)
    objects = UserManager()

    USERNAME_FIELD = "username"

    class Meta(BaseMeta):
        db_table = "user"
        verbose_name = _("user")
        verbose_name_plural = _("users")


    @property
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return f"{self.first_name}"

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


    def __str__(self):
        return f"{self.username} {self.first_name}"