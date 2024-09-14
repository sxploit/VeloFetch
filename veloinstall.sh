#!/bin/bash
VELOFETCH="velofetch.py"
VELOFETCH_ALIAS="velofetch"

chmod +x "$VELOFETCH"
sudo cp "$VELOFETCH" "/usr/local/bin/$VELOFETCH_ALIAS"