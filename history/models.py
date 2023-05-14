from django.db import models
from django.core.exceptions import ValidationError
import re

# ip アドレスのバリデーション用
pattern = "([0-9]{3}\.){3}\.[0-9]{3}"
matcher = re.compile(pattern)

def validate_ip(value):
    if not matcher.match(value):
        raise ValidationError(
            _("%{value} is not valid ip!"),
            params={"value",value}
        )

class AccessHistory(models.Model):
    # データの設定
    ip=models.CharField("ip",max_length=200,validators=[validate_ip])
    access_time=models.DateTimeField("date accessed")

    # __str__メソッドのオーバーライド
    # ページ表示する際に使用
    def __str__(self) -> str:
        return "ip : %s / access time : %s" % (self.ip,self.access_time)
