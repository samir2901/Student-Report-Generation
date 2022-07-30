from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("PrepPrimaryReportCard Format.pdf")
writer = PdfWriter()

page = reader.pages[0]
fields = reader.get_fields()

writer.add_page(page)

writer.update_page_form_field_values(
    writer.pages[0],
    {
        "id" : "03-0186",
        "name" : "Samiruddin Thunder",
        "class" : "0",
        "section" : "A",
        "engMark" : "100",
        "mathMark" : "100",
        "evsMark" : "100",
        "totalMark" : "300",
        "remarks" : "Promoted to Class 1"
    }
)

with open("03-186.pdf", "wb") as output_stream:
    writer.write(output_stream)