
from pyzbar import pyzbar
import cv2

image = cv2.imread('your image path') # put it in your code location
#QRcode.png

barcodes = pyzbar.decode(image)
for barcode in barcodes:
    (x,y,w,h) = barcode.rect
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

    barcodeData = barcode.data.decode('utf-8')
    barcodeTypes = barcode.type
    text = "{} ({})".format(barcodeData,barcodeTypes)
    cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0, 255),2)
    # cv2.putText(image,text,(x,y-10),cv2.FONT_HERSEY_SIMPLEX,0.5,(0,0,255),2)

    print("[INFO] Found{} barcode: {} ".format(barcodeTypes,barcodeData))

cv2.imshow("Image",image)
cv2.waitKey(0)

    
    