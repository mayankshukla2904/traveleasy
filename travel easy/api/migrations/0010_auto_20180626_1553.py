
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='image',
        ),
        migrations.AlterField(
            model_name='cityimage',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.City'),
        ),
        migrations.AlterField(
            model_name='cityimage',
            name='image_url',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
