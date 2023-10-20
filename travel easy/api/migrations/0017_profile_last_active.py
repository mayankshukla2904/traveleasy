
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_passwordverification'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_active',
            field=models.DateTimeField(null=True),
        ),
    ]
