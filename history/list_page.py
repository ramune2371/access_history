from django.http import HttpResponse
from django.utils import timezone as tz
from history.models import AccessHistory

class ListPage:
    def list(request):
        ip = request.META.get('REMOTE_ADDR')
        AccessHistory(ip=ip,access_time=tz.datetime.now()).save()
        query_set = AccessHistory.objects.all()
        response_str=''
        for qs in query_set:
            response_str = response_str + str(qs) + "<br>"
        return HttpResponse(response_str)
        