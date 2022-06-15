from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
import uuid as uuid_lib


class CustomUserManager(UserManager):
  use_in_migrations = True
  def _create_user(self, username, email, password, **extra_fields):
    if not email:
      raise ValueError('The given email must be set')
    email = self.normalize_email(email)
    username = self.model.normalize_username(username)
    user = self.model(username, email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_user(self, username, email, password=None, **extra_fields):
      extra_fields.setdefault('is_staff', False)
      extra_fields.setdefault('is_superuser', False)
      return self._create_user(username, email, password, **extra_fields)

  def create_superuser(self, username, email, password, **extra_fields):
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)
      
      if extra_fields.get("is_staff") is not True:
          raise ValueError('Superuser must have is_staff=True.')
      if extra_fields.get("is_superuser") is not True:
          raise ValueError('Superuser must have is_superuser=True.')
      return self._create_user(username, email, password, **extra_fields)


class UserDB(AbstractBaseUser, PermissionsMixin):
    """Custom User"""
    class Meta:
        verbose_name = 'userDB'
        verbose_name_plural = 'userDB'


    GENDER_CHOICES = (
    ('1', 'woman'),
    ('2', 'man'),
    ('3', 'other'),
    )

    uuid = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)     # 管理ID
    username_validators = UnicodeUsernameValidator()     #不正な文字列が含まれていないかチェック
    username = models.CharField(max_length=13, unique=True, help_text="ニックネームを入力してください")     #ユーザ氏名
    email = models.EmailField(unique=True, null=False, blank=False)     #メールアドレス = これで認証する
    icon = models.ImageField('icon', upload_to='media/user/icon', null=True, blank=True)     #アイコン
    profile = models.TextField('profile', blank=True, help_text="プロフィールを255字以内で入力してください")     #プロフィール
    birthday = models.DateField('birthday', null=True, default=timezone.now)     #誕生日
    gender = models.CharField("gender", max_length=1, choices=GENDER_CHOICES, blank=False)     #性別
    is_active = models.BooleanField(default=True) # アクティブ権限
    is_staff = models.BooleanField(default=False) # スタッフ権限
    is_superuser = models.BooleanField(default=False) # 管理者権限
    date_joined = models.DateTimeField(default=timezone.now) # アカウント作成日時
    password_changed = models.BooleanField(default=False) # パスワードを変更したかどうかのフラグ
    password_changed_date = models.DateTimeField(blank=True, null=True) # 最終パスワード変更日時

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELD = ['email', 'username']

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username


class ContentsDB(models.Model):
    class Meta:
        verbose_name = 'contentsDB'
        verbose_name_plural = 'contentsDB'
    
    name = 0
    address = 0
    classification = 0
    telephone = 0
    picture = 0
    price = 0
    detail = 0
    open_time = 0
    stay_time = 0
    comments = 0
    star = 0
    editer = 0
    renew_date = 0
    
    