
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='trip',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Trip'),
        ),
    ]
