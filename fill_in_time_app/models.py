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
        verbose_name = 'UserDB'
        verbose_name_plural = 'UserDB'


    GENDER_CHOICES = (
    (1, 'woman'),
    (2, 'man'),
    (3, 'other'),
    )

    uuid = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)     # 管理ID
    username_validators = UnicodeUsernameValidator()     #不正な文字列が含まれていないかチェック
    username = models.CharField(max_length=15, unique=True, help_text="ニックネームを入力してください")     #ユーザ氏名
    email = models.EmailField(unique=True, null=False, blank=False)     #メールアドレス = これで認証する
    icon = models.ImageField('icon', upload_to='media/user/icon', null=True, blank=True)     #アイコン
    profile = models.TextField('profile', blank=True, help_text="プロフィールを255字以内で入力してください")     #プロフィール
    birthday = models.DateField('birthday', blank=True, default=timezone.now)     #誕生日
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=True, null=True)     #性別
    is_active = models.BooleanField(default=True) # アクティブ権限
    is_staff = models.BooleanField(default=False) # スタッフ権限
    is_superuser = models.BooleanField(default=False) # 管理者権限
    date_joined = models.DateTimeField(default=timezone.now) # アカウント作成日時
    password_changed = models.BooleanField(default=False, null=True) # パスワードを変更したかどうかのフラグ
    password_changed_date = models.DateTimeField(null=True) # 最終パスワード変更日時

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
        return self.uuid

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.username


class ContentsDB(models.Model):
    class Meta:
        verbose_name = 'contentsDB'
        verbose_name_plural = 'contentsDB'
    
    classifications = (
        (1, '見る'),
        (2, '聞く'),
        (3, '体験する'),
        (4, '食べる'),
        (5, '飲む'),
        (6, '運動'),
    )
    prices = (
        (0, '0円'),
        (1000, '1000円以内'),
        (2000, '2000円以内'),
        (3000, '3000円以内'),
        (4000, '4000円以内'),
        (5000, '5000円以内'),
        (5001, '5000円以上'),
    )
    stay_time = (
        (0.25, '15分'),
        (0.50, '30分'),
        (1.00, '1時間'),
        (1.50, '1時間半'),
        (2.00, '2時間'),
        (2.50, '2時間半'),
        (3.00, '3時間'),
        (4.00, '4時間'),
        (5.00, '5時間'),
    )
    stars = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    name = models.CharField(max_length=100, blank=False, null=False, help_text="店舗名もしくは場所の名前を入力してください")     #店舗もしくは場所の名前
    address = models.CharField(max_length=150, blank=False, null=False, help_text="住所を入力してください")     #店舗もしくは場所の住所
    homepage = models.CharField(max_length=100, blank=True, null=True, help_text="URLを入力してください")     #店舗もしくは場所のURL
    classification = models.IntegerField("classification", choices=classifications, blank=True)     #分類
    telephone = models.CharField(max_length=20, blank=True, null=True, help_text="電話番号を入力してください")     #店舗もしくは場所の電話番号
    picture = models.ImageField('icon', upload_to='media/contents', null=True, blank=True)     #写真
    price = models.IntegerField('price', choices=prices, blank=True)     #価格
    detail = models.TextField(max_length=255, blank=True, null=True)     #詳細
    open_time = models.TextField(max_length=255, blank=True, null=True, help_text="営業時間を入力してください")      #営業時間
    not_open_day = models.CharField(max_length=100, blank=True, null=True, help_text="定休日を入力してください")     #定休日
    min_stay_time = models.FloatField("min_stay_time", choices=stay_time, blank=False, null=False)     #最小滞在時間
    max_stay_time = models.FloatField("max_stay_time", choices=stay_time, blank=False, null=False)     #最大滞在時間
    how_come = models.TextField(max_length=255, blank=True, null=True, help_text="アクセス方法を入力してください")      #アクセス
    comments = models.TextField(max_length=255, blank=True, null=True)      #コメント
    star = models.FloatField("star", choices=stars, blank=True)     #評価
    editer = models.TextField(blank=False, null=False)     #作成者
    renew_date = models.DateTimeField(default=timezone.now)      #最新更新日
    
    # 投稿1つずつの表紙
    def __str__(self):
        return self.name