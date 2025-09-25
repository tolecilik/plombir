FROM ubuntu:20.04

# Install tools
RUN apt-get update && apt-get install -y \
    wget curl bash \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy files ke container
COPY . .

# Kasih izin eksekusi
RUN chmod +x script.sh

# Jalankan script
CMD ["./script.sh"]
