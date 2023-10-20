
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_city_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
