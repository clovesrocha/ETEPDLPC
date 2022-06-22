#exercicio
dict = {'nome': 'Guido van Rossum',
        'linguagem': 'Python',
        'similar': ['c','Modula-3','lisp'],
        'users': '1000000'}
for k,v in dict.items():
    print(k,v)

import json

json.dumps(dict)
with open('arquivos/dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict))