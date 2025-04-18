# Generated by Django 4.2.18 on 2025-02-02 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Job position title', max_length=200)),
                ('company', models.CharField(help_text='Company offering the position', max_length=200)),
                ('description', models.TextField(help_text='Detailed job description')),
                ('employment_type', models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract'), ('freelance', 'Freelance'), ('internship', 'Internship')], help_text='Type of employment offered', max_length=20)),
                ('location', models.CharField(help_text="Job location or 'Remote'", max_length=200)),
                ('salary_range', models.CharField(blank=True, help_text='Expected salary range', max_length=100)),
                ('posted_date', models.DateTimeField(auto_now_add=True, help_text='When the job was posted')),
                ('required_skills', models.ManyToManyField(help_text='Skills required for this position', related_name='required_for_jobs', to='skills.skill')),
            ],
        ),
    ]
