import pyautogui
import time

# Enable safety feature (for emergency stop: move mouse to corner)
pyautogui.FAILSAFE = True

# Size of the square (in pixels)
square_size = 100

# Speed of mouse movement (in seconds)
move_duration = 0.25

# Tweening function for smooth movement
tween_func = pyautogui.easeInOutQuad


def move_in_square():
    """Moves the mouse in a square"""
    # Save current position
    start_x, start_y = pyautogui.position()

    print(f"Starting square movement from position ({start_x}, {start_y})")

    # Move right
    pyautogui.moveTo(start_x + square_size, start_y,
                     duration=move_duration, tween=tween_func)

    # Move down
    pyautogui.moveTo(start_x + square_size, start_y + square_size,
                     duration=move_duration, tween=tween_func)

    # Move left
    pyautogui.moveTo(start_x, start_y + square_size,
                     duration=move_duration, tween=tween_func)

    # Move up (back to start)
    pyautogui.moveTo(start_x, start_y,
                     duration=move_duration, tween=tween_func)

    print("Square movement completed")


def main():
    print("MousePatrol started!")
    print("To exit: Press Ctrl+C or move the mouse to the upper left corner")
    print("-" * 50)

    try:
        while True:
            move_in_square()
            print(f"Waiting 60 seconds until the next movement...")
            time.sleep(60)  # Wait 60 seconds = 1 minute

    except KeyboardInterrupt:
        print("\nProgram terminated.")
    except pyautogui.FailSafeException:
        print("\nEmergency stop: Mouse moved to corner.")


if __name__ == "__main__":
    main()
