import kivy
import livedragonMain
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.title = 'Whale Combat - Deceiful Candle'
        return Label(text = "Test content")
        
if __name__ == "__main__":
    MyApp().run()