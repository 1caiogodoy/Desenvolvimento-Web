from ftplib import FTP
import os

# Esse aqui são dados de um servidor publico ftp que serve para testes
ftp = FTP("ftp.dlptest.com")
ftp.login("dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu")

print("Conectado!")

arquivos = ftp.nlst()
print("Arquivos no servidor:")
for arq in arquivos:
    print(arq)

if not os.path.exists("downloads"):
    os.mkdir("downloads")

for arq in arquivos:
    if not arq.endswith(".txt"):
        continue

    try:
        caminho = os.path.join("downloads", arq)

        with open(caminho, "wb") as f:
            ftp.retrbinary("RETR " + arq, f.write)

        print("Baixado:", arq)

    except:
        print("Erro:", arq)

try:
    with open("arquivo.txt", "rb") as f:
        ftp.storbinary("STOR arquivo.txt", f)
    print("Arquivo enviado")
except:
    print("Não foi possível enviar o arquivo")

ftp.quit()
print("Finalizado!")