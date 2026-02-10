import asyncio
import grpc

from control_and_telemetry.server.auth import TokenValidationInterceptor, create_ssl_credentials

from control_and_telemetry.grpc_python import control_pb2_grpc, control_pb2, telemetry_pb2_grpc, telemetry_pb2, admin_pb2_grpc, admin_pb2

class ControlServiceAsync(control_pb2_grpc.ControlServiceServicer):
    async def SetMotor(self, request, context):
        print(f"[AsyncControl] SetMotor called: {request}")
        md = dict(context.invocation_metadata())
        print(f"Metadata: {md}")
        return control_pb2.SetMotorResponse(accepted=True)

    async def StopAll(self, request, context):
        print(f"[AsyncControl] StopAll called: {request}")
        return control_pb2.StopAllResponse(stopped=True)

    async def LiveControl(self, request_iterator, context):
        print("[AsyncControl] LiveControl stream started")
        async for req in request_iterator:
            print(f"[AsyncControl] Received: {req}")
            if context.cancelled():
                print("[AsyncControl] Client cancelled")
                break
            yield control_pb2.LiveControlResponse(state=None)
        print("[AsyncControl] LiveControl stream ended")

class TelemetryServiceAsync(telemetry_pb2_grpc.TelemetryServiceServicer):
    async def SubscribeTelemetry(self, request, context):
        print(f"[AsyncTelemetry] SubscribeTelemetry: {request}")
        for i in range(5):
            if context.cancelled():
                print("[AsyncTelemetry] Client cancelled")
                break
            msg = telemetry_pb2.TelemetryMessage(
                sensor_id=f"sensor_{i}",
                value=i*10,
                timestamp_unix_ms=int(asyncio.get_event_loop().time() * 1000)
            )
            print(f"[AsyncTelemetry] Sending: {msg}")
            yield msg
            await asyncio.sleep(1)

class AdminServiceAsync(admin_pb2_grpc.AdminServiceServicer):
    async def GetStatus(self, request, context):
        print(f"[AsyncAdmin] GetStatus called: {request}")
        return admin_pb2.GetStatusResponse(status="OK")

    async def Restart(self, request, context):
        print(f"[AsyncAdmin] Restart called: {request}")
        return admin_pb2.RestartResponse(accepted=True)

async def serve():
    server = grpc.aio.server(
        interceptors=[TokenValidationInterceptor()]
    )

    control_pb2_grpc.add_ControlServiceServicer_to_server(ControlServiceAsync(), server)
    telemetry_pb2_grpc.add_TelemetryServiceServicer_to_server(TelemetryServiceAsync(), server)
    admin_pb2_grpc.add_AdminServiceServicer_to_server(AdminServiceAsync(), server)

    server.add_secure_port(
        '[::]:50051', create_ssl_credentials()
    )
    print("Async gRPC server starting on port 50051...")
    await server.start()
    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        print("Async server stopping gracefully...")
        await server.stop(0)

if __name__ == "__main__":
    asyncio.run(serve())
