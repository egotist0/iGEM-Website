from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from django import http
from function.models import array, svm, seq
from rest_framework.response import Response
from rest_framework import status
from function.serializer import arraySerializer, svmSerializer, seqSerializer

import time
from SJTUFold.GNN_model_pred import get_pred_GNN_tri
from DD.hybrid import spurious_hybrid
from dataAnalysis.workspace import select
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class arraysGenericAPIView_v1(GenericAPIView):
    """
        可以接收JSON内容POST请求的视图。
    """
    parser_classes = (JSONParser,)

    # 公共属性
    queryset = array.objects.all()
    serializer_class = arraySerializer

    def post(self, request):
        if request.method != 'POST':
            return Response("Please re-enter",status=status.HTTP_400_BAD_REQUEST)


        # 获取参数
        data_dict = request.data
        body = data_dict["body"]

        flag = True

        for i in body:
            flag = True
            if i not in "ATCGUatcgu":
                flag = False
                break

        if flag == False:
            return Response("The input sequences should all be composed of ATCGU (atcgu), please re-enter",
                            status=status.HTTP_400_BAD_REQUEST)

        outcome = get_pred_GNN_tri(body)
        data_dict["result"] = str(outcome).replace('\n', '')

        # 序列化器
        serializer = self.get_serializer(data=data_dict)

        # 校验,入库
        serializer.is_valid(raise_exception=True)
        serializer.save()


        # 此处再调用模型进行处理
        return Response(serializer.data, status=status.HTTP_201_CREATED, )





class arraysGenericAPIView_v2(GenericAPIView):

    """
        可以接收JSON内容POST请求的视图。
    """
    parser_classes = (JSONParser,)

    # 公共属性
    queryset = array.objects.all()
    serializer_class = arraySerializer

    def post(self, request):
        if request.method != 'POST':
            return Response("Please re-enter",status=status.HTTP_400_BAD_REQUEST)


        # 获取参数
        data_dict = request.data
        body = data_dict["body"]

        flag = True

        for i in body:
            flag = True
            if i not in "ATCGUatcgu":
                flag = False
                break

        if flag == False:
            return Response("The input sequences should all be composed of ATCGU (atcgu), please re-enter",
                            status=status.HTTP_400_BAD_REQUEST)

        outcome = get_pred_GNN_tri(body)
        data_dict["result"] = str(outcome).replace('\n', '')

        # 序列化器
        serializer = self.get_serializer(data=data_dict)

        # 校验,入库
        serializer.is_valid(raise_exception=True)
        serializer.save()

        result={
            "structure":serializer.data["result"],
            "sequence":serializer.data["body"],
        }

        # 此处再调用模型进行处理
        return Response(result, status=status.HTTP_201_CREATED, )

"""
SVM分类部分
"""

class svmsGenericAPIView(GenericAPIView):
    # 公共属性
    serializer_class = svmSerializer
    queryset = svm.objects.all()

    def post(self, request):
        data_dict = request.data
        data_dict["result"] = "unknown"
        # 序列化器
        serializer = self.get_serializer(data=data_dict)

        # 校验,入库
        serializer.is_valid(raise_exception=True)
        serializer.save()

        file1 = BASE_DIR + "/file_page1/" + str(data_dict["file1"])
        file2 = BASE_DIR + "/file_page2/" + str(data_dict["file2"])

        print('\n'+file1+file2)
        
        #time.sleep(10) 
        result = str(select(file1, file2))
        print(result)
        result_dict = {
            "result":result,
        }
        #data_dict["result"] = result

        # 序列化器
        #serializer = self.get_serializer(data=data_dict)

        # 校验,入库
        #serializer.is_valid(raise_exception=True)
        #serializer.save()

        return Response(result_dict, status=status.HTTP_201_CREATED, )

"""
杂交分数计算部分
"""


class seqsGenericAPIView(GenericAPIView):
    """
        可以接收JSON内容POST请求的视图。
    """
    parser_classes = (JSONParser,)

    # 公共属性
    queryset = seq.objects.all()
    serializer_class = seqSerializer

    def post(self, request):
        # 获取参数
        data_dict = request.data
        body = data_dict["body"]
        # print(body)
        num = data_dict["num"]

        seqlist = body.split(' ')

        for i in seqlist:
            for j in i:
                flag = True
                if j not in "ATCGUatcgu":
                    flag = False
                    break

            if flag == False:
                return Response("The input sequences should all be composed of ATCGU (atcgu), please re-enter",
                                status=status.HTTP_400_BAD_REQUEST)
        if num != len(seqlist):
            return Response("The number of input sequences should be consistent with num",
                            status=status.HTTP_400_BAD_REQUEST)
        score = spurious_hybrid(num, seqlist)
        data_dict["result"] = str(score)

        # 序列化器
        serializer = self.get_serializer(data=data_dict)

        # 校验,入库
        serializer.is_valid(raise_exception=True)
        serializer.save()

         # 此处再调用模型进行处理
        result={
            "num":int(eval(serializer.data["result"])),
        }
        return Response(result, status=status.HTTP_201_CREATED, )


# Create your views here.
