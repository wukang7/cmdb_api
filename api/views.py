import json
from django.shortcuts import render

from cmdb import models
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from api.services.memory import process_memory_info
from api.services.board import process_board_info
from api.services.basic import process_basic_info
from api.services.cpu import process_cpu_info
from api.services.network import process_network_info

# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class Server(View):
    def get(self,request):
        res = {}
        s = models.Server.objects.all().filter(hostname="").values_list('manage_ip','agent__ssh_port')
        iplist = []
        for ip,port in s:
            if port is None:
                port=22
            ipport="{}:{}".format(ip,port)
            iplist.append(ipport)
        #list = [i[0] for i in models.Server.objects.all().values_list('manage_ip','agent')]
        res['server_list']=iplist
        return JsonResponse(res)

    def post(self,request):
        server_info = request.body.decode("utf-8")
        # print(server_info)
        server_info_dict = json.loads(server_info)
        ip = server_info_dict['ip']
        host_obj=models.Server.objects.all().filter(manage_ip=ip).first()


        #内存
        memory_dict = server_info_dict['memory']
        process_memory_info(host_obj,memory_dict)

        #主板
        board_dict = server_info_dict['board']
        process_board_info(host_obj, board_dict)

        #基本信息
        basic_dict = server_info_dict['basic']
        process_basic_info(host_obj, basic_dict)

        #cpu
        cpu_dict = server_info_dict['cpu']
        process_cpu_info(host_obj, cpu_dict)

        #网络
        network_dict = server_info_dict['network']
        process_network_info(host_obj, network_dict)


        return  JsonResponse({"code":"0"})
