from device_controller.grpc_python.device_controller_pb2_grpc import DeviceManagerServicer
from device_controller.grpc_python.device_controller_pb2 import DeviceResponse, DeviceList, StatusCode, DeviceId, DeviceInfo, Empty

class DeviceManagerService(DeviceManagerServicer):
    def RegisterDevice(self, request: DeviceInfo, context):
        # Implement device registration logic here
        return DeviceResponse(code=StatusCode.SUCCESS, message=f'Device "{request.id}" with name "{request.name}" registered successfully.')

    def ListDevices(self, request: Empty, context):
        # Implement logic to list devices here
        return DeviceList(devices=[
            DeviceInfo(id='test', name='Dummy device')
        ])

    def DeregisterDevice(self, request: DeviceId, context):
        # Implement device deregistration logic here
        return DeviceResponse(code=StatusCode.SUCCESS, message=f'Device "{request.id}" deregistered successfully.')
