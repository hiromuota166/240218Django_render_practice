from django.urls import path
from .views import IndexView, some_model_list, create_post

urlpatterns = [
    # path("エンドポイントURL",リクエストが来たときに実行されるビュー関数,URLパターンの名前)
    path("", IndexView.as_view(), name="index"),
    path("api/some_model_list/", some_model_list, name="some_model_list"),
    path("api/posts/create/", create_post, name="create_post")
]