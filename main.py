import pyautogui
# import PIL
import subprocess
import threading
import time

class ScreenTextChecker:
    # confidence = 0.6
    def __init__(self, screenshot_path, confidence=0.6):
        self.screenshot_path = screenshot_path
        self.confidence = confidence
        self.text_location = None
        self.identifier = None

    def take_screenshot(self):
        screen = pyautogui.screenshot()
        screen.save(self.screenshot_path)

    def check_text_on_screen(self, text):
        self.take_screenshot()
        try:
            location = pyautogui.locateCenterOnScreen(image=text, confidence=self.confidence)
            if location is not None:
                self.text_location = location
                return True
            else:
                return False
        except pyautogui.ImageNotFoundException:
            print("image not found")
            return False

    def get_text_location(self):
        return self.text_location

    def text_to_find(self, identifier):
        text_names = ['launcher.png', 'start.png', 'come_in.png']
        self.identifier = identifier
        if self.identifier < 4:
            text = text_names[self.identifier]
            return text
        else:
            return None


def run_as_admin():
    subprocess.Popen(['C:\\Program Files\\Genshin Impact\\launcher.exe'])


def run_launcher():
    threading.Thread(target=run_as_admin).start()


if __name__ == "__main__":
    run_launcher()
    time.sleep(30)
    checker = ScreenTextChecker(screenshot_path="screenshot.png")
    identifier = 0

    attempts = 3

    time.sleep(5)
    text_to_find = checker.text_to_find(identifier)
    for i in range(attempts):
        text_to_find = checker.text_to_find(identifier)
        if checker.check_text_on_screen(text_to_find):
            if text_to_find == "start.png" or text_to_find == "come_in.png":
                screen_width, screen_height = pyautogui.size()
                text_location = [screen_width // 2, screen_height // 2]
            else:
                text_location = checker.get_text_location()
            pyautogui.click(text_location[0], text_location[1])
            identifier += 1
            time.sleep(60)
        else:
            print("Error while finding image")
            break

