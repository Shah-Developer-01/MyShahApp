from kivy.app import App
from kivy.uix.label import Label

class ShahApp(App):
    def build(self):
        return Label(text="SHAH MISSION APK SUCCESS")

if __name__ == "__main__":
    ShahApp().run()
