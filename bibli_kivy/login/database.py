import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")
                
    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]



#Explicação por blocos:
#Bloco 1: Importações Iniciais
#Importa o módulo datetime para manipular datas e horários.

#Bloco 2: Definição da Classe DataBase
#Define a classe DataBase com um construtor __init__ que recebe um nome de arquivo.
#Inicializa propriedades filename, users, e file e chama o método load().

#Bloco 3: Método load() da Classe DataBase
#Abre o arquivo no modo de leitura.
#Inicializa o dicionário users.
#Percorre cada linha do arquivo, separa os valores por ponto e vírgula e armazena no dicionário users.
#Fecha o arquivo.

#Bloco 4: Método get_user() da Classe DataBase
#Recebe um e-mail como argumento.
#Verifica se o e-mail existe no dicionário users e retorna as
    #informações do usuário correspondente ou -1 se não encontrado.

#Bloco 5: Método add_user() da Classe DataBase
#Recebe e-mail, senha e nome como argumentos.
#Verifica se o e-mail já existe no dicionário users.
#Se não existir, adiciona as informações do novo usuário ao dicionário, incluindo
    #a data de criação, e chama save() para salvar as alterações no arquivo.

#Bloco 6: Método validate() da Classe DataBase
#Recebe e-mail e senha como argumentos.
#Chama get_user() para verificar se o e-mail existe no dicionário.
#Se existir, compara a senha fornecida com a senha registrada para esse e-mail.

#Bloco 7: Método save() da Classe DataBase
#Abre o arquivo no modo de escrita.
#Percorre o dicionário users e escreve as informações dos usuários no arquivo.

#Bloco 8: Método Estático get_date() da Classe DataBase
#Retorna a data atual em formato de string.
    
