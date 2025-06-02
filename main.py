import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")

moedas = {
    "BRL": "Real Brasileiro",
    "USD": "Dólar Americano",
    "EUR": "Euro",
    "CAD": "Dólar Canadense",
    "AUD": "Dólar Australiano",
    "CHF": "Franco Suíço",
    "JPY": "Iene Japonês",
    "CNY": "Yuan Chinês"
}

taxas_cambio = {
    "BRL": 1.0,
    "USD": 5.67,
    "EUR": 6.25,
    "CAD": 4.00,
    "AUD": 3.63,
    "CHF": 6.49,
    "JPY": 0.0385,
    "CNY": 0.779
}

def converter_moeda():
    try:
        valor = float(entrada_valor.get())
        moeda_origem = valor_moeda_origem.get()
        moeda_destino = var_moeda_destino.get()

        if moeda_origem not in taxas_cambio or moeda_destino not in taxas_cambio:
            messagebox.showerror("Erro", "Selecione as moedas corretamente")
            return
        if valor <= 0:
            messagebox.showerror("Erro", "Digite um valor positivo")
            return
        
        valor_usd = valor / taxas_cambio[moeda_origem]
        valor_convertido = valor_usd * taxas_cambio[moeda_destino]

        if moeda_destino in ["BRL", "USD", "EUR"]:
            resultado_formatado = f"{round(valor_convertido): .0f}"
        else:
            resultado_formatado = f"{round(valor_convertido, 2): .2f}"

        var_resultado.set(f"{resultado_formatado} {moeda_destino}")
        taxa = taxas_cambio[moeda_destino] / taxas_cambio[moeda_origem]
        var_taxa.set(f"1 {moeda_origem} = {taxa:.4f} {moeda_destino}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro na conversão: {str(e)}") 

def trocar_moedas():
    origem = var_moeda_origem.get()
    destino = var_moeda_destino.get()
    var_moeda_origem.set(destino)
    var_moeda_destino.set(origem)
    if entrada_valor.get():
        converter_moeda()

def validar_valor(novo_valor):
    if novo_valor == "":
        return True
    if novo_valor.count(".") > 1:
        return False
    try:
#Serve para verificar se a string termina com "." auxiliando na conversão evitando erros, contendo que seja escrito um número
        float(novo_valor + "0") if novo_valor.endswith(".") else float(novo_valor)
        return True
    except ValueError:
        return False
    
def limpar_campos():
    entrada_valor.delete(0, ctk.END)
    var_resultado.set("")
    var_taxa.set("")
    var_moeda_origem.set("BRL")
    var_moeda_destino.set("USD")

def ao_apertar_enter(event):#event serve para reagir com o usuário 
    converter_moeda()

janela = ctk.CTk()
janela.title("Conversor de Moedas")
janela.geometry("400x400")

#Redimensionar  tanto na horizontal como vertical
janela.resizable(True, True)
janela.configure(bg="#fff")

janela.mainloop()