import tkinter as tk
from tkinter import messagebox
import random

# Classe que representa o jogo de Bingo
class BingoGame:
    def __init__(self, root):
        # Configuração inicial da janela principal
        self.root = root
        self.root.title("Bingo Game")
        self.root.config(bg="AliceBlue")
        self.root.geometry("500x700")

        # Cria a cartela do jogador com números aleatórios
        self.player_card = self.generate_card()
        self.called_numbers = []  # Lista para armazenar os números já sorteados

        # Frame para exibir a cartela do jogador
        self.card_frame = tk.Frame(self.root)
        self.card_frame.pack(pady=10)
        self.card_buttons = []  # Lista para armazenar os botões da cartela

        # Criação dos botões da cartela
        for i in range(5):  # 5 linhas
            row = []
            for j in range(5):  # 5 colunas
                number = self.player_card[i][j]
                # Cria um botão para cada número na cartela
                btn = tk.Button(self.card_frame, text=str(number), width=5, height=2, font=("Arial", 14),
                                state="normal")
                btn.grid(row=i, column=j, padx=5, pady=5)  # Posiciona o botão na grade
                row.append(btn)  # Adiciona o botão à linha
            self.card_buttons.append(row)  # Adiciona a linha de botões à lista principal

        # Botão para sortear números
        self.draw_button = tk.Button(self.root, text="Sortear Número", command=self.draw_number, font=("Arial", 14))
        self.draw_button.pack(pady=10)

        # Label para exibir o número sorteado
        self.current_number_label = tk.Label(self.root, text="Número sorteado: --", font=("Arial", 16))
        self.current_number_label.pack(pady=10)

        # Label para exibir todos os números sorteados
        self.called_numbers_label = tk.Label(self.root, text="Números sorteados: ", font=("Arial", 12), wraplength=400)
        self.called_numbers_label.pack(pady=10)

    # Método para gerar a cartela do jogador
    def generate_card(self):
        card = []  # Lista para armazenar as linhas da cartela
        for i in range(5):  # 5 colunas, cada uma com um intervalo diferente
            column_range = range(i * 15 + 1, i * 15 + 16)  # Define o intervalo de números para a coluna
            column_numbers = random.sample(column_range, 5)  # Seleciona 5 números aleatórios sem repetição
            card.append(column_numbers)  # Adiciona a coluna à cartela
        card[2][2] = "LIVRE"  # Espaço livre no centro da cartela
        return card

    # Método para sortear um número
    def draw_number(self):
        # Verifica se todos os números já foram sorteados
        if len(self.called_numbers) >= 75:
            messagebox.showinfo("Fim de jogo", "Todos os números já foram sorteados!")
            return

        # Sorteia um número ainda não sorteado
        while True:
            number = random.randint(1, 75)  # Gera um número aleatório entre 1 e 75
            if number not in self.called_numbers:  # Garante que o número ainda não foi sorteado
                self.called_numbers.append(number)  # Adiciona o número à lista de sorteados
                break

        # Atualiza a interface com o número sorteado
        self.current_number_label.config(text=f"Número sorteado: {number}")
        self.called_numbers_label.config(text=f"Números sorteados: {', '.join(map(str, self.called_numbers))}")

        # Verifica se o número sorteado está na cartela
        self.check_card(number)

    # Método para verificar se um número sorteado está na cartela
    def check_card(self, number):
        for i in range(5):  # Percorre as linhas da cartela
            for j in range(5):  # Percorre as colunas da cartela
                if self.player_card[i][j] == number:  # Se o número estiver na cartela
                    # Atualiza o botão correspondente para indicar o número sorteado
                    self.card_buttons[i][j].config(bg="green", fg="white") 

# Inicializa o jogo de Bingo
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    game = BingoGame(root)  # Instancia o jogo de Bingo
    root.mainloop()  # Inicia o loop principal da interface
