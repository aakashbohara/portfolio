# Generated manually to fix terminal hang issues
import fontawesome_6.fields
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilesetting',
            name='logo',
            field=models.ImageField(blank=True, help_text='Upload a logo to replace the text name in navbar', null=True, upload_to='profile/logo/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=fontawesome_6.fields.IconField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=fontawesome_6.fields.IconField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='icon',
            field=fontawesome_6.fields.IconField(blank=True, max_length=100),
        ),
    ]
