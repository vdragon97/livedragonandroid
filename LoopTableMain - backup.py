import livedragonMain
import time
from datetime import datetime
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
import userReadTelegramSMS
import ast

class MyApp(MDApp):
    def build(self):
        self.title = 'WShale Combat - Deceiful Candle'
        layout = AnchorLayout()
        tableData = ast.literal_eval(userReadTelegramSMS.__loadLastMessage__())
        print(tableData)
        screen = Screen()
        table = MDDataTable(
            size_hint=(1, 1),
            pos_hint = {'center_x': 0.1, 'center_y': 0.1},
            rows_num = 200,
            #use_pagination=True,
            column_data = [
                ("Time", dp(20)),
                ("Price", dp(20)),
                ("Position", dp(20)),
                ("Volume", dp(20))
            ],
            row_data = tableData
            )
        #self.theme_cls.theme_style = "Light"
        #self.theme_cls.primary_palette = "BlueGray"
        #screen.add_widget(table)    
        #return screen
        layout.add_widget(table)
        return layout
            
if __name__ == "__main__":
    MyApp().run()