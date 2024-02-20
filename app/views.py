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

@api_view(['POST'])
def create_post(request):
    serializer = MyModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)