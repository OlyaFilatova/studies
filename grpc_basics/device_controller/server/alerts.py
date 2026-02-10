from device_controller.grpc_python.device_controller_pb2_grpc import AlertsServicer
from device_controller.grpc_python.device_controller_pb2 import DeviceId, Alert

class AlertsService(AlertsServicer):
    def SubscribeAlerts(self, request: DeviceId, context):
        # Implement alert subscription logic here
        yield Alert(device_id=request.id, type="temperature_high", message="High temperature detected.", timestamp=1234567890)
