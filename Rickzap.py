# Importar o Flet
import flet as ft

# Criando função principal para rodar o aplicativo
def main(page: ft.Page):  # Recebe 'page' como argumento
    # título
    titulo = ft.Text("RickZap")
    
    def entrar_chat(evento):
        # Fechar o pop-up
        popup.open = False
        # Sumir com o titulo
        page.remove(titulo)
        # Sumir com o botao
        page.remove(botao)
        
        
        
        
        pagina.update()
      
    
    # Criando pop-up
    titulo_popup = ft.Text("Bem-vindo ao RickZap")
    caixa_nome = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])
    
    # Função para abrir o modal
    def abrir_modal(evento):
        page.dialog = popup  # Configura o pop-up para a página
        popup.open = True    # Abre o pop-up
        page.update()        # Atualiza a página
        print("Clicou no botão")
      
    # Botão inicial
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_modal)
      
    # Colocar os elementos na página
    page.add(titulo)  # Adiciona o título à página
    page.add(botao)   # Adiciona o botão à página
  
# Executando
ft.app(target=main, view=ft.WEB_BROWSER)
