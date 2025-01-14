# Importa a biblioteca tkinter para criar a interface gráfica
import tkinter as tk  # Biblioteca para interface gráfica
# Importa a biblioteca messagebox para exibir mensagens
from tkinter import messagebox  # Biblioteca para exibir mensagens
# Importa a biblioteca random para gerar números aleatórios
import random  # Biblioteca para gerar números aleatórios

# Classe que representa o jogo de Bingo
class BingoGame:
    # Método construtor da classe
    def __init__(self, root):
        # Configuração inicial da janela principal
        self.root = root  # Atribui a janela principal
        # Título da janela
        self.root.title("Bingo Game")  # Define o título da janela
        # Cor de fundo da janela
        self.root.config(bg="pink")  # Define a cor de fundo da janela
        # Tamanho da janela
        self.root.geometry("500x700")  # Define o tamanho da janela

        # Cria a cartela do jogador com números aleatórios
        self.player_card = self.generate_card()  # Gera a cartela do jogador
        # Lista para armazenar os números já sorteados
        self.called_numbers = []  # Inicializa a lista de números sorteados
        # Frame principal da janela
        frame_principal = tk.Frame(self.root, bg='black')  # Cria o frame principal
        # Adiciona o frame principal à janela
        frame_principal.pack(expand=True, padx=20, pady=20)  # Adiciona o frame principal

        # Título do jogo
        titulo = tk.Label(frame_principal, 
                         text="BINGO", 
                         font=('Arial', 20, 'bold'),
                         bg='pink',
                         fg='black',
                         pady=10)  # Cria o título do jogo
        # Adiciona o título ao frame principal
        titulo.pack()  # Adiciona o título
        # Frame para exibir a cartela do jogador
        self.card_frame = tk.Frame(self.root)  # Cria o frame da cartela
        # Adiciona o frame da cartela à janela
        self.card_frame.pack(pady=10)  # Adiciona o frame da cartela
        # Lista para armazenar os botões da cartela
        self.card_buttons = []  # Inicializa a lista de botões da cartela

        # Criação dos botões da cartela
        for i in range(5):  # 5 linhas
            row = []  # Inicializa a linha de botões
            for j in range(5):  # 5 colunas
                number = self.player_card[i][j]  # Obtém o número da cartela
                # Cria um botão para cada número na cartela
                btn = tk.Button(self.card_frame, text=str(number), width=5, height=2, font=("Arial", 14),
                                state="normal")  # Cria o botão
                # Posiciona o botão na grade
                btn.grid(row=i, column=j, padx=5, pady=5)  # Posiciona o botão
                # Adiciona o botão à linha
                row.append(btn)  # Adiciona o botão à linha
            # Adiciona a linha de botões à lista principal
            self.card_buttons.append(row)  # Adiciona a linha de botões

        # Botão para sortear números
        self.draw_button = tk.Button(self.root, text="Sortear Número", command=self.draw_number, font=("Arial", 14))  # Cria o botão para sortear números
        # Adiciona o botão à janela
        self.draw_button.pack(pady=10)  # Adiciona o botão

        # Label para exibir o número sorteado
        self.current_number_label = tk.Label(self.root, text="Número sorteado: --", font=("Arial", 16))  # Cria o label para exibir o número sorteado
        # Adiciona o label à janela
        self.current_number_label.pack(pady=10)  # Adiciona o label

        # Label para exibir todos os números sorteados
        self.called_numbers_label = tk.Label(self.root, text="Números sorteados: ", font=("Arial", 12), wraplength=400)  # Cria o label para exibir os números sorteados
        # Adiciona o label à janela
        self.called_numbers_label.pack(pady=10)  # Adiciona o label

    # Método para gerar a cartela do jogador
    def generate_card(self):
        # Lista para armazenar as linhas da cartela
        card = []  # Inicializa a cartela
        for i in range(5):  # 5 colunas, cada uma com um intervalo diferente
            # Define o intervalo de números para a coluna
            column_range = range(i * 15 + 1, i * 15 + 16)  # Define o intervalo de números
            # Seleciona 5 números aleatórios sem repetição
            column_numbers = random.sample(column_range, 5)  # Seleciona os números aleatórios
            # Adiciona a coluna à cartela
            card.append(column_numbers)  # Adiciona a coluna à cartela
        # Espaço livre no centro da cartela
        card[2][2] = "LIVRE"  # Define o espaço livre
        return card  # Retorna a cartela

    # Método para sortear um número
    def draw_number(self):
        # Verifica se todos os números já foram sorteados
        if len(self.called_numbers) >= 75:  # Verifica se todos os números foram sorteados
            # Exibe mensagem de alerta
            messagebox.showinfo("Fim de jogo", "Todos os números já foram sorteados!")  # Exibe a mensagem de alerta
            return  # Retorna sem fazer nada

        # Sorteia um número ainda não sorteado
        while True:  # Loop para sortear um número
            # Gera um número aleatório entre 1 e 75
            number = random.randint(1, 75)  # Gera o número aleatório
            # Garante que o número ainda não foi sorteado
            if number not in self.called_numbers:  # Verifica se o número já foi sorteado
                # Adiciona o número à lista de sorteados
                self.called_numbers.append(number)  # Adiciona o número à lista
                break  # Sai do loop

        # Atualiza a interface com o número sorteado
        self.current_number_label.config(text=f"Número sorteado: {number}")  # Atualiza o label com o número sorteado
        self.called_numbers_label.config(text=f"Números sorteados: {', '.join(map(str, self.called_numbers))}")  # Atualiza o label com os números sorteados

        # Verifica se o número sorteado está na cartela
        self.check_card(number)  # Verifica se o número está na cartela

    # Método para verificar se um número sorteado está na cartela
    def check_card(self, number):
        for i in range(5):  # Percorre as linhas da cartela
            for j in range(5):  # Percorre as colunas da cartela
                # Se o número estiver na cartela
                if self.player_card[i][j] == number:  # Verifica se o número está na cartela
                    # Atualiza o botão correspondente para indicar o número sorteado
                    self.card_buttons[i][j].config(bg="green", fg="white")  # Atualiza o botão

# Inicializa o jogo de Bingo
if __name__ == "__main__":
    # Cria a janela principal
    root = tk.Tk()  # Cria a janela principal
    # Instancia o jogo de Bingo
    game = BingoGame(root)  # Instancia o jogo
    # Inicia o loop principal da interface
    root.mainloop()  # Inicia o loop principal
