import grpc

from control_and_telemetry.auth.credentials import load_credential_from_file
from control_and_telemetry.auth.jwt import verify_jwt
from control_and_telemetry.auth.consts import AUTH_HEADER_KEY

def create_ssl_credentials():
    return grpc.ssl_server_credentials(
        (
            (
                load_credential_from_file("security/certs/server/server.key"),
                load_credential_from_file("security/certs/server/server.crt")
            ),
        ),
        root_certificates=load_credential_from_file("security/certs/ca/ca.crt")
    )

class TokenValidationInterceptor(grpc.aio.ServerInterceptor):
    def __init__(self, skip_methods=None):
        self.skip_methods = skip_methods or []

    async def intercept_service(self, continuation, handler_call_details):
        if handler_call_details.method in self.skip_methods:
            return await continuation(handler_call_details)

        metadata = dict(handler_call_details.invocation_metadata or [])
        auth_header = metadata.get(AUTH_HEADER_KEY)

        if not auth_header:
            raise

        if type(auth_header) == bytes:
            auth_header = str(auth_header)
        
        token: str = auth_header.split(" ")[-1]

        try:
            claims = verify_jwt(token)
            print(f"[AUTH] JWT OK: {claims}")
        except Exception:
            raise

        return await continuation(handler_call_details)
