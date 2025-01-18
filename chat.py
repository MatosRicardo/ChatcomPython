# Importar o Flet
import flet as ft

# Criando função principal para rodar o aplicativo
def main(page: ft.Page):  # Recebe 'page' como argumento
    # Título inicial
    titulo = ft.Text("Chatzap", size=30, weight="bold")
    
    def enviar_mensagem_tunel2(mensagem)
    # Todos os usuarios iram receber a mensagem
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        page.update()
    
    # Container para o chat
    chat = ft.Column()
    
    # Criando o campo para o nome do usuário
    caixa_nome = ft.TextField(label="Digite seu nome")
    
    # Função para enviar mensagens
    def enviar_mensagem_tunel(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        texto = ft.Text(f"{nome_usuario}: {texto_campo_mensagem}")
        chat.controls.append(texto)

        # Se um arquivo for selecionado, enviar o nome do arquivo
        if file_picker.files:
            for arquivo in file_picker.files:
                chat.controls.append(ft.Text(f"{nome_usuario} enviou o arquivo: {arquivo.name}"))
        
        campo_enviar_mensagem.value = ""  # Limpa o campo de mensagem após envio
        page.update()

    # Campo e botão para enviar mensagens
    campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem...", on_submit=enviar_mensagem_tunel)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem_tunel)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar_mensagem], spacing=10)
    
    # Função para entrar no chat
    def entrar_chat(evento):
        # Fechar o pop-up
        popup.open = False
        # Remover elementos iniciais
        page.controls.clear()
        # Adicionar chat
        page.add(chat)
        # Adicionar campo de mensagem e botão à página
        page.add(linha_enviar)
        
        # Adicionar a mensagem, "fulano entrou no chat"
        nome_usuario = caixa_nome.value
        texto_mensagem = ft.Text(f"{nome_usuario} entrou no chat")
        chat.controls.append(texto_mensagem)
        page.update()
    
    # Criando pop-up
    titulo_popup = ft.Text("Bem-vindo ao Chatzap")
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
    
    # Adicionando o file picker
    def on_file_selected(evento):
        print("Arquivo selecionado:", evento.files)
    
    file_picker = ft.FilePicker(on_result=on_file_selected)
    botao_selecionar_arquivo = ft.ElevatedButton("Selecionar Arquivo", on_click=lambda e: file_picker.pick_files())
    
    # Colocar os elementos iniciais na página
    page.add(titulo)  # Adiciona o título à página
    page.add(botao)   # Adiciona o botão à página
    page.add(botao_selecionar_arquivo)  # Adiciona o botão para selecionar o arquivo
  
# Executando
ft.app(target=main, view=ft.WEB_BROWSER)
