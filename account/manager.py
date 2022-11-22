from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('email could not be empty')
        elif not username:
            raise ValueError('username could not be empty')
        elif not password:
            raise ValueError('password could not be empty')

        else:
            user = self.model(
                email=email,
                username=username
            )
            user.set_password(password)
            user.is_valid = True
            user.save()
            return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save()
        return user
