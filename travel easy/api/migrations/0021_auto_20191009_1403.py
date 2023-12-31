
import api.modules.users.enums
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_trip_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordverification',
            name='mode',
            field=models.TextField(choices=[(api.modules.users.enums.PasswordVerificationModeChoice('Forget Password'), 'Forget Password'), (api.modules.users.enums.PasswordVerificationModeChoice('Email Verification'), 'Email Verification')], default=api.modules.users.enums.PasswordVerificationModeChoice('Forget Password'), max_length=30),
        ),
        migrations.AlterField(
            model_name='passwordverification',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='passwordverification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
