import django.utils.timezone as timezone
from django.db import models

class UserProfile(models.Model):
    """
    用户信息
    """
    name = models.CharField(u'姓名', max_length=32)
    email = models.EmailField(u'邮箱')
    phone = models.CharField(u'座机', max_length=32)
    mobile = models.CharField(u'手机', max_length=32)
    password = models.CharField(u'密码', max_length=64)

    class Meta:
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.name

class UserGroup(models.Model):
    """
    用户组
    """
    name = models.CharField(max_length=32, unique=True)
    users = models.ManyToManyField('UserProfile')

    class Meta:
        verbose_name_plural = "用户组表"

    def __str__(self):
        return self.name


class BusinessUnit(models.Model):
    """
    业务线
    """
    name = models.CharField('业务线', max_length=64, unique=True)
    abbreviation_name = models.CharField('缩写名', max_length=32, null=True)
    #contact = models.ForeignKey('UserProfile', verbose_name='业务联系人', related_name='c',on_delete=models.CASCADE)
    #manager = models.ForeignKey('UserProfile', verbose_name='系统管理员', related_name='m',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "业务线表"

    def __str__(self):
        return self.name


class IDC(models.Model):
    """
    机房信息
    """
    name = models.CharField('机房', max_length=32)
    floor = models.IntegerField('楼层', default=1)

    class Meta:
        verbose_name_plural = "机房表"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    资产标签
    """
    name = models.CharField('标签', max_length=32, unique=True)

    class Meta:
        verbose_name_plural = "标签表"

    def __str__(self):
        return self.name

class Env(models.Model):
    """
    资产环境
    """
    name = models.CharField('环境名', max_length=32, unique=True)
    abbreviation_name = models.CharField('缩写名', max_length=12, null=True)
    class Meta:
        verbose_name_plural = "服务器所属环境表"

    def __str__(self):
        return self.name


class Agent(models.Model):
    """
    代理商
    """
    name = models.CharField('代理商名字', max_length=32, unique=True)
    abbreviation_name = models.CharField('缩写名', max_length=32, null=True)

    class Meta:
        verbose_name_plural = "游戏代理商表"

    def __str__(self):
        return self.name


class Server(models.Model):
    """
    服务器信息
    """
    # device_type_choices = (
    #     (1, '服务器'),
    #     (2, '交换机'),
    #     (3, '防火墙'),
    # )
    # device_status_choices = (
    #     (1, '上架'),
    #     (2, '在线'),
    #     (3, '离线'),
    #     (4, '下架'),
    # )
    #
    # device_type_id = models.IntegerField('服务器类型',choices=device_type_choices, null=True,default=1)
    # device_status_id = models.IntegerField('服务器状态',choices=device_status_choices, null=True,default=1)
    #
    # cabinet_num = models.CharField('机柜号', max_length=30, null=True, blank=True)
    # cabinet_order = models.CharField('机柜中序号', max_length=30, null=True, blank=True)
    #
    # idc = models.ForeignKey('IDC', verbose_name='IDC机房', null=True, blank=True,on_delete=models.CASCADE)
    #
    #tag = models.ManyToManyField('Tag',default=1)
    manage_ip = models.GenericIPAddressField('管理IP',null=True, blank=True)	#
    hostname = models.CharField('主机名',max_length=128,null=True,blank=True)		#unique=True
    sn = models.CharField('SN号', max_length=64,null=True,blank=True)			#db_index=True
    manufacturer = models.CharField(verbose_name='制造商', max_length=64, null=True, blank=True)
    model = models.CharField('型号', max_length=64, null=True, blank=True)
    os_platform = models.CharField('系统', max_length=16, null=True, blank=True)
    os_version = models.CharField('系统版本', max_length=50, null=True, blank=True)
    cpu_count = models.IntegerField('CPU个数', null=True, blank=True)
    cpu_physical_count = models.IntegerField('CPU物理个数', null=True, blank=True)
    cpu_model = models.CharField('CPU型号', max_length=128, null=True, blank=True)


    create_at = models.DateTimeField('创建日期',null=True, default = timezone.now,blank=True)
    last_mod = models.DateTimeField('最后修改日期',null=True, auto_now = True,blank=True)

    business_unit = models.ForeignKey('BusinessUnit', default=1,verbose_name='属于的业务线', null=True, blank=True,on_delete=models.CASCADE)
    env = models.ForeignKey('Env',default=1, verbose_name='所属环境', null=True, blank=True,on_delete=models.CASCADE)
    agent = models.ForeignKey('Agent', default=7,verbose_name='代理商', null=True, blank=True,on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "服务器表"

    def __str__(self):
        return self.manage_ip


class Disk(models.Model):
    """
    硬盘信息
    """
    slot = models.CharField('插槽位', max_length=8)
    model = models.CharField('磁盘型号', max_length=32)
    capacity = models.CharField('磁盘容量GB', max_length=32)
    pd_type = models.CharField('磁盘类型', max_length=32)
    server_obj = models.ForeignKey('Server',related_name='disk',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "硬盘表"

    def __str__(self):
        return self.slot


class NIC(models.Model):
    """
    网卡信息
    """
    name = models.CharField('网卡名称', max_length=128)
    hwaddr = models.CharField('网卡mac地址', max_length=64)
    broadcast = models.CharField('网卡广播地址',max_length=64,null=True)
    netmask = models.CharField('网卡掩码地址',max_length=64)
    address = models.CharField('网卡ip地址', max_length=256)
    up = models.BooleanField(default=False)
    server_obj = models.ForeignKey('Server',related_name='nic',on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "网卡表"

    def __str__(self):
        return self.name


class Memory(models.Model):
    """
    内存信息
    """
    slot = models.CharField('插槽位', max_length=32)
    manufacturer = models.CharField('制造商', max_length=32, null=True, blank=True)
    model = models.CharField('型号', max_length=64)
    capacity = models.FloatField('容量', null=True, blank=True)
    sn = models.CharField('内存SN号', max_length=64, null=True, blank=True)
    speed = models.CharField('速度', max_length=16, null=True, blank=True)

    server_obj = models.ForeignKey('Server',related_name='memory',on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "内存表"

    def __str__(self):
        return self.slot

class AssetRecord(models.Model):
    """
    资产变更记录,creator为空时，表示是资产汇报的数据。
    """
    asset_obj = models.ForeignKey('Server', related_name='ar',on_delete=models.CASCADE)
    content = models.TextField(null=True)# 新增硬盘
    creator = models.ForeignKey('UserProfile', null=True, blank=True,on_delete=models.CASCADE) #
    create_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "资产记录表"

    def __str__(self):
        return "%s" %(self.content)
        # return "%s-%s-%s" % (self.asset_obj.idc.name, self.asset_obj.cabinet_num, self.asset_obj.cabinet_order)


class ErrorLog(models.Model):
    """
    错误日志,如：agent采集数据错误 或 运行错误
    """
    asset_obj = models.ForeignKey('Server', null=True, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=16)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "错误日志表"

    def __str__(self):
        return self.title

