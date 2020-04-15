import json
from cmdb import models

def process_board_info(host_obj,board_dict):
    if board_dict['status'] == False:
        print("获取主机主板信息失败%s" % (board_dict['error']))
        return
    '''
    {'manufacturer': 'LENOVO', 'model': 'ThinkServer TS250', 'sn': 'PC0WGVR9'}
    '''
    new_board_dict = board_dict['data']
    db_board_queryset=models.Server.objects.filter(manage_ip=(getattr(host_obj, "manage_ip"))).all()[0]
    for key,value in new_board_dict.items():
        db_value = getattr(db_board_queryset, key)
        new_value = value
        if new_value != db_value:
            content="{}主机的{},从{}变更为{}".format(getattr(host_obj, "hostname"),key,db_value,new_value)
            models.AssetRecord.objects.create(asset_obj=host_obj, content=content, )
            print(content)
    models.Server.objects.filter(manage_ip=(getattr(host_obj, "manage_ip"))).update(**new_board_dict)


    #可以实现 但是没有日志。。。
    #models.Server.objects.filter(manage_ip=(getattr(host_obj, "manage_ip"))).update(**new_board_dict)



