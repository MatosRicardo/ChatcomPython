# Importar o Flet
import flet as ft

# Criando função principal para rodar o aplicativo
def main ():
  # título
  titulo = ft.Text("RickZap")
  pagina.add(titulo)
  
  # botão inicial
  botao = ft.ElevatedButton("Iniciar Chat")
  pagina.addd(botao)
  
# Executando
ft.app(main)