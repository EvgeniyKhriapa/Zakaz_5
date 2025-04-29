import sass
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class SassHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".scss"):
            print(f"Файл {event.src_path} змінено! Євгеній, зачекайте, виконується компіляція...")
            sass.compile(dirname=('scss', 'css'))
            print("✅ SASS оновлено!")

observer = Observer()
observer.schedule(SassHandler(), path="./scss", recursive=True)
observer.start()

print("🔄 Євгеній, чекаю зміни у SCSS... (натисни Ctrl+C для виходу)")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
