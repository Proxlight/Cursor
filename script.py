import pyautogui
import time

# Get the screen width and height
screen_width, screen_height = pyautogui.size()

# Calculate the desired position (e.g., center of the screen)
target_x, target_y = screen_width // 2, screen_height // 2

# Move the cursor to the target position
pyautogui.moveTo(target_x, target_y, duration=1)

# Optional: Pause for a moment to see the cursor movement
time.sleep(2)

# Move the cursor back to the original position (0, 0)
pyautogui.moveTo(0, 0, duration=1)
