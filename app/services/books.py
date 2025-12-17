import os
import json
import fitz


def extract_metadata_from_pdf(pdf_path, output_image_folder):
    """Extract metadata from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        meta = doc.metadata
        book_info = {
            "title": meta.get("title") or os.path.basename(pdf_path),
            "author": meta.get("author") or "Unknown Author",
            "year": meta.get("creationDate")[2:6] if meta.get("creationDate") else "Unknown",
            "subject": meta.get("subject") or "N/A",
            "keywords": meta.get("keywords") or "N/A"
        }

        if not os.path.exists(output_image_folder):
            os.makedirs(output_image_folder)
            
        page = doc.load_page(0)  # Load the first page
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Scale up for better quality
        
        image_filename = f"{os.path.splitext(os.path.basename(pdf_path))[0]}_cover.png"
        image_path = os.path.join(output_image_folder, image_filename)
        pix.save(image_path)

        book_info["cover_image"] = image_path
        doc.close()
        return book_info
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return None

    
books_folder = r"app\data\books"
covers_folder = r"app\metadata\books\covers"
all_books_metadata = []

for file in os.listdir(books_folder):
    if file.endswith(".pdf"):
        full_path = os.path.join(books_folder, file)
        data = extract_metadata_from_pdf(full_path, covers_folder)
        if data:
            all_books_metadata.append(data)

# Save to your JSON file
with open('app/metadata/books/books_metadata.json', 'w') as f:
    json.dump(all_books_metadata, f, indent=4)

print("Metadata extraction complete!")

def get_books_metadata():
    """Return the list of books metadata."""
    return all_books_metadata

