#!/bin/bash

# Define paths
TEMP_FILE="/tmp/screenshot_$(date +%s).png"
SAVE_DIR="$HOME/Files/Images/Screenshots"
FINAL_FILE="$SAVE_DIR/satty-$(date +%Y%m%d_%H%M%S).png"

mkdir -p "$SAVE_DIR"

# 1. Capture and copy to clipboard instantly
grim -g "$(slurp)" - | tee "$TEMP_FILE" | wl-copy

# 2. Send notification with an action
# The 'default' action happens if you click the notification body
# The 'edit' action is a specific button
ACTION=$(dunstify -i "$TEMP_FILE" "Screenshot Captured" "Copied to clipboard" \
    --action="edit,Edit with Satty" \
    --timeout=5000)

# 3. Handle the button click
if [ "$ACTION" == "edit" ]; then
    # Open Satty. When you save in Satty, it goes to your final folder
    satty --filename "$TEMP_FILE" --fullscreen --output-filename "$FINAL_FILE"
else
    # If not editing, just move the temp file to your permanent storage
    mv "$TEMP_FILE" "$FINAL_FILE"
fi