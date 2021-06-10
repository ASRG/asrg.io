from django.contrib.auth.password_validation import CommonPasswordValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

# https://docs.djangoproject.com/en/2.0/_modules/django/contrib/auth/password_validation/#MinimumLengthValidator


class CommonPasswordValidatorCustom(CommonPasswordValidator):
    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                _("This password is too common. The password needs to include: TODO "),
                code="password_too_common",
            )
