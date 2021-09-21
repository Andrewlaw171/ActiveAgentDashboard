from django.contrib import admin
from .models import AgentSession, ActiveAgentsPerHour

admin.site.register(AgentSession)
admin.site.register(ActiveAgentsPerHour)
