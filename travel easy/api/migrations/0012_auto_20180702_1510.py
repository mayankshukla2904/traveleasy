
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_cityvisitlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_name',
            field=models.CharField(max_length=128),
        ),
    ]
