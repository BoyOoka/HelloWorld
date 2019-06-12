# -*- coding: utf-8 -*-
from TestModel.models import Test
from django.http import HttpResponse
# 数据库操作


def test_db(request):
    test1 = Test(name='w3cschool.cn')
    response = ""
    test1.save()
    # 通过objects模型管理器的all()获得所有数据行类似select * from
    list = Test.objects.all()
    print(list)
    # filter相当于where,设置过滤条件
    response2 = Test.objects.filter(id=1)
    # 获取单个对象
    response3 = Test.objects.get(id=1)
    # 限制返回数据 相当于offset 0 limit 2
    response4 = Test.objects.order_by('name')[0:2]
    # 数据排序
    response5 = Test.objects.order_by('id')
    # 多条件
    response6 = Test.objects.filter(name='w3cschool.cn1').order_by('id')
    # 修改数据
    test = Test.objects.get(id=1)
    test.name = 'w3c教程'
    test.save()
    # 另一种修改数据
    Test.objects.filter(id=2).update(name='w3c教程Update')
    # 修改所有列
    # Test.objects.all().update(name='w3c教程update_all')

    # 删除数据
    test2 = Test.objects.get(id=3)
    test2.delete()
    # Test.objects.filter(id=1).delete()
    # 删除所有数据
    # Test.objects.all().delete()
    # 输出所有数据
    for var in response5:
        response = response + var.name + "\n"
    print(response5)
    return HttpResponse("<p>" + response + "</p>")


    # return HttpResponse("<p>数据添加成功！</p>")

