import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GitAutoPushHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        try:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Auto update from folder drop"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print("✅ Changes pushed to GitHub.")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Git push failed: {e}")

if __name__ == "__main__":
    path = "."  # Watch current directory
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
