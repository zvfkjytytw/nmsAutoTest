'''
API requests to NMS
'''
import requests
import json

class nmsRequest(object):

    def __init__(self, nms_ip, api_key, obj_type):
        self.obj_type = obj_type
        self.session = requests.Session()
#        self.nms_ip = nms_ip
#        self.api_key = api_key
        self.url = r"http://" + nms_ip + r"/jsonapi/?token=" + api_key + r"&out=json"

    def select(self, id):
        data = {"request":{
                    "object": self.obj_type,
                    "action": "select",
                    "id": id
        }}

        result = self.session.post(url=self.url, data=json.dumps(data))
        return result

    def list(self):
        data = {"request":{
                    "object":self.obj.type,
                    "action":"list"
        }}
        result = self.session.post(url=self.url, data=json.dumps(data))
        return result

    def insert(self, data):

    def update(self, id, data):

    def delete(self, id):
"""
    nms_requests = ("select", "list", "insert", "update", "delete", "search")
    nms_ip = "10.0.2.5"
    api_key = "eastar"

    def __init__(self, req_type):
        if req_type in nmsRequest.nms_requests:
            self.req_type = req_type
        else:
            print("Wrong request type! Create a select request by default.\n")
            self.name = nmsRequest.nms_requests[0]

    def url(self):
        return f'http://{self.nms_ip}/jsonapi/?token={self.api_key}&out=json'

    def get_url(self):
        print(self.url)

    def data(self, obj_type, ):
        data_dict = {"select":'{"request":{"object":"' + obj_type + '","action":"select","id":"??"}}',
                     "list":'{"request":{"object":"' + obj_type +'","action":"list"}}',
                     "insert":'{"request":{"object":"' + obj_type +'","action":"insert"},"data":{ ??? }}',
                     "update":'{"request":{"object":"' + obj_type + '","action":"update","id":"??"},"data":{ ??? }}',
                     "delete":'{"request":{"object":"' + obj_type + '","action":"delete","id":"??"}}',
                     "search":'{"request":{"action":"search","find":{"object":"' + obj_type + '","where":{ ??? }}}}'
                    }
#        return '{"request":{"object":"station","action":"' + self.req_type + '","id":18"}}'
        return data_dict[self.req_type]

    def get_data(self):
        print(self.data)

    def apply(self):
        import requests
        result requests.post(url=self.url, data=self.data)
        return result
"""


