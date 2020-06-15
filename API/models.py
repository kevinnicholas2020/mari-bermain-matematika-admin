from django.db import models
import uuid

# Create your models here.
class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=25)
    gender = models.CharField(max_length=1)
    pialaEmas = models.IntegerField()
    pialaPerak = models.IntegerField()
    pialaTembaga = models.IntegerField()
    score = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.score = (self.pialaEmas * 10) + self.pialaPerak + (self.pialaTembaga * 0.1)
        super(Player, self).save(*args, **kwargs)