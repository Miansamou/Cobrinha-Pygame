import mysql.connector

class DBConfig:
    def __init__(self):

        # Inicializção da váriavel de conexão
        self.estaConectado = True

        try:
            # Inicio da conexão com o banco de dados
            self.db = mysql.connector.connect(
                host="ranking.mysql.dbaas.com.br",
                user="ranking",
                passwd="Loca@1020",
                db="ranking"
            )

            self.cursor = self.db.cursor()

        # Caso ocorra algum erro de conexão, será mostrada a mensagem abaixo
        except:
            print("Não foi possível se conectar com o banco de dados")
            self.estaConectado = False

    # Função responsável por realizar a inserção de dados no BD, sendo eles: Nickname e o Score, respectivamente
    def insert(self, Tabela, nickName, Score):

        if self.estaConectado:

            sql_insert_Query = "INSERT INTO `" + Tabela + "`(`NickName`, `Score`) VALUES('" + nickName + "', '" + str(Score) + "')"

            self.cursor.execute(sql_insert_Query)

            self.db.commit()

        else:
            print("Sem conexão com o banco de dados")

    # Função responsável por organizar a tabela em ordem crescente
    def organizarTabela(self, Tabela):

        if self.estaConectado:

            sql_select_Query = "select * from `" + Tabela + "` ORDER BY Score DESC"

            self.cursor.execute(sql_select_Query)

        else:
            print("Sem conexão com o banco de dados")

    # Sempre que o jogo for finalizado, a conexão com o banco precisa ser finalizada também
    def encerrarConexao(self):
        if self.estaConectado:

            self.db.close()
            self.cursor.close()

        else:
            print("Sem conexão com o banco de dados")