#!/usr/bin/env bash
# ------------------------------------------------------------------
# create_certs.sh
# Generates:
# 1) Root CA
# 2) Server certificate (TLS/mTLS)
# 3) Client certificate (for mTLS)
# 4) JWT signing key pair (RS256)
# ------------------------------------------------------------------

# Get the directory where the script is located
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Change the current working directory to SCRIPT_DIR
cd "$SCRIPT_DIR"

set -euo pipefail

# -------------------------
# CONFIGURATION
# -------------------------
CERTS_DIR="./certs"
CA_DIR="$CERTS_DIR/ca"
SERVER_DIR="$CERTS_DIR/server"
CLIENT_DIR="$CERTS_DIR/client"
JWT_DIR="$CERTS_DIR/jwt"

SERVER_CN="server_container"
CLIENT_CN="robotics-client"
JWT_KEY_NAME="jwtRS256"

DAYS_VALID=365
RSA_BITS=4096

# Optional SAN (Subject Alternative Name) for server cert
SAN_DNS="server"

# -------------------------
# CREATE DIRECTORY STRUCTURE
# -------------------------
mkdir -p "$CA_DIR" "$SERVER_DIR" "$CLIENT_DIR" "$JWT_DIR"

echo "Directories created under $CERTS_DIR"

# -------------------------
# 1) CREATE ROOT CA
# -------------------------
echo "Generating root CA..."
openssl genrsa -out "$CA_DIR/ca.key" $RSA_BITS
openssl req -x509 -new -nodes -key "$CA_DIR/ca.key" \
    -sha256 -days $((DAYS_VALID*10)) \
    -subj "/CN=robotics-ca" \
    -out "$CA_DIR/ca.crt"
echo "Root CA generated at $CA_DIR/ca.crt"

# -------------------------
# 2) SERVER CERTIFICATE
# -------------------------
echo "Generating server certificate..."

# Private key
openssl genrsa -out "$SERVER_DIR/server.key" $RSA_BITS

# CSR
openssl req -new -key "$SERVER_DIR/server.key" \
    -subj "/CN=$SERVER_CN" \
    -out "$SERVER_DIR/server.csr"

# SAN config
cat > "$SERVER_DIR/server.ext" <<EOF
subjectAltName = @alt_names

[alt_names]
DNS.1=$SERVER_CN
DNS.2=localhost
EOF

# Sign CSR with CA
openssl x509 -req -in "$SERVER_DIR/server.csr" \
    -CA "$CA_DIR/ca.crt" -CAkey "$CA_DIR/ca.key" -CAcreateserial \
    -out "$SERVER_DIR/server.crt" -days $DAYS_VALID -sha256 \
    -extfile "$SERVER_DIR/server.ext"

echo "Server certificate generated at $SERVER_DIR/server.crt"

# -------------------------
# 3) CLIENT CERTIFICATE
# -------------------------
echo "Generating client certificate..."

# Private key
openssl genrsa -out "$CLIENT_DIR/client.key" $RSA_BITS

# CSR
openssl req -new -key "$CLIENT_DIR/client.key" \
    -subj "/CN=$CLIENT_CN" \
    -out "$CLIENT_DIR/client.csr"

# Sign with CA
openssl x509 -req -in "$CLIENT_DIR/client.csr" \
    -CA "$CA_DIR/ca.crt" -CAkey "$CA_DIR/ca.key" -CAcreateserial \
    -out "$CLIENT_DIR/client.crt" -days $DAYS_VALID -sha256

echo "Client certificate generated at $CLIENT_DIR/client.crt"

# -------------------------
# 4) JWT SIGNING KEY
# -------------------------
echo "Generating JWT signing keys..."

openssl genrsa -out "$JWT_DIR/$JWT_KEY_NAME.key" $RSA_BITS
openssl rsa -in "$JWT_DIR/$JWT_KEY_NAME.key" -pubout -out "$JWT_DIR/$JWT_KEY_NAME.key.pub"

echo "JWT private key: $JWT_DIR/$JWT_KEY_NAME.key"
echo "JWT public key:  $JWT_DIR/$JWT_KEY_NAME.key.pub"

# -------------------------
# 5) PERMISSIONS
# -------------------------
chmod 600 "$CA_DIR/ca.key" "$SERVER_DIR/server.key" "$CLIENT_DIR/client.key" "$JWT_DIR/$JWT_KEY_NAME.key"

echo "All keys are restricted to owner only."

# -------------------------
# 6) VERIFY CERTIFICATES
# -------------------------
echo "Verifying server certificate..."
openssl verify -CAfile "$CA_DIR/ca.crt" "$SERVER_DIR/server.crt"

echo "Verifying client certificate..."
openssl verify -CAfile "$CA_DIR/ca.crt" "$CLIENT_DIR/client.crt"

echo "✅ All certificates created successfully!"
