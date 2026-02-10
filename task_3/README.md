# Task 3

Explores basic functionality of gRPC framework https://grpc.io/docs/languages/python/.

## Running project

### Create virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Start server

`python -m device_controller.server.entrypoint`

### Run client

`python -m device_controller.client.entrypoint`

## Update after proto edit

`python -m grpc_tools.protoc -Idevice_controller/grpc_python=device_controller/protos --python_out=. --grpc_python_out=. --pyi_out=. device_controller/protos/device_controller.proto`

## Covered gRPC functionalities

- splitting project code into several folders (protos, grpc_python, server, client)
- create and serve 4 kinds of RPC methods
- call 4 kinds of RPC methods
- synchronous server and client implementations
