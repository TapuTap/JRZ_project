# Generated by Django 4.2.2 on 2023-06-19 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_system', '0013_remove_application_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentDayOff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start_date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end_date')),
                ('parental_status', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Raising 1 child under 12 years old'), (1, 'Raising 2 or more children under 12 years old'), (2, 'Raising 3 or more children under 12 years old'), (3, 'Raising 1 child with disabilities'), (4, 'Raising 2 or more children with disabilities')], db_index=True, default=0, null=True, verbose_name='parental_status')),
            ],
            options={
                'verbose_name': 'parent day-off',
                'verbose_name_plural': 'parent day-offs',
            },
        ),
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npd', models.BooleanField(verbose_name='npd')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start_date')),
            ],
            options={
                'verbose_name': 'taxes',
                'verbose_name_plural': 'taxes',
            },
        ),
        migrations.CreateModel(
            name='Termination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminate_date', models.DateField(blank=True, null=True, verbose_name='terminate_date')),
            ],
            options={
                'verbose_name': 'termination',
                'verbose_name_plural': 'terminations',
            },
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start_date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end_date')),
                ('payout_before', models.BooleanField(verbose_name='payout_before')),
            ],
            options={
                'verbose_name': 'vacation',
                'verbose_name_plural': 'vacations',
            },
        ),
    ]