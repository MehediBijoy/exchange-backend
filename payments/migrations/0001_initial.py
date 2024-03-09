# Generated by Django 5.0.2 on 2024-03-07 17:48

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('chain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('received_address', models.CharField(max_length=255)),
                (
                    'amount',
                    models.DecimalField(
                        decimal_places=12,
                        max_digits=18,
                        validators=[
                            django.core.validators.MinValueValidator(
                                Decimal(
                                    '0.01000000000000000020816681711721685132943093776702880859375'
                                )
                            )
                        ],
                    ),
                ),
                ('paid_amount', models.DecimalField(decimal_places=12, max_digits=18)),
                ('tx_hash', models.CharField(max_length=255)),
                (
                    'status',
                    models.IntegerField(
                        choices=[(0, 'accepted'), (1, 'pending'), (2, 'confirmed')],
                        default=0,
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'base_asset',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='asset',
                        to='chain.asset',
                    ),
                ),
                (
                    'payment_address',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='key_pair',
                        to='chain.encryptedkeypair',
                    ),
                ),
            ],
            options={
                'verbose_name': 'payment',
                'verbose_name_plural': 'payments',
                'db_table': 'payment',
            },
        ),
    ]