import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        # Cria o display da calculadora
        self.display = tk.Entry(master, width=20, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Cria os botões da calculadora
        self.criar_botoes()

    def criar_botoes(self):
        # Lista com as configurações dos botões
        botoes = [
            {"text": "7", "row": 1, "column": 0},
            {"text": "8", "row": 1, "column": 1},
            {"text": "9", "row": 1, "column": 2},
            {"text": "/", "row": 1, "column": 3},
            {"text": "4", "row": 2, "column": 0},
            {"text": "5", "row": 2, "column": 1},
            {"text": "6", "row": 2, "column": 2},
            {"text": "*", "row": 2, "column": 3},
            {"text": "1", "row": 3, "column": 0},
            {"text": "2", "row": 3, "column": 1},
            {"text": "3", "row": 3, "column": 2},
            {"text": "-", "row": 3, "column": 3},
            {"text": "0", "row": 4, "column": 0},
            {"text": ".", "row": 4, "column": 1},
            {"text": "=", "row": 4, "column": 2},
            {"text": "+", "row": 4, "column": 3},
        ]

        # Cria os botões e define as funções que serão chamadas ao clicá-los
        for botao in botoes:
            tk.Button(self.master, text=botao["text"], width=5, height=2, command=lambda valor=botao["text"]: self.clicou(valor)).grid(row=botao["row"], column=botao["column"], padx=5, pady=5)

    def clicou(self, valor):
        if valor == "=":
            # Calcula a expressão digitada no display e exibe o resultado
            resultado = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, resultado)
        elif valor == "C":
            # Limpa o display
            self.display.delete(0, tk.END)
        else:
            # Adiciona o valor do botão no display
            self.display.insert(tk.END, valor)

# Cria a janela da calculadora
root = tk.Tk()
app = Calculadora(root)

root.mainloop()
