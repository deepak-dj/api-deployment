from spire.doc import Document   # pip install Spire.Doc==12.7.1
from spire.doc import FileFormat
import os
import fitz  # PyMuPDF==1.24.10


def word_from_pdf(input_dox, output_pdf, final_output_pdf, line_to_remove):

    # Code to convert docx to pdf
    document = Document()
    document.LoadFromFile(input_dox)  # enter correct path of the input file

    document.SaveToFile(output_pdf, FileFormat.PDF) # enter correct path of the output file
    document.Close()

    # Code to remove water mark
    doc = fitz.open(output_pdf)
    for page in doc:
        text_instances = page.search_for(line_to_remove)
        for inst in text_instances:
            page.add_redact_annot(inst)

        page.apply_redactions()

    doc.save(final_output_pdf)
    doc.close()


input_docx = 'dummy.docx' # enter correct path of the output file
output_pdf = 'output.pdf' # enter correct path of the final output file
final_output_pdf = 'final.pdf' # enter correct path of the final output file
line_to_remove = "Evaluation Warning: The document was created with Spire.Doc for Python."
word_from_pdf(input_docx, output_pdf, final_output_pdf, line_to_remove)
if os.path.exists(output_pdf):
    os.remove(output_pdf)
print(f"output pdf --------------------- '{final_output_pdf}'.")
