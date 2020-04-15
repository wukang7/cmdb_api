from django.http import HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from api import models
from rest_framework import serializers

class Server(APIView):
    def get(self,request):
        return Response({"code":1,"msg":"hello"})


class Depart(APIView):
    def get(self,request):
        result = models.Depart.objects.all().values("id","title","count")
        return Response(result)


class DepartSerializer(serializers.ModelSerializer):
    class Meta:
        # 模型名称
        model = models.Depart
        # 序列化返回的字段
        # fields = ('id', 'title', 'count')
        fields = "__all__"
        # 这个字段不返回
        # exclude = ('count',)
        # 显示的深度
        # depth = 1
        # 默认只读,不接受用户修改  跟字段设置的read_only=True效果一样
        # read_only_fields = ('account_name',)

class DepartView(APIView):
    def get(self,request,*args,**kwargs):
        did = kwargs.get('pk')
        if not did:
            result = models.Depart.objects.all()
            print(result)
            #序列化多个obj
            ser = DepartSerializer(instance=result,many=True)
            print(ser.data)
            return Response(ser.data)
        else:
            result = models.Depart.objects.filter(id=did).first()
            #序列化一个obj
            ser = DepartSerializer(instance=result,many=False)
            return Response(ser.data)

    def post(self,request,*args,**kwargs):
        # print(request.body)
        # print(request.POST)
        data = request.data
        ser = DepartSerializer(data=data)
        if ser.is_valid():
            new_object=ser.save()
            return Response("添加成功")
        # models.Depart.objects.create(**data)
        return Response(ser.errors)

    def delete(self,request,*args,**kwargs):
        did = kwargs.get('pk')
        print(did)

        models.Depart.objects.filter(id=did).delete()
        return Response("删除成功")


from rest_framework.viewsets import ModelViewSet
class NewDepartView(ModelViewSet):
    queryset = models.Depart.objects.all()
    serializer_class = DepartSerializer