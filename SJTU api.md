# SJTU api

+ 地址：[二级结构预测](http://47.103.25.116/function/v1/array/)

+ 传输要求：json格式

+ 传输格式(POST请求)：

  ```json
  {
      "body": "",
      "result": ""
  }
  ```

  其中body为必填字段，为ATCGU(atcgu)组成的序列，长度限制为**1到100**，超过100无法计算

  result为不需要填写的字段

+ 返回格式：

  1. 正确访问

     ```json
     HTTP 201 Created
     Allow: POST, OPTIONS
     Content-Type: application/json
     Vary: Accept
     
     {
         "id": 18,
         "body": "CGGGAUGUGGCCCAGCUUGGUAGGGCACUGCGUUCGGGACGCAGGAGUCGCGCGUUCAAAUCGCGCCAUCCCGACCA",
         "time": "2021-10-13T13:47:24.497716Z",
         "result": "(((((((..((((.........))))((((((.......))))))....(((((.......))))))))))))...."
     }
     ```

     其中需要的信息为`"body"`为用户输入的信息,`"result"`为结构预测结果，长度与body长度一致，`"time"`为创建时间（POST）请求发送时间。

     成功访问返回`HTTP 201 Created`

  2. 存在除了ATCGUatcgu以外的字段

     ```json
     HTTP 400 Bad Request
     Allow: POST, OPTIONS
     Content-Type: application/json
     Vary: Accept
     
     "The input sequences should all be composed of ATCGU (atcgu), please re-enter"
     ```

     `HTTP 400 Bad Request`

+ 可视化：

  这个可以调用一个现成的工具

  [forna](rna.tbi.univie.ac.at/forna/)

  在它的git（https://github.com/ViennaRNA/forna）上有详细的api调用方法，大致就是`json`格式的传入序列和结构即可；

+ 后续更新版本会以/v2/array，/v3/array的形式放出，调用方法类似

