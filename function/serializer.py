from rest_framework import serializers
from function.models import array, svm, seq
from rest_framework.viewsets import ModelViewSet


class arraySerializer(serializers.ModelSerializer):
    class Meta:
        model = array  # 参考模型类生成字段
        fields = "__all__"  # 生成所有字段
        extra_kwargs = {
            'array': {'help_text': 'Input the array composed of ATCGU (atcgu) and calculate the secondary structure'}
        }

    # def validate_body(self, value):
    #     print("value = {}".format(value))
    #
    #
    #     for i in value:
    #         flag = True
    #         if i not in "ATCGUatcgu":
    #             flag = False
    #             break
    #
    #     if flag == False:
    #         raise serializers.ValidationError("The input sequence should all be composed of ATCGU (atcgu), please re-enter")
    #
    #
    #     return value


class svmSerializer(serializers.ModelSerializer):
    class Meta:
        model = svm  # 参考模型类生成字段
        fields = "__all__"
        extra_kwargs = {
            'num': {'help_text': 'Enter the number of other sequences in the environment'},
            'body': {'help_text': 'Enter sequences set that matches the above number, each separated by ' ''},
        }


class seqSerializer(serializers.ModelSerializer):
    class Meta:
        model = seq  # 参考模型类生成字段
        fields = "__all__"  # 生成所有字段
        extra_kargs = {
            'file1': {'help_text': 'This is a file containing the data of various indicators of healthy people '},
            'file2': {'help_text': 'This is a file containing the data of various indicators of patients '},
            'result': {'help_text': 'The picked indicators,which help in prob development'}
        }
