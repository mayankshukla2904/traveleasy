
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_merge_20180703_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.TextField(default=None, null=True),
        ),
    ]
