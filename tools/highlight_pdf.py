import fitz
import re
import unicodedata
import os

pdf_path = "project/TCC 2 - Letícia Padilha Câmara (1).pdf"
output_path = "project/TCC 2 - Letícia Padilha Câmara (1).pdf"
markdown_path = "project/parecer_avaliador.md"

# Text overrides for cases where the reviewer's text differs from the actual PDF text
text_overrides = {
    "preservação e o conhecimento, utiliza-se as plataformas": "preservação e conhecimento, utiliza-se as plataformas",
    "imagem classificada pelo modelo de Machine Learning seja abaixo": "resultado classificado pelo modelo de Machine Learning seja abaixo",
    "resultado este dentro": "retornado este dentro",
    "maioria dos erros ocorreu entre": "parte significativa dos erros ocorreu entre",
    "tecnicamente viável e qualificado": "tecnicamente viável e qua- lificado"
}

def normalize_text(text):
    return unicodedata.normalize("NFKC", text).strip()

def make_human_comment(correct, justification):
    just_lower = justification.lower()
    
    if correct == "—" or not correct:
        return justification
        
    if "digitação" in just_lower or "ortográfico" in just_lower or "grafia" in just_lower:
        return f"Ajustar a grafia para '{correct}' (correção de digitação)."
    elif "concordância" in just_lower:
        return f"Ajustar para '{correct}' para corrigir a concordância."
    elif "gerundismo" in just_lower or "gerúndio" in just_lower:
        return f"Evitar o gerundismo aqui. Recomendo reescrever como '{correct}' para melhorar a fluidez."
    elif "crase" in just_lower:
        return f"Ajustar para '{correct}' (uso correto da crase)."
    elif "verbal" in just_lower or "regência" in just_lower:
        return f"Ajustar para '{correct}' (correção verbal/regência)."
    elif "redundância" in just_lower or "redundante" in just_lower:
        return f"Remover a redundância. Sugiro reescrever como '{correct}'."
    elif "informal" in just_lower or "acadêmico" in just_lower:
        return f"Substituir por '{correct}' para manter o tom acadêmico adequado."
    elif "pontuação" in just_lower or "vírgula" in just_lower:
        return f"Ajustar a pontuação para '{correct}'."
    elif "artigo" in just_lower:
        return f"Ajustar para '{correct}' (inserção de artigo necessário)."
    elif "gênero" in just_lower:
        return f"Ajustar concordância de gênero para '{correct}'."
    elif "número" in just_lower:
        return f"Ajustar concordância de número para '{correct}'."
        
    clean_just = justification.rstrip('.')
    if clean_just and clean_just[0].isupper():
        clean_just = clean_just[0].lower() + clean_just[1:]
    return f"Sugiro alterar para '{correct}' ({clean_just})."

def parse_markdown_table(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    corrections = []
    
    # Find rows matching | page | line | incorrect | correct | justification |
    pattern = re.compile(r'^\|\s*(?:\*\*)?(\d+)(?:\*\*)?\s*\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$', re.MULTILINE)
    matches = pattern.findall(content)
    
    for match in matches:
        page_num = int(match[0])
        line_num = int(match[1])
        incorrect_raw = match[2]
        correct_raw = match[3]
        justification = match[4]
        
        # Clean incorrect text
        # Remove quotes and ellipsis
        incorrect = incorrect_raw
        for prefix in ['"...', '...', '"']:
            if incorrect.startswith(prefix):
                incorrect = incorrect[len(prefix):]
        for suffix in ['..."', '...', '"']:
            if incorrect.endswith(suffix):
                incorrect = incorrect[:-len(suffix)]
        incorrect = incorrect.strip()
        
        # Apply override if applicable
        if incorrect in text_overrides:
            incorrect = text_overrides[incorrect]
            
        # Clean correct text
        correct = correct_raw
        for prefix in ['"...', '...', '"']:
            if correct.startswith(prefix):
                correct = correct[len(prefix):]
        for suffix in ['..."', '...', '"']:
            if correct.endswith(suffix):
                correct = correct[:-len(suffix)]
        correct = correct.strip()
        
        # Determine sticky note text
        note_text = make_human_comment(correct, justification)
            
        corrections.append({
            "page": page_num,
            "line": line_num,
            "incorrect_raw": incorrect_raw,
            "incorrect": normalize_text(incorrect),
            "correct": correct,
            "note_text": note_text
        })
        
    return corrections

def highlight_pdf():
    print("Parsing markdown table...")
    corrections = parse_markdown_table(markdown_path)
    print(f"Parsed {len(corrections)} corrections from markdown.")
    
    # Check both NFD and NFC paths for the PDF file
    actual_pdf_path = pdf_path
    if not os.path.exists(actual_pdf_path):
        # Let's list files in project to find if there's any variation
        files = os.listdir("project")
        found = False
        for f in files:
            if normalize_text(f).lower() == normalize_text(os.path.basename(pdf_path)).lower():
                actual_pdf_path = os.path.join("project", f)
                found = True
                break
        if not found:
            print(f"Error: PDF file not found at {pdf_path}")
            return

    print(f"Using PDF file: {actual_pdf_path}")
    doc = fitz.open(actual_pdf_path)
    print(f"Opened PDF with {len(doc)} pages.")
    
    success_count = 0
    fail_count = 0
    
    for item in corrections:
        page_num = item["page"]
        search_str = item["incorrect"]
        
        # Skip if search_str is empty/placeholder
        if not search_str or search_str == "—":
            print(f"Skipping page {page_num} (empty search string).")
            fail_count += 1
            continue
            
        # Target physical page (0-indexed)
        p_phys = page_num - 1
        
        # Generate search page candidates to handle page offsets gracefully
        # Prioritize the specified page, then offsets of +1 to +6, then -1 and -2
        search_pages = []
        for offset in [0, 1, 2, 3, 4, 5, 6, -1, -2]:
            candidate = p_phys + offset
            if 0 <= candidate < len(doc) and candidate not in search_pages:
                search_pages.append(candidate)
                
        # Search candidate pages
        rects = None
        matched_page_idx = -1
        for p_idx in search_pages:
            rects = doc[p_idx].search_for(search_str)
            if rects:
                matched_page_idx = p_idx
                break
                
        # Fallback to searching the whole document if not found in nearby pages
        if not rects:
            for p_idx in range(len(doc)):
                if p_idx not in search_pages:
                    rects = doc[p_idx].search_for(search_str)
                    if rects:
                        matched_page_idx = p_idx
                        break
                        
        if rects:
            page = doc[matched_page_idx]
            
            # Highlight all matched rectangles on this page
            for rect in rects:
                annot = page.add_highlight_annot(rect)
                annot.set_colors(stroke=[0.72, 0.88, 1.0]) # Pastel blue color (RGB: 184, 224, 255)
                annot.update()
                
            # Add exactly one sticky note (Text annotation) near the first highlight rect
            rect = rects[0]
            note_point = fitz.Point(rect.x1 + 10, rect.y0)
            
            # Adjust coordinates to keep the note icon inside the page boundaries
            if note_point.x > page.rect.width - 20:
                note_point.x = rect.x0 - 20
            if note_point.x < 10:
                note_point.x = 10
                
            note_annot = page.add_text_annot(note_point, item["note_text"])
            note_annot.set_colors(stroke=[0.3, 0.6, 0.9]) # Softer blue for the sticky note icon
            note_annot.update()
            
            print(f"Successfully highlighted '{search_str}' on physical page {matched_page_idx + 1} (reported doc page {page_num}).")
            success_count += 1
        else:
            print(f"FAILED to find text '{search_str}' (reported doc page {page_num}).")
            fail_count += 1
            
    # Save the modified document to a temp path and replace the original
    temp_output_path = actual_pdf_path + ".temp.pdf"
    doc.save(temp_output_path)
    doc.close()
    
    if os.path.exists(temp_output_path):
        if os.path.exists(actual_pdf_path):
            os.remove(actual_pdf_path)
        os.rename(temp_output_path, actual_pdf_path)
        print(f"Saved modified PDF to {actual_pdf_path}")
    
    print(f"Finished: {success_count} succeeded, {fail_count} failed.")

if __name__ == "__main__":
    highlight_pdf()
