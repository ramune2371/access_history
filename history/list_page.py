from django.http import HttpResponse
from django.template import loader
from django.utils import timezone as tz
from history.models import AccessHistory

class ListPage:
    def list(request):
        # requestからIP情報を取得
        ip = request.META.get('REMOTE_ADDR')

        # テーブルへ保管
        AccessHistory(ip=ip,access_time=tz.datetime.now()).save()

        # レスポンスの組み立て
        query_set = AccessHistory.objects.all()
        template = loader.get_template('history/list.html')
        context = {'accesshistory_list':query_set}
        # レスポンス返却
        return HttpResponse(template.render(context,request))
        