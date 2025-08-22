from django.contrib import admin
from .models import User  # or UserAccount if that's your model name

admin.site.register(User)  # or UserAccount