from django.views.generic import View
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import MyModelSerializer

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "app/index.html")

@api_view(['GET'])
def some_model_list(request):

    # データベースからPostモデルの全データを取得、JSON形式で返す

    data = Post.objects.all()
    serializer = MyModelSerializer(data, many=True)
    return Response(serializer.data)
