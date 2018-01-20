from django.contrib import admin
from . models import *

class authorAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["name"]
    class Meta:
        Model = author
admin.site.register(author,authorAdmin)

class articaleAdmin(admin.ModelAdmin):
    list_display = ["__str__","created_date"]
    list_filter = ["created_date","category"]
    search_fields = ["title"]
    list_per_page = 10
    class Meta:
        Model = articale
admin.site.register(articale,articaleAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["name"]
    list_per_page = 10
    class Meta:
        Model = category
admin.site.register(category,categoryAdmin)
