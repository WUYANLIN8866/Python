import cv2
'''讀取cv2函式庫'''
casc_path= "C:\\Users\\enter\\AppData\\Roaming\\Python\\Python35\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
'''讀取辨識檔'''
faceCascade=cv2.CascadeClassifier(casc_path)
'''辨識臉部'''
cap = cv2.VideoCapture(0)
'''開啟攝影機並將變數存在cap'''
ret, img = cap.read()
while(cap.isOpened()):
    k = cv2.waitKey(1)
    if k == ord("z") or k == ord("Z"):
                break
    if ret == True:
        cv2.rectangle(img,(10,img.shape[0]-20),(110,img.shape[0]),(0,0,0),-1)
        faces=faceCascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=3,minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
            cv2.namedWindow("facedetect")
            cv2.imshow("facedetect",img)
cap.release()
cv2.destroyAllWindows()