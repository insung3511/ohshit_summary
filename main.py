from pdf_to_text import PDF2Text

FILE_PATH = "test_pdf.pdf"
saveAsFile = True
saveFilePath = "converted_file.txt"

converter = PDF2Text(FILE_PATH=FILE_PATH,
                     saveAsFile=saveAsFile,
                     saveFilePath=saveFilePath)
converter.converter()
