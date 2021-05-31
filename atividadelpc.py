class Pilha:

    def __init__(self, ):
        self.elementos = list()
        self.elementos2 = list()

    def desempilhar(self, ):
        return self.elementos.pop()

    def desempilhar2(self, ):
        return self.elementos2.pop()

    def verificaMaior1(self):
        e1 = self.elementos[0]
        for val in self.elementos:
            if e1 < val:
                e1 = int(val)
        print("O maior número da pilha 1 é:")
        return e1

    def verificaMaior2(self):
        e2 = self.elementos2[0]
        for val in self.elementos2:
            if e2 < val:
                e2 = int(val)
        print("O maior número da pilha 2 é:")
        return e2

    def somar(self, ):
        app = self.elementos2.append(self.elementos[-1])
        p = self.elementos.pop()
        return app, p


pilha = Pilha()

for i in range(0, 5):
    n = int(input(f"Digite o {i + 1}º item da sua 1ª pilha: "))
    pilha.elementos.append(n)

print(60 * "_")
print("Empilhando a sua primeira lista!")
print(pilha.elementos)
print(60 * "_")

for i in range(0, 5):
    n = int(input(f"Digite o {i + 1}º item da sua 2ª pilha: "))
    pilha.elementos2.append(n)

print(60 * "_")
print("Empilhando a sua segunda lista!")
print(pilha.elementos2)
print(60 * "_")

tam = len(pilha.elementos)
tam2 = len(pilha.elementos2)

print(60 * "_")

confirmation = "s"

while confirmation == "s":
    print(60 * "_")

    opcao = int(input('''
    [1]- Desempilhar (Não priorize o desempilhamento)
    [2]- Somar Vetor (Não priorize a soma dos vetores)
    [3]- Pares
    [4]- Negativos
    [5]- Verificar maior
    Resposta: '''))

    if opcao == 1:
        for _ in range(0, tam):
            print(f'O {_ + 1}º lemento a ser removido da sua primeira pilha é: {pilha.elementos[-1]}')
            print(pilha.elementos)
            pilha.desempilhar()
            if not pilha.elementos:
                print('A pilha não possui nenhum elemento.')
        print(60 * "_")

        for x in range(0, tam2):
            print(f'O {x + 1}º elemento a ser removido da sua segunda pilha é: {pilha.elementos2[-1]}')
            print(pilha.elementos2)
            pilha.desempilhar2()
            if not pilha.elementos2:
                print('A pilha não possui nenhum elemento.')
        print(60 * "_")

    if opcao == 2:
        q = len(pilha.elementos)
        for _ in range(0, q):
            pilha.somar()

        pilha.elementos2.sort()
        print(pilha.elementos2)
        print(60 * "_")

    if opcao == 3:
        print("Verificando a primeira pilha")
        print(60 * "_")
        print(60 * "_")

        for a in range(0, tam):
            if (pilha.elementos[a] % 2) == 0:
                print(f'Número par: {pilha.elementos[a]}')
                print(60 * "_")

            elif pilha.elementos[a] % 2 == 1:
                print(f'Número ímpar: {pilha.elementos[a]}')
                print(60 * "_")

        print("Verificando a segunda pilha")
        print(60 * "_")
        print(60 * "_")

        for z in range(0, tam2):
            if pilha.elementos2[0] % 2 == 0:
                print(f'Numero par: {pilha.elementos2[z]}')
                print(60 * "_")

            elif pilha.elementos2[0] % 2 == 1:
                print(f'Número ímpar: {pilha.elementos2[z]}')
                print(60 * "_")

    if opcao == 4:
        print("Verificando a primeira pilha")
        print(60 * "_")
        print(f'A quantidade de elementos na lista são: {tam}')

        for c in range(0, tam):
            if pilha.elementos[c] < 0:
                print(f'O número negativo é: {pilha.elementos[c]}')
                pilha.desempilhar()
            else:
                print(f'O número: {pilha.elementos[c]} é positivo.')
        print(60 * "_")

        print("Verificando a segunda pilha")
        print(60 * "_")
        print(f'A quantidade de elementos na lista são: {tam2}')

        for y in range(0, tam):
            if pilha.elementos2[y] < 0:
                print(f'Número negativo: {pilha.elementos2[y]}')
            else:
                print(f'O número: {pilha.elementos2[y]} é positivo.')
        print(60 * "_")


    if opcao == 5:
        print(pilha.verificaMaior1())
        print(pilha.verificaMaior2())

    confirmation = input("Você quer continuar? [s/n]")
