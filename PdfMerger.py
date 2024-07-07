from PyPDF2 import PdfMerger
import os


def merge_pdfs(input_dir, output_filename):
    merger = PdfMerger()

    # Obtener todos los archivos PDF en el directorio
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

    # Ordenar los archivos alfabéticamente
    pdf_files.sort()

    # Añadir cada PDF al merger
    for pdf in pdf_files:
        merger.append(os.path.join(input_dir, pdf))

    # Escribir el PDF combinado
    merger.write(output_filename)
    merger.close()


# Uso del script
input_directory = "E:\\"
output_file = "documento_combinado.pdf"

merge_pdfs(input_directory, output_file)
print(f"PDFs combinados en {output_file}")
