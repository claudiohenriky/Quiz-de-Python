#===================================================
#DESAFIO DEV:MINI-QUIZ DE TECNOLOGIA 🐍
#===================================================
#IINTITUIÇÃO: Colégio Estadual Jardim Oriente (CEJO)
#CURSO:Técnico em Desenvolvimento de Sistemas
#ESTUDADE: Claudio Henriky Gomes Santos 
#TURMA: 1°B (VESPERTINO)
#DATA:06/10/2026
#UC: Lógica de Programação |/Programação de Apps |
#DESCRIÇÂO: MINI-QUIZ DE TECNOLOGIA
#==================================================

print("=== BEM-VINDO AO QUIZ TECH CEJO/SENAI ===")
nome = input("Digite seu nome: ")
print(f"\nÓla,{nome}! Responda às perguntas com A, B ou C:\n")

pontuacao = 0
#___ PERGUNTA 1 ___
print("1) Qual linguagem estamos aprendendo nessa aula ? ")
print("A)HTML")
print("B) Python")
print("C)C++")
resposta1 = input("Sua resposta: ").upper()
if resposta1 == "B":
    print("✔ Resposta correta! +1 ponto.\n")
    pontuacao = pontuacao + 1
else:
    print("❌ Resposta incorreta. A certa era B (Python).\n")
# --- PERGUNTA 2 ---

print("2) O que significa a sigla SGBD em Banco de Dados ?")
print("A) Sistema de Gerenciamento de Banco de Dados")
print("B) Sistema Geral de Busca Digital")
print("C) Software de Gravação de Baixo Desenpenho")
resposta2 = input("Sua resposta: ").upper()
if resposta2 == "A":
    print("✔ Resposta correta! +1 ponto.\n")
    pontuacao = pontuacao + 1
else: print("❌ Resposta incorreta. A certa era A.\n")

#--- PERGUNTA 3 ---
print("3)Qual comando em Python é usado para exibir mensagens na tela ?")
print("A) input()")
print("B) print()")
print("C) import()")
resposta3 = input("Sua resposta: ").upper()
if resposta3 == "B":
    print("✔ Resposta correta! +1 ponto.\n")
    pontuacao = pontuacao + 1
else:
    print("❌ Resposta incorreta. A certa era B.\n")

# --- PERGUNTA 4 ---
print("4) Qual é a função do comando input() em Python?")
print("A) Exibir uma mensagem na tela")
print("B) Receber uma entrada de texto do utilizador")
print("C) Fechar o programa")
resposta4 = input("Sua resposta: ").upper()
if resposta4 == "B":
    print("✔ Resposta correta! +1 ponto.\n")
    pontuacao = pontuacao + 1
else:
    print("❌ Resposta incorreta. A certa era B.\n")


# --- PERGUNTA 5 ---
print("5) Qual símbolo é usado para fazer comentários de uma linha em Python?")
print("A) //")
print("B) <!-- -->")
print("C) #")
resposta5 = input("Sua resposta: ").upper()
if resposta5 == "C":
    print("✔ Resposta correta! +1 ponto.\n")
    pontuacao = pontuacao + 1
else:
    print("❌ Resposta incorreta. A certa era C.\n")

#--- RESULTADO FINAL ---
print("====================================================")
print(f"Fim do Quiz, {nome}!")
print(f"Sua pontuação final foi: {pontuacao} de 5 pontos.")
if pontuacao == 5:
    print("Exelente! Você acertou tudo!")
elif pontuacao >= 1:
    print("Bom trabalho! Dá para melhorar revisando o conteúdo.")
else:
    print("Precisa estudar mais um pouquinho!")
print("======================================================================")
