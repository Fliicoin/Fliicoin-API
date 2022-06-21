class fliicoin:
    def blocks(type):
        if type.lower() == 'all':
            return ('Network Blocks (amount per block):\nFast: 10\nMedium: 5\nSlow: 3\nUltra-Slow: 1')
        elif type.lower() == 'fast':
            return ('Fast Network Block: 10')
        elif type.lower() == 'medium':
            return ('Medium Network Block: 10')
        elif type.lower() == 'slow':
            return ('Slow Network Block: 10')
        elif type.lower() == 'ultra-slow':
            return ('Ultra-slow Network Block: 10')
        else:
            return ('Invalid network type. Please use fast, medium, slow, ultra-slow, or all')

    def block(type):
        print('Please use blocks instead of block')

    def server():
        from urllib.request import urlopen
        import json
        url = "https://server.fliicoin.com/server"
        response = urlopen(url)
        data = response.read()
        data = (str(data))
        return (data)

    def mine(username, guess):
        from urllib.request import urlopen
        import json
        url = ('https://server.fliicoin.com/mine?username=' + username + '&guess=' + guess)
        response = urlopen(url)
        data = response.read()
        data = (str(data))
        return (data)

    def qr(username, imagedestination):
        import urllib
        from urllib.request import urlopen, Request
        import json
        import PyQRCode
        from PyQRCode import QRCode

        url = ('https://server.fliicoin.com/qr?username=' + username)
        try:
            conn = urlopen(url)
        except urllib.error.HTTPError as e:
            response = urlopen('https://server.fliicoin.com/qr?username=' + username)
            data = response.read()
            data = (str(data))
            return (data)
        except urllib.error.URLError as e:
            print('URLError: {}'.format(e.reason))
        else:
            image = urllib.request.urlretrieve('https://server.fliicoin.com/qr?username=' + username)
            s = ("fliicoin.com/user/" + username)
            url = pyqrcode.create(s)
            url.png((imagedestination), scale = 8)
            return ('QR-Code save to the destination: ' + imagedestination)