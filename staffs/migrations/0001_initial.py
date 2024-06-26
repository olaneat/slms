# Generated by Django 3.0 on 2020-01-11 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('middle_name', models.CharField(blank=True, max_length=250, null=True)),
                ('surname', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=15)),
                ('staff_id', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='img/staff')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('blood_group', models.CharField(choices=[('AA', 'AA'), ('A+', 'A+'), ('A-', 'A-'), ('0+', '0+')], max_length=10)),
                ('nationality', models.CharField(max_length=150)),
                ('state_of_origin', models.CharField(max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Staff Profile',
                'verbose_name_plural': 'Staffs Profile',
                'ordering': ('-surname', '-first_name'),
            },
        ),
    ]
