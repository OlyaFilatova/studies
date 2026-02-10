from typing import Iterable
from device_controller.grpc_python.device_controller_pb2 import SensorRequest
from device_controller.grpc_python.device_controller_pb2_grpc import DeviceMonitorStub

class DeviceMonitorClient:
    def __init__(self, stub: DeviceMonitorStub):
        self.stub = stub

    def stream_sensor_data(self, sensor_requests: Iterable[SensorRequest]):
        for response in self.stub.StreamSensorData(sensor_requests):
            yield response
