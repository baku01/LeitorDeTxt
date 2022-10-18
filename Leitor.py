

import os




print("""      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)  L0gic_B0mb \n""")


pasta = input("Caminho:")
os.getcwd()
ArquivoProcurado = input("Arquivos desejado: ")




for diretorios, subpastas, arquivos in os.walk(pasta):
    a = os.path.join(diretorios, ArquivoProcurado)
    if os.path.isfile(a):
        with open(a, encoding="utf-8") as LerAquivo:
            Conteudo = LerAquivo.read()
            print(Conteudo)
    
