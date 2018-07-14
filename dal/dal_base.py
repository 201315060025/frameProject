#coding:utf-8
from tools.singleton import Singleton  ## 单利模式
from db.mysqlapp import MySQLApp  ## 连接通道
#这个 基类 可以理解是对每个数据表的 共同的操作，
class Dal_Base:
    __metaclass__ = Singleton
    def __init__(self):
        self._m_cache = dict()
    ## 增加一条记录
    def add(self,mInstance):
        mInstance.id = mInstance.save()  #传入参数的方法都是被 加  的属性和方法,属性和方法添加后就可以使用了
        self._m_cache[mInstance.id] = mInstance
        return mInstance.id
    ## 在缓存中是否有这条记录，如果没有增加到缓存当中
    def get(self,pk,modelclass):
        pk = int(pk)
        if (pk in self._m_cache) == False:
           md = modelclass.get(pk)##调用的是 orm中的get方法 fanhizhibuzhidao
           if md == None:
              return None
           self._m_cache[pk] = md  ##内存中储存记录的形式
        return self._m_cache[pk]  ##返回一个值在内存中的一个指
    ## 修改数据
    def update(self,pk,modelclass,**kwargs):##传入的参数有主键，类名，元组
        pk = int(pk)
        if (pk in self._m_cache) == False:#判断主键的记录是否在缓存中，如果不在
           self.get(pk,modelclass)       ## 参考地15行的方法
        md = self._m_cache[pk]
        for k,v in kwargs.iteritems():
            if md.__mappings__[k].innertype == 'int':
                v = (int)(v)
            elif md.__mappings__[k].innertype == 'str':
                v = (str)(v)

            self._m_cache[pk][k] = v  ##在缓存中修改
        return self._m_cache[pk].update(pk,**kwargs)

    def delete(self,pk,modelclass):
        pk = int(pk)
        if (pk in self._m_cache) == False:
           self.get(pk,modelclass)

        self._m_cache[pk].delete(pk)
        del self._m_cache[pk]   ##点播：可以从缓存和数据库两个角度去考虑

#根据某种属性返回满足条件的记录
    def getValueByAttr(self,attr,value):##主要用于判断是否该记录存在  id=1和getuserByattr相比返回一个主键
        result = []  # 返回一个    列表
        bfit = True  #self._m_cache里面装的是什么 da:User[id]={"name":"blx","age":"11","class":"clasd"}
        for k, v in self._m_cache.iteritems():##
                if isinstance(value, dict):#对象属于某个类别 value 的属性是否属于dict字典
                    for k1, v1 in value.iteritems():  ##p={a=1,b=2,c=3} id=p
                        if v[attr][k1] != v1:  ##p[id][a] != 1
                            bfit = False
                            break
                    if bfit:  ##u如果bfit 是一个true
                        result.append(k)
                else:
                    if v[attr] == value:  ##  参考第十二行：self._m_cache[newUser.id] = newUser，内存的储存形式
                        result.append(k)   ##k的值是是主键id  保存到内存里面
        return result

    def initDB(self,tablename,cls):
            db = MySQLApp().getInstance()
            sql = 'select  * from ' + tablename
            db.query(sql)
            result = db.fetchAllRows()
            #对行进行循环
            for row in result:
                md = cls(**row)
                self._m_cache[md.id] = md
                # print(md)
            print self._m_cache


            db.close()
            return result

    #取得所有id
    def getAllID(self):
         result = []
         for k,v in self._m_cache.iteritems():
             result.append(k)
         return result

    def getNameById(self,allID,modelclass):
        resultName=[]
        for pk in allID:
            ## 这句话是错误的额 条件永远不成立！
            if (pk in self._m_cache[pk]) == False:
                md=self.get(pk,modelclass)
                self._m_cache[pk]=md
            resultName.append(self._m_cache[pk].name)
        return resultName

    ## 此方法只用于createAct和createOrg中
    def getStateById(self,idlist):
        stateList=[]
        for id in idlist:
            md=self._m_cache[id]
            stateList.append(md.state)
        return stateList






