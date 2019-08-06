from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager

#Modelo User
#sirve crear usuario y para el manejo de lus usuario 
class User(AbstractBaseUser, PermissionsMixin):
    customer_id = models.AutoField(primary_key=True)
    email = models.EmailField(_('Email Address'), unique=True)
    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Staff'), default=False)
    credit_card = models.TextField()
    address_1 = models.CharField(max_length=250)
    address_2 = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    day_phone = models.CharField(max_length=250)
    eve_phone = models.CharField(max_length=250)
    mob_phone = models.CharField(max_length=250)
    image =  models.ImageField(upload_to="perfil_imagenes", blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return f'{self.email}'
