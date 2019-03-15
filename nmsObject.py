'''
Classes for the objects from NMS
 
'''

class nmsObject(object):

    def __init__(self, name):
        self.name = name


class nmsController(nmsObject):
    def __init__(self, name, net_id=1, contype=1, uhp_model=1):
        super().__init__()
        self.net_id = net_id
        self.contype = contype
        self.uhp_model = uhp_model
        self.obj_type = "controller"


    def set_netid(self,net_id):
        self.net_id = net_id

    def set_type(self, contype):
        self.contype = contype

    def set_uhp_model(self, uhp_model):
        self.uhp_model = uhp_model

'''
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




