import pdfplumber
from gtts import gTTS


# article

# article = ''
language = 'en'
# gtts_transformer = gTTS(text=book,lang=language)
# gtts_transformer.save(book + ".mp3")
# print("audiobook completed")


# pdf


# pdf_name = input("enter the name of the pdf ")
# pdf_path = "/Users/markchafin/Downloads/audiobook_creater/" + pdf_name + ".pdf"
pdf_path = "give_and_take.pdf"
text = list()
pdf = pdfplumber.open(pdf_path)

for num in range(20, 25):
    print("scanning page " + str(num))
    page = pdf.pages[num]
    print("Extracting text from page " + str(num))
    pdftext = page.extract_text()
    text.append(pdftext)
print(text)
print(len(text))

pdf.close()

print("creating string")
googletext = ' '.join(map(str, text))
print("string created")


print(googletext)



print("sending to google")
gtts_transformer = gTTS(text=googletext, lang=language)
print("saving")
gtts_transformer.save("give and take.mp3")
print("audiobook completed")


