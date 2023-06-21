# Generated by Django 4.2.2 on 2023-06-21 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hr_system', '0019_applicationinstance_applicant_alter_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationinstance',
            name='applicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicant_instances', to=settings.AUTH_USER_MODEL, verbose_name='applicant'),
        ),
        migrations.AlterField(
            model_name='applicationinstance',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('New', 'New'), ('Approved', 'Approved'), ('Declined', 'Declined')], db_index=True, default=0, null=True, verbose_name='status'),
        ),
    ]
