from django.contrib.auth.password_validation import CommonPasswordValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

# https://docs.djangoproject.com/en/2.0/_modules/django/contrib/auth/password_validation/#MinimumLengthValidator


class CommonPasswordValidatorCustom(CommonPasswordValidator):
    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                _(
                    "Your password was found in a database with most common passwords! Please eneter another password!"
                ),
                code="password_too_common",
            )
