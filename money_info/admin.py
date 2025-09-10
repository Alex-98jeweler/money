from django.contrib import admin

from . import models


admin.site.register(
    [models.Type, models.Status, models.Category, models.SubCategory]
)