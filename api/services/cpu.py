import json
from cmdb import models

def process_cpu_info(host_obj,cpu_dict):
    if cpu_dict['status'] == False:
        print("获取主机cpu信息失败%s" % (cpu_dict['error']))
        return

    new_cpu_dict = cpu_dict['data']
    # print(new_cpu_dict)
    db_cpu_queryset=models.Server.objects.filter(manage_ip=(getattr(host_obj, "manage_ip"))).all()[0]
    for key,value in new_cpu_dict.items():
        db_value = getattr(db_cpu_queryset, key)
        new_value = value
        if new_value != db_value:
            content="{}主机的{},从{}变更为{}".format(getattr(host_obj, "hostname"),key,db_value,new_value)
            models.AssetRecord.objects.create(asset_obj=host_obj, content=content, )
            print(content)
    models.Server.objects.filter(manage_ip=(getattr(host_obj, "manage_ip"))).update(**new_cpu_dict)