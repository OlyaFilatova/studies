import asyncio
import contextlib
import os
import grpc

from control_and_telemetry.client.auth import create_credentials
from control_and_telemetry.grpc_python import control_pb2_grpc, control_pb2, telemetry_pb2_grpc, telemetry_pb2, admin_pb2_grpc, admin_pb2
from control_and_telemetry.grpc_python.common.robot_types_pb2 import MotorCommand

default_path = "http://localhost:50051"
SERVER_ADDRESS = os.getenv('BACKEND_URL', default_path)

METADATA = (
    ("x-request-id", "req-1234"),
    ("x-client-id", "client-1")
)

@contextlib.asynccontextmanager
async def create_client_channel(addr):
    channel = grpc.aio.secure_channel(addr, create_credentials())
    yield channel

async def control_client():
    async with create_client_channel(SERVER_ADDRESS) as channel:
        stub = control_pb2_grpc.ControlServiceStub(channel)

        response = await stub.SetMotor(
            control_pb2.SetMotorRequest(command=MotorCommand(motor_id=1, speed=0.5)),
            metadata=METADATA
        )
        print(f"[ControlClient] SetMotor response: {response}")

        async def live_commands():
            for i in range(3):
                yield control_pb2.LiveControlRequest(command=MotorCommand(motor_id=i, speed=i*0.1))
                await asyncio.sleep(0.5)

        async for resp in stub.LiveControl(live_commands(), metadata=METADATA):
            print(f"[ControlClient] LiveControl response: {resp}")

async def telemetry_client():
    async with create_client_channel(SERVER_ADDRESS) as channel:
        stub = telemetry_pb2_grpc.TelemetryServiceStub(channel)

        request = telemetry_pb2.TelemetrySubscription(sensor_ids=["sensor_0", "sensor_1"])
        async for msg in stub.SubscribeTelemetry(request, metadata=METADATA):
            print(f"[TelemetryClient] Received telemetry: {msg}")

async def admin_client():
    async with create_client_channel(SERVER_ADDRESS) as channel:
        stub = admin_pb2_grpc.AdminServiceStub(channel)

        response = await stub.GetStatus(admin_pb2.GetStatusRequest(), metadata=METADATA)
        print(f"[AdminClient] GetStatus response: {response}")

        response = await stub.Restart(admin_pb2.RestartRequest(), metadata=METADATA)
        print(f"[AdminClient] Restart response: {response}")

async def main():
    print("Starting async gRPC clients...")
    await asyncio.gather(
        control_client(),
        telemetry_client(),
        admin_client()
    )

if __name__ == "__main__":
    asyncio.run(main())
