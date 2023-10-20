
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_profile_last_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='nickname',
            field=models.TextField(blank=True, null=True),
        ),
    ]
