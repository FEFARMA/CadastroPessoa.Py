# 1 - Pessoa Fisica / 2 - Pessoa Juridica / 3 - Sair
# 1 - Cadastrar Pessoa Fisica / 2 - Lista Pessoa Fisica / 3 - Sair
# 1 - Cadastrar Pessoa Juridica/ 2 - Lista Pessoa Juridica / 3 - Sair

from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica


def main():
    lista_pf = []
    while True:
        opcao = int(input("Escolha um opcao: 1 - Pessoa Fisica / 2 - Pessoa Juridia / 0 - Sair"))
        if opcao == 1:
            while True:
                opcaopf =int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Volatar ao menu anterior"))
                # Cadastrar uma Pessoa Fisica
                if opcaopf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome da pessoa fisica")
                    novapf.cpf = input("Digite o CPF")
                    novapf.rendimento = float(input("Digite o rendimento mensal (Digite somente numeros):"))

                    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ") # Solicita a data de nascimento
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue # Retornar ao inicio do loop

                    # Cadastro de Endereco
                    novo_end_pf.logradouro = input("Digite o logradouro: ")
                    novo_end_pf.numero = input("Digite o numero")
                    end_comercial = input("Este endereco e comercial? S/N ")
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S'

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso !!")
                # Listar Pessoa Fisica
                elif opcaopf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome} ")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Endereco: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%y')}")
                            print(f"Imposto a ser pago: R$: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista vazia")

                 # SAIR DO MENU ATUAL
                elif opcaopf == 0:
                    print("Voltando ao menu anterior")
                    break
                else:
                    print("Opcao invalida, por favor digite uma das opcoes indicadas")

        elif opcao == 2:
            print("Funcionalidade para pessoa juridica nao implementadas")
            pass
        elif opcao == 0:
            print("Obrigado por utilizar o nosso sistema! Valeu! ")
        else:
            print("Opcao invalida, por favor digite uma das opcoes validas! ")
        
if __name__== "__main__":
    main() # Chama a funcao principal
        
    
