# Generated by Django 5.0.2 on 2024-04-02 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_rename_words_sents_readingtest_words_and_sents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 1',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 10',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 11',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 12',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 13',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 14',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 15',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 16',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 17',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 18',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 19',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 2',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 20',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 3',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 4',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 5',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 6',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 7',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 8',
        ),
        migrations.RemoveField(
            model_name='level_1_const',
            name='word 9',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='sound_id',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 1',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 10',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 11',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 12',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 13',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 14',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 15',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 16',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 17',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 18',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 19',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 2',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 20',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 3',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 4',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 5',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 6',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 7',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 8',
        ),
        migrations.RemoveField(
            model_name='level_2_v_d',
            name='word 9',
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_1',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_10',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_11',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_12',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_13',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_14',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_15',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_16',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_17',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_18',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_19',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_2',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_20',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_3',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_4',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_5',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_6',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_7',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_8',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_1_const',
            name='word_9',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_1',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_10',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_11',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_12',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_13',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_14',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_15',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_16',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_17',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_18',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_19',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_2',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_20',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_3',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_4',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_5',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_6',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_7',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_8',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='level_2_v_d',
            name='word_9',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
