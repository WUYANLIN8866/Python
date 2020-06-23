import cv2
'''讀取cv2函式庫'''
cv2.namedWindow("frame")
'''視窗名稱 ''' 
cap = cv2.VideoCapture(0)
'''開啟攝影機並將變數存在cap'''
while(cap.isOpened()):
    '''當攝影機為開啟狀態就無限執行'''
    ret, img = cap.read()
    if ret == True:
        cv2.imshow("frame",img)
        '''如果讀取成功就在視窗顯示'''
        k = cv2.waitKey(1)
        if k == ord("z") or k == ord("Z"):
            cv2.imwrite("C:\\Users\\K556UQ\\Desktop\\python photo\\a2.jpg",img)
            '''每100毫秒檢查一次是否按下z/Z'''
            break
cap.release()
'''關閉攝影機'''
cv2.destroyAllWindows()
'''關閉視窗 '''