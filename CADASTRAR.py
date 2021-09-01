import pymysql.cursors

conexao = pymysql.connect(

    host='localhost',
    user='root',
    passwd='',
    db='cadastrarelogar',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor



)

autentico = False

def logarCadastrar():

    existente = 0
    autenticado = False

    if decisa == 1:
        print('ok colocou para logar')

        usuario = input('digite seu usuario')
        senha = input('sua senha')

        for dado in resultado:
            if usuario == dado['usuario'] and senha == dado['senha']:
                print(f'usuario logado com sucesso {usuario}')
                autenticado = True

        if not autenticado:
            print('erro ao tentar logar')


    if decisa == 2:
        nome = input('nome')
        sobrenome = input('sobrenome')
        idade = input('idade')
        cpf = input('cpf')

        usuario = input('usuario')
        senha = input('crie uma senha')


        #validador de usuario

        for dado in resultado:
            if usuario == dado['usuario'] and senha == dado['senha']:
                existente = 1


        if existente == 1:
            print('usuario existente')




        try:
            with conexao.cursor() as cursor:
                cursor.execute('insert into usuarios(nome, sobrenome, idade, cpf, usuario, senha) values (%s, %s, %s, %s, %s, %s)', (nome, sobrenome, idade, cpf, usuario, senha))
                print('usuario cadastrado com sucesso')
        except:
            print('falha ao tentar acessar o banco de dados')





    return autenticado



while not autentico:

    decisa = int(input('1 para logar, 2 para cadastrar'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from usuarios')
            resultado = cursor.fetchall()
    except:
        print('erro ao conectar ao bancod e dados')



    autentico = logarCadastrar()

    if autentico == True:
        print('Usuario autenticado')


