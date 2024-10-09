import os
from docx import Document

def search_in_docx(folder_path, search_phrase):
    results = []

    
    for filename in os.listdir(folder_path):
        if filename.endswith('.docx'):
            doc_path = os.path.join(folder_path, filename)
            try:
                doc = Document(doc_path)
                
                for para in doc.paragraphs:
                    if search_phrase in para.text:
                        results.append((filename, para.text))
            except Exception as e:
                print(f"Erro ao ler {filename}: {e}")

    return results


folder_path = r'C:\Users\Techsallus\Downloads\Manuais (1)\Manuais'
search_phrase = 'compatibilidade'

found_results = search_in_docx(folder_path, search_phrase)


if found_results:
    print("Resultados encontrados:")
    for filename, text in found_results:
        print(f"Arquivo: {filename} - Texto: {text}\n")
else:
    print("Nenhum resultado encontrado.")
