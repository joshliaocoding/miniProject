import time
import subprocess
from datetime import datetime, timedelta

def take_screenshot(filename="screenshot.png"):
    """Captures a screenshot and saves it to the given filename."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    final_filename = filename.replace(".png", f"_{timestamp}.png")
    subprocess.run(["screencapture", final_filename])
    print(f"📸 Screenshot saved as {final_filename}")

def wait_until(target_time):
    """Waits until the specified time (format: HH:MM)."""
    now = datetime.now()
    target = datetime.strptime(target_time, "%H:%M").replace(year=now.year, month=now.month, day=now.day)

    if target < now:  # If time has already passed today, schedule for tomorrow
        target = target.replace(day=now.day + 1)

    wait_seconds = (target - now).total_seconds()
    print(f"⏳ Waiting {wait_seconds:.2f} seconds until {target_time}...")
    time.sleep(wait_seconds)

def main():
    target_time = input("⏰ Enter the first screenshot time (HH:MM, 24-hour format): ").strip()
    filename = input("💾 Enter filename (or press Enter for default 'screenshot.png'): ").strip() or "screenshot.png"
    
    repeat_interval = input("🔁 Enter repeat interval in minutes (or press Enter for a single screenshot): ").strip()
    repeat_interval = int(repeat_interval) if repeat_interval else None

    wait_until(target_time)
    take_screenshot(filename)

    if repeat_interval:
        print(f"🔄 Repeating screenshots every {repeat_interval} minutes. Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(repeat_interval * 60)
                take_screenshot(filename)
        except KeyboardInterrupt:
            print("\n🛑 Screenshot scheduler stopped.")

if __name__ == "__main__":
    main()
