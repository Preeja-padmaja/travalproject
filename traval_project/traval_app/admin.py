from django.contrib import admin
from .models import traval_table
from .models import team_table


# Register your models here.
admin.site.register(traval_table)
admin.site.register(team_table)