from django.contrib import admin
from .models import Blog  # Make sure the model is imported from the correct location

# Register your Blog model here
admin.site.register(Blog)
