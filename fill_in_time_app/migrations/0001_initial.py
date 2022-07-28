# Generated by Django 4.0.3 on 2022-07-12 16:42

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentsDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='店舗名もしくは場所の名前を入力してください', max_length=100)),
                ('address', models.CharField(help_text='住所を入力してください', max_length=150)),
                ('homepage', models.CharField(blank=True, help_text='URLを入力してください', max_length=100, null=True)),
                ('classification', models.IntegerField(blank=True, choices=[(1, '見る'), (2, '聞く'), (3, '体験する'), (4, '食べる'), (5, '飲む'), (6, '運動')], verbose_name='classification')),
                ('telephone', models.CharField(blank=True, help_text='電話番号を入力してください', max_length=20, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='media/contents', verbose_name='icon')),
                ('price', models.IntegerField(blank=True, choices=[(0, '0円'), (1000, '1000円以内'), (2000, '2000円以内'), (3000, '3000円以内'), (4000, '4000円以内'), (5000, '5000円以内'), (5001, '5000円以上')], verbose_name='price')),
                ('detail', models.TextField(blank=True, max_length=255, null=True)),
                ('open_time', models.TextField(blank=True, help_text='営業時間を入力してください', max_length=255, null=True)),
                ('not_open_day', models.CharField(blank=True, help_text='定休日を入力してください', max_length=100, null=True)),
                ('min_stay_time', models.FloatField(choices=[(0.25, '15分'), (0.5, '30分'), (1.0, '1時間'), (1.5, '1時間半'), (2.0, '2時間'), (2.5, '2時間半'), (3.0, '3時間'), (4.0, '4時間'), (5.0, '5時間')], verbose_name='min_stay_time')),
                ('max_stay_time', models.FloatField(choices=[(0.25, '15分'), (0.5, '30分'), (1.0, '1時間'), (1.5, '1時間半'), (2.0, '2時間'), (2.5, '2時間半'), (3.0, '3時間'), (4.0, '4時間'), (5.0, '5時間')], verbose_name='max_stay_time')),
                ('how_come', models.TextField(blank=True, help_text='アクセス方法を入力してください', max_length=255, null=True)),
                ('comments', models.TextField(blank=True, max_length=255, null=True)),
                ('star', models.FloatField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='star')),
                ('editer', models.TextField()),
                ('renew_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'contentsDB',
                'verbose_name_plural': 'contentsDB',
            },
        ),
        migrations.CreateModel(
            name='UserDB',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(help_text='ニックネームを入力してください', max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='media/user/icon', verbose_name='icon')),
                ('profile', models.TextField(blank=True, help_text='プロフィールを255字以内で入力してください', verbose_name='profile')),
                ('birthday', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='birthday')),
                ('gender', models.IntegerField(blank=True, choices=[(1, 'woman'), (2, 'man'), (3, 'other')], null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('password_changed', models.BooleanField(default=False, null=True)),
                ('password_changed_date', models.DateTimeField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'UserDB',
                'verbose_name_plural': 'UserDB',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]