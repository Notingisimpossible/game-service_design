import json,os
import random


class CPlayer():
    def __init__(self):
        self.baseInfo={
            "id":0,
            "name":'',
            "nickname":'',
            "HP":100,
            "MP":0,
            "LV":1,
            "VIPLV":0,
            "LVExp":0,
            "VIPExp":0,

            "emails":[],
            "skills":[],
            
        }
        self.dtInfo={
            "lastlogin":'2019-3-13',
            "playtotaltime":500,
        }

        #self.new_skill() 
        pass

    def new_skill(self):
        skillid= random.randint(1,3)
        self.baseInfo["skills"].append(skillid)

    def setName(self,name):
        self.baseInfo["name"]=name
