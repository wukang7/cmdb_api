import json
from cmdb import models

def process_memory_info(host_obj,memory_dict):
    if memory_dict['status'] == False:
        print("获取主机内存信息失败%s"%(memory_dict['error']))
        return
    new_memory_dict = memory_dict['data']
    db_memory_queryset = models.Memory.objects.filter(server_obj=host_obj).all()
    db_memory_dict = { row.slot:row for row in db_memory_queryset }

    # print(new_memory_dict)
    # print("###################")
    # print(db_memory_dict)

    new_memory_slot_set = set(new_memory_dict)
    db_memory_slot_set = set(db_memory_dict)

    create_slot_set = new_memory_slot_set-db_memory_slot_set
    remove_slot_set = db_memory_slot_set-new_memory_slot_set
    update_slot_set = new_memory_slot_set&db_memory_slot_set

    # print("新增:",create_slot_set)
    # print("移除:",remove_slot_set)
    # print("更新:",update_slot_set)

    for slot in create_slot_set:
        content="%s新增%s槽位内存,大小是%s"%(getattr(host_obj,"hostname"),slot,new_memory_dict[slot]['capacity'])
        print(content)
        models.AssetRecord.objects.create(asset_obj=host_obj,content=content,)
        models.Memory.objects.create(**new_memory_dict[slot],server_obj=host_obj)

    for slot in remove_slot_set:
        content="%s删除%s槽位的内存，大小是%s"%(getattr(host_obj,"hostname"),slot,new_memory_dict[slot]['capacity'])
        print(content)
        models.Memory.objects.filter(server_obj=host_obj,slot=slot).delete()

    for slot in update_slot_set:
        db_memory_obj = db_memory_dict[slot]    #对象
        # new_memory_dict[slot]   #字典
        for key,value in new_memory_dict[slot].items():
            db_value = getattr(db_memory_obj,key)
            new_value = value
            if new_value != db_value:
                content = "{}的{}槽位的内存，{}的{}变更为{}".format(getattr(host_obj, "hostname"),slot,key,db_value,new_value)
                models.AssetRecord.objects.create(asset_obj=host_obj, content=content, )
                print(content)
                setattr(db_memory_obj,key,new_value)
        db_memory_obj.save()