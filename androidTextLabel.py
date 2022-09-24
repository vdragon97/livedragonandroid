import kivy
import userReadTelegramSMS
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.title = 'Whale Combat - Deceiful Candle'
        try:
            return Label(text = userReadTelegramSMS.__loadLastMessage__())
        except:
            return Label(text = "No information found")
if __name__ == "__main__":
    MyApp().run()