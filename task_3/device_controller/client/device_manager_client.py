from device_controller.grpc_python.device_controller_pb2 import Empty, DeviceId, DeviceInfo
from device_controller.grpc_python.device_controller_pb2_grpc import DeviceManagerStub

class DeviceManagerClient:
    def __init__(self, stub: DeviceManagerStub):
        self.stub = stub

    def register_device(self, device_info: DeviceInfo):
        return self.stub.RegisterDevice(device_info)

    def list_devices(self):
        return self.stub.ListDevices(Empty())

    def deregister_device(self, device_id: DeviceId):
        return self.stub.DeregisterDevice(device_id)
