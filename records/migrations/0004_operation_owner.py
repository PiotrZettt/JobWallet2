# Generated by Django 4.0.dev20210521113437 on 2021-12-05 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('records', '0003_alter_operation_comments_alter_wallet_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='operations', to='auth.user'),
        ),
    ]
