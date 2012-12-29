import uuid

from groundstation.proto.gizmo_pb2 import Gizmo

from groundstation import logger
log = logger.getLogger(__name__)

class InvalidRequest(Exception):
    pass

class Request(object):
    VALID_REQUESTS = {
            "LISTALLOBJECTS": "handle_listallobjects",
            "FETCHOBJECT": "handle_fetchobject"
    }
    _Response = None

    def __init__(self, verb, station=None, stream=None, payload=None):
        # Cheat and load this at class definition time
        if not self._Response:
            res = __import__("groundstation.transfer.response")
            self._Response = res.transfer.response.Response
        self.type = "REQUEST"
        self.id = uuid.uuid1()
        self.verb = verb
        self.station = station
        self.stream = stream
        self.payload = payload
        self.validate()

    @classmethod
    def from_gizmo(klass, gizmo, station, stream):
        return klass(gizmo.verb, station, stream, gizmo.payload)

    # @property
    # def station(self):
    #     return self.station

    # @station.setter
    # (self, station):
    #     self.station = station

    def SerializeToString(self):
        gizmo = Gizmo()
        gizmo.id = str(self.id)
        gizmo.type = Gizmo.REQUEST
        gizmo.verb = self.verb
        if self.payload:
            gizmo.payload = self.payload
        return gizmo.SerializeToString()

    def validate(self):
        if self.verb not in self.VALID_REQUESTS:
            raise Exception("Invalid Request: %s" % (self.verb))

    def process(self):
        self.__getattribute__(self.VALID_REQUESTS[self.verb])()

    def handle_listallobjects(self):
        log.info("Handling LISTALLOBJECTS")
        for i in self.station.objects():
            log.debug(" Sending %s " % (i))
            response = self._Response(self.id, self.station.repo[i])
            self.stream.enqueue(response)
        terminate = self._Response(self.id, None)
        self.stream.enqueue(terminate)

    def handle_fetchobject(self):
        pass # TODO
