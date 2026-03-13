from kivy.app import App
from kivy.uix.label import Label

class A_App(App):
    def build(self):
        # Ye aapki app ka simple screen hai
        return Label(text="A App is Running!", font_size='50sp')

if __name__ == '__main__':
    A_App().run()
