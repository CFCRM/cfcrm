# Generated by Django 3.1.7 on 2022-01-19 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20220119_1107'),
        ('account', '0005_auto_20220119_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalResidenceDetails',
            fields=[
                ('sal_res_det_id', models.AutoField(primary_key=True, serialize=False)),
                ('addi_details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.additionaldetails')),
                ('current_location_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.city')),
                ('current_residence_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.residencetype')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.state')),
            ],
        ),
    ]
