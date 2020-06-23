import cv2
'''讀取cv2函式庫'''
casc_path= "C:\\Users\\enter\\AppData\\Roaming\\Python\\Python35\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
'''讀取辨識檔'''
faceCascade=cv2.CascadeClassifier(casc_path)
'''辨識臉部'''
img=cv2.imread("C:\\Users\\K556UQ\\Desktop\\PROGRAM\\python photo\\555.jpg")
'''要辨識的照片'''
faces=faceCascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=3,minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)
'''辨識結果變數=辨識物件變數.辨識多張臉部 回傳(x座標,y座標,臉部寬度(w)及高度(h)(圖片,特徵比對正常參數1.1,控制誤檢參數,最小控制區塊,按比例正常檢測)'''
cv2.rectangle(img,(10,img.shape[0]-20),(110,img.shape[0]),(0,0,0),-1)
'''在畫面左下方畫一個舉行作為印出有幾個人的文字用''' 
cv2.putText(img,"Find"+str(len(faces))+"face!",(10,img.shape[0]-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
'''用白色的字顯示有幾張臉'''
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
'''用回全在每一張臉上畫矩形'''
cv2.namedWindow("facedetect")
'''視窗名稱 ''' 
cv2.imshow("facedetect",img)
'''顯示圖片'''   
cv2.waitKey(0)
'''設定時間關閉    0=持續開啟  '''
cv2.destroyWindow("facedetect")
'''關閉視窗 '''