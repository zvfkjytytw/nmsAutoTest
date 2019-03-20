'''
API requests to NMS
'''
import requests
import json

class nmsRequest(object):

    def __init__(self, nms_ip, api_key):
        self.session = requests.Session()
        self.nms_ip = nms_ip
        self.api_key = api_key
        self.url = r"http://" + self.nms_ip + r"/jsonapi/?token=" + self.api_key + r"&out=json"
        print(self.url)

    def select(self, item, id):
        # The item defines the request object parameter: teleport, satellite, controller, station ...
        data = {"request":{
                    "object": item,
                    "action": "select",
                    "id": id
        }}
        result = self.session.post(url=self.url, data=json.dumps(data))
        return result

    def list(self, item):
        data = {"request":{
                    "object":item,
                    "action":"list"
        }}
        result = self.session.post(url=self.url, data=json.dumps(data))
        return result

    def insert(self, item, data):
        data = {"request":{
                    "object":item,
                    "action":"insert"
                    },
                "data":data
        }
        result = self.session.post(url=self.url, data=json.dumps(data))
        return result

    def update(self, item, id, data):
        data = {"request":{
                    "object":item,
                    "action":"update",
                    "id":id
                    },
                "data":data
        }
        result = self.session.post(url=self.url, data=json.dumps(data))
        return result

    def delete(self, item, id):
        data = {"request":{
                    "object":item,
                    "action":"delete",
                    "id":id
        }}
        result = self.session.post(url=self.url, data=json.dumps(data))
        return result