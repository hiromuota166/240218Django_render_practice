from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model() # ユーザーモデル関数を取得


class Command(BaseCommand):
  def handle(self, *args, ** options):
    if not User.objects.filter(username=settings.SUPERUSER_NAME).exists(): # ユーザーが存在しない場合
      User.objects.create_superuser(
        username=settings.SUPERUSER_NAME,
        email=settings.SUPERUSER_EMAIL,
        password=settings.SUPERUSER_PASSWORD,
      )
      print("スーパーユーザーを作成しました")
