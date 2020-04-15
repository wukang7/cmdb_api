import json
from cmdb import models

def process_network_info(host_obj,network_dict):
    if network_dict['status'] == False:
        print("获取主机网卡信息失败%s"%(network_dict['error']))
        return
    new_network_dict = network_dict['data']
    for name,network_info in new_network_dict.items():
        inet_dict = network_info['inet'][0]
        new_network_dict[name].update(inet_dict)
        del new_network_dict[name]['inet']

    db_network_queryset = models.NIC.objects.filter(server_obj=host_obj).all()
    db_network_dict = { row.name:row for row in db_network_queryset }

    new_network_name_set = set(new_network_dict)
    db_network_name_set = set(db_network_dict)


    create_name_set = new_network_name_set-db_network_name_set
    remove_name_set = db_network_name_set-new_network_name_set
    update_name_set = new_network_name_set&db_network_name_set

    # print("新增:",create_name_set)
    # print("移除:",remove_name_set)
    # print("更新:",update_name_set)


    for name in create_name_set:
        hostname=getattr(host_obj,"hostname")
        ip = new_network_dict[name]['address']
        content="{}新增{}网卡,ip是{}".format(hostname,name,ip)
        print(content)
        models.AssetRecord.objects.create(asset_obj=host_obj,content=content,)
        models.NIC.objects.create(**new_network_dict[name],name=name,server_obj=host_obj)

    for name in remove_name_set:
        hostname = getattr(host_obj, "hostname")
        ip = new_network_dict[name]['address']
        content = "{}移除{}网卡,ip是{}".format(hostname, name, ip)
        print(content)
        models.NIC.objects.filter(server_obj=host_obj,name=name).delete()

    for name in update_name_set:
        db_network_obj = db_network_dict[name]    #对象
        # new_network_dict[name]   #字典
        for key,value in new_network_dict[name].items():
            db_value = getattr(db_network_obj,key)
            new_value = value
            if new_value != db_value:
                hostname = getattr(host_obj, "hostname")
                ip = new_network_dict[name]['address']
                content = "{}的{}网卡，{}的{}变更为{}".format(hostname,name,key,db_value,new_value)
                models.AssetRecord.objects.create(asset_obj=host_obj, content=content, )
                print(content)
                setattr(db_network_obj,key,new_value)
        db_network_obj.save()