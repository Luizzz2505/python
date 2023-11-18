# if / elif       / else
# se / se não se / se não 

# muda o fluxo do nosso código

entrada = input('Você quer "entrar" ou "sair"? ')

# tipo boolean, porque só executa um bloco se ele for verdadeiro, senão vai para outro bloco
if entrada == 'entrar': # condição
    print('Você entrou no sistema') # esse trecho de código está dentro do if e só será executado se a condição for verdadeira
elif entrada == 'sair': # coloca-se a condição no elif tbm
    print('Você saiu do sistema')
else: # aqui eu criei esse else para barrar o usuário de prosseguir no sistema caso ele tenha digitado ao de diferente 
    print('Comando inválido')
# if, elif e else dependem um do outro. O único que pode estar sozinho é o if (em casos de houver somente uma condição)
# else é sempre a última opção