from __future__ import print_function

import logging

import grpc
from device_controller.grpc_python.device_controller_pb2 import DeviceInfo, DeviceId, Empty, CommandRequest, SensorRequest
from device_controller.client.client import IoTClient

server_path = "localhost:50051"

def generate_messages():
    messages = [
        SensorRequest(device_id='laptop'),
        SensorRequest(device_id='stove')
    ]
    for msg in messages:
        print(f"Sending {msg.device_id}")
        yield msg

def run():
    with grpc.insecure_channel(server_path) as channel:
        client = IoTClient(channel)
        try:
            response = client.device_manager.RegisterDevice(DeviceInfo(id="lamp", name="Test Lamp"))
            print(response.message)

            response = client.device_manager.DeregisterDevice(DeviceId(id="lamp"))
            print(response.message)

            response = client.device_manager.ListDevices(Empty())
            print(type(response.devices))
            print(len(response.devices))
            print(response.devices[0].id)
            print(response.devices[0].name)

            # ===
            response = client.device_control.SendCommand(CommandRequest(
                device_id='door',
                command='close'
            ))
            print(response)

            response = client.device_control.StreamDeviceCommands(DeviceId(
                id='faucet'
            ))
            for command in response:
                print(command)
            # ===
            response = client.alerts.SubscribeAlerts(DeviceId(
                id='faucet'
            ))
            for alert in response:
                print(alert)
            # ===
            response = client.device_monitor.StreamSensorData(generate_messages())
            for data in response:
                print(data)
        except grpc.RpcError as exc:
            print("Server failed with code", exc.code)


if __name__ == "__main__":
    logging.basicConfig()
    run()
