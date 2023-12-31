
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_feedback_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityfact',
            name='source_text',
            field=models.TextField(default='Google'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cityfact',
            name='source_url',
            field=models.TextField(default='https://www.google.com'),
            preserve_default=False,
        ),
    ]
