from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class ClienteUserManager(BaseUserManager):

    def create_user(self, email, data_nascimento, senha):
        if not email:
            raise ValueError('Email é obrigatório para criação de usuário.')

        user = self.model(
            email=self.normalize_email(email),
            data_nascimento=data_nascimento,
        )

        user.set_password(senha)
        user.save(using=self._db)
        return user


class ClienteUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    data_nascimento = models.DateField()
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = ClienteUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['data_nascimento']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
