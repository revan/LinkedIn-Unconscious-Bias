from django.contrib import admin

# Register your models here.
from .models import Candidate, Experiment, Pair
admin.site.register(Candidate)
admin.site.register(Experiment)
admin.site.register(Pair)
