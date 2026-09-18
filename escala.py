from pathlib import Path

path_bd = Path("sincro-escala/BD") / "escalas_bd.txt"
escalas = []

def cadastrar_escalas(): 
    escala = input("Digite o nome da Escala: ")
    with open(path_bd,"a", encoding="utf-8") as arquivo:
        arquivo.write(f"{escala}\n")

    print(f"O nome cadastrado foi: {escala}")
    print("===================================================")
    print("Você gostaria de adicionar uma nova Escala?")
    print(" 1. Sim ✅​")
    print(" 2. Não ❌​")
    seguir_cadastro = input("Escolha uma opção: ")
    print("===================================================")
    if seguir_cadastro == "1":
        cadastrar_escalas()
    if seguir_cadastro == "2":
        print("Cadastro concluído!​✅​")
    
def listar_escala(): 
    with open(path_bd,"r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome_limpo = linha.strip()
            if nome_limpo not in escalas:
                escalas.append(nome_limpo)

    print("\n".join(escalas))
    
def excluir_escala():
    listar_escala()
    escala = input("Qual Escala você deseja deletar?: ")
    with open(path_bd,"r", encoding="utf-8") as arquivo:
        nomes = arquivo.readlines()
       
    with open(path_bd,"w", encoding="utf-8") as arquivo:
        for linha in nomes:
            if linha.strip() == escala:
                linha = "" 

            arquivo.write(linha) 
