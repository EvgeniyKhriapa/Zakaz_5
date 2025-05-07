import sass
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from threading import Timer

# Налаштування затримки (у секундах)
DEBOUNCE_DELAY = 5  # Змініть на потрібне значення

class SassHandler(FileSystemEventHandler):
    def __init__(self):
        self.debounce_timer = None
    
    def on_modified(self, event):
        if event.src_path.endswith(".scss"):
            # Скасовуємо попередній таймер, якщо він є
            if self.debounce_timer is not None:
                self.debounce_timer.cancel()
            
            # Створюємо новий таймер
            self.debounce_timer = Timer(DEBOUNCE_DELAY, self.compile_sass, [event.src_path])
            self.debounce_timer.start()
    
    def compile_sass(self, src_path):
        print(f"Файл {src_path} змінено! Компіляція")
        sass.compile(dirname=('scss', 'css'))
        print("✅ Оновлено!")

observer = Observer()
observer.schedule(SassHandler(), path="./scss", recursive=True)
observer.start()

print("🔄 Очікую...")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()