import requests
import xml.etree.ElementTree as ET
import csv
import os
import tkinter as tk
from tkinter import messagebox

def search_arxiv(query, max_results=15):
    url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        messagebox.showerror("Erro", "Erro na requisição")
        return None

def process_results(xml_data):
    root = ET.fromstring(xml_data)
    entries = root.findall('{http://www.w3.org/2005/Atom}entry')
    
    articles = []
    
    for entry in entries:
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        link = entry.find('{http://www.w3.org/2005/Atom}id').text
        
        articles.append({
            'title': title.strip(),
            'link': link.strip()
        })
    
    return articles

def display_articles(articles):
    text = ""
    for i, article in enumerate(articles, 1):
        text += f"Artigo {i}:\n  Título: {article['title']}\n  Link: {article['link']}\n\n"
    return text

def save_to_csv(selected_articles, search_term):
    base_filename = f"{search_term.replace(' ', '_')}.csv"
    filename = base_filename
    if os.path.exists(filename):
        base, ext = os.path.splitext(base_filename)
        i = 1
        while os.path.exists(f"{base}_{i}{ext}"):
            i += 1
        filename = f"{base}_{i}{ext}"
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Título', 'Link'])
        for article in selected_articles:
            writer.writerow([article['title'], article['link']])
    messagebox.showinfo("Sucesso", f"Arquivo '{filename}' gerado com sucesso!")

def search_and_display():
    query = search_entry.get()
    xml_data = search_arxiv(query)
    
    if xml_data:
        articles = process_results(xml_data)
        result_text.set(display_articles(articles))
        
        save_choice = messagebox.askyesno("Salvar", " Salvar os artigos em um arquivo CSV?")
        
        if save_choice:
            selected_articles = []
            for i, article in enumerate(articles, 1):
                save_article = messagebox.askyesno("Salvar", f"Deseja salvar o Artigo {i}? (Título: {article['title']})")
                if save_article:
                    selected_articles.append(article)
            
            if selected_articles:
                save_to_csv(selected_articles, query)
            else:
                messagebox.showinfo("Informação", "Nenhum artigo foi selecionado para salvar.")
        else:
            messagebox.showinfo("Informação", "Os artigos não foram salvos.")
    else:
        messagebox.showerror("Erro", "Nenhum dado retornado.")

#teste ----------------------------------------------------------------
root = tk.Tk()
root.title("Arxiv Bot")

tk.Label(root, text="Digite o termo de pesquisa:").pack(pady=5)
search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=5)

tk.Button(root, text="Buscar", command=search_and_display).pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify=tk.LEFT).pack(pady=10)

root.mainloop()
