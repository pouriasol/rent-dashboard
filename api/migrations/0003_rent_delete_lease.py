# Generated by Django 4.1.3 on 2022-11-02 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_alter_lease_landlord_alter_lease_tenant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mortgage_amount', models.IntegerField()),
                ('rent_amount', models.IntegerField()),
                ('meterage', models.IntegerField()),
                ('type', models.CharField(max_length=30)),
                ('use', models.CharField(max_length=30)),
                ('bedrooms', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=11)),
                ('zip', models.CharField(max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rent_landlord', to=settings.AUTH_USER_MODEL)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rent_tenant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='lease',
        ),
    ]