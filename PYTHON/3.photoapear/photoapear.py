import cv2  
'''讀取cv2函式庫'''
img = cv2.imread("D:\\PROGRAM\\python photo\\PHOTO\\watch3.jpg")
'''img=圖檔'''
cv2.namedWindow("Image") 
'''視窗名稱 ''' 
cv2.imshow("Image", img)
'''顯示圖片'''   
cv2.waitKey (0)
'''設定時間關閉    0=持續開啟  '''
cv2.destroyAllWindows() 
'''關閉視窗 '''