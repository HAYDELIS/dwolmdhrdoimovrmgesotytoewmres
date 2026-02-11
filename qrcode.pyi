import qrcode

link = "https://www.youtube.com/results?search_query=plim+plim+las+hormiguitas"
img = qrcode.make(link)
img.save("qrcode.png")