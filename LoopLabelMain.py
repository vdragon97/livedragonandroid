import kivy
import userReadTelegramSMS
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from datetime import datetime

class SharckCombat(App):
    count = 0
    def build(self):
        self.title = 'Whale Combat - Deceiful Candle'
        self.myLabel = Label(text='Waiting for updates...')
        Clock.schedule_interval(self.UpdateTelegramSMS, 2)
        return self.myLabel 

    def UpdateTelegramSMS(self, dt):
        self.count = self.count+1
        self.myLabel.text = datetime.now().strftime("%d/%m/%Y, %H:%M:%S") + "\n" + userReadTelegramSMS.__loadLastMessage__()
if __name__ == '__main__':

    SharckCombat().run()