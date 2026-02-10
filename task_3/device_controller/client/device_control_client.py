from device_controller.grpc_python.device_controller_pb2 import CommandRequest, DeviceId
from device_controller.grpc_python.device_controller_pb2_grpc import DeviceControlStub

class DeviceControlClient:
    def __init__(self, stub: DeviceControlStub):
        self.stub = stub

    def send_command(self, command_request: CommandRequest):
        return self.stub.SendCommand(command_request)

    def stream_device_commands(self, device_id: DeviceId):
        for response in self.stub.StreamDeviceCommands(device_id):
            yield response
