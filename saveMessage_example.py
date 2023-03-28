from cryptographyFramework import *

initializeWrite()
user = "Fulano"
password = "1234"
encryptedText = encryptMessage(user, password, "Não aguento mais aaaaaaaaaaaa")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Não aguento mais aaaaaaaaaaaa!")
saveNewLine(encryptedText)

