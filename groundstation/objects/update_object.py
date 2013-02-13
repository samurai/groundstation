import update_object_pb2

class UpdateObject(object):
    data_members = [parents, data]
    def __init__(self, parents, data):
        self.parents = parents
        self.data = data
        self.sha1 = None

    @property
    def sha1(self):
        if self.sha1:
            return self.sha1
        # XXX Calculate sha1 of this object

    @staticmethod
    def from_object(obj):
        """Convert an object straight from Git into a RootObject"""
        protobuf = update_object_pb2.UpdateObject()
        protobuf.ParseFromString(obj)
        return UpdateObject(protobuf.parents, protobuf.data)

    def as_object(self):
        """Convert a RootObject into data suitable to write into the database
        as a Git object"""
        protobuf = update_object_pb2.UpdateObject()
        for member in self.data_members:
            setattr(protobuf, member, getattr(self, member))
        return protobuf.SerializeToString()
