from django.db import models


class AgentSession(models.Model):
    agentId = models.CharField(max_length=38)
    callStartTime = models.DateTimeField()
    callEndTime = models.DateTimeField()


class GraphSpan(models.Model):
    startTime = models.DateField()

