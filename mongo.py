#coding=utf-8
"""
这个类负责对mongo数据库的增删改查处理
"""
from pymongo import MongoClient

class Mongo(object):

    def __init__(self,host="localhost",port=27017):
        self.client = MongoClient(host,port)

    def insert(self,database,collection,document):
        """
        :param database:数据库
        :param collection:表
        :param document:数据
        :return:
        """
        database = self.client.get_database(database)      #数据库存在的话就直接获取，没有就自动创建database
        collection = database.get_collection(collection)
        result = collection.insert_one(document)
        if result.acknowledged:
            return result.inserted_id
        else:
            return None

    def delete(self, database, collection, filter):
        """
        :param database:
        :param collection:
        :param filter:
        :return:
        """
        database = self.client.get_database(database)
        collection = database.get_collection(collection)
        result = collection.delete_many(filter)         #filter需为json格式
        if result.acknowledged:
            return result.deleted_count
        else:
            return 0

    def update(self):
        pass

    def search(self,database,collection,filter):
        database = self.client.get_database(database)
        collection = database.get_collection(collection)
        skip = int(filter.pop('skip',0))
        limit = int(filter.pop('limit',10))
        condition = filter.pop('filter',{})
        result = list(collection.find(condition,limit=limit,skip=skip))
        for r in result:
            r['_id'] = str(r['_id'])
        return result

if __name__ == '__main__':
    mongo = Mongo()
    # mongo.insert("testfan","user",{
    #     'name':'damao',
    #     'age':'99',
    #     'sex':'male',
    #     'salary':'high'
    # })
    # mongo.delete("testfan","user",{'name':'damao'})
    print (mongo.search("testfan","user",{'education':'doctor'}))