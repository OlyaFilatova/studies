from grpc import Channel
from device_controller.grpc_python import device_controller_pb2_grpc

class IoTClient:
    def __init__(self, channel: Channel):
        self.device_manager = device_controller_pb2_grpc.DeviceManagerStub(channel)
        self.device_control = device_controller_pb2_grpc.DeviceControlStub(channel)
        self.device_monitor = device_controller_pb2_grpc.DeviceMonitorStub(channel)
        self.alerts = device_controller_pb2_grpc.AlertsStub(channel)
