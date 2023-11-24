# Generated by Django 4.2.7 on 2023-11-24 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_diplom', '0003_manager_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_diplom.company')),
            ],
        ),
    ]