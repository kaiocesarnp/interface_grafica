from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""
        
class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created
 
class WindowManager(ScreenManager):
    pass

    def invalidLogin():
        pop = Popup(title='Invalid Login', content = label(text = 'Invalid username or password.'),
        size_hint = (None, None), size = (400, 400))
        pop.open()

    def invalidForm():
        pop = Popup(title = 'Invalid Form', content = label(text = 'Please fill in all inputs with valid information.'),
        size_hint = (None, None), size = (400, 400))
        pop.open()

kv = Builder.load_file("my.kv")
sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name = "login"),
CreateAccountWindow(name = "create"), MainWindow(name = "main")]
for Screen in screens:
    sm.add_widget(Screen)
 
sm.current = "login"

class MyMainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyMainApp().run()

#Explicação linha à linha:

#Linhas 'from':
    #São as importações necessárias para as várias partes da biblioteca Kivy, como a criação de aplicativos (App),
    #a definição de interfaces de usuário (Builder), o gerenciamento de telas (ScreenManager, Screen),
    #propriedades de objetos (ObjectProperty), pop-ups (Popup) e rótulos (Label).
    #Também há uma importação de uma classe DataBase do arquivo "database.py".


#CreateAccountWindow:
    #Aqui é definida a classe CreateAccountWindow, que herda de Screen. Essa classe representa a tela de criação de conta.
    #Ela possui três propriedades de objetos: namee, email e password, que se referem aos campos de entrada na interface.

    #Método submit() da Classe CreateAccountWindow:
        #O método submit() é chamado quando o botão de submissão é pressionado. Ele verifica se os campos foram preenchidos corretamente e,
        #se sim, adiciona o usuário ao banco de dados e redireciona para a tela de login.
        #Se os campos não estiverem preenchidos corretamente, exibe um pop-up de erro.


#class LoginWindow(Screen):
    #Aqui é definida a classe LoginWindow, que herda da classe Screen.
    #Ela representa a tela de login e possui propriedades de objetos email e password.

    #Métodos loginBtn() e createBtn() da Classe LoginWindow:
        #O método loginBtn() é chamado quando o botão de login é pressionado. Ele verifica se as credenciais de login são válidas e redireciona para a tela principal. Caso contrário, exibe um pop-up de erro.
        #O método createBtn() redireciona para a tela de criação de conta.

    
#class MainWindow(Screen):
    #A classe MainWindow representa a tela principal após o login. Ela herda de Screen e possui propriedades de objetos n, created e email.

    #Métodos logOut() e on_enter() da Classe MainWindow:
        #O método logOut() é chamado quando o botão de logout é pressionado, redirecionando para a tela de login.
        #O método on_enter() é chamado quando a tela é acessada e exibe informações da conta na tela principal.


#class WindowManager(ScreenManager):
    #Esta classe herda de ScreenManager.
    #Ela contém os métodos estáticos invalidLogin() e invalidForm() que exibem pop-ups de erro para login inválido e formulário inválido, respectivamente.


#kv = Builder.load_file("my.kv"):
    #Aqui, o arquivo "my.kv" é carregado para definir a aparência da interface gráfica.
    

#WindowManager, Banco de Dados e Telas:
    #Uma instância de WindowManager é criada.
    #Uma instância do banco de dados DataBase é criada.
    #Uma lista de telas (screens) é definida com as telas de login, criação de conta e tela principal. As telas são adicionadas ao WindowManager.


#sm.current = "login" & 
    #A tela inicial é definida como "login".


#class MyMainApp(App):
    #É criada a classe MyMainApp que herda de App.

    #Método build() da Classe MyMainApp:
        #Este método retorna a instância do WindowManager que será usada como a raiz do aplicativo.


#Execução do Aplicativo:
    #O bloco if __name__ == "__main__":
        #verifica se o script está sendo executado diretamente, não sendo importado como um módulo.
        #Se for o caso, a instância de MyMainApp é criada e o aplicativo é executado.

















    
