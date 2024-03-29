# Generated by Django 5.0.2 on 2024-02-17 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_rename_firstname_contact_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address_aptnum',
            field=models.CharField(blank=True, max_length=10, verbose_name='Address Apartment Number'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address_city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address_country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address_street',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address_zip',
            field=models.CharField(blank=True, max_length=10, verbose_name='Address ZIP Code'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_of_birth',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='social_github',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='social_instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='social_linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='social_twitter',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
