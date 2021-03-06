# Generated by Django 3.0.7 on 2020-09-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0009_auto_20200824_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawNEU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PIN_Patient', models.CharField(max_length=100)),
                ('Member_c', models.CharField(choices=[('1', 'mother'), ('2', 'father'), ('3', 'child')], max_length=1)),
                ('TimePeriod', models.CharField(choices=[('1', '16-20 weeks'), ('2', '22-26 weeks'), ('3', '24-28 weeks')], max_length=1)),
                ('Analyte', models.CharField(choices=[('USB', 'Antimony - Urine'), ('UTAS', 'Arsenic - Urine'), ('UBA', 'Barium - Urine'), ('UBE', 'Beryllium - Urine'), ('UCD', 'Cadmium - Urine'), ('UCS', 'Cesium - Urine'), ('UCR', 'Chromium - Urine'), ('UCO', 'Cobalt - Urine'), ('UCU', 'Copper - Urine'), ('UPB', 'Lead - Urine'), ('UMN', 'Manganese - Urine'), ('UHG', 'Mercury - Urine'), ('UMO', 'Molybdenum - Urine'), ('UNI', 'Nickel - Urine'), ('UPT', 'Platinum - Urine'), ('USE', 'Selenium - Urine'), ('UTL', 'Thallium - Urine'), ('USN', 'Tin - Urine'), ('UTU', 'Tungsten - Urine'), ('UUR', 'Uranium - Urine'), ('UVA', 'Vanadium - Urine'), ('UZN', 'Zinc - Urine'), ('BSB', 'Antimony - Blood'), ('BTAS', 'Arsenic - Blood'), ('BAL', 'Aluminum - Blood'), ('BBE', 'Beryllium - Blood'), ('BBA', 'Barium - Blood'), ('BCD', 'Cadmium - Blood'), ('BCS', 'Cesium - Blood'), ('BCO', 'Cobalt - Blood'), ('BCU', 'Copper - Blood'), ('BCR', 'Chromium - Blood'), ('BFE', 'Iron - Blood'), ('BPB', 'Lead - Blood'), ('BPB2', 'Lead (208) - Blood'), ('BMB', 'Manganese - Blood'), ('BHG', 'Mercury - Blood'), ('BMO', 'Molybdenum - Blood'), ('BNI', 'Nickel - Blood'), ('BPT', 'Platinum - Blood'), ('BTL', 'Thallium - Blood'), ('BTU', 'Tungsten - Blood'), ('BUR', 'Uranium - Blood'), ('BVA', 'Vanadium - Blood'), ('BSE', 'Selenium - Blood'), ('BSEG', 'Selenium+G1124 - Blood'), ('BSN', 'Tin - Blood'), ('BZN', 'Zinc - Blood')], max_length=4)),
                ('Result', models.FloatField()),
                ('LOD', models.FloatField()),
                ('Outcome', models.CharField(blank=True, choices=[('0', 'term'), ('1', 'preterm')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='rawunm',
            name='TimePeriod',
            field=models.CharField(choices=[('1', 'enrollment'), ('3', 'week 36/delivery')], max_length=1),
        ),
    ]
