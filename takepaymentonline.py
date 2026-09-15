import qrcode
#take upi id as a input
upi_id = input('enter your upi id :')
#define payment url 

phonepe_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
supermoney_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr code for each payment url
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
supermoney_qr = qrcode.make(supermoney_url)

#save qr code images
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
supermoney_qr.save('supermoney_qr.png')

#display the qr code image so install PIL/pillow liabrary
phonepe_qr.show()
paytm_qr.show()
supermoney_qr.show()

