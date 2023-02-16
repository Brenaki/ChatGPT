# ChatGPT

<div>
  
<p>Para criar uma interface gráfica em Python que permita adicionar palavras em um arquivo JSON, podemos usar a biblioteca tkinter para criar a janela e os elementos da interface, e a biblioteca json para manipular o arquivo JSON. Aqui está um exemplo de código:<p>

  <div>
  <code>
    
        import tkinter as tk
        import json

        class DicionarioGUI:
            def __init__(self, arquivo):
                self.arquivo = arquivo
                self.dicionario = self.carregar_dicionario()
        
                self.root = tk.Tk()
                self.root.title("Dicionário")
        
                # Cria os elementos da interface
                self.lbl_palavra = tk.Label(self.root, text="Palavra em inglês:")
                self.lbl_palavra.grid(row=0, column=0, padx=5, pady=5, sticky="w")
                self.ent_palavra = tk.Entry(self.root)
                self.ent_palavra.grid(row=0, column=1, padx=5, pady=5)
                self.lbl_traducao = tk.Label(self.root, text="Tradução em português:")
                self.lbl_traducao.grid(row=1, column=0, padx=5, pady=5, sticky="w")
                self.ent_traducao = tk.Entry(self.root)
                self.ent_traducao.grid(row=1, column=1, padx=5, pady=5)
                self.btn_adicionar = tk.Button(self.root, text="Adicionar", command=self.adicionar_palavra)
                self.btn_adicionar.grid(row=2, column=0, padx=5, pady=5)
                self.btn_sair = tk.Button(self.root, text="Sair", command=self.sair)
                self.btn_sair.grid(row=2, column=1, padx=5, pady=5)

                self.root.mainloop()
        
            def carregar_dicionario(self):
                try:
                with open(self.arquivo, "r") as f:
                return json.load(f)
            except FileNotFoundError:
                return {}
        
            def salvar_dicionario(self):
                with open(self.arquivo, "w") as f:
                    json.dump(self.dicionario, f)
        
                def adicionar_palavra(self):
                    palavra = self.ent_palavra.get()
                    traducao = self.ent_traducao.get()
        
                if palavra and traducao:
                    self.dicionario[palavra] = traducao
                    self.salvar_dicionario()
                    self.ent_palavra.delete(0, tk.END)
                    self.ent_traducao.delete(0, tk.END)
                    tk.messagebox.showinfo("Adicionar Palavra", f"A palavra '{palavra}' foi adicionada ao dicionário.")
                else:
                    tk.messagebox.showerror("Adicionar Palavra", "Por favor, digite a palavra em inglês e a tradução em português.")
        
                def sair(self):
                    self.root.destroy()

                if __name__ == '__main__':
                app = DicionarioGUI("dicionario.json")

</code>
 </div>
  
<p>Neste exemplo, a classe DicionarioGUI representa a interface gráfica do dicionário. O construtor da classe carrega o dicionário do arquivo JSON e cria os elementos da interface. O método carregar_dicionario carrega o dicionário do arquivo JSON e retorna um dicionário vazio se o arquivo não existir. O método salvar_dicionario salva o dicionário atual no arquivo JSON. O método adicionar_palavra é chamado quando o usuário clica no botão<p>
</div>
