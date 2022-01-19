#coding:utf-8

from tools.singleton import Singleton
from  tools.utils import Utils
##以上两个是基类
from model.act import Act  ##是数据库中的表抽象成类 进而对象 并继承基类
from model.gly import Gly
from model.fj import Fj
from db.mysqlapp import MySQLApp ## 连接通道 涉及连接通道
from dal.dal_base import Dal_Base  ## 数据称的基类


class Dal_Fj(Dal_Base):
    def __init__(self):
        Dal_Base.__init__(self)

    def addFj(self, newFj):#newAct可以是一个对象   一个对象包含所有的需要传输的信息
       return self.add(newFj) ## add继承基类的属性方法add(),

    def getFj(self, pk):
        return self.get(pk, Fj)

    def updateFj(self, pk, **kwargs):
        return self.update(pk, Fj, **kwargs)

    def deleteFj(self, pk):
        # return self.delete(pk,Act)
        self.delete(pk, Fj)

#根据某种属性返回满足条件的记录
    def getActByAttr(self, attr, value):
        return self.getValueByAttr(attr,value)

    def initCache(self):
        self.initDB('fj', Fj)

#取得某个头衔的成员id
    def getActTitleMember(self, pk, title):
        act = self.getAct(pk)
        outResult = Utils().decodeMutilFormat(act.memlist,';',':')
        for k,v in outResult.iteritems():
            if int(v[1]) == title:
                return v[0]

    ## 根据所有的活动id 获取所有的活动名称
    def getActNameById(self, allID):
        return self.getNameById(allID,Act)
