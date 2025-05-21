import tkinter as tk
from tkinter import ttk, messagebox

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