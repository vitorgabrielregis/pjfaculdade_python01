import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")  

moedas = {
    "BRL": "Real Brasileiro",
    "USD": "Dólar Americano",
    "EUR": "Euro",
    "CAD": "Dólar Canadense",
    "AUD": "Dólar Australiano",
    "CHF": "Franco Suíço",
    "JPY": "Iene Japonês",
    "CNY": "Yuan Chinês",
    "GBP": "Libra Esterlina",
    "ARS": "Peso Argentino",
    "MXN": "Peso Mexicano",
    "RUB": "Rublo Russo",
    "KRW": "Won Sul-Coreano",
    "INR": "Rúpia Indiana",
    "ZAR": "Rand Sul-Africano",
    "SEK": "Coroa Sueca",
    "NOK": "Coroa Norueguesa",
    "TRY": "Lira Turca"
}


taxas_cambio = {
    "BRL": 1.0,
    "USD": 0.1764,
    "EUR": 0.16,
    "CAD": 0.25,
    "AUD": 0.2755,
    "CHF": 0.1541,
    "JPY": 25.97,
    "CNY": 1.2837,
    "GBP": 0.135,
    "ARS": 154.32,
    "MXN": 3.12,
    "RUB": 16.48,
    "KRW": 237.52,
    "INR": 14.72,
    "ZAR": 3.30,
    "SEK": 1.77,
    "NOK": 1.82,
    "TRY": 5.69 
}


def alterar_tema():
    atual = ctk.get_appearance_mode()
    novo = "Light" if atual == "Dark" else "Dark"
    ctk.set_appearance_mode(novo)
    
def converter_moeda():
    try:
        valor = float(entrada_valor.get())
        moeda_origem = var_moeda_origem.get()
        moeda_destino = var_moeda_destino.get()

        if moeda_origem not in taxas_cambio or moeda_destino not in taxas_cambio:
            messagebox.showerror("Erro", "Selecione as moedas corretamente")
            return
        if valor <= 0:
            messagebox.showerror("Erro", "Digite um valor positivo")
            return

        valor_convertido = valor * taxas_cambio[moeda_destino] / taxas_cambio[moeda_origem]
        resultado_formatado = f"{valor_convertido:,.2f}"
        var_resultado.set(f"{resultado_formatado} {moeda_destino}")

        taxa = taxas_cambio[moeda_destino] / taxas_cambio[moeda_origem]
        var_taxa.set(f"1 {moeda_origem} = {taxa:.4f} {moeda_destino}")

        entrada = f"{valor:.2f} {moeda_origem} → {resultado_formatado} {moeda_destino} | Taxa: {taxa:.4f}"
        historico.append(entrada)
        if len(historico) > 10:
            historico.pop(0)

        caixa_historico.configure(state="normal")
        caixa_historico.delete("1.0", "end")
        for linha in historico:
            caixa_historico.insert("end", linha + "\n")
        caixa_historico.configure(state="disabled")
        caixa_historico.see("end")

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
    historico.clear()
    caixa_historico.configure(state="normal")
    caixa_historico.delete("1.0", "end")
    caixa_historico.configure(state="disabled")

def ao_apertar_enter(event):#event serve para reagir com o usuário 
    converter_moeda()

janela = ctk.CTk()
janela.title("Conversor de Moedas")
janela.geometry("500x460")

var_moeda_origem = ctk.StringVar(value="BRL")
var_moeda_destino = ctk.StringVar(value="USD")

var_resultado = ctk.StringVar()
var_taxa = ctk.StringVar()
historico = []

validar_cmd = janela.register(validar_valor)

ctk.CTkButton(janela, text="Novo Tema", command=alterar_tema).pack(pady=5)

ctk.CTkLabel(janela, text="Valor:", font=("Arial", 14)).pack(pady=5)
entrada_valor = ctk.CTkEntry(janela, validate="key", validatecommand=(validar_cmd, "%P"))
entrada_valor.pack(pady=5)

ctk.CTkLabel(janela, text="Moeda de origem:", font=("Arial", 14)).pack(pady=5)
ctk.CTkOptionMenu(janela, variable=var_moeda_origem, values=list(moedas.keys())).pack(pady=5)

ctk.CTkLabel(janela, text="Moeda de destino:", font=("Arial", 14)).pack(pady=5)
ctk.CTkOptionMenu(janela, variable=var_moeda_destino, values=list(moedas.keys())).pack(pady=5)

ctk.CTkButton(janela, text="Converter", command=converter_moeda).pack(pady=10)
ctk.CTkButton(janela, text="Trocar Moedas", command=trocar_moedas).pack(pady=5)
ctk.CTkButton(janela, text="Limpar", command=limpar_campos).pack(pady=5)

ctk.CTkLabel(janela, text="Resultado:", font=("Arial", 14)).pack(pady=5)
ctk.CTkLabel(janela, textvariable=var_resultado, font=("Arial", 16, "bold")).pack(pady=2)
ctk.CTkLabel(janela, textvariable=var_taxa, font=("Arial", 12)).pack(pady=2)

frame_historico = ctk.CTkFrame(janela)
frame_historico.pack(fill="both", expand=True, padx=10, pady=(10, 10))

ctk.CTkLabel(frame_historico, text="Histórico de Conversões:", font=("Arial", 14)).pack(anchor="w")
caixa_historico = ctk.CTkTextbox(frame_historico, height=120, state="disabled", wrap="none")
caixa_historico.pack(fill="both", expand=True)

janela.bind("<Return>", ao_apertar_enter)

janela.mainloop()