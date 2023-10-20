
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_profile_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
