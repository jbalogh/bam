from django.db import models


class Mission(models.Model):
    name = models.CharField(max_length=255)

    @classmethod
    def go(cls, command):
        Mission.objects.create(name=command)
