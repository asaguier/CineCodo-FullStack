from django.contrib import admin
from .models import Peli
#from .models import Proxima
#from .models import Estreno

class PelisAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

# Register your models here.
admin.site.register(Peli, PelisAdmin)
#admin.site.register(Proxima, PelisAdmin)
#admin.site.register(Estreno, PelisAdmin)
