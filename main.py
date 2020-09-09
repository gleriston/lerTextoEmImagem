from PIL import Image 

import pytesseract 

# print( pytesseract.image_to_string( Image.open("./lord.jpeg") ) ) 

arquivoTexto = open("./relatorio.txt", "w")

arquivoTexto.write(pytesseract.image_to_string( Image.open("./lord.jpeg") ))

arquivoTexto.close()
