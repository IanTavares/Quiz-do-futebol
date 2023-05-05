from time import sleep
print("Seja bem vindo ao quiz do Esporte")
user = input("Quer começar a jogar? (S/N): ")
if user in 'Nn':
    quit()

score = 0

print("COMEÇANDO...")
sleep(2)
print("PRIMEIRA PERGUNTA")
print("Qual clube brasileiro tem o maior número de títulos da Copa Libertadores da América? \n (A) Grêmio \n (B) São Paulo \n (C) Santos \n (D)Flamengo \n (E)Palmeiras")
user_1 = input("Resposta: ")
sleep(1)
if user_1 == "E":
    print("CORRETO! Palmeiras com 2 títulos")
    score = score + 1
else:
    print("INCORRETO!")

print("SEGUNDA PERGUNTA")
sleep(2)
print("Qual jogador brasileiro foi eleito o melhor do mundo pela FIFA em 1999? \n (A) Ronaldo \n (B) Ronaldinho \n (C) Kaká \n (D)Romário \n (E)Rivaldo")
user_1 = input("Resposta: ")
sleep(1)
if user_1 == "E":
    print("CORRETO! Rivaldo")
    score = score + 1
else:
    print("INCORRETO!")

print("TERCEIRA PERGUNTA")
sleep(2)
print("Em que ano o Brasil sediou a Copa do Mundo pela primeira vez? \n (A) 1954 \n (B) 1958 \n (C) 1962 \n (D)1966 \n (E)1970")
user_1 = input("Resposta: ")
sleep(1)
if user_1 == "B":
    print("CORRETO! 1958")
    score = score + 1
else:
    print("INCORRETO!")

print("QUARTA PERGUNTA")
sleep(2)
print("Qual foi o resultado da final da Copa do Mundo de 2002, vencida pelo Brasil? \n (A) Brasil 1x0 Alemanha \n (B) Brasil 2x1 Itália \n (C) Brasil 2x0 Alemanha \n (D)Brasil 3x1 França \n (E)Brasil 2x0 Inglaterra")
user_1 = input("Resposta: ")
sleep(1)
if user_1 == "C":
    print("CORRETO! Brasil 2x0 Alemanha")
    score = score + 1
else:
    print("INCORRETO! (C)Brasil 2x0 Alemanha")

print("QUINTA PERGUNTA")
sleep(2)
print("Em que cidade brasileira fica o Estádio do Maracanã? \n (A) Rio de Janeiro \n (B) Minas Gerais \n (C) São Paulo \n (D) Ceará \n (E)Rio grande do Norte")
user_1 = input("Resposta: ")
sleep(1)
if user_1 == "A":
    print("CORRETO! Rio de janeiro")
    score = score + 1
else:
    print("INCORRETO!")

print("SEXTA PERGUNTA")
sleep(2)
print("Qual jogador brasileiro é considerado o maior artilheiro da história da Seleção Brasileira? \n (A) Romário \n (B) Ronaldo \n (C) Pelé \n (D) Garrincha \n (E) Zé Ramalho")
user_1 = input("Resposta: ")
sleep(1)
if user_1 == "C":
    print("CORRETO! Pelé, com 77 gols marcados.")
    score = score + 1
else:
    print("INCORRETO!")

print("SÉTIMA PERGUNTA")
sleep(2)
print("Qual clube brasileiro foi o primeiro a conquistar a Tríplice Coroa (Campeonato Brasileiro, Copa do Brasil e Copa Libertadores na mesma temporada)? \n (A)São Paulo \n (B)Flamengo \n (C)Santos \n (D)Internacional \n (E)Grêmio")
user_1 = input("Resposta: ")
sleep(1)
if user_1 == "A":
    print("CORRETO! São Paulo, em 1993")
    score = score + 1
else:
    print("INCORRETO!")

print("OITAVA PERGUNTA")
sleep(2)
print("Qual foi o primeiro time brasileiro a vencer a Copa Intercontinental (atual Mundial de Clubes)? \n (A)São Paulo \n (B)Flamengo \n (C)Santos \n (D)Internacional \n (E)Grêmio")
user_1 = input("Resposta: ")
sleep(1)
if user_1 == "C":
    print("CORRETO! Santos, em 1962")
    score = score + 1
else:
    print("INCORRETO!")

print("NONA PERGUNTA")
sleep(2)
print("Qual jogador brasileiro foi artilheiro da Copa do Mundo de 1994, vencida pelo Brasil? \n (A)Ronaldo \n (B)Romário \n (C)Bebeto \n (D)Edmundo \n (E)Batistuta")
user_1 = input("Resposta: ")
sleep(1)
if user_1 == "B":
    print("CORRETO! Romário, com 5 gols")
    score = score + 1
else:
    print("INCORRETO!")

print("DÉCIMA E ULTIMA PERGUNTA")
sleep(2)
print("Em que ano o Brasil conquistou a medalha de ouro no futebol masculino nas Olimpíadas? \n (A)1996 \n (B)2000 \n (C)2004 \n (D)2008 \n (E)2016")
user_1 = input("Resposta: ")
sleep(1)
if user_1 == "E":
    print("CORRETO! 2016")
    score = score + 1
else:
    print("INCORRETO!")

print(f'QUIZ DO FUTEBOL ACABOU & SUA PONTUAÇÃO FOI: {score}/10')