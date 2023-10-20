
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='type',
            field=models.CharField(default='Other', max_length=255),
        ),
    ]
