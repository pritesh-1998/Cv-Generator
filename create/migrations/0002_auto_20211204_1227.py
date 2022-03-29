# Generated by Django 3.2.9 on 2021-12-04 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumedata',
            name='achievements',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='end',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='martial_status',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='school',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='skills1',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='skills2',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='skills3',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='skills4',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='social_media',
        ),
        migrations.RemoveField(
            model_name='resumedata',
            name='start',
        ),
        migrations.AddField(
            model_name='resumedata',
            name='b_year',
            field=models.CharField(default='bachelors degree year', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='bd',
            field=models.CharField(default='bachelors degree degree', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='binst',
            field=models.CharField(default='bachelors degree institute', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='bt',
            field=models.CharField(default='bachelors degree town', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='company_name',
            field=models.CharField(default='company Name', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='company_name1',
            field=models.CharField(default='company Name', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='company_name2',
            field=models.CharField(default='company Name', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='end_date',
            field=models.CharField(default='end Date', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='end_date1',
            field=models.CharField(default='end Date', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='end_date2',
            field=models.CharField(default='end Date', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='job_town',
            field=models.CharField(default='job Town', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='job_town1',
            field=models.CharField(default='job Town', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='job_town2',
            field=models.CharField(default='job Town', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='jobdes',
            field=models.CharField(default='job Designation', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='jobdes1',
            field=models.CharField(default='job Designation', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='jobdes2',
            field=models.CharField(default='job Designation', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='jobdescription',
            field=models.CharField(default='Job Description', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='jobdescription1',
            field=models.CharField(default='Job Description', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='jobdescription2',
            field=models.CharField(default='Job Description', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='p_year',
            field=models.CharField(default='post degreeyear', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='pd',
            field=models.CharField(default='post graduation degree', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='pdf',
            field=models.FileField(blank=True, upload_to='resources/pdf_files'),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='pinst',
            field=models.CharField(default='post degree institute', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='pt',
            field=models.CharField(default='post degree town', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='ref_company',
            field=models.CharField(default='reference_company', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='ref_des',
            field=models.CharField(default='reference_des', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='ref_email',
            field=models.CharField(default='reference_email', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='ref_name',
            field=models.CharField(default='reference_name', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='ref_phone',
            field=models.CharField(default='reference_phone', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='resumeobj',
            field=models.CharField(default='resumeobj', max_length=10000),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='skills',
            field=models.CharField(default='skills1', max_length=2000),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='start_date',
            field=models.CharField(default='start Date', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='start_date1',
            field=models.CharField(default='start Date', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='start_date2',
            field=models.CharField(default='start Date', max_length=100),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='website',
            field=models.URLField(default='websiteaddress.com', max_length=800),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='word_files',
            field=models.FileField(blank=True, upload_to='resources/word_files'),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='zipcode',
            field=models.CharField(default='400607', max_length=10),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='address',
            field=models.CharField(default='Proper address', max_length=800),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='city',
            field=models.CharField(default='city', max_length=100),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='fname',
            field=models.CharField(default='name', max_length=100),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='hobbies',
            field=models.CharField(default='hobbies', max_length=100),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='linkedIn_url',
            field=models.URLField(default='linkedin.com', max_length=800),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='lname',
            field=models.CharField(default='lname', max_length=100),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='nationality',
            field=models.CharField(default='nationality', max_length=50),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='phone',
            field=models.CharField(default='123456789', max_length=100),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='place_of_birth',
            field=models.CharField(default='place_of_birth', max_length=100),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='resources/profileimages'),
        ),
    ]
