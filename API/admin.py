from django.contrib import admin
from . models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'gender', 'pialaTembaga', 'pialaPerak', 'pialaEmas', 'score')
    list_filter = ('id', 'nama', 'gender', 'pialaTembaga', 'pialaPerak', 'pialaEmas', 'score')
    ordering = ['-score']
    pass

admin.site.register(Player, PlayerAdmin)
# Register your models here.
