# Generated by Django 4.0.6 on 2022-08-05 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUsers', '0003_alter_posts_title_alter_users_email_alter_users_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('detailedReview', models.CharField(max_length=240)),
            ],
        ),
    ]