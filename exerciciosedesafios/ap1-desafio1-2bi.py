#ETE PORTO DIGITAL
#PROFESSOR: CLOVES ROCHA
#DISCIPLINA: LPC

#[AP1] Exercícios II e Desafios I - 2º BIMESTRE
#TRANSFORME ALGORITMOS EM CÓDIGOS DE SINTAXE PYTHON.

#1 Vale 0,5 na N1 do 2º BIMESTRE.
Algoritmo VetorNumeros
inicio

	var
		vet[I0], n, i, inteiro;
		ArqEntr Arquivo;
	abrir (ArqEntr);
	para i de 0 até 9 passo +I faça
		lerArq (n);
		Vet[i] <- n;
		escrever (Vet[i]);
	fimpara;
	fechar (ArqEn);
fim

#2 Vale 0,5 na N1 do 2º BIMESTRE.
Algoritmo MaiorNumero
inicio

	var
			maior, i, n inteiro;
			ArqEntr Arquivo;
	abrir (ArqEntr, n);
	lerArq(maior);
	para i de I até I9 passo +I faça
			lerArq(maior);
			se (n > maior)
				então
					maior <- n;
			fimse;
	fimpara;
	escrever (maior);
	fechar (ArqEntr, n);
	retornar maior;
fim

#3 Vale 0,5 na N1 do 2º BIMESTRE.
Algoritmo SomaVetor
inicio

	var 
			n, i, s <- 0 inteiro;
			ArqEntr Arquivo;
	abrir (ArqEntr);
	para i de o até 29 passo +I faça
			lerArq(lerArq, n);
			s <- s + n;
		fimpara
		escrever (s);
		fechar (ArqEntr);
fim

#4 Vale 0,5 na N1 do 2º BIMESTRE.
Algoritmo ParesVetor
inicio

	var
		i, n inteiro;
		ArqEntr Arquivo;

	abrir (ArqEntr);
	para i de o até I4 passo +I faça
		ler (ArqEntr, n);
		se (n mod 2 == 0)
				então
						escrever (n);
		fimse
		fechar (ArqEntr);
fim

#5 Vale 0,5 na N1 do 2º BIMESTRE.
Algoritmo PositivoVetor
inicio

		var
				n, i, s <- 0 inteiro;
				ArqEntr Arquivo;

		abrir (ArqEntr);
		para i de 0 até 9 passo +I faça
				ler (ArqEntr, n);
				se (n > 0)
						então
								s <- s + n;
				fimse;
		fimpara;
		escrever (s);
		fechar (ArqEntr);
fim

#6 Vale 0,5 na N1 do 2º BIMESTRE.
Algoritmo VetorNumeros
inicio
		
		var
				n, i inteiro;
				ArqEntr Arquivo;
				P Pilha;
		P <- novo Pilha (I0);
		abrir(ArqEntr);
		para i de 0 até 9 passo +I faça
				lerArq (n);
				P.Empilhar (n);
		fimpara
		P.Mostrar();
		fechar (ArqEntr);
fim

#7 Vale 0,5 na N1 do 2º BIMESTRE.
inteiro MaiorNumero (P Pilha)
inicio
		
		var
				n, maior <- P.Desempilhar(), i, tam inteiro;

		tam <- P.tamanho;
		para i de I até (tam-I) passo +I faça
				n <- P.Desempilhar();
				se (n > maior)
						então
								maior <- n;
				fimse;
		fimpara;
		retornar maior;
fim

#8 Vale 0,5 na N1 do 2º BIMESTRE.
SomaVetor (P Pilha)
inicio
		
		var 
				i, s <- 0 inteiro;
				tam inteiro;

		tam <- P.tamanho;
		para i de 0 até (tam-I) passo +I faça
				s <- s + P.Desempilhar();
		fimpara;
		escrever s;
fim

#9 Vale 0,5 na N1 do 2º BIMESTRE.
ParesVetor (P ListaLigada)
inicio

		var
				i, s tam inteiro;
				tam <- P.ContarNos();

		para i de 0 até (tam-I) passo +I faça
		 		n <- P.Remover(P.ElementoInio());
		 		se (n mod 2 == 0)
		 				então 
		 						escrever (n);
		 		fimse;
		fimpara;
fim

#10 Vale 0,5 na N1 do 2º BIMESTRE.
real PositivoVetor(P ListaLigada)								
inicio
		
		var
				n, tam i, s <- 0 inteiro;

			tam <- P.ContarNos();
			para i de 0 até (tam-I) passo +I faça
				n <- P.Remover(P.ElementoInicio());
				se (n > 0)
						então
								s <- + n;
				fimse;
			fimpara;
			retornar s;
fim

print('Nunca Desista de Seus Sonhos ou Diminua o Brilho dos Seus Olhos!') 
print('Um grande abraço, Prof. MSc. Cloves Rocha.')











