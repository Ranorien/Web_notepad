from django.contrib import admin

# Register your models here.
from .models import Topic, Note   # dot means - find models in the same dir
admin.site.register(Topic)
admin.site.register(Note)
