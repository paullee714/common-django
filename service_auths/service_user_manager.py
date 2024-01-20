from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, nickname, email, password):
        if not email:
            raise ValueError("이메일은 필수값입니다.")
        user = self.model(nickname=nickname, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, email, password):
        user = self.create_user(
            nickname=nickname, email=self.normalize_email(email), password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username, "is_active": True})
