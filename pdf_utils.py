import pypdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from io import BytesIO

def create_notes_pdf(uploaded_pdf, layout="1-slide-per-page", orientation="Portrait"):
    """
    Processes the uploaded PDF and generates a new PDF with structured slides and notes space.
    
    - layout: "1-slide-per-page" or "2-slides-per-page"
    - orientation: "Portrait" or "Landscape"
    
    Returns:
    - BytesIO buffer containing the new PDF
    """

    # Read the uploaded PDF
    pdf_reader = pypdf.PdfReader(uploaded_pdf)
    num_pages = len(pdf_reader.pages)

    # Set page size based on orientation
    page_size = landscape(letter) if orientation == "Landscape" else letter

    # Create a new PDF buffer
    output_buffer = BytesIO()
    pdf_canvas = canvas.Canvas(output_buffer, pagesize=page_size)

    # Define margins and spacing
    margin_x = 50
    margin_y = 50
    note_line_spacing = 14  # Standard line spacing in points

    for i in range(num_pages):
        page = pdf_reader.pages[i]

        # Add slide (placeholder for now)
        pdf_canvas.drawString(margin_x, page_size[1] - margin_y, f"Slide {i+1}")

        # Automatically calculate note lines based on available space
        note_start_y = 200  # Start drawing notes from this height
        note_area_height = page_size[1] - margin_y - note_start_y  # Available space for notes
        num_lines = note_area_height // note_line_spacing  # How many lines fit

        # Draw note lines
        y_position = note_start_y
        for _ in range(int(num_lines)):
            pdf_canvas.line(margin_x, y_position, page_size[0] - margin_x, y_position)
            y_position -= note_line_spacing

        pdf_canvas.showPage()  # Move to next page

    # Save PDF to memory
    pdf_canvas.save()
    output_buffer.seek(0)
    return output_buffer
