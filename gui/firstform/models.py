# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class ClientRoom(models.Model):
    client = models.ForeignKey(Client, models.DO_NOTHING)
    room = models.ForeignKey('Room', models.DO_NOTHING)
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_room'


class ClientService(models.Model):
    client = models.ForeignKey(Client, models.DO_NOTHING)
    service = models.ForeignKey('Service', models.DO_NOTHING)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_service'


class Room(models.Model):
    price = models.DecimalField(max_digits=18, decimal_places=2)
    apart_num = models.IntegerField()
    free = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Service(models.Model):
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'service'
