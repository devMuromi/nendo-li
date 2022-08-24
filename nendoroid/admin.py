from django.contrib import admin

from .models import Nendoroid
from .models import Series
from .models import Manufacturer
from .models import Sculptor

admin.site.register(Nendoroid)
admin.site.register(Series)
admin.site.register(Manufacturer)
admin.site.register(Sculptor)
