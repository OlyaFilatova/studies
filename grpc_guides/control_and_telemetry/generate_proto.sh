#!/usr/bin/env bash

# Get the directory where the script is located
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Change the current working directory to SCRIPT_DIR
cd "$SCRIPT_DIR/../"

set -euo pipefail

# -------------------------
# CONFIGURATION
# -------------------------
PROTO_SRC_DIR="./control_and_telemetry/protos"
PROTO_OUT_DIR="./control_and_telemetry/grpc_python"
PYTHON_MODULE_NAME="control_and_telemetry/grpc_python"

# Ensure directories exist
mkdir -p "$PROTO_OUT_DIR"
mkdir -p "$PROTO_OUT_DIR/common"

# -------------------------
# CHECK DEPENDENCIES
# -------------------------
if ! command -v python3 &> /dev/null; then
    echo "Python3 is required"
    exit 1
fi

if ! python3 -c "import grpc_tools" &> /dev/null; then
    echo "grpcio-tools not installed. Installing..."
    python3 -m pip install --upgrade grpcio grpcio-tools
fi

# Optional: Install typing support
python3 -m pip install --upgrade mypy-protobuf

# -------------------------
# CLEAN PREVIOUS GENERATED FILES
# -------------------------
echo "Cleaning previous generated files..."
find "$PROTO_OUT_DIR" -type f -name "*.py" -delete
find "$PROTO_OUT_DIR" -type f -name "*.pyi" -delete

# -------------------------
# GENERATE GRPC PYTHON CODE
# -------------------------
echo "Generating Python gRPC code from .proto files..."

echo "Processing files..."
python3 -m grpc_tools.protoc \
    -I "$PROTO_SRC_DIR" \
    --python_out=$PYTHON_MODULE_NAME \
    --grpc_python_out=$PYTHON_MODULE_NAME \
    --pyi_out=$PYTHON_MODULE_NAME \
    $(find $PROTO_SRC_DIR -name "*.proto")

# -------------------------
# generate __init__.py files for module imports
# -------------------------
echo "Creating __init__.py files..."
find "$PROTO_OUT_DIR" -type d -exec touch {}/__init__.py \;

echo "✅ Python gRPC code generated successfully in $PROTO_OUT_DIR"
