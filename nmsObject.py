'''
Classes for the objects from NMS
 
'''
import nmsRequest
import json

class nmsObject(object):

    def __init__(self, name):
        self.name = name


class nmsController(nmsObject):

    controller_counts = 0
    min_frequency = 950000
    max_frequency = 2050000
    min_symrate = 100
    max_tdm_symrate = 64000
    max_tdma_symrate = 8000
    min_fec = 0
    max_fec = 18

    def __init__(self, name, net_id=1, contype=1, uhp_model=1):
        self.name = name
        self.net_id = net_id
        self.con_type = contype
        self.uhp_model = uhp_model
        self.obj_type = "controller"
        self.tdmtx_freq = int(nmsController.min_frequency)
        self.tdmtx_symrate = int(nmsController.min_symrate)
        self.tdmrx_freq = int(nmsController.min_frequency + 5000)
        self.tdmrx_symrate = int(nmsController.min_symrate)
        self.request = nmsRequest()

    def build_dict(self):
        data = {}
        data["name"] = self.name
        data["tdmtx_freq"] = self.tdmtx_freq
        data["tdmtx_symrate"] = self.tdmtx_symrate
        data["tdmrx_freq"] = self.tdmrx_freq
        data["tdmrx_symrate"] = self.tdmrx_symrate
        return json.dumps(data)

    def create(self):
        print("create")
        self.request.insert(url, data)

    def update(self, data):
        print("update: " + data)

    def delete(self):
        print("delete")

    def enable(self):
        print("enable")
        e_data = {"enabled":1}
        self.request.update

    def disable(self):
        print("disable")





""" def set_netid(self,net_id):
        self.net_id = net_id

    def set_type(self, contype):
        self.contype = contype

    def set_uhp_model(self, uhp_model):
        self.uhp_model = uhp_model

Formatting of the RX setup settings
'''        
    def set_tdmrx_freq(self, frequency):
        self.tdmrx_freq = frequency

    def set_tdmrx_symrate(self, symrate):
        self.tdmrx_symrate = symrate

    def set_tmdtx_freq(self, frequency):
        self.tdmtx_freq = frequency

    def set_tdmtx_symrate(self, symrate):
        self.tdmtx_symrate = symrate

'''
Default initializing of the controller
'''
    def init_default(self):
        self.tdmtx_freq = 950000
        self.tdmtx_symrate = 1000
        self.tdmrx_freq = 950000
        self.tdmrx_symrate = 1000
"""
class nmsRFfeed(nmsObject):
    def __init__(self):
        self.rf_name = "RF_first"
        self.t_name = "T_first"
        self.t_longitude = "37.62"
        self.t_latitude = "55.76"
        self.s_name = "S_first"
        self.s_longitude = "123.45"
# will receive id from nms API request insert teleport
    def setTeleportID(self, id):
        self.t_id = id
# will receive id from nms API request insert satellite
    def setSatelliteID(self, id):
        self.s_id = id
# will receive id from nms API request insert RF feed
    def setRFfeedID(self, id):
        self.rf_id = id


class nmsModem(nmsObject):
    nmsModem_count = 0
    def __init__(self, name, ip_addr, serial, platform):
        self.name = name
        self.ip_addr = ip_addr
        self.serial = serial
        self.platform = platform
        self.id = 0
        self.timeout = 40
        self.password = "nms_test"

    def set_rffeed(self, rffeed_id, teleport_id):
        self.rffeed_id = rffeed_id
        self.teleport_id = teleport_id

