# 意图识别系统API说明
API说明如下


## 1.参数传入api

| 字段名 | 数据类型 |  说明 | 备注  | 
| ------ | ------ | ------ |------ |
| dataSourceType | 整型 | 用户选择数据源输入，文本，excel数据库，1是文本，2是excel,3是数据库 | 必传参数，且只能选择一种 |
| txtAddress | 字符串 | 数据源是文本即dataSourceType=1,该字段有值 | 可选参数 |
| excelAddress | 字符串 | 数据源是文本即dataSourceType=2,该字段有值 | 可选参数 |
| ip | 字符串 | 数据源是文本即dataSourceType=3,该字段有值, 数据库ip | 可选参数 |
| name | 字符串 | 数据源是文本即dataSourceType=3,该字段有值 , 数据库用户名| 可选参数  |
| pwd | 字符串 | 数据源是文本即dataSourceType=3,该字段有值, 数据库密码 | 可选参数  |
| modelType | 整型 | 用户选择用模型训练，规则，1是模型，2是规则,3是所有 | 必传参数， 可以多选 |
| modelWeight | 整型 | 用户选择两种方案共用即modelType=3,模型权重 |  |
| ruleWeight | 整型 | 用户选择两种方案共用即modelType=3,规则权重 |  |

### Request

`GET /intention-recognition-result`

    curl -i -H 'Accept: application/json' http://172.27.96.226:8001/intention-recognition-result

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {'state': 200, 'message': 'OK', 'data': {'yitu':"正常" }}