"""
Nome do arquivo: tela_iluminacao.py
Equipe: João, José, Maria e Pedro.
Turma: G91234
Semestre: 2025.1
"""

# import tkinter as tk
# import serial

# # Substitua 'COM3' pela porta correta ao usar de fato
# try:
#     arduino = serial.Serial('COM3', 9600)
# except:
#     arduino = None

# def enviar_comando(comando):
#     if arduino:
#         arduino.write(comando.encode())

# def abrir_tela_iluminacao():
#     janela = tk.Toplevel()
#     janela.title("Controle de Iluminação")

#     setores = {
#         "Oficina": "O",
#         "Galpão 1": "G1",
#         "Galpão 2": "G2",
#         "Galpão 3": "G3",
#         "Escritório": "E",
#         "Corredor": "C",
#         "Área Serviço": "S",
#         "Área Externa": "X"
#     }

#     for i, (setor, comando) in enumerate(setores.items()):
#         frame = tk.Frame(janela)
#         frame.grid(row=i, column=0, pady=2)
#         tk.Label(frame, text=setor).pack(side=tk.LEFT, padx=5)
#         tk.Button(frame, text="Ligar", command=lambda c=comando: enviar_comando(c.lower())).pack(side=tk.LEFT)
#         tk.Button(frame, text="Desligar", command=lambda c=comando: enviar_comando(c.upper())).pack(side=tk.LEFT)
