from django.contrib import admin
from .models import Realtor


@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_mvp')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
    list_filter = ('id',)



