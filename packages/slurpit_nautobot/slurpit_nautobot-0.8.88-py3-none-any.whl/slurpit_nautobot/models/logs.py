from ..management.choices import LogLevelChoices, LogCategoryChoices
from django.db import models
from django.utils.translation import gettext as _
# from nautobot.extras.querysets import ObjectChangeQuerySet
from nautobot.apps.models import BaseModel

class SlurpitLog(BaseModel):
    log_time = models.DateTimeField(blank=True, auto_now=True, editable=False)
    level = models.CharField(
        max_length=100, 
        choices=LogLevelChoices,
        default=LogLevelChoices.LOG_DEFAULT,
        editable=False,
    )
    category = models.CharField(
        max_length=50, 
        choices=LogCategoryChoices,
        default=LogCategoryChoices.INIT,
        editable=False,
    )
    message = models.CharField(max_length=200)

    # objects = ObjectChangeQuerySet.as_manager()
    
    def get_absolute_url(self):        
        return '/'

    def info(category, message):
        SlurpitLog.objects.create(level=LogLevelChoices.LOG_INFO, category=category, message=message)

    def warn(category, message):
        SlurpitLog.objects.create(level=LogLevelChoices.LOG_WARNING, category=category, message=message)

    def success(category, message):
        SlurpitLog.objects.create(level=LogLevelChoices.LOG_SUCCESS, category=category, message=message)

    def failure(category, message):
        SlurpitLog.objects.create(level=LogLevelChoices.LOG_FAILURE, category=category, message=message)
