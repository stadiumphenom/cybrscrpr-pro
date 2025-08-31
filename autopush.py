import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GitAutoPushHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_push = 0

    def on_any_event(self, event):
        if time.time() - self.last_push < 5:
            return
        self.last_push = time.time()

        try:
            # Only commit if there are changes
            status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
            if not status.stdout.strip():
                return

            # Detect current branch
            branch = subprocess.check_output(["git", "branch", "--show-current"]).decode().strip()

            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Auto update from folder drop"], check=True)
            subprocess.run(["git", "push", "origin", branch], check=True)
            print(f"✅ Changes pushed to GitHub branch: {branch}")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Git error: {e}")

if __name__ == "__main__":
    path = "."
    event_handler = GitAutoPushHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("🔁 Watching for changes... Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
