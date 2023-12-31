
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_auto_20180626_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('COMMON', 'Common'), ('TRIP', 'Trip')], default='Common', max_length=100)),
                ('text', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('destined_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destined_user', to=settings.AUTH_USER_MODEL)),
                ('initiator_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiator_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
