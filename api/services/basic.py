import json
from cmdb import models

def process_basic_info(host_obj,basic_dict):
    if basic_dict['status'] == False:
        print("获取主机基本信息失败%s" % (basic_dict['error']))
        return

    new_basic_dict = basic_dict['data']
    # print(new_basic_dict)
    db_basic_queryset=models.Server.objects.filter(manage_ip=(getattr(host_obj, "manage_ip"))).all()[0]
    for key,value in new_basic_dict.items():
        db_value = getattr(db_basic_queryset, key)
        new_value = value
        if new_value != db_value:
            content="{}主机的{},从{}变更为{}".format(getattr(host_obj, "hostname"),key,db_value,new_value)
            models.AssetRecord.objects.create(asset_obj=host_obj, content=content, )
            print(content)
    models.Server.objects.filter(manage_ip=(getattr(host_obj, "manage_ip"))).update(**new_basic_dict)