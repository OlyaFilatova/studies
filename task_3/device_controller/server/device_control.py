from device_controller.grpc_python.device_controller_pb2_grpc import DeviceControlServicer
from device_controller.grpc_python.device_controller_pb2 import CommandResponse, CommandRequest, DeviceId

class DeviceControlService(DeviceControlServicer):
    def SendCommand(self, request: CommandRequest, context):
        # Implement command sending logic here
        return CommandResponse(device_id=request.device_id, success=True, message=f'Command "{request.command}" for device "{request.device_id}" with params "{request.parameters.__str__()}" executed successfully.')

    def StreamDeviceCommands(self, request: DeviceId, context):
        # Implement streaming logic here
        yield CommandResponse(device_id=request.id, success=True, message=f'Streaming command "turn left .1" for "{request.id}".')
        yield CommandResponse(device_id=request.id, success=True, message=f'Streaming command "turn left .2" for "{request.id}".')
