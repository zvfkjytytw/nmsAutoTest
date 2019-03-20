'''
Classes for the objects from NMS:

'''

class nmsObject(object):
    def __init__(self):
        pass
"""
class for management of the controllers in a NMS server
controller types:
9:      Start Hub 
10:     Multi Frequency Hub 
        Outroute            
"""
class nmsController(nmsObject):

    obj_type: str
    controller_counts: int = 0
    min_frequency: int = 950000
    max_frequency: int = 2050000
    min_symrate: int = 100
    max_tdm_symrate: int = 64000
    max_tdma_symrate: int = 8000
    min_fec: int = 0
    max_fec: int = 18

    def __init__(self, name, con_type=9, uhp_model=1, net_id=1):
        super().__init__()
# necessary parameters
        self.name = name
        self.network_id = net_id
        self.type = con_type
        self.uhp_model = uhp_model
# parameters by default
        self.obj = "controller"
        self.tdmtx_freq = int(nmsController.min_frequency)
        self.tdmtx_symrate = int(nmsController.min_symrate)
        self.tdmrx_freq = int(nmsController.min_frequency + 5000)
        self.tdmrx_symrate = int(nmsController.min_symrate)

    def data(self):
        data = {"name":self.name,
                "network_id":self.network_id,
                "tdmtx_freq":self.tdmtx_freq,
                "tdmtx_symrate":self.tdmtx_symrate,
                "tdmrx_freq":self.tdmrx_freq,
                "tdmrx_symrate":self.tdmrx_symrate
        }
        return data

class nmsRFfeed(nmsObject):
    def __init__(self):
        super().__init__()
# Teleport parameters
        self.t_id = 0
        self.t_obj = "teleport"
        self.t_name = "T_first"
        self.t_longitude = "37.62"
        self.t_latitude = "55.76"
# Satellite parameters
        self.s_id = 0
        self.s_obj = "satellite"
        self.s_name = "S_first"
        self.s_longitude = "123.45"
# RF Feed parameters
        self.rf_id = 0
        self.rf_obj = "rffeed"
        self.rf_name = "RF_first"

    def t_data(self):
        data = {"name":self.t_name,
                "latitude":self.t_latitude,
                "longitude":self.t_longitude
        }
        return data

    def s_data(self):
        data = {"name":self.s_name,
                "longitude":self.s_longitude
        }
        return data

    def rf_data(self):
        data = {"name":self.rf_name,
                "teleport_id":self.t_id,
                "satellite_id":self.s_id
        }
        return data

class nmsModem(nmsObject):
    nmsModem_count = 0
    def __init__(self, name, ip_addr, serial, platform):
        super().__init__()
        self.name = name
        self.ip_addr = ip_addr
        self.serial = serial
        self.platform = platform
        self.timeout = 40
        self.password = "nms_test"
        self.rffeed_id = 0
        self.teleport_id = 0
        self.id = 0
        self.obj = "modem"

    def set_rffeed(self, rffeed_id, teleport_id):
        self.rffeed_id = rffeed_id
        self.teleport_id = teleport_id

    def data(self):
        data = {"name":self.name,
                "ip_addr":self.ip_addr,
                "serial_num":self.serial,
                "platform":self.platform,
                "teleport_id":self.teleport_id,
                "rffeed_id":self.rffeed_id,
                "password":self.password,
                "timeout":self.timeout
        }
        return data