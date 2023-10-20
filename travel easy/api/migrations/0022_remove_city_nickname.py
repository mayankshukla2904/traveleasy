
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20191009_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='nickname',
        ),
    ]
