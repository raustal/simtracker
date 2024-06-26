# Generated by Django 4.2.11 on 2024-04-24 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medventory', '0003_unit_medication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medication',
            name='trade_name',
        ),
        migrations.CreateModel(
            name='TradeName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_name', models.CharField(max_length=64)),
                ('generic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_names', to='medventory.medication')),
            ],
        ),
        migrations.AddField(
            model_name='medication',
            name='trade_name',
            field=models.ManyToManyField(related_name='trade_names', to='medventory.tradename'),
        ),
    ]
