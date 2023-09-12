import qrcode

link = "https://www.instagram.com"

codigo = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=2,
    border=2,
)
codigo.add_data(link)
codigo.make(fit=True)

imagem = codigo.make_image(fill_color="black", back_color="white")

imagem.show()
