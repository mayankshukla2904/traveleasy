
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180624_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityfact',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facts', to='api.City'),
        ),
    ]
