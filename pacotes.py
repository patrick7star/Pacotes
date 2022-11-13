#!/usr/bin/python3 -O
"""
Programa em sí que baixa os pacotes
e arruma no atual diretório. Também
é possível selecionar o arquivo
específico a extrair.
"""

# deste programa:
from gerenciador import carrega, mapa, listagem, carrega_rust
from obtencao import baixa

# biblioteca externa:
from python_utilitarios.utilitarios import arvore
GalhoTipo = arvore.GalhoTipo
arvore = arvore.arvore

# biblioteca padrão do Python:
from sys import argv, platform
from shutil import move
from time import sleep
from os.path import basename, exists
from shutil import rmtree


# listando os pacotes ...
if __debug__:
   print("argumentos passados:", argv, end="\n\n")

# ativa versão para o Rust packages
# caso seja pedido.
versao_rust = False
if "--rust" in argv:
   indice = argv.index("--rust")
   argv.pop(indice)
   versao_rust = True
   assert versao_rust
   print("versão Rust acionada.")
   del carrega
else:
   assert not versao_rust
   if __debug__:
      print("versão Python acionada.")
...


if len(argv) == 1:
   if not versao_rust:
      listagem()
   else:
      carrega_rust()
else:
   if versao_rust:
      if __debug__:
         print("foi acionado?")
      carrega_rust()
   else:
      carrega()

   for arg in argv[1:]:
      caminho = baixa(arg, mapa)
      estrutura = arvore(caminho, True, GalhoTipo.FINO)

      # remove o diretório/arquivo se existente.
      nome_dir = basename(caminho)
      if exists(nome_dir):
         rmtree(nome_dir, ignore_errors=True)
         print("'{}' removido.".format(nome_dir))
      ...

      move(caminho, ".")
      print(
         "{}\n\"{}\" foi baixado com sucesso." 
         .format(estrutura, arg), 
         end="\n\n"
      )
   ...
...

# pausa para ver os output por alguns segundos.
if platform == "win32":
   sleep(5.5)
