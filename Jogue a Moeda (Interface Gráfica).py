import tkinter as tk
from tkinter import messagebox
import random

# Função para simular as jogadas
def simular():
    cara = 0
    coroa = 0
    for _ in range(6000):
        if random.choice(["cara", "coroa"]) == "cara":
            cara += 1
        else:
            coroa += 1
    
    # Atualiza os resultados na interface
    resultado_cara.config(text=f"Quantidade de vezes que deu Cara: {cara}")
    resultado_coroa.config(text=f"Quantidade de vezes que deu Coroa: {coroa}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Jogue a Moeda")
janela.geometry("400x300")
janela.configure(bg="#f0f8ff")

# Título
titulo = tk.Label(janela, text="Jogue a Moeda", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333399")
titulo.pack(pady=10)

# Resultados
resultado_cara = tk.Label(janela, text="Quantidade de vezes que deu Cara: 0", font=("Arial", 12), bg="#f0f8ff", fg="#333333")
resultado_cara.pack(pady=5)

resultado_coroa = tk.Label(janela, text="Quantidade de vezes que deu Coroa: 0", font=("Arial", 12), bg="#f0f8ff", fg="#333333")
resultado_coroa.pack(pady=5)

# Botão para simular
botao_simular = tk.Button(janela, text="Simular", font=("Arial", 12, "bold"), bg="#4caf50", fg="white", padx=20, pady=10, command=simular)
botao_simular.pack(pady=20)

# Botão para sair
botao_sair = tk.Button(janela, text="Sair", font=("Arial", 12, "bold"), bg="#f44336", fg="white", padx=20, pady=10, command=janela.quit)
botao_sair.pack(pady=10)

# Inicia o loop principal
janela.mainloop()
