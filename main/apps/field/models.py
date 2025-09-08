from django.db import models
from ..common.models import BaseModel, BaseMeta
from .utils import upload_field_images
from ..user.models import User
from django.utils.translation import gettext as _
from django.contrib.gis.db import models as gis_models


class Field(BaseModel):
    field = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='field_owner')
    images = models.ImageField(upload_to=upload_field_images, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)  
    longitude = models.FloatField(null=True, blank=True)


    def __str__(self):
        return f'{self.owner} {self.field}'
    
    class Meta(BaseMeta):
        db_table = "fields"
        verbose_name = _('Field')
        verbose_name_plural = _('Fields')


    @property
    def location(self):
        if self.latitude and self.longitude:
            return gis_models.Point(self.longitude, self.latitude)
        return None