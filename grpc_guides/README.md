# gRPC guides

Explores gRPC functionality described at https://grpc.io/docs/guides/.

Its development is currently in progress.

## Running project

### Create virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Generate certs

Make sure openssl is installed
`openssl --version`

To install on Ubuntu/Debian
`sudo apt-get install openssl`

To install on MacOS
`brew install openssl`

Run generation script

```sh
cd control_and_telemetry/security
chmod +x create_certs.sh
./create_certs.sh
```

### Running project

1. Start Docker
2. cd to `study-grpc/project_2`
3. run `docker-compose -f docker-compose.yml up -d`
4. read terminal outputs in containers

### Generates Python gRPC code from .proto files

```sh
chmod +x generate_proto.sh
./generate_proto.sh
```

## Project folder structure
```
control_and_telemetry/
│
├── protos/
│   └── common/
│
├── client/
│   └── client.py
│
├── grpc_python/
│   └── common/
│
├── security/
│   ├── create_certs.sh
│   └── certs/
│       ├── ca/
│       ├── client/
│       ├── server/
│       └── jwt/
│
├── server/
│   └── server.py
│
└── generate_proto.sh
```

## 

- Created project plan
- Created script for generating certificates
- Created script for generating gRPC code
- Created temporary dummy async server and client that are put in different Docker containers
- Created .proto files
- Generated gRPC code
- Added mTSL protection
- Added JWT authentication with interceptor

## other gRPC Functionalities to explore

- cancel RPC from client side (with server knowing and reacting) and from server side
- add compression logic with CRIME and BEAST attacks prevention.
- add timeout to protect client from waiting forever.
- attach channelz for debugging purposes and retrieve debug info.
- create rich error details and unpack them on client side.
    - use good status codes
- limit bandwidth on server and client sides.
- add health check service to a server, and react to it on the client side.
- send metadata at the start of request or response, or at the end of sending response and read metadata on the other side.
- add keepalive for improving performance and reliability.
- use interceptors to create logic that is not specific to a single RPC method.
- add reflection to make API specs publicly available
- add observability using OpenTelemetry plugin
- add retry policy
- stop server gracefully
- make client wait for server
- use uds
- use multiprocessing
- use xds
