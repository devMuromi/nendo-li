from django.contrib import admin

from .models import Nendoroid
from .models import Series
from .models import Manufacturer
from .models import Sculptor
from .models import NendoroidPhoto

admin.site.register(Nendoroid)
admin.site.register(Series)
admin.site.register(Manufacturer)
admin.site.register(Sculptor)
admin.site.register(NendoroidPhoto)
