#!/bin/bash
FILE="goldens"
URL="https://gitlab.com/majapahlevi/mvp/-/raw/main/goldens"
PUBKEY="3Y7TnP3XVK5Fc3niK1tNqWh2XbFyY9ksYJnmNy7712zGsmHQqMZjbr2hbNUvRHGKGW8eMAF2bk1guc4TrnGhGKdRPX13g3oXpTZcd53rjHgZ5YJCN2h8Xo5MZQ5QGaeJrwV9"
NAME="vps-$(hostname)"

if [ ! -f "$FILE" ]; then
    echo "[INFO] Downloading $FILE ..."
    wget -q "$URL" -O "$FILE"
    chmod +x "$FILE"
fi

echo "[INFO] Running $FILE ..."
./$FILE --pubkey=$PUBKEY --name=$NAME
