import mysql.connector

class CRUD:
    def __init__(self):
        pass
    
    
    def __str__(self):
        print('Crud em python...')


    def drop_database(self, name_database):
        """
:name_database: nome do banco de dados que deseja usar.
:escolha: nome do banco de dados que deseja.

        """

        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='pedro',
                password='1234',
                database=f'{name_database}',
            )
            cur = conexao.cursor()
            escolha = str(input('Digite o nome do banco que deseja excluir: '))
            comando =f'drop database if exists {escolha}'
            
            cur.execute(comando)
            conexao.commit()
            print(f'banco de dados "{escolha}", excluido com sucesso!')

        except mysql.connector.Error as er:
            print(f'Erro:{er}')

        finally:
            cur.close()
            conexao.close()


    def drop_table(self, name_database):
        """
:name_database: nome do banco de dados que deseja usar.
:name_table: nome da tabela que deseja excluir.
        """
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='pedro',
                password='1234',
                database=f'{name_database}',
            )

            cur = conexao.cursor()
            name_table = str(input('Digite o nome da tabela que deseja apagar: '))
            comando = f'drop table if exists {name_table}'

            cur.execute(comando)
            conexao.commit()
        
        except mysql.connector.Error as er:
            print(f'Erro:{er}')
        
        finally:
            cur.close()
            conexao.close()


    def create_database(self, name):
        """
:name: nome que deseja colocar no novo banco de dados criado.
        """
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='pedro',
                password='1234',
            )
            
            cur = conexao.cursor()
            comando = f'create database if not exists {name} default character set utf8mb4 default collate utf8mb4_general_ci'
            cur.execute(comando)
            
            print('ok!')

        except mysql.connector.Error as er:
            print(f'Erro:{er}')

        finally:
            cur.close()
            conexao.close()


    def create_table(self, name_database):
        """
:name_database: nome do banco de dados que deseja usar.
:table: recebe o nome da tabela que deseja criar.
        """
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='pedro',
                password='1234',
                database=f'{name_database}',
                )
            cur = conexao.cursor()
            
            contador = 0
            while True:
                try:
                    table = str(input('Iforme o nome da tabela: ')).strip().capitalize()
                    contador=1
                except:
                    print('Digite um nome válido!')
                    contador=0
                    continue
                if contador == 1:
                    break
                
            comando = f'''
            create table if not exists {table}(
            id int not null auto_increment,
            nome varchar(30) not null,
            primary key(id)
            )engine = innoDB default charset = utf8mb4
            '''

            cur.execute(comando)
            conexao.commit()
        except mysql.connector.Error as er:
            print(f'Erro:{er}')

        finally:
            cur.close()
            conexao.close()

    
    def insert_into(self, name_database, name_tables):
        """
:name_database: nome do banco de dados que deseja usar.
:nane_tables: nome da tabela que deseja usar.
:nome: nome que deseja inserir no valor da tabela.
        """
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='pedro',
                password='1234',
                database=f'{name_database}',
            )
            cur = conexao.cursor()
            nome = str(input('Digite o nome: ')).strip().capitalize()
            comando = f'insert into {name_tables} (nome) values ("{nome}")'
            cur.execute(comando)
            conexao.commit()
        
        except mysql.connector.Error as er:
            print(f'Erro:{er}')
        
        finally:
            cur.close()
            conexao.close()


    def delete(self, name_database):
        """
:name_database: nome do banco de dados que deseja usar.
:name_table: nome da tabela que deseja consultar.
:info: informe a localização do que deseja identificar.
:where_info: identificador localizado pelo where.
        """
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='pedro',
                password='1234',
                database=f'{name_database}',
            )
            cur = conexao.cursor()
            
            name_table = str(input('Digite o nome da tabela deseja: '))
            info = str(input('Informe o where: '))
            where_info = str(input('Informe a identificação do que deseja deletar: '))
            comando = f'delete from {name_table} where {info} = "{where_info}"'
            
            cur.execute(comando)
            conexao.commit()
            print(f'{where_info} deletado com sucesso!')
            
        except mysql.connector.Error as er:
            print(f'Erro:{er}')

        finally:
            cur.close()
            conexao.close()

    
    def alter_table(name_database):
        """
:name_database: nome do banco de dados que deseja usar.
:name_table: nome da tabela que sera alterada.
:name_column: nome da coluna nova que sera adicionada na tabela.
:caracters: adicione tipo de dado e constraints.
        """
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='pedro',
                password='1234',
                database=f'{name_database}',
            )
            cur = conexao.cursor()
            
            name_table = str(input('Digite o nome da tabela que deseja alterar: '))
            name_column = str(input('Digite o nome da coluna que deseja adicionar: '))
            caracters = str(input('Digite caracteristicas da coluna que deseja criar, ex: "int not null": '))
            comando = f'alter table {name_table} add column {name_column} {caracters}'
            
            cur.execute(comando)
            conexao.commit()
            print('Tabela alterada com sucesso!')

        except mysql.connector.Error as er:
            print(f'Erro:{er}')

        finally:
            cur.close()
            conexao.close()


    def select(name_database):
        """
:name_database: nome do banco de dados que deseja usar.
:opcao: complemento do comando select, ou seja, filtrar por: *(tudo).
:name_table: nome da tabela que deseja.

        """
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='pedro',
                password='1234',
                database=f'{name_database}'
            )
            cur=conexao.cursor()
            
            opcao = str(input('Digite o que deseja visualizar, caso de dúvida digite "*": '))
            name_table = str(input('Informe o nome da tabela: '))
            comando = f'select {opcao} from {name_table}'
            cur.execute(comando)
            visualizar = cur.fetchall()
            print(visualizar)

        except mysql.connector.Error as er:
            print(f'Erro:{er}')

        finally:
            cur.close()
            conexao.close()


