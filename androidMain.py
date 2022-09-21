import livedragonMain
import time
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class MyApp(MDApp):
    def build(self):
        self.title = 'Whale Combat - Deceiful Candle'
        tableData = livedragonMain.callLiveDragon("21/09/2022", "VN30F2210", "0.8", "09:00:00", "14:30:00")
        
        screen = Screen()
        table = MDDataTable(
            size_hint = (0.9, 0.6),
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            rows_num = 20,
            column_data = [
                ("Time", dp(30)),
                ("Price", dp(30)),
                ("Vol", dp(30))
            ],
            row_data = tableData
            )
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        screen.add_widget(table)    
        return screen
        
if __name__ == "__main__":
    MyApp().run()