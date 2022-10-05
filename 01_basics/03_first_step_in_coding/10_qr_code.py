import pyqrcode

address = 'https://www.inoreader.com/'
url = pyqrcode.create(address)
url.png('my_rrs_reader.png', scale=8)
