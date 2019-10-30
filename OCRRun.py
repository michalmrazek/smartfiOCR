import pytesseract
from PIL import Image
import requests
from pdf2image import convert_from_path


def test():
    response = requests.get("https://www.nvaccess.org/wp-content/uploads/2017/10/ocrimage.png", stream=True)
    img = Image.open(response.raw)
    result = pytesseract.image_to_string(img)
    return "result: {}".format(result)

def test_pdf():
    url = "http://visibillity.com/collateral/electronic_documents/invoice.pdf"
    r = requests.get(url)
    with open('/data/invoice.pdf', 'wb') as fd:
        for chunk in r.iter_content(20000):
            fd.write(chunk)
    images = convert_from_path("/data/invoice.pdf")
    for i, image in enumerate(images):
        image.save('data/out_{}.jpg'.format(i), 'JPEG')
    img = Image.open("data/out_0.jpg")
    print(pytesseract.image_to_string(img))

def main():
    result = test()
    print(result)
    with open("data/Output.txt", "w") as text_file:
        print(result, file=text_file)
    test_pdf()

if __name__== "__main__":
   main()
