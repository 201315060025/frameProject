#coding:utf-8

import json
import tornado.web
import time
import os
from model.user import User
from model.createact import CreateAct
from model.createorg import CreateOrg
from model.officer import Officer
from model.org import Org
from model.orgapply import OrgApply
from model.act import Act

from dal.dal_act import Dal_Act
from dal.dal_user import Dal_User
from dal.dal_createact import Dal_CreateAct
from dal.dal_createorg import Dal_CreateOrg
from dal.dal_officer import Dal_Officer
from dal.dal_org import Dal_Org
from dal.dal_orgapply import Dal_OrgApply

from configs.config_error import configs_error
from tools.utils import Utils
from configs.config_error import http_reponse
from dal.dal_earthquake import Dal_Earthquake
from dal.dal_gly import Dal_Gly
from model.earthquake import Earthquake
from model.gly import Gly
from db.mysqlapp import MySQLApp
USERID = 0


# class BaseHandler(tornado.web.RequestHandler):
#     def get_current_user(self):
#         return self.get_secure_cookie(USERID)


class SaveEarthquakeInfo(tornado.web.RequestHandler):
    def get(self):
        # query earthquake info
        response = {'status': 200, 'message': 'ok'}
        eqname = self.get_argument('eqname', '').encode("utf8")
        lon = str(self.get_argument('lon', 0))
        lan = str(self.get_argument('lan', 0))
        eq_level = self.get_argument('eq_level', 0)
        eq_depth = str(self.get_argument('eq_depth', 0))
        happen_time = self.get_argument('happen_time', 0)
        eq_explain = self.get_argument('eq_explain', '')
        earthquake_id = int(self.get_argument('earthquake_id', 0))

        if not eqname:
            response.update({"status": 1002, "message": 'eq_name and happend_time is not null'})
            response = json.dumps(response)
            response = self.get_argument('jsoncallback')+"("+response+")"
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write(response)
            return None
        # add new earthquake
        if not earthquake_id:
            newEarth = Earthquake(eqname=eqname, longitude=lon, latitude=lan, level=eq_level, depth=eq_depth,
                                  introduction=eq_explain)
            newID = Dal_Earthquake().addEarthquake(newEarth)
            response.update({"newid": newID})
            response = json.dumps(response)
            response = self.get_argument('jsoncallback')+"("+response+")"
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write(response)
            return None

        # update eatthquake
        parames = {"eqname": eqname, "longitude": lon, "latitude": lan, "level": eq_level, "depth": eq_depth,
                   "introduction": eq_explain}
        Dal_Earthquake().updateEarthquake(earthquake_id, **parames)
        response = json.dumps(response)
        response = self.get_argument('jsoncallback')+"("+response+")"
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)
        return None


class SaveUserInfo(tornado.web.RequestHandler):
    def get(self):
        # query earthquake info
        response = {'status': 200, 'message': 'ok'}

        email = self.get_argument('email', '')
        pwd = self.get_argument('pwd', '')
        user_status = self.get_argument('user_status', 0)
        true_name = self.get_argument('true_name', '')
        login_name = self.get_argument('login_name', '')

        user_id = int(self.get_argument('user_id', 0))

        if not(pwd and true_name):
            response.update({"status": 1003, "message": 'user name and pwd is not null'})
            response = json.dumps(response)
            response = self.get_arguments('jsoncallback')[0]+"("+response+")"
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write(response)
            return None
        # add new earthquake
        if not user_id:
            newuser = Gly(XM=true_name, MM=pwd, DLM=login_name, YX=email)
            newID = Dal_Gly().addGly(newuser)
            response.update({"newid": newID})
            response = json.dumps(response)
            response = self.get_argument('jsoncallback')+"("+response+")"
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write(response)
            return None

        # update eatthquake
        parames = {"XM": true_name, "MM": pwd, "DLM": login_name, "YX": email}
        Dal_Gly().updateGly(user_id, **parames)
        response = json.dumps(response)
        response = self.get_argument('jsoncallback')+"("+response+")"
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(response)
        return None

