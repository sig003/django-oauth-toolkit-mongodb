from django.db import models
from djongo import models as djongoModels

class House(models.Model):
    house_id = models.CharField(max_length=256)

    class Meta:
        abstract = True

class Users(models.Model):
    _id = djongoModels.ObjectIdField()
    email = djongoModels.CharField(max_length=256)
    name = djongoModels.CharField(max_length=256)
    #house = djongoModels.CharField(max_length=256)
    house = djongoModels.JSONField()
    # house = djongoModels.ArrayField(
    #      model_container=House
    #  )

    class Meta:
        db_table = "drf_users"

    objects = djongoModels.DjongoManager()

class Address(models.Model):
    main = models.CharField(max_length=256)
    sub = models.CharField(max_length=256)

    class Meta:
        abstract = True

class Houses(models.Model):
    _id = djongoModels.ObjectIdField()
    house_id = djongoModels.CharField(max_length=256)
    name = djongoModels.CharField(max_length=256)
    address = djongoModels.ArrayField(
        model_container=Address,
    )

    class Meta:
        db_table = "drf_houses"
