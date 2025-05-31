import requests
from tkinter import *

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

janela = Tk ()
janela.title ("Conversão de moedas")

janela.mainloop()