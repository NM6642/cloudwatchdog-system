#!/bin/bash
LOG_FILE="/app/logs.txt"

if [ -f "$LOG_FILE" ]; then
    echo "Truncating log file..."
    > "$LOG_FILE"
    echo "Log file reset."
fi
