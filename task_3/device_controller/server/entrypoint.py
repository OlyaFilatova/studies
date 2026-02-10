import grpc
from concurrent import futures
import logging

from device_controller.grpc_python import device_controller_pb2_grpc
from device_controller.server.device_manager import DeviceManagerService
from device_controller.server.device_control import DeviceControlService
from device_controller.server.device_monitor import DeviceMonitorService
from device_controller.server.alerts import AlertsService

logging.basicConfig(level=logging.INFO)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    device_controller_pb2_grpc.add_DeviceManagerServicer_to_server(DeviceManagerService(), server)
    device_controller_pb2_grpc.add_DeviceControlServicer_to_server(DeviceControlService(), server)
    device_controller_pb2_grpc.add_DeviceMonitorServicer_to_server(DeviceMonitorService(), server)
    device_controller_pb2_grpc.add_AlertsServicer_to_server(AlertsService(), server)

    server.add_insecure_port('[::]:50051')
    logging.info("Server started on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
