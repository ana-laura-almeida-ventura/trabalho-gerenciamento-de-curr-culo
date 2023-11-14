import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image, ImageTk

class Gerenciamento:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Currículos")
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='candidatos'
        )
        self.cursor = self.connection.cursor()

        self.criar_titulo()

    def criar_titulo(self):
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        self.style.configure("Treeview", font=("Arial", 12), rowheight=25)

        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.label = ttk.Label(self.frame, text="Gerenciamento de Currículos", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        self.criar_butoes()
        self.criar_table()

    def criar_butoes(self):
        botao = ttk.Frame(self.frame)
        botao.pack(pady=10)

        self.add_botao = ttk.Button(botao, text="Adicionar Candidato", command=self.add_candidato, style="TButton")
        self.add_botao.grid(row=0, column=0, padx=5)

        self.botao_pesquisar = ttk.Button(botao, text="Pesquisar Candidatos", command=self.pesquisar_candidatos, style="TButton")
        self.botao_pesquisar.grid(row=0, column=1, padx=5)

        self.botao_gerar_pdf_completo = ttk.Button(botao, text="Gerar Relatório Completo", command=self.gerar_pdf_completo, style="TButton")
        self.botao_gerar_pdf_completo.grid(row=0, column=2, padx=5)

        self.botao_gerar_pdf_resumido = ttk.Button(botao, text="Gerar Relatório Resumido", command=self.gerar_pdf_resumido, style="TButton")
        self.botao_gerar_pdf_resumido.grid(row=0, column=3, padx=5)

    def criar_table(self):
        tree_frame = ttk.Frame(self.frame)
        tree_frame.pack(fill="both", expand=True)

        self.tituloTabela = ttk.Treeview(tree_frame, columns=("ID", "Nome", "Telefone", "Minibio", "Entrevista", "Teórico", "Prático", "Soft Skills"))
        self.tituloTabela.heading("#1", text="ID")
        self.tituloTabela.heading("#2", text="Nome")
        self.tituloTabela.heading("#3", text="Telefone")
        self.tituloTabela.heading("#4", text="Minibio")
        self.tituloTabela.heading("#5", text="Entrevista")
        self.tituloTabela.heading("#6", text="Teórico")
        self.tituloTabela.heading("#7", text="Prático")
        self.tituloTabela.heading("#8", text="Soft Skills")

        self.tituloTabela.column("#1", width=50)
        self.tituloTabela.column("#2", width=300)
        self.tituloTabela.column("#3", width=120)
        self.tituloTabela.column("#4", width=300)
        self.tituloTabela.column("#5", width=100)
        self.tituloTabela.column("#6", width=100)
        self.tituloTabela.column("#7", width=100)
        self.tituloTabela.column("#8", width=100)   
        self.tituloTabela.pack(side="top", fill="both", expand=True)

    def add_candidato(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Adicionar Candidato")

        add_window.geometry("400x300")

        nome = tk.StringVar()
        telefone = tk.StringVar()
        minibio = tk.StringVar()
        entrevista = tk.DoubleVar()
        teorico = tk.DoubleVar()
        pratico = tk.DoubleVar()
        soft_skills = tk.DoubleVar()

        tk.Label(add_window, text="Nome:").pack()
        tk.Entry(add_window, textvariable=nome).pack()

        tk.Label(add_window, text="Telefone:").pack()
        tk.Entry(add_window, textvariable=telefone).pack()

        tk.Label(add_window, text="Minibio:").pack()
        tk.Entry(add_window, textvariable=minibio).pack()

        tk.Label(add_window, text="Entrevista (0-10):").pack()
        tk.Entry(add_window, textvariable=entrevista).pack()

        tk.Label(add_window, text="Teórico (0-10):").pack()
        tk.Entry(add_window, textvariable=teorico).pack()

        tk.Label(add_window, text="Prático (0-10):").pack()
        tk.Entry(add_window, textvariable=pratico).pack()

        tk.Label(add_window, text="Soft Skills (0-10):").pack()
        tk.Entry(add_window, textvariable=soft_skills).pack()

        def insert_candidato():
            nome_value  = nome.get()
            telefone_value = telefone.get()
            minibio_value = minibio.get()
            entrevista_value = entrevista.get()
            teorico_value = teorico.get()
            pratico_value = pratico.get()
            soft_skills_value = soft_skills.get()

            query = "INSERT INTO candidatos (nome, telefone, minibio, entrevista, teste_teórico, teste_prático, soft_skills) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (nome_value , telefone_value, minibio_value, entrevista_value, teorico_value, pratico_value, soft_skills_value)
            self.cursor.execute(query, values)
            self.connection.commit()
            add_window.destroy()
            messagebox.showinfo("Candidato Adicionado", "Candidato adicionado com sucesso!")
            self.update_table()

        tk.Button(add_window, text="Adicionar Candidato", command=insert_candidato).pack()

    def pesquisar_candidatos(self):
        pesquisar_window = tk.Toplevel(self.root)
        pesquisar_window.title("Pesquisar Candidatos")

        pesquisar_window.geometry("200x100")

        pesquisar_label = tk.Label(pesquisar_window, text="Critérios de Pesquisa:")
        pesquisar_label.pack()

        pesquisa = tk.StringVar()
        pesquisar_entry = tk.Entry(pesquisar_window, textvariable=pesquisa)
        pesquisar_entry.pack()

        def pesquisar():
            criteria = pesquisa.get()
            self.cursor.execute(f"SELECT * FROM candidatos WHERE nome LIKE '%{criteria}%'")
            candidatos = self.cursor.fetchall()
            self.update_table(candidatos)
            pesquisar_window.destroy()

        botao_pesquisar = tk.Button(pesquisar_window, text="Pesquisar", command=pesquisar)
        botao_pesquisar.pack()


    def gerar_pdf_completo(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

        if file_path:
            c = canvas.Canvas(file_path, pagesize=letter)
            c.drawString(100, 750, "Relatório Completo de Candidatos")
            c.line(100, 747, 530, 747)

            candidatos = self.get_all_candidatos()
            y = 720

            for candidato in candidatos:
                y -= 20
                c.drawString(100, y, f"Nome: {candidato[1]}")
                y -= 15
                c.drawString(100, y, f"Telefone: {candidato[2]}")
                y -= 15
                c.drawString(100, y, f"Minibio: {candidato[3]}")
                y -= 15
                c.drawString(100, y, f"Entrevista: {candidato[4]}")
                y -= 15
                c.drawString(100, y, f"Teórico: {candidato[5]}")
                y -= 15
                c.drawString(100, y, f"Prático: {candidato[6]}")
                y -= 15
                c.drawString(100, y, f"Soft Skills: {candidato[7]}")
                y -= 30

                if y < 50:
                    c.showPage()
                    y = 720

            c.save()
            messagebox.showinfo("Relatório Gerado", "Relatório completo gerado com sucesso!")

    def gerar_pdf_resumido(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

        if file_path:
            c = canvas.Canvas(file_path, pagesize=letter)
            c.drawString(100, 750, "Relatório Completo de Candidatos")
            c.line(100, 747, 530, 747)

            candidatos = self.get_all_candidatos()
            y = 720

            for candidato in candidatos:
                y -= 20
                c.drawString(100, y, f"Nome: {candidato[1]}")
                y -= 15
                c.drawString(100, y, f"Entrevista: {candidato[4]}")
                y -= 15
                c.drawString(100, y, f"Teórico: {candidato[5]}")
                y -= 15
                c.drawString(100, y, f"Prático: {candidato[6]}")
                y -= 15
                c.drawString(100, y, f"Soft Skills: {candidato[7]}")
                y -= 30

                if y < 50:
                    c.showPage()
                    y = 720

            c.save()
            messagebox.showinfo("Relatório Gerado", "Relatório completo gerado com sucesso!")

    def get_all_candidatos(self):
        self.cursor.execute("SELECT * FROM candidatos")
        candidatos = self.cursor.fetchall()
        return candidatos

    def update_table(self, candidatos=None):
        for item in self.tituloTabela.get_children():
            self.tituloTabela.delete(item)
        if candidatos is None:
            candidatos = self.get_all_candidatos()
        for candidato in candidatos:
            self.tituloTabela.insert("", "end", values=candidato)