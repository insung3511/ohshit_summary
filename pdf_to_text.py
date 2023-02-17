import PyPDF2 as pp2
import tqdm


class PDF2Text:
    def __init__(self, FILE_PATH, saveAsFile, saveFilePath):
        """Document

        FILE_PATH : string
        Enter a pdf file path to read.

        saveAsFile : boolean
        True or False, saved file the converted contents.

        saveFilePath : string
        where to save, converted results.

        """
        self.FILE_PATH = FILE_PATH
        self.saveAsFile = saveAsFile
        self.saveFilePath = saveFilePath

    def converter(self):
        convertedText = str()
        paperTitle = str()
        paperTitleHasSaved = False

        pdfFileObj = open(self.FILE_PATH, "rb")
        pdfFileReader = pp2.PdfFileReader(pdfFileObj)
        pdfPages = pdfFileReader.numPages
        print(f"[INFO] Total pages : {pdfPages}")

        for pageIndex in tqdm.tqdm(range(pdfPages)):
            pdfPageObj = pdfFileReader.getPage(pageIndex)
            extractTextObj = pdfPageObj.extractText()
            for inPageTexts in range(len(extractTextObj.splitlines())):
                if inPageTexts == 0 and paperTitleHasSaved == False:
                    paperTitle = extractTextObj.splitlines()[0]
                    paperTitleHasSaved = True

                convertedText += extractTextObj

        print(f"[INFO] Paper name : {paperTitle}")

        if self.saveAsFile:
            with open(self.saveFilePath, "w") as convertedSaver:
                convertedSaver.writelines(convertedText)
