#!/bin/bash

OUT_DIR="/var/lib/homeassistant/homeassistant/smartctl"
mkdir -p "$OUT_DIR"

for arg in sd{a..m}; do
    if [ -e "/dev/$arg" ]; then
        /usr/sbin/smartctl --info --all --json --nocheck standby "/dev/$arg" > "$OUT_DIR/$arg.json"
    else
        echo "Устройство /dev/$arg не найдено, пропускаем..."
    fi
done