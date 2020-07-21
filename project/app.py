from views.AuthView import AuthView
from views.MainView import MainView

class MyApp:

    def run(self):
        av = AuthView()
        av.transfer_control = self.voice
        av.load()
        
    def voice(self):
        mv = MainView()
        mv.load()

app = MyApp()
app.run()