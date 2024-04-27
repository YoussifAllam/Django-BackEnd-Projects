from django.db import models

# LEVELS TABLES

class Level_1_const(models.Model):
    # sound_id = models.AutoField(primary_key=True)
    sound = models.CharField(max_length = 10)
    description = models.TextField()
    word_1 = models.CharField(max_length=40, blank=True)
    word_2 = models.CharField(max_length=40, blank=True)
    word_3 = models.CharField(max_length=40, blank=True)
    word_4 = models.CharField(max_length=40, blank=True)
    word_5 = models.CharField(max_length=40, blank=True)
    word_6 = models.CharField(max_length=40, blank=True)
    word_7 = models.CharField(max_length=40, blank=True)
    word_8 = models.CharField(max_length=40, blank=True)
    word_9 = models.CharField(max_length=40, blank=True)
    word_10 = models.CharField(max_length=40, blank=True)
    word_11 = models.CharField(max_length=40, blank=True)
    word_12 = models.CharField(max_length=40, blank=True)
    word_13 = models.CharField(max_length=40, blank=True)
    word_14 = models.CharField(max_length=40, blank=True)
    word_15 = models.CharField(max_length=40, blank=True)
    word_16 = models.CharField(max_length=40, blank=True)
    word_17 = models.CharField(max_length=40, blank=True)
    word_18 = models.CharField(max_length=40, blank=True)
    word_19 = models.CharField(max_length=40, blank=True)
    word_20 = models.CharField(max_length=40, blank=True)

# words_numbers= 20

# for i in range(1, words_numbers + 1):
#     field_name = f'word {i}'
#     field = models.CharField(max_length=40, blank=True, verbose_name = f'Word {i}')
#     Level_1_const.add_to_class(field_name, field)

###########################################################################

class Level_2_v_d(models.Model):
    # sound_id = models.AutoField(primary_key=True)
    sound = models.CharField(max_length = 10)
    description = models.TextField()
    word_1 = models.CharField(max_length=40, blank=True)
    word_2 = models.CharField(max_length=40, blank=True)
    word_3 = models.CharField(max_length=40, blank=True)
    word_4 = models.CharField(max_length=40, blank=True)
    word_5 = models.CharField(max_length=40, blank=True)
    word_6 = models.CharField(max_length=40, blank=True)
    word_7 = models.CharField(max_length=40, blank=True)
    word_8 = models.CharField(max_length=40, blank=True)
    word_9 = models.CharField(max_length=40, blank=True)
    word_10 = models.CharField(max_length=40, blank=True)
    word_11 = models.CharField(max_length=40, blank=True)
    word_12 = models.CharField(max_length=40, blank=True)
    word_13 = models.CharField(max_length=40, blank=True)
    word_14 = models.CharField(max_length=40, blank=True)
    word_15 = models.CharField(max_length=40, blank=True)
    word_16 = models.CharField(max_length=40, blank=True)
    word_17 = models.CharField(max_length=40, blank=True)
    word_18 = models.CharField(max_length=40, blank=True)
    word_19 = models.CharField(max_length=40, blank=True)
    word_20 = models.CharField(max_length=40, blank=True)

# words_numbers= 20

# for i in range(1, words_numbers + 1):
#     field_name = f'word {i}'
#     field = models.CharField(max_length=40, blank=True, verbose_name=f'Word {i}')
#     Level_2_v_d.add_to_class(field_name, field)

#################################################################

class Level_3_sent(models.Model):
    sentence_id = models.AutoField(primary_key=True)
    sentence = models.CharField(max_length=200, blank=True)
    # sound = models.CharField(max = 10)
    # description = models.TextField()

# sent_number= 20

# for i in range(1, sent_number + 1):
#     field_name = f'word {i}'
#     field = models.CharField(max_length=40, blank=True, verbose_name=f'Word {i}')
#     Level_3_sent.add_to_class(field_name, field)
    

#TEST TABLE
class  ReadingTest(models.Model):
    id = models.AutoField(primary_key=True)
    words_and_sents = models.CharField(max_length = 200, blank = True)

