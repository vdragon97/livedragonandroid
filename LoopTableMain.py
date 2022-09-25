from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
import userReadTelegramSMS
import ast
from kivy.clock import Clock

class MyApp(MDApp):
    def build(self):
        self.title = 'Whale Combat - Deceiful Candle'
        self.layout = AnchorLayout()
        #screen = Screen()
        Clock.schedule_interval(self.UpdateTelegramSMS, 10)
        return self.layout
        
    def UpdateTelegramSMS(self, dt):
        try:
            tableData = ast.literal_eval(userReadTelegramSMS.__loadLastMessage__())
        except:
            tableData = ast.literal_eval("[('No','Data','Found','Today')]")
        print(tableData)
        table = MDDataTable(
            size_hint=(1, 1),
            pos_hint = {'center_x': 0.1, 'center_y': 0.1},
            rows_num = 200,
            use_pagination=True,
            column_data = [
                ("  Time", dp(20)),
                ("  Price", dp(20)),
                ("Position", dp(20)),
                ("Volume", dp(20))
            ],
            row_data = tableData
            )
        #self.layout.remove_widget(table)
        self.layout.clear_widgets()    
        self.layout.add_widget(table)
if __name__ == "__main__":
    MyApp().run()