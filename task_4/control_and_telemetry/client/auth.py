import grpc

from control_and_telemetry.auth.consts import AUTH_HEADER_KEY
from control_and_telemetry.auth.credentials import load_credential_from_file
from control_and_telemetry.auth.jwt import create_jwt

def create_credentials():
    # Call credential object will be invoked for every single RPC
    call_credentials = grpc.access_token_call_credentials(
        f"{AUTH_HEADER_KEY}: Bearer {create_jwt('a', 'b')}"
    )
    # Channel credential will be valid for the entire channel
    ca = load_credential_from_file("security/certs/ca/ca.crt")
    cert = load_credential_from_file("security/certs/client/client.crt")
    key = load_credential_from_file("security/certs/client/client.key")

    channel_credential = grpc.ssl_channel_credentials(
        root_certificates=ca,
        private_key=key,
        certificate_chain=cert,
    )
    # Combining channel credentials and call credentials together
    return grpc.composite_channel_credentials(
        channel_credential,
        call_credentials,
    )
