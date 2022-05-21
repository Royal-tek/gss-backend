# Generated by Django 3.2.6 on 2022-05-21 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=256)),
                ('lastname', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=256)),
                ('occupation', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=256)),
                ('lastname', models.CharField(max_length=256)),
                ('dob', models.DateField()),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=256)),
                ('state_of_origin', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('next_of_kin_number', models.IntegerField()),
                ('disabilities', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.parent')),
            ],
        ),
    ]
