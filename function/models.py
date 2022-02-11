from django.db import models


# 用于构建二级结构预测接口的模型
class array(models.Model):
    # 定义字段是否可以为空,blank 用于字段的HTML表单验证，即判断用户是否可以不输入数据
    body = models.CharField(max_length=120, verbose_name='input array')
    time = models.DateTimeField(auto_now_add=True, verbose_name="date")
    result = models.TextField(blank=True)

    class Meta:
        ordering = ['time']
        db_table = 'db_array'  # 指定数据库表名
        verbose_name = 'array'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称


# 用于连接SVM二分类部分的模型
class svm(models.Model):
    file1 = models.FileField(verbose_name="Healthy people", upload_to='file_page1')
    file2 = models.FileField(verbose_name="Patients", upload_to='file_page2')
    time = models.DateTimeField(auto_now_add=True, verbose_name="date")
    result = models.TextField( verbose_name='specified result',blank=True)

    class Meta:
        ordering = ['time']
        db_table = 'db_svm'  # 指定数据库表名
        verbose_name = 'svm'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.name


# 用于计算杂交评分的模型
class seq(models.Model):
    num = models.IntegerField(verbose_name='num')
    body = models.TextField(verbose_name='Sequence set')
    time = models.DateTimeField(auto_now_add=True, verbose_name="date")
    result = models.CharField(max_length=20, verbose_name='score',blank=True)

    class Meta:
        ordering = ['time']
        db_table = 'db_seq'  # 指定数据库表名
        verbose_name = 'seq'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.body

# Create your models here.
