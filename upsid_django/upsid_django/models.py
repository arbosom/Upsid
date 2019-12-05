# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Branches(models.Model):
    famille = models.TextField()

    class Meta:
        managed = False
        db_table = 'Branches'


class Langues(models.Model):
    upsid = models.IntegerField(primary_key=True)
    nom = models.TextField()
    biblio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Langues'


class LanguesBranches(models.Model):
    famille = models.ForeignKey(Branches, models.DO_NOTHING, db_column='famille', primary_key=True)
    upsid = models.ForeignKey(Langues, models.DO_NOTHING, db_column='upsid')

    class Meta:
        managed = False
        db_table = 'Langues_Branches'
        unique_together = (('famille', 'upsid'),)


class LanguesGeolocalisation(models.Model):
    upsid = models.ForeignKey(Langues, models.DO_NOTHING, db_column='upsid', primary_key=True)
    variete = models.CharField(max_length=100)
    geolocalisation = models.TextField()

    class Meta:
        managed = False
        db_table = 'Langues_geolocalisation'
        unique_together = (('upsid', 'variete'),)


class Phonemes(models.Model):
    ipa = models.TextField(db_column='IPA')  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Phonemes'


class PhonemesLangues(models.Model):
    upsid = models.ForeignKey(Langues, models.DO_NOTHING, db_column='upsid', primary_key=True)
    phoneme = models.ForeignKey(Phonemes, models.DO_NOTHING, db_column='phoneme')

    class Meta:
        managed = False
        db_table = 'Phonemes_Langues'
        unique_together = (('upsid', 'phoneme'),)
