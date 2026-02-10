import time
from typing import Iterable
from device_controller.grpc_python.device_controller_pb2_grpc import DeviceMonitorServicer
from device_controller.grpc_python.device_controller_pb2 import SensorData, SensorRequest

class DeviceMonitorService(DeviceMonitorServicer):
    def StreamSensorData(self, request_iterator: Iterable[SensorRequest], context):
        for request in request_iterator:
            # Implement sensor data streaming logic here
            yield SensorData(device_id=request.device_id, readings={"temperature": 25.0}, timestamp=int(time.time()))
            time.sleep(1)
            yield SensorData(device_id=request.device_id, readings={"temperature": 25.0}, timestamp=int(time.time()))
