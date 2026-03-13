from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.network.urlrequest import UrlRequest
import json

class A_App(App):
    def build(self):
        # Yahan apna Firebase URL check kar lena
        self.firebase_url = "https://shah-a-social-default-rtdb.firebaseio.com/posts.json"
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Brand Name
        layout.add_widget(Label(text="A", font_size='60sp', bold=True, size_hint_y=None, height=100))
        
        # Input Box
        self.post_input = TextInput(hint_text="What's happening?", size_hint_y=None, height=150, multiline=True)
        layout.add_widget(self.post_input)
        
        # Post Button
        btn = Button(text="POST", size_hint_y=None, height=60, background_color=(0, 0, 0, 1), font_size='20sp')
        btn.bind(on_release=self.send_to_world)
        layout.add_widget(btn)
        
        # Feed Section
        self.feed = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.feed.bind(minimum_height=self.feed.setter('height'))
        
        scroll = ScrollView()
        scroll.add_widget(self.feed)
        layout.add_widget(scroll)
        
        return layout

    def send_to_world(self, instance):
        if self.post_input.text:
            data = json.dumps({"user": "Shah", "content": self.post_input.text})
            UrlRequest(self.firebase_url, req_body=data, method='POST')
            self.post_input.text = ""

if __name__ == '__main__':
    A_App().run()
