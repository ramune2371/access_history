from django.http import HttpResponseBadRequest
from history.models import AccessHistory
from django.utils import timezone as tz

class PageBase:
    def access(request):
        ip = request.META.get('REMOTE_ADDR')
        AccessHistory(user_name=ip,access_time=tz.datetime.now()).save()
        return HttpResponseBadRequest("")