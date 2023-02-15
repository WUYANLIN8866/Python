import cv2,os,numpy as np,xml.etree.ElementTree as XET
global PASS,FAIL,datapath,CHeck255Stander
StartNumber = 0                                                                                                         #基本參數設定
CHeck255Stander = StartNumber
CHeck255Stander = StartNumber + 1
CHeck255SUMStander = 75*6
filenum = StartNumber
PASS = StartNumber
FAIL = StartNumber
Left_LED_TEST_FAIL = StartNumber
TestResult = StartNumber
white_lower = np.array([255, 255, 255])                                                                                 #設定白色數值最低[R,G,B]
white_upper = white_lower                                                                                               #設定白色數值最高[R,G,B]
LED_lower = np.array([50,  50,  50])                                                                                   #設定白色數值最低[R,G,B]
LED_upper = white_upper                                                                                                 #設定白色數值最高[R,G,B]
datapath = ""                                                               #設定 檔案路徑
def CheckUpSevenSegmentDisplayNumber(datapath,SN,xmlpath):
    try:
        XMLDATA = XET.parse(xmlpath)
        XMLDATA = XMLDATA.getroot()
        openlog = str(XMLDATA[7].text)
        seven_segment_display_number = 0                                                                                    # 設定 seven_segment_display_number 起始值 = 0
        Up_seven_segment_display_PASS = 0
        if openlog == 1:
            Up_seven_segment_display2_log = open(datapath + "log\\UUT (" + str(SN) + ")_Up_seven_segment_display.log", 'w')
        original_img = cv2.imread(datapath + str(SN) + ".png")                                                #設定 拍完的照片 = original_img
        cv2.imwrite(datapath + "TEST\\result_" + str(SN) + ".png", original_img)                                         #另存 拍完的照片  路徑datapath + "result_UUT (" + str(SN) + ").png"
        Process_photo = cv2.imread(datapath + "TEST\\result_" + str(SN) + ".png")                                        #設定 拍完的照片 = Process_photo
        Up_seven_segment_display = Process_photo[450:700, 1100:1500]                                                        #設定 絕對座標切割參數(上方七段顯示器)
        #Down_seven_segment_display = Process_photo[950:1200, 1100:1500]                                                     # 設定 絕對座標切割參數(上方七段顯示器)
        cv2.imwrite(datapath + "TEST\\result_" + str(SN) + ".png", Up_seven_segment_display)                             #使用 絕對座標切割參數 製作切割圖片
        Up_seven_segment_display = cv2.imread(datapath + "TEST\\result_" + str(SN) + ".png")                             #設定 切割圖片 = Up_seven_segment_display
        SetStanderRange = cv2.inRange(Up_seven_segment_display, white_lower, white_upper)                                   #設定只抓取白色
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
        SetStanderRange = cv2.dilate(SetStanderRange, kernel)
        SetStanderRange = cv2.erode(SetStanderRange, kernel)

        contours, hierarchy = cv2.findContours(SetStanderRange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            Up_seven_segment_display_2_A_Check255 = 0
            Up_seven_segment_display_2_B_Check255 = 0
            Up_seven_segment_display_2_C_Check255 = 0
            Up_seven_segment_display_2_D_Check255 = 0
            Up_seven_segment_display_2_E_Check255 = 0
            Up_seven_segment_display_2_F_Check255 = 0
            Up_seven_segment_display_2_G_Check255 = 0
            area = cv2.contourArea(contour)
            if (area > 300):                                                                                                #設定精度
                seven_segment_display_number += 1
                x, y, w, h = cv2.boundingRect(contour)                                                                      #取得 白色的相對四點座標
                Up_seven_segment_display_2 = Up_seven_segment_display[y:y + h, x:x + w]                                     #用 白色的相對四點座標 做二次切割
                cv2.imwrite(datapath + "TEST\\result_" + str(SN) + ".png",Up_seven_segment_display_2)  # 另存 二次切割圖片 路徑datapath + "result_UUT (" + str(SN) + ").png"
                total_heigh = Up_seven_segment_display_2.shape[0]
                total_width = Up_seven_segment_display_2.shape[1]
                Up_seven_segment_display_2 = cv2.imread(datapath + "TEST\\result_" + str(SN) + ".png")
                Up_seven_segment_display_2_A = Up_seven_segment_display_2[0                     :                            5,     int(total_width/2+10):     int(total_width/2+15)]
                Up_seven_segment_display_2_B = Up_seven_segment_display_2[int(total_heigh/4)    :         int(total_heigh/4+5),     int(total_width - 15):     int(total_width - 10)]
                Up_seven_segment_display_2_C = Up_seven_segment_display_2[int(total_heigh/4*3)  :  int(total_heigh / 4*3 +  5),     int(total_width - 25):     int(total_width - 20)]
                Up_seven_segment_display_2_D = Up_seven_segment_display_2[int(total_heigh-20)   :          int(total_heigh-15), int(total_width / 2 + 15): int(total_width / 2 + 20)]
                Up_seven_segment_display_2_E = Up_seven_segment_display_2[int(total_heigh/4*3+5):int(total_heigh / 4 * 3 + 10),                        10:                        15]
                Up_seven_segment_display_2_F = Up_seven_segment_display_2[int(total_heigh/4)    :    int(total_heigh / 4 +  5),                        15:                        20]
                Up_seven_segment_display_2_G = Up_seven_segment_display_2[int(total_heigh/2-5)  :           int(total_heigh/2),     int(total_width/2-10):      int(total_width/2-5)]
                #
                # cv2.imwrite(datapath + "Up_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_A.png", Up_seven_segment_display_2_A)
                # cv2.imwrite(datapath + "Up_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_B.png", Up_seven_segment_display_2_B)
                # cv2.imwrite(datapath + "Up_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_C.png", Up_seven_segment_display_2_C)
                # cv2.imwrite(datapath + "Up_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_D.png", Up_seven_segment_display_2_D)
                # cv2.imwrite(datapath + "Up_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_E.png", Up_seven_segment_display_2_E)
                # cv2.imwrite(datapath + "Up_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_F.png", Up_seven_segment_display_2_F)
                # cv2.imwrite(datapath + "Up_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_G.png", Up_seven_segment_display_2_G)

                if openlog == 1:
                    Up_seven_segment_display2_log.write("Up_seven_segment_display:"+"\n")
                for j in range(5):
                    for j1 in range(5):
                        if openlog == 1:
                            Up_seven_segment_display2_log.write("Up_seven_segment_display_2_A[" + str(j) + "][" + str(j1) + "][0]:" + str(Up_seven_segment_display_2_A[j][j1][0]) + "   Up_seven_segment_display_2_A[" + str(j) + "][" + str(j1) + "][1]:" + str(Up_seven_segment_display_2_A[j][j1][1]) + "   Up_seven_segment_display_2_A[" + str(j) + "][" + str(j1) + "][2]:" + str(Up_seven_segment_display_2_A[j][j1][2]) + "\n")
                            Up_seven_segment_display2_log.write("Up_seven_segment_display_2_B[" + str(j) + "][" + str(j1) + "][0]:" + str(Up_seven_segment_display_2_B[j][j1][0]) + "   Up_seven_segment_display_2_B[" + str(j) + "][" + str(j1) + "][1]:" + str(Up_seven_segment_display_2_B[j][j1][1]) + "   Up_seven_segment_display_2_B[" + str(j) + "][" + str(j1) + "][2]:" + str(Up_seven_segment_display_2_B[j][j1][2]) + "\n")
                            Up_seven_segment_display2_log.write("Up_seven_segment_display_2_C[" + str(j) + "][" + str(j1) + "][0]:" + str(Up_seven_segment_display_2_C[j][j1][0]) + "   Up_seven_segment_display_2_C[" + str(j) + "][" + str(j1) + "][1]:" + str(Up_seven_segment_display_2_C[j][j1][1]) + "   Up_seven_segment_display_2_C[" + str(j) + "][" + str(j1) + "][2]:" + str(Up_seven_segment_display_2_C[j][j1][2]) + "\n")
                            Up_seven_segment_display2_log.write("Up_seven_segment_display_2_D[" + str(j) + "][" + str(j1) + "][0]:" + str(Up_seven_segment_display_2_D[j][j1][0]) + "   Up_seven_segment_display_2_D[" + str(j) + "][" + str(j1) + "][1]:" + str(Up_seven_segment_display_2_D[j][j1][1]) + "   Up_seven_segment_display_2_D[" + str(j) + "][" + str(j1) + "][2]:" + str(Up_seven_segment_display_2_D[j][j1][2]) + "\n")
                            Up_seven_segment_display2_log.write("Up_seven_segment_display_2_E[" + str(j) + "][" + str(j1) + "][0]:" + str(Up_seven_segment_display_2_E[j][j1][0]) + "   Up_seven_segment_display_2_E[" + str(j) + "][" + str(j1) + "][1]:" + str(Up_seven_segment_display_2_E[j][j1][1]) + "   Up_seven_segment_display_2_E[" + str(j) + "][" + str(j1) + "][2]:" + str(Up_seven_segment_display_2_E[j][j1][2]) + "\n")
                            Up_seven_segment_display2_log.write("Up_seven_segment_display_2_F[" + str(j) + "][" + str(j1) + "][0]:" + str(Up_seven_segment_display_2_F[j][j1][0]) + "   Up_seven_segment_display_2_F[" + str(j) + "][" + str(j1) + "][1]:" + str(Up_seven_segment_display_2_F[j][j1][1]) + "   Up_seven_segment_display_2_F[" + str(j) + "][" + str(j1) + "][2]:" + str(Up_seven_segment_display_2_F[j][j1][2]) + "\n")
                            Up_seven_segment_display2_log.write("Up_seven_segment_display_2_G[" + str(j) + "][" + str(j1) + "][0]:" + str(Up_seven_segment_display_2_G[j][j1][0]) + "   Up_seven_segment_display_2_G[" + str(j) + "][" + str(j1) + "][1]:" + str(Up_seven_segment_display_2_G[j][j1][1]) + "   Up_seven_segment_display_2_G[" + str(j) + "][" + str(j1) + "][2]:" + str(Up_seven_segment_display_2_G[j][j1][2]) + "\n")

                        for j3 in range(3):
                                if Up_seven_segment_display_2_A[j][j1][j3] > 254:
                                    Up_seven_segment_display_2_A_Check255 += 1
                                if Up_seven_segment_display_2_B[j][j1][j3] > 254:
                                    Up_seven_segment_display_2_B_Check255 += 1
                                if Up_seven_segment_display_2_C[j][j1][j3] > 254:
                                    Up_seven_segment_display_2_C_Check255 += 1
                                if Up_seven_segment_display_2_D[j][j1][j3] > 254:
                                    Up_seven_segment_display_2_D_Check255 += 1
                                if Up_seven_segment_display_2_E[j][j1][j3] > 254:
                                    Up_seven_segment_display_2_E_Check255 += 1
                                if Up_seven_segment_display_2_F[j][j1][j3] > 254:
                                    Up_seven_segment_display_2_F_Check255 += 1
                                if Up_seven_segment_display_2_G[j][j1][j3] > 254:
                                    Up_seven_segment_display_2_G_Check255 += 1
                # print("UP: \n",Up_seven_segment_display_2_A_Check255,Up_seven_segment_display_2_B_Check255,Up_seven_segment_display_2_C_Check255,Up_seven_segment_display_2_D_Check255,Up_seven_segment_display_2_E_Check255,Up_seven_segment_display_2_F_Check255,Up_seven_segment_display_2_G_Check255)
                # print("Sum_up:",Up_seven_segment_display_2_A_Check255 + Up_seven_segment_display_2_B_Check255 + Up_seven_segment_display_2_C_Check255 + Up_seven_segment_display_2_D_Check255 + Up_seven_segment_display_2_E_Check255 + Up_seven_segment_display_2_F_Check255 + Up_seven_segment_display_2_G_Check255)
                if Up_seven_segment_display_2_A_Check255 > CHeck255Stander and Up_seven_segment_display_2_B_Check255 > CHeck255Stander and Up_seven_segment_display_2_C_Check255 > CHeck255Stander and Up_seven_segment_display_2_D_Check255 > CHeck255Stander and Up_seven_segment_display_2_E_Check255 > CHeck255Stander and Up_seven_segment_display_2_F_Check255 > CHeck255Stander and Up_seven_segment_display_2_G_Check255 > CHeck255Stander:
                    Up_seven_segment_display_PASS += 1
                elif Up_seven_segment_display_2_A_Check255 + Up_seven_segment_display_2_B_Check255 + Up_seven_segment_display_2_C_Check255 + Up_seven_segment_display_2_D_Check255 + Up_seven_segment_display_2_E_Check255 + Up_seven_segment_display_2_F_Check255 + Up_seven_segment_display_2_G_Check255 > CHeck255SUMStander:
                    Up_seven_segment_display_PASS += 1
        # os.remove(datapath + "TEST\\result_UUT (" + str(SN) + ").png")
    except:
        # os.remove(datapath + "TEST\\result_UUT (" + str(SN) + ").png")
        Up_seven_segment_display_PASS = 0
    return Up_seven_segment_display_PASS
def CheckDownSevenSegmentDisplayNumber(datapath,SN,xmlpath):
    try:
        XMLDATA = XET.parse(xmlpath)
        XMLDATA = XMLDATA.getroot()
        openlog = str(XMLDATA[7].text)
        seven_segment_display_number = 0                                                                                    # 設定 seven_segment_display_number 起始值 = 0
        Down_seven_segment_display_PASS = 0
        if openlog == 1:
            Down_seven_segment_display2_log = open(datapath + "log\\UUT (" + str(SN) + ")_Down_seven_segment_display.log", 'w')
        original_img = cv2.imread(datapath + str(SN) + ".png")                                                #設定 拍完的照片 = original_img
        cv2.imwrite(datapath + "TEST\\result_" + str(SN) + ".png", original_img)                                         #另存 拍完的照片  路徑datapath + "result_UUT (" + str(SN) + ").png"
        Process_photo = cv2.imread(datapath + "\\TEST\\result_" + str(SN) + ".png")                                        #設定 拍完的照片 = Process_photo
        Down_seven_segment_display = Process_photo[1300:1500, 1100:1500]                                                     # 設定 絕對座標切割參數(上方七段顯示器)
        cv2.imwrite(datapath + "TEST\\result_" + str(SN) + ".png", Down_seven_segment_display)                             #使用 絕對座標切割參數 製作切割圖片
        Down_seven_segment_display = cv2.imread(datapath + "TEST\\result_" + str(SN) + ".png")                             #設定 切割圖片 = Down_seven_segment_display
        SetStanderRange = cv2.inRange(Down_seven_segment_display, white_lower, white_upper)                                   #設定只抓取白色
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
        SetStanderRange = cv2.dilate(SetStanderRange, kernel)
        SetStanderRange = cv2.erode(SetStanderRange, kernel)

        contours, hierarchy = cv2.findContours(SetStanderRange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            Down_seven_segment_display_2_A_Check255 = 0
            Down_seven_segment_display_2_B_Check255 = 0
            Down_seven_segment_display_2_C_Check255 = 0
            Down_seven_segment_display_2_D_Check255 = 0
            Down_seven_segment_display_2_E_Check255 = 0
            Down_seven_segment_display_2_F_Check255 = 0
            Down_seven_segment_display_2_G_Check255 = 0
            area = cv2.contourArea(contour)
            if (area > 300):                                                                                                #設定精度
                seven_segment_display_number += 1
                x, y, w, h = cv2.boundingRect(contour)                                                                      #取得 白色的相對四點座標
                Down_seven_segment_display_2 = Down_seven_segment_display[y:y + h, x:x + w]                                     #用 白色的相對四點座標 做二次切割
                cv2.imwrite(datapath + "TEST\\Down_seven_segment_display_UUT (" + str(SN) + ")_"+str(seven_segment_display_number)+".png", Down_seven_segment_display_2)   #另存 二次切割圖片 路徑datapath + "result_UUT (" + str(SN) + ").png"
                total_heigh = Down_seven_segment_display_2.shape[0]
                total_width = Down_seven_segment_display_2.shape[1]
                Down_seven_segment_display_2 = cv2.imread(datapath + "TEST\\Down_seven_segment_display_UUT (" + str(SN) + ")_"+str(seven_segment_display_number)+".png")
                Down_seven_segment_display_2_A = Down_seven_segment_display_2[0                     :                            5,     int(total_width/2+10):     int(total_width/2+15)]
                Down_seven_segment_display_2_B = Down_seven_segment_display_2[int(total_heigh/4)    :         int(total_heigh/4+5),     int(total_width - 15):     int(total_width - 10)]
                Down_seven_segment_display_2_C = Down_seven_segment_display_2[int(total_heigh/4*3)  :  int(total_heigh / 4*3 +  5),     int(total_width - 25):     int(total_width - 20)]
                Down_seven_segment_display_2_D = Down_seven_segment_display_2[int(total_heigh-20)   :          int(total_heigh-15), int(total_width / 2 + 15): int(total_width / 2 + 20)]
                Down_seven_segment_display_2_E = Down_seven_segment_display_2[int(total_heigh/4*3+5):int(total_heigh / 4 * 3 + 10),                        10:                        15]
                Down_seven_segment_display_2_F = Down_seven_segment_display_2[int(total_heigh/4)    :    int(total_heigh / 4 +  5),                        15:                        20]
                Down_seven_segment_display_2_G = Down_seven_segment_display_2[int(total_heigh/2-5)  :           int(total_heigh/2),     int(total_width/2-10):      int(total_width/2-5)]
                #
                # cv2.imwrite(datapath + "Down_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_A.png", Down_seven_segment_display_2_A)
                # cv2.imwrite(datapath + "Down_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_B.png", Down_seven_segment_display_2_B)
                # cv2.imwrite(datapath + "Down_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_C.png", Down_seven_segment_display_2_C)
                # cv2.imwrite(datapath + "Down_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_D.png", Down_seven_segment_display_2_D)
                # cv2.imwrite(datapath + "Down_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_E.png", Down_seven_segment_display_2_E)
                # cv2.imwrite(datapath + "Down_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_F.png", Down_seven_segment_display_2_F)
                # cv2.imwrite(datapath + "Down_seven_segment_display_UUT (" + str(SN) + ")_" + str(seven_segment_display_number) + "_G.png", Down_seven_segment_display_2_G)

                if openlog == 1:
                    Down_seven_segment_display2_log.write("Down_seven_segment_display:"+"\n")
                for j in range(5):
                    for j1 in range(5):
                        if openlog == 1:
                            Down_seven_segment_display2_log.write("Down_seven_segment_display_2_A[" + str(j) + "][" + str(j1) + "][0]:" + str(Down_seven_segment_display_2_A[j][j1][0]) + "   Down_seven_segment_display_2_A[" + str(j) + "][" + str(j1) + "][1]:" + str(Down_seven_segment_display_2_A[j][j1][1]) + "   Down_seven_segment_display_2_A[" + str(j) + "][" + str(j1) + "][2]:" + str(Down_seven_segment_display_2_A[j][j1][2]) + "\n")
                            Down_seven_segment_display2_log.write("Down_seven_segment_display_2_B[" + str(j) + "][" + str(j1) + "][0]:" + str(Down_seven_segment_display_2_B[j][j1][0]) + "   Down_seven_segment_display_2_B[" + str(j) + "][" + str(j1) + "][1]:" + str(Down_seven_segment_display_2_B[j][j1][1]) + "   Down_seven_segment_display_2_B[" + str(j) + "][" + str(j1) + "][2]:" + str(Down_seven_segment_display_2_B[j][j1][2]) + "\n")
                            Down_seven_segment_display2_log.write("Down_seven_segment_display_2_C[" + str(j) + "][" + str(j1) + "][0]:" + str(Down_seven_segment_display_2_C[j][j1][0]) + "   Down_seven_segment_display_2_C[" + str(j) + "][" + str(j1) + "][1]:" + str(Down_seven_segment_display_2_C[j][j1][1]) + "   Down_seven_segment_display_2_C[" + str(j) + "][" + str(j1) + "][2]:" + str(Down_seven_segment_display_2_C[j][j1][2]) + "\n")
                            Down_seven_segment_display2_log.write("Down_seven_segment_display_2_D[" + str(j) + "][" + str(j1) + "][0]:" + str(Down_seven_segment_display_2_D[j][j1][0]) + "   Down_seven_segment_display_2_D[" + str(j) + "][" + str(j1) + "][1]:" + str(Down_seven_segment_display_2_D[j][j1][1]) + "   Down_seven_segment_display_2_D[" + str(j) + "][" + str(j1) + "][2]:" + str(Down_seven_segment_display_2_D[j][j1][2]) + "\n")
                            Down_seven_segment_display2_log.write("Down_seven_segment_display_2_E[" + str(j) + "][" + str(j1) + "][0]:" + str(Down_seven_segment_display_2_E[j][j1][0]) + "   Down_seven_segment_display_2_E[" + str(j) + "][" + str(j1) + "][1]:" + str(Down_seven_segment_display_2_E[j][j1][1]) + "   Down_seven_segment_display_2_E[" + str(j) + "][" + str(j1) + "][2]:" + str(Down_seven_segment_display_2_E[j][j1][2]) + "\n")
                            Down_seven_segment_display2_log.write("Down_seven_segment_display_2_F[" + str(j) + "][" + str(j1) + "][0]:" + str(Down_seven_segment_display_2_F[j][j1][0]) + "   Down_seven_segment_display_2_F[" + str(j) + "][" + str(j1) + "][1]:" + str(Down_seven_segment_display_2_F[j][j1][1]) + "   Down_seven_segment_display_2_F[" + str(j) + "][" + str(j1) + "][2]:" + str(Down_seven_segment_display_2_F[j][j1][2]) + "\n")
                            Down_seven_segment_display2_log.write("Down_seven_segment_display_2_G[" + str(j) + "][" + str(j1) + "][0]:" + str(Down_seven_segment_display_2_G[j][j1][0]) + "   Down_seven_segment_display_2_G[" + str(j) + "][" + str(j1) + "][1]:" + str(Down_seven_segment_display_2_G[j][j1][1]) + "   Down_seven_segment_display_2_G[" + str(j) + "][" + str(j1) + "][2]:" + str(Down_seven_segment_display_2_G[j][j1][2]) + "\n")

                        for j3 in range(3):
                                if Down_seven_segment_display_2_A[j][j1][j3] > 254:
                                    Down_seven_segment_display_2_A_Check255 += 1
                                if Down_seven_segment_display_2_B[j][j1][j3] > 254:
                                    Down_seven_segment_display_2_B_Check255 += 1
                                if Down_seven_segment_display_2_C[j][j1][j3] > 254:
                                    Down_seven_segment_display_2_C_Check255 += 1
                                if Down_seven_segment_display_2_D[j][j1][j3] > 254:
                                    Down_seven_segment_display_2_D_Check255 += 1
                                if Down_seven_segment_display_2_E[j][j1][j3] > 254:
                                    Down_seven_segment_display_2_E_Check255 += 1
                                if Down_seven_segment_display_2_F[j][j1][j3] > 254:
                                    Down_seven_segment_display_2_F_Check255 += 1
                                if Down_seven_segment_display_2_G[j][j1][j3] > 254:
                                    Down_seven_segment_display_2_G_Check255 += 1
                # print("DOWN: \n",Down_seven_segment_display_2_A_Check255,Down_seven_segment_display_2_B_Check255,Down_seven_segment_display_2_C_Check255,Down_seven_segment_display_2_D_Check255,Down_seven_segment_display_2_E_Check255,Down_seven_segment_display_2_F_Check255,Down_seven_segment_display_2_G_Check255)
                # print("Sum_down:",Down_seven_segment_display_2_A_Check255 + Down_seven_segment_display_2_B_Check255 + Down_seven_segment_display_2_C_Check255 + Down_seven_segment_display_2_D_Check255 + Down_seven_segment_display_2_E_Check255 + Down_seven_segment_display_2_F_Check255 + Down_seven_segment_display_2_G_Check255)
                if Down_seven_segment_display_2_A_Check255 > CHeck255Stander and Down_seven_segment_display_2_B_Check255 > CHeck255Stander and Down_seven_segment_display_2_C_Check255 > CHeck255Stander and Down_seven_segment_display_2_D_Check255 > CHeck255Stander and Down_seven_segment_display_2_E_Check255 > CHeck255Stander and Down_seven_segment_display_2_F_Check255 > CHeck255Stander and Down_seven_segment_display_2_G_Check255 > CHeck255Stander:
                    Down_seven_segment_display_PASS += 1
                elif Down_seven_segment_display_2_A_Check255 + Down_seven_segment_display_2_B_Check255 + Down_seven_segment_display_2_C_Check255 + Down_seven_segment_display_2_D_Check255 + Down_seven_segment_display_2_E_Check255 + Down_seven_segment_display_2_F_Check255 + Down_seven_segment_display_2_G_Check255 > CHeck255SUMStander:
                    Down_seven_segment_display_PASS += 1
        os.remove(datapath + "TEST\\result_" + str(SN) + ".png")
    except:
        os.remove(datapath + "TEST\\result_" + str(SN) + ".png")
        Down_seven_segment_display_PASS = 0
    return Down_seven_segment_display_PASS
def TestRightLed(datapath,SN,PASS,FAIL):
    Right_LED_01_Check255 = 0
    Right_LED_02_Check255 = 0
    Right_LED_03_Check255 = 0
    Right_LED_04_Check255 = 0
    Right_LED_05_Check255 = 0
    Right_LED_06_Check255 = 0
    Right_LED_07_Check255 = 0
    Right_LED_08_Check255 = 0
    Right_LED_09_Check255 = 0
    Right_LED_10_Check255 = 0
    Right_LED_11_Check255 = 0
    Right_LED_12_Check255 = 0
    Right_LED_13_Check255 = 0
    Right_LED_14_Check255 = 0
    Right_LED_15_Check255 = 0
    Right_LED_16_Check255 = 0
    Right_LED_17_Check255 = 0
    Right_LED_18_Check255 = 0
    Right_LED_19_Check255 = 0
    Right_LED_20_Check255 = 0
    Right_LED_21_Check255 = 0
    Right_LED_22_Check255 = 0
    Right_LED_23_Check255 = 0
    Right_LED_24_Check255 = 0
    Right_LED_25_Check255 = 0
    Right_LED_26_Check255 = 0
    Right_LED_27_Check255 = 0
    Right_LED_28_Check255 = 0
    Right_LED_29_Check255 = 0
    Right_LED_30_Check255 = 0
    
    original_img = cv2.imread(datapath + str(SN) + ".png")  # 設定 拍完的照片 = original_img
    cv2.imwrite(datapath + "TEST\\Right_LED_" + str(SN) + ".png",
                original_img)  # 另存 拍完的照片  路徑datapath + "result_UUT (" + str(SN) + ").png"
    Process_photo = cv2.imread(datapath + "TEST\\Right_LED_" + str(SN) + ".png")  # 設定 拍完的照片 = Process_photo

    Right_LED = Process_photo[int(Process_photo.shape[0] * 0.17):int(Process_photo.shape[0] * 0.86),int(Process_photo.shape[1] * 0.6):int(Process_photo.shape[1] * 0.92)]
    
    RightLED_01_10 = Right_LED[0:Right_LED.shape[0], 0:int(Right_LED.shape[1] * 0.3)]
    RightLED1 = Right_LED[int(0 + 0 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 0 * Right_LED.shape[0] / 10),0:int(Right_LED.shape[1] * 0.3)]
    RightLED2 = Right_LED[int(0 + 1 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 1 * Right_LED.shape[0] / 10),0:int(Right_LED.shape[1] * 0.3)]
    RightLED3 = Right_LED[int(0 + 2 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 2 * Right_LED.shape[0] / 10),0:int(Right_LED.shape[1] * 0.3)]
    RightLED4 = Right_LED[int(0 + 3 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 3 * Right_LED.shape[0] / 10),0:int(Right_LED.shape[1] * 0.3)]
    RightLED5 = Right_LED[int(0 + 4 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 4 * Right_LED.shape[0] / 10),0:int(Right_LED.shape[1] * 0.3)]
    RightLED6 = Right_LED[int(0 + 5 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 5 * Right_LED.shape[0] / 10),0:int(Right_LED.shape[1] * 0.3)]
    RightLED7 = Right_LED[int(0 + 6 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 6 * Right_LED.shape[0] / 10),0:int(Right_LED.shape[1] * 0.3)]
    RightLED8 = Right_LED[int(0 + 7 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 7 * Right_LED.shape[0] / 10),0:int(Right_LED.shape[1] * 0.3)]
    RightLED9 = Right_LED[int(0 + 8 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 8 * Right_LED.shape[0] / 10),0:int(Right_LED.shape[1] * 0.3)]
    RightLED10 = Right_LED[int(0 + 9 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 9 * Right_LED.shape[0] / 10),0:int(Right_LED.shape[1] * 0.3)]
    
    RightLED_11_20 = Right_LED[0:Right_LED.shape[0],int(Right_LED.shape[1] * 0.3):int(Right_LED.shape[1] * 0.55)]
    RightLED11 = Right_LED[int(0 + 0 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 0 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.3):int(Right_LED.shape[1] * 0.55)]
    RightLED12 = Right_LED[int(0 + 1 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 1 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.3):int(Right_LED.shape[1] * 0.55)]
    RightLED13 = Right_LED[int(0 + 2 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 2 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.3):int(Right_LED.shape[1] * 0.55)]
    RightLED14 = Right_LED[int(0 + 3 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 3 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.3):int(Right_LED.shape[1] * 0.55)]
    RightLED15 = Right_LED[int(0 + 4 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 4 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.3):int(Right_LED.shape[1] * 0.55)]
    RightLED16 = Right_LED[int(0 + 5 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 5 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.3):int(Right_LED.shape[1] * 0.55)]
    RightLED17 = Right_LED[int(0 + 6 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 6 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.3):int(Right_LED.shape[1] * 0.55)]
    RightLED18 = Right_LED[int(0 + 7 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 7 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.3):int(Right_LED.shape[1] * 0.55)]
    RightLED19 = Right_LED[int(0 + 8 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 8 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.3):int(Right_LED.shape[1] * 0.55)]
    RightLED20 = Right_LED[int(0 + 9 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 9 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.3):int(Right_LED.shape[1] * 0.55)]
    
    RightLED_21_30 = Right_LED[0:Right_LED.shape[0],int(Right_LED.shape[1] * 0.55):int(Right_LED.shape[1] * 0.85)]
    RightLED21 = Right_LED[int(0 + 0 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 0 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.55):int(Right_LED.shape[1] * 0.85)]
    RightLED22 = Right_LED[int(0 + 1 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 1 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.55):int(Right_LED.shape[1] * 0.85)]
    RightLED23 = Right_LED[int(0 + 2 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 2 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.55):int(Right_LED.shape[1] * 0.85)]
    RightLED24 = Right_LED[int(0 + 3 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 3 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.55):int(Right_LED.shape[1] * 0.85)]
    RightLED25 = Right_LED[int(0 + 4 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 4 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.55):int(Right_LED.shape[1] * 0.85)]
    RightLED26 = Right_LED[int(0 + 5 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 5 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.55):int(Right_LED.shape[1] * 0.85)]
    RightLED27 = Right_LED[int(0 + 6 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 6 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.55):int(Right_LED.shape[1] * 0.85)]
    RightLED28 = Right_LED[int(0 + 7 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 7 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.55):int(Right_LED.shape[1] * 0.85)]
    RightLED29 = Right_LED[int(0 + 8 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 8 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.55):int(Right_LED.shape[1] * 0.85)]
    RightLED30 = Right_LED[int(0 + 9 * Right_LED.shape[0] / 10):int(Right_LED.shape[0] / 10 + 9 * Right_LED.shape[0] / 10),int(Right_LED.shape[1] * 0.55):int(Right_LED.shape[1] * 0.85)]


    # cv2.imwrite(datapath + "TEST\\Right_LED_01_10_UUT (" + str(SN) + ").png",RightLED_01_10)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_01_UUT (" + str(SN) + ").png", RightLED1)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_02_UUT (" + str(SN) + ").png", RightLED2)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_03_UUT (" + str(SN) + ").png", RightLED3)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_04_UUT (" + str(SN) + ").png", RightLED4)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_05_UUT (" + str(SN) + ").png", RightLED5)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_06_UUT (" + str(SN) + ").png", RightLED6)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_07_UUT (" + str(SN) + ").png", RightLED7)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_08_UUT (" + str(SN) + ").png", RightLED8)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_09_UUT (" + str(SN) + ").png", RightLED9)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_10_UUT (" + str(SN) + ").png", RightLED10)  # 使用 絕對座標切割參數 製作切割圖片
    #
    # cv2.imwrite(datapath + "TEST\\Right_LED_11_20_UUT (" + str(SN) + ").png",RightLED_11_20)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_11_UUT (" + str(SN) + ").png", RightLED11)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_12_UUT (" + str(SN) + ").png", RightLED12)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_13_UUT (" + str(SN) + ").png", RightLED13)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_14_UUT (" + str(SN) + ").png", RightLED14)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_15_UUT (" + str(SN) + ").png", RightLED15)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_16_UUT (" + str(SN) + ").png", RightLED16)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_17_UUT (" + str(SN) + ").png", RightLED17)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_18_UUT (" + str(SN) + ").png", RightLED18)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_19_UUT (" + str(SN) + ").png", RightLED19)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_20_UUT (" + str(SN) + ").png", RightLED20)  # 使用 絕對座標切割參數 製作切割圖片
    #
    # cv2.imwrite(datapath + "TEST\\Right_LED_21_30_UUT (" + str(SN) + ").png",RightLED_21_30)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_21_UUT (" + str(SN) + ").png", RightLED21)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_22_UUT (" + str(SN) + ").png", RightLED22)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_23_UUT (" + str(SN) + ").png", RightLED23)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_24_UUT (" + str(SN) + ").png", RightLED24)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_25_UUT (" + str(SN) + ").png", RightLED25)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_26_UUT (" + str(SN) + ").png", RightLED26)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_27_UUT (" + str(SN) + ").png", RightLED27)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_28_UUT (" + str(SN) + ").png", RightLED28)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_29_UUT (" + str(SN) + ").png", RightLED29)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Right_LED_30_UUT (" + str(SN) + ").png", RightLED30)  # 使用 絕對座標切割參數 製作切割圖片

    # Right_LED_01 = cv2.imread(datapath + "TEST\\Right_LED_01_UUT (" + str(SN) + ").png")
    # Right_LED_02 = cv2.imread(datapath + "TEST\\Right_LED_02_UUT (" + str(SN) + ").png")
    # Right_LED_03 = cv2.imread(datapath + "TEST\\Right_LED_03_UUT (" + str(SN) + ").png")
    # Right_LED_04 = cv2.imread(datapath + "TEST\\Right_LED_04_UUT (" + str(SN) + ").png")
    # Right_LED_05 = cv2.imread(datapath + "TEST\\Right_LED_05_UUT (" + str(SN) + ").png")
    # Right_LED_06 = cv2.imread(datapath + "TEST\\Right_LED_06_UUT (" + str(SN) + ").png")
    # Right_LED_07 = cv2.imread(datapath + "TEST\\Right_LED_07_UUT (" + str(SN) + ").png")
    # Right_LED_08 = cv2.imread(datapath + "TEST\\Right_LED_08_UUT (" + str(SN) + ").png")
    # Right_LED_09 = cv2.imread(datapath + "TEST\\Right_LED_09_UUT (" + str(SN) + ").png")
    # Right_LED_10 = cv2.imread(datapath + "TEST\\Right_LED_10_UUT (" + str(SN) + ").png")
    # Right_LED_11 = cv2.imread(datapath + "TEST\\Right_LED_11_UUT (" + str(SN) + ").png")
    # Right_LED_12 = cv2.imread(datapath + "TEST\\Right_LED_12_UUT (" + str(SN) + ").png")
    # Right_LED_13 = cv2.imread(datapath + "TEST\\Right_LED_13_UUT (" + str(SN) + ").png")
    # Right_LED_14 = cv2.imread(datapath + "TEST\\Right_LED_14_UUT (" + str(SN) + ").png")
    # Right_LED_15 = cv2.imread(datapath + "TEST\\Right_LED_15_UUT (" + str(SN) + ").png")
    # Right_LED_16 = cv2.imread(datapath + "TEST\\Right_LED_16_UUT (" + str(SN) + ").png")
    # Right_LED_17 = cv2.imread(datapath + "TEST\\Right_LED_17_UUT (" + str(SN) + ").png")
    # Right_LED_18 = cv2.imread(datapath + "TEST\\Right_LED_18_UUT (" + str(SN) + ").png")
    # Right_LED_19 = cv2.imread(datapath + "TEST\\Right_LED_19_UUT (" + str(SN) + ").png")
    # Right_LED_20 = cv2.imread(datapath + "TEST\\Right_LED_20_UUT (" + str(SN) + ").png")
    # Right_LED_21 = cv2.imread(datapath + "TEST\\Right_LED_21_UUT (" + str(SN) + ").png")
    # Right_LED_22 = cv2.imread(datapath + "TEST\\Right_LED_22_UUT (" + str(SN) + ").png")
    # Right_LED_23 = cv2.imread(datapath + "TEST\\Right_LED_23_UUT (" + str(SN) + ").png")
    # Right_LED_24 = cv2.imread(datapath + "TEST\\Right_LED_24_UUT (" + str(SN) + ").png")
    # Right_LED_25 = cv2.imread(datapath + "TEST\\Right_LED_25_UUT (" + str(SN) + ").png")
    # Right_LED_26 = cv2.imread(datapath + "TEST\\Right_LED_26_UUT (" + str(SN) + ").png")
    # Right_LED_27 = cv2.imread(datapath + "TEST\\Right_LED_27_UUT (" + str(SN) + ").png")
    # Right_LED_28 = cv2.imread(datapath + "TEST\\Right_LED_28_UUT (" + str(SN) + ").png")
    # Right_LED_29 = cv2.imread(datapath + "TEST\\Right_LED_29_UUT (" + str(SN) + ").png")
    # Right_LED_30 = cv2.imread(datapath + "TEST\\Right_LED_30_UUT (" + str(SN) + ").png")

    Right_LED_01 = RightLED1
    Right_LED_02 = RightLED2
    Right_LED_03 = RightLED3
    Right_LED_04 = RightLED4
    Right_LED_05 = RightLED5
    Right_LED_06 = RightLED6
    Right_LED_07 = RightLED7
    Right_LED_08 = RightLED8
    Right_LED_09 = RightLED9
    Right_LED_10 = RightLED10
    Right_LED_11 = RightLED11
    Right_LED_12 = RightLED12
    Right_LED_13 = RightLED13
    Right_LED_14 = RightLED14
    Right_LED_15 = RightLED15
    Right_LED_16 = RightLED16
    Right_LED_17 = RightLED17
    Right_LED_18 = RightLED18
    Right_LED_19 = RightLED19
    Right_LED_20 = RightLED20
    Right_LED_21 = RightLED21
    Right_LED_22 = RightLED22
    Right_LED_23 = RightLED23
    Right_LED_24 = RightLED24
    Right_LED_25 = RightLED25
    Right_LED_26 = RightLED26
    Right_LED_27 = RightLED27
    Right_LED_28 = RightLED28
    Right_LED_29 = RightLED29
    Right_LED_30 = RightLED30
    try:
        for j in range(134):
            for j1 in range(207):
                for j3 in range(3):
                    if Right_LED_01[j][j1][j3] > CHeck255Stander: Right_LED_01_Check255 += 1
                    if Right_LED_02[j][j1][j3] > CHeck255Stander: Right_LED_02_Check255 += 1
                    if Right_LED_03[j][j1][j3] > CHeck255Stander: Right_LED_03_Check255 += 1
                    if Right_LED_04[j][j1][j3] > CHeck255Stander: Right_LED_04_Check255 += 1
                    if Right_LED_05[j][j1][j3] > CHeck255Stander: Right_LED_05_Check255 += 1
                    if Right_LED_06[j][j1][j3] > CHeck255Stander: Right_LED_06_Check255 += 1
                    if Right_LED_07[j][j1][j3] > CHeck255Stander: Right_LED_07_Check255 += 1
                    if Right_LED_08[j][j1][j3] > CHeck255Stander: Right_LED_08_Check255 += 1
                    if Right_LED_09[j][j1][j3] > CHeck255Stander: Right_LED_09_Check255 += 1
                    if Right_LED_10[j][j1][j3] > CHeck255Stander: Right_LED_10_Check255 += 1
                    if Right_LED_11[j][j1][j3] > CHeck255Stander: Right_LED_11_Check255 += 1
                    if Right_LED_12[j][j1][j3] > CHeck255Stander: Right_LED_12_Check255 += 1
                    if Right_LED_13[j][j1][j3] > CHeck255Stander: Right_LED_13_Check255 += 1
                    if Right_LED_14[j][j1][j3] > CHeck255Stander: Right_LED_14_Check255 += 1
                    if Right_LED_15[j][j1][j3] > CHeck255Stander: Right_LED_15_Check255 += 1
                    if Right_LED_16[j][j1][j3] > CHeck255Stander: Right_LED_16_Check255 += 1
                    if Right_LED_17[j][j1][j3] > CHeck255Stander: Right_LED_17_Check255 += 1
                    if Right_LED_18[j][j1][j3] > CHeck255Stander: Right_LED_18_Check255 += 1
                    if Right_LED_19[j][j1][j3] > CHeck255Stander: Right_LED_19_Check255 += 1
                    if Right_LED_20[j][j1][j3] > CHeck255Stander: Right_LED_20_Check255 += 1
                    if Right_LED_21[j][j1][j3] > CHeck255Stander: Right_LED_21_Check255 += 1
                    if Right_LED_22[j][j1][j3] > CHeck255Stander: Right_LED_22_Check255 += 1
                    if Right_LED_23[j][j1][j3] > CHeck255Stander: Right_LED_23_Check255 += 1
                    if Right_LED_24[j][j1][j3] > CHeck255Stander: Right_LED_24_Check255 += 1
                    if Right_LED_25[j][j1][j3] > CHeck255Stander: Right_LED_25_Check255 += 1
                    if Right_LED_26[j][j1][j3] > CHeck255Stander: Right_LED_26_Check255 += 1
                    if Right_LED_27[j][j1][j3] > CHeck255Stander: Right_LED_27_Check255 += 1
                    if Right_LED_28[j][j1][j3] > CHeck255Stander: Right_LED_28_Check255 += 1
                    if Right_LED_29[j][j1][j3] > CHeck255Stander: Right_LED_29_Check255 += 1
                    if Right_LED_30[j][j1][j3] > CHeck255Stander: Right_LED_30_Check255 += 1
    except:
        Donothing = 1
    PassNum = 0
    if Right_LED_01_Check255 > PassNum and Right_LED_02_Check255 > PassNum and  Right_LED_04_Check255 > PassNum and Right_LED_05_Check255 > PassNum and Right_LED_06_Check255 > PassNum and Right_LED_07_Check255 > PassNum and Right_LED_08_Check255 > PassNum and Right_LED_09_Check255 > PassNum and Right_LED_10_Check255 > PassNum and Right_LED_11_Check255 > PassNum and Right_LED_12_Check255 > PassNum and Right_LED_13_Check255 > PassNum and Right_LED_14_Check255 > PassNum and Right_LED_15_Check255 > PassNum and Right_LED_16_Check255 > PassNum and Right_LED_17_Check255 > PassNum and Right_LED_18_Check255 > PassNum and Right_LED_19_Check255 > PassNum and Right_LED_20_Check255 > PassNum and Right_LED_21_Check255 > PassNum and Right_LED_22_Check255 > PassNum and Right_LED_23_Check255 > PassNum  and Right_LED_26_Check255 > PassNum and Right_LED_27_Check255 > PassNum and Right_LED_28_Check255 > PassNum and Right_LED_30_Check255 > PassNum:
        PASS = 1
    else:
        print(Right_LED_01_Check255, Right_LED_02_Check255,  Right_LED_04_Check255,
              Right_LED_05_Check255, Right_LED_06_Check255, Right_LED_07_Check255, Right_LED_08_Check255,
              Right_LED_09_Check255, Right_LED_10_Check255, Right_LED_11_Check255, Right_LED_12_Check255,
              Right_LED_13_Check255, Right_LED_14_Check255, Right_LED_15_Check255, Right_LED_16_Check255,
              Right_LED_17_Check255, Right_LED_18_Check255, Right_LED_19_Check255, Right_LED_20_Check255,
              Right_LED_21_Check255, Right_LED_22_Check255, Right_LED_23_Check255, Right_LED_26_Check255,
              Right_LED_27_Check255, Right_LED_28_Check255,
              Right_LED_29_Check255, Right_LED_30_Check255)

        FAIL = 1
    return PASS, FAIL
def TestLeftLed(datapath,SN,PASS, FAIL):
    Left_LED_01_Check255 = 0
    Left_LED_02_Check255 = 0
    Left_LED_03_Check255 = 0
    Left_LED_04_Check255 = 0
    Left_LED_05_Check255 = 0
    Left_LED_06_Check255 = 0
    Left_LED_07_Check255 = 0
    Left_LED_08_Check255 = 0
    Left_LED_09_Check255 = 0
    Left_LED_10_Check255 = 0
    Left_LED_11_Check255 = 0
    Left_LED_12_Check255 = 0
    Left_LED_13_Check255 = 0
    Left_LED_14_Check255 = 0
    Left_LED_15_Check255 = 0
    Left_LED_16_Check255 = 0
    Left_LED_17_Check255 = 0
    Left_LED_18_Check255 = 0
    Left_LED_19_Check255 = 0
    Left_LED_20_Check255 = 0
    Left_LED_21_Check255 = 0
    Left_LED_22_Check255 = 0
    Left_LED_23_Check255 = 0
    Left_LED_24_Check255 = 0
    Left_LED_25_Check255 = 0
    Left_LED_26_Check255 = 0
    Left_LED_27_Check255 = 0
    Left_LED_28_Check255 = 0
    Left_LED_29_Check255 = 0
    Left_LED_30_Check255 = 0

    original_img = cv2.imread(datapath + str(SN) + ".png")  # 設定 拍完的照片 = original_img
    cv2.imwrite(datapath + "TEST\\Left_LED_" + str(SN) + ".png",
                original_img)  # 另存 拍完的照片  路徑datapath + "result_UUT (" + str(SN) + ").png"
    Process_photo = cv2.imread(datapath + "TEST\\Left_LED_" + str(SN) + ".png")  # 設定 拍完的照片 = Process_photo

    Left_LED = Process_photo[int(Process_photo.shape[0] * 0.17):int(Process_photo.shape[0] * 0.86),int(Process_photo.shape[1] * 0.05):int(Process_photo.shape[1] * 0.3)]

    LeftLED_01_10 = Left_LED[0:Left_LED.shape[0], 0:int(Left_LED.shape[1] * 0.3)]
    LeftLED1 = Left_LED[
                int(0 + 0 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 0 * Left_LED.shape[0] / 10),
                0:int(Left_LED.shape[1] * 0.3)]
    LeftLED2 = Left_LED[
                int(0 + 1 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 1 * Left_LED.shape[0] / 10),
                0:int(Left_LED.shape[1] * 0.3)]
    LeftLED3 = Left_LED[
                int(0 + 2 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 2 * Left_LED.shape[0] / 10),
                0:int(Left_LED.shape[1] * 0.3)]
    LeftLED4 = Left_LED[
                int(0 + 3 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 3 * Left_LED.shape[0] / 10),
                0:int(Left_LED.shape[1] * 0.3)]
    LeftLED5 = Left_LED[
                int(0 + 4 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 4 * Left_LED.shape[0] / 10),
                0:int(Left_LED.shape[1] * 0.3)]
    LeftLED6 = Left_LED[
                int(0 + 5 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 5 * Left_LED.shape[0] / 10),
                0:int(Left_LED.shape[1] * 0.3)]
    LeftLED7 = Left_LED[
                int(0 + 6 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 6 * Left_LED.shape[0] / 10),
                0:int(Left_LED.shape[1] * 0.3)]
    LeftLED8 = Left_LED[
                int(0 + 7 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 7 * Left_LED.shape[0] / 10),
                0:int(Left_LED.shape[1] * 0.3)]
    LeftLED9 = Left_LED[
                int(0 + 8 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 8 * Left_LED.shape[0] / 10),
                0:int(Left_LED.shape[1] * 0.3)]
    LeftLED10 = Left_LED[
                 int(0 + 9 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 9 * Left_LED.shape[0] / 10),
                 0:int(Left_LED.shape[1] * 0.3)]

    LeftLED_11_20 = Left_LED[0:Left_LED.shape[0], int(Left_LED.shape[1] * 0.3):int(Left_LED.shape[1] * 0.55)]
    LeftLED11 = Left_LED[
                 int(0 + 0 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 0 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.3):int(Left_LED.shape[1] * 0.55)]
    LeftLED12 = Left_LED[
                 int(0 + 1 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 1 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.3):int(Left_LED.shape[1] * 0.55)]
    LeftLED13 = Left_LED[
                 int(0 + 2 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 2 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.3):int(Left_LED.shape[1] * 0.55)]
    LeftLED14 = Left_LED[
                 int(0 + 3 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 3 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.3):int(Left_LED.shape[1] * 0.55)]
    LeftLED15 = Left_LED[
                 int(0 + 4 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 4 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.3):int(Left_LED.shape[1] * 0.55)]
    LeftLED16 = Left_LED[
                 int(0 + 5 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 5 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.3):int(Left_LED.shape[1] * 0.55)]
    LeftLED17 = Left_LED[
                 int(0 + 6 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 6 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.3):int(Left_LED.shape[1] * 0.55)]
    LeftLED18 = Left_LED[
                 int(0 + 7 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 7 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.3):int(Left_LED.shape[1] * 0.55)]
    LeftLED19 = Left_LED[
                 int(0 + 8 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 8 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.3):int(Left_LED.shape[1] * 0.55)]
    LeftLED20 = Left_LED[
                 int(0 + 9 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 9 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.3):int(Left_LED.shape[1] * 0.55)]

    LeftLED_21_30 = Left_LED[0:Left_LED.shape[0], int(Left_LED.shape[1] * 0.55):int(Left_LED.shape[1] * 0.85)]
    LeftLED21 = Left_LED[
                 int(0 + 0 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 0 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.55):int(Left_LED.shape[1] * 0.85)]
    LeftLED22 = Left_LED[
                 int(0 + 1 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 1 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.55):int(Left_LED.shape[1] * 0.85)]
    LeftLED23 = Left_LED[
                 int(0 + 2 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 2 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.55):int(Left_LED.shape[1] * 0.85)]
    LeftLED24 = Left_LED[
                 int(0 + 3 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 3 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.55):int(Left_LED.shape[1] * 0.85)]
    LeftLED25 = Left_LED[
                 int(0 + 4 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 4 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.55):int(Left_LED.shape[1] * 0.85)]
    LeftLED26 = Left_LED[
                 int(0 + 5 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 5 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.55):int(Left_LED.shape[1] * 0.85)]
    LeftLED27 = Left_LED[
                 int(0 + 6 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 6 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.55):int(Left_LED.shape[1] * 0.85)]
    LeftLED28 = Left_LED[
                 int(0 + 7 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 7 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.55):int(Left_LED.shape[1] * 0.85)]
    LeftLED29 = Left_LED[
                 int(0 + 8 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 8 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.55):int(Left_LED.shape[1] * 0.85)]
    LeftLED30 = Left_LED[
                 int(0 + 9 * Left_LED.shape[0] / 10):int(Left_LED.shape[0] / 10 + 9 * Left_LED.shape[0] / 10),
                 int(Left_LED.shape[1] * 0.55):int(Left_LED.shape[1] * 0.85)]

    # cv2.imwrite(datapath + "TEST\\Left_LED_01_10_UUT (" + str(SN) + ").png", LeftLED_01_10)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_01_UUT (" + str(SN) + ").png", LeftLED1)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_02_UUT (" + str(SN) + ").png", LeftLED2)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_03_UUT (" + str(SN) + ").png", LeftLED3)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_04_UUT (" + str(SN) + ").png", LeftLED4)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_05_UUT (" + str(SN) + ").png", LeftLED5)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_06_UUT (" + str(SN) + ").png", LeftLED6)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_07_UUT (" + str(SN) + ").png", LeftLED7)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_08_UUT (" + str(SN) + ").png", LeftLED8)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_09_UUT (" + str(SN) + ").png", LeftLED9)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_10_UUT (" + str(SN) + ").png", LeftLED10)  # 使用 絕對座標切割參數 製作切割圖片
    # 
    # cv2.imwrite(datapath + "TEST\\Left_LED_11_20_UUT (" + str(SN) + ").png", LeftLED_11_20)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_11_UUT (" + str(SN) + ").png", LeftLED11)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_12_UUT (" + str(SN) + ").png", LeftLED12)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_13_UUT (" + str(SN) + ").png", LeftLED13)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_14_UUT (" + str(SN) + ").png", LeftLED14)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_15_UUT (" + str(SN) + ").png", LeftLED15)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_16_UUT (" + str(SN) + ").png", LeftLED16)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_17_UUT (" + str(SN) + ").png", LeftLED17)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_18_UUT (" + str(SN) + ").png", LeftLED18)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_19_UUT (" + str(SN) + ").png", LeftLED19)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_20_UUT (" + str(SN) + ").png", LeftLED20)  # 使用 絕對座標切割參數 製作切割圖片
    # 
    # cv2.imwrite(datapath + "TEST\\Left_LED_21_30_UUT (" + str(SN) + ").png", LeftLED_21_30)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_21_UUT (" + str(SN) + ").png", LeftLED21)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_22_UUT (" + str(SN) + ").png", LeftLED22)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_23_UUT (" + str(SN) + ").png", LeftLED23)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_24_UUT (" + str(SN) + ").png", LeftLED24)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_25_UUT (" + str(SN) + ").png", LeftLED25)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_26_UUT (" + str(SN) + ").png", LeftLED26)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_27_UUT (" + str(SN) + ").png", LeftLED27)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_28_UUT (" + str(SN) + ").png", LeftLED28)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_29_UUT (" + str(SN) + ").png", LeftLED29)  # 使用 絕對座標切割參數 製作切割圖片
    # cv2.imwrite(datapath + "TEST\\Left_LED_30_UUT (" + str(SN) + ").png", LeftLED30)  # 使用 絕對座標切割參數 製作切割圖片
    # 
    # Left_LED_01 = cv2.imread(datapath + "TEST\\Left_LED_01_UUT (" + str(SN) + ").png")
    # Left_LED_02 = cv2.imread(datapath + "TEST\\Left_LED_02_UUT (" + str(SN) + ").png")
    # Left_LED_03 = cv2.imread(datapath + "TEST\\Left_LED_03_UUT (" + str(SN) + ").png")
    # Left_LED_04 = cv2.imread(datapath + "TEST\\Left_LED_04_UUT (" + str(SN) + ").png")
    # Left_LED_05 = cv2.imread(datapath + "TEST\\Left_LED_05_UUT (" + str(SN) + ").png")
    # Left_LED_06 = cv2.imread(datapath + "TEST\\Left_LED_06_UUT (" + str(SN) + ").png")
    # Left_LED_07 = cv2.imread(datapath + "TEST\\Left_LED_07_UUT (" + str(SN) + ").png")
    # Left_LED_08 = cv2.imread(datapath + "TEST\\Left_LED_08_UUT (" + str(SN) + ").png")
    # Left_LED_09 = cv2.imread(datapath + "TEST\\Left_LED_09_UUT (" + str(SN) + ").png")
    # Left_LED_10 = cv2.imread(datapath + "TEST\\Left_LED_10_UUT (" + str(SN) + ").png")
    # Left_LED_11 = cv2.imread(datapath + "TEST\\Left_LED_11_UUT (" + str(SN) + ").png")
    # Left_LED_12 = cv2.imread(datapath + "TEST\\Left_LED_12_UUT (" + str(SN) + ").png")
    # Left_LED_13 = cv2.imread(datapath + "TEST\\Left_LED_13_UUT (" + str(SN) + ").png")
    # Left_LED_14 = cv2.imread(datapath + "TEST\\Left_LED_14_UUT (" + str(SN) + ").png")
    # Left_LED_15 = cv2.imread(datapath + "TEST\\Left_LED_15_UUT (" + str(SN) + ").png")
    # Left_LED_16 = cv2.imread(datapath + "TEST\\Left_LED_16_UUT (" + str(SN) + ").png")
    # Left_LED_17 = cv2.imread(datapath + "TEST\\Left_LED_17_UUT (" + str(SN) + ").png")
    # Left_LED_18 = cv2.imread(datapath + "TEST\\Left_LED_18_UUT (" + str(SN) + ").png")
    # Left_LED_19 = cv2.imread(datapath + "TEST\\Left_LED_19_UUT (" + str(SN) + ").png")
    # Left_LED_20 = cv2.imread(datapath + "TEST\\Left_LED_20_UUT (" + str(SN) + ").png")
    # Left_LED_21 = cv2.imread(datapath + "TEST\\Left_LED_21_UUT (" + str(SN) + ").png")
    # Left_LED_22 = cv2.imread(datapath + "TEST\\Left_LED_22_UUT (" + str(SN) + ").png")
    # Left_LED_23 = cv2.imread(datapath + "TEST\\Left_LED_23_UUT (" + str(SN) + ").png")
    # Left_LED_24 = cv2.imread(datapath + "TEST\\Left_LED_24_UUT (" + str(SN) + ").png")
    # Left_LED_25 = cv2.imread(datapath + "TEST\\Left_LED_25_UUT (" + str(SN) + ").png")
    # Left_LED_26 = cv2.imread(datapath + "TEST\\Left_LED_26_UUT (" + str(SN) + ").png")
    # Left_LED_27 = cv2.imread(datapath + "TEST\\Left_LED_27_UUT (" + str(SN) + ").png")
    # Left_LED_28 = cv2.imread(datapath + "TEST\\Left_LED_28_UUT (" + str(SN) + ").png")
    # Left_LED_29 = cv2.imread(datapath + "TEST\\Left_LED_29_UUT (" + str(SN) + ").png")
    # Left_LED_30 = cv2.imread(datapath + "TEST\\Left_LED_30_UUT (" + str(SN) + ").png")

    Left_LED_01 = LeftLED1
    Left_LED_02 = LeftLED2
    Left_LED_03 = LeftLED3
    Left_LED_04 = LeftLED4
    Left_LED_05 = LeftLED5
    Left_LED_06 = LeftLED6
    Left_LED_07 = LeftLED7
    Left_LED_08 = LeftLED8
    Left_LED_09 = LeftLED9
    Left_LED_10 = LeftLED10
    Left_LED_11 = LeftLED11
    Left_LED_12 = LeftLED12
    Left_LED_13 = LeftLED13
    Left_LED_14 = LeftLED14
    Left_LED_15 = LeftLED15
    Left_LED_16 = LeftLED16
    Left_LED_17 = LeftLED17
    Left_LED_18 = LeftLED18
    Left_LED_19 = LeftLED19
    Left_LED_20 = LeftLED20
    Left_LED_21 = LeftLED21
    Left_LED_22 = LeftLED22
    Left_LED_23 = LeftLED23
    Left_LED_24 = LeftLED24
    Left_LED_25 = LeftLED25
    Left_LED_26 = LeftLED26
    Left_LED_27 = LeftLED27
    Left_LED_28 = LeftLED28
    Left_LED_29 = LeftLED29
    Left_LED_30 = LeftLED30
    
    try:
        for j in range(134):
            for j1 in range(160):
                for j3 in range(3):
                    if Left_LED_01[j][j1][j3] > CHeck255Stander: Left_LED_01_Check255 += 1
                    if Left_LED_02[j][j1][j3] > CHeck255Stander: Left_LED_02_Check255 += 1
                    if Left_LED_03[j][j1][j3] > CHeck255Stander: Left_LED_03_Check255 += 1
                    if Left_LED_04[j][j1][j3] > CHeck255Stander: Left_LED_04_Check255 += 1
                    if Left_LED_05[j][j1][j3] > CHeck255Stander: Left_LED_05_Check255 += 1
                    if Left_LED_06[j][j1][j3] > CHeck255Stander: Left_LED_06_Check255 += 1
                    if Left_LED_07[j][j1][j3] > CHeck255Stander: Left_LED_07_Check255 += 1
                    if Left_LED_08[j][j1][j3] > CHeck255Stander: Left_LED_08_Check255 += 1
                    if Left_LED_09[j][j1][j3] > CHeck255Stander: Left_LED_09_Check255 += 1
                    if Left_LED_10[j][j1][j3] > CHeck255Stander: Left_LED_10_Check255 += 1
                    if Left_LED_11[j][j1][j3] > CHeck255Stander: Left_LED_11_Check255 += 1
                    if Left_LED_12[j][j1][j3] > CHeck255Stander: Left_LED_12_Check255 += 1
                    if Left_LED_13[j][j1][j3] > CHeck255Stander: Left_LED_13_Check255 += 1
                    if Left_LED_14[j][j1][j3] > CHeck255Stander: Left_LED_14_Check255 += 1
                    if Left_LED_15[j][j1][j3] > CHeck255Stander: Left_LED_15_Check255 += 1
                    if Left_LED_16[j][j1][j3] > CHeck255Stander: Left_LED_16_Check255 += 1
                    if Left_LED_17[j][j1][j3] > CHeck255Stander: Left_LED_17_Check255 += 1
                    if Left_LED_18[j][j1][j3] > CHeck255Stander: Left_LED_18_Check255 += 1
                    if Left_LED_19[j][j1][j3] > CHeck255Stander: Left_LED_19_Check255 += 1
                    if Left_LED_20[j][j1][j3] > CHeck255Stander: Left_LED_20_Check255 += 1
                    if Left_LED_21[j][j1][j3] > CHeck255Stander: Left_LED_21_Check255 += 1
                    if Left_LED_22[j][j1][j3] > CHeck255Stander: Left_LED_22_Check255 += 1
                    if Left_LED_23[j][j1][j3] > CHeck255Stander: Left_LED_23_Check255 += 1
                    if Left_LED_24[j][j1][j3] > CHeck255Stander: Left_LED_24_Check255 += 1
                    if Left_LED_25[j][j1][j3] > CHeck255Stander: Left_LED_25_Check255 += 1
                    if Left_LED_26[j][j1][j3] > CHeck255Stander: Left_LED_26_Check255 += 1
                    if Left_LED_27[j][j1][j3] > CHeck255Stander: Left_LED_27_Check255 += 1
                    if Left_LED_28[j][j1][j3] > CHeck255Stander: Left_LED_28_Check255 += 1
                    if Left_LED_29[j][j1][j3] > CHeck255Stander: Left_LED_29_Check255 += 1
                    if Left_LED_30[j][j1][j3] > CHeck255Stander: Left_LED_30_Check255 += 1
    except:
        Donothing = 1
    PassNum = 0
    if Left_LED_01_Check255 > PassNum and Left_LED_02_Check255 > PassNum and Left_LED_04_Check255 > PassNum and Left_LED_05_Check255 > PassNum and Left_LED_06_Check255 > PassNum and Left_LED_07_Check255 > PassNum and Left_LED_08_Check255 > PassNum and Left_LED_09_Check255 > PassNum and Left_LED_10_Check255 > PassNum and Left_LED_11_Check255 > PassNum and Left_LED_12_Check255 > PassNum and Left_LED_13_Check255 > PassNum and Left_LED_14_Check255 > PassNum and Left_LED_15_Check255 > PassNum and Left_LED_16_Check255 > PassNum and Left_LED_17_Check255 > PassNum and Left_LED_18_Check255 > PassNum and Left_LED_19_Check255 > PassNum and Left_LED_20_Check255 > PassNum and Left_LED_21_Check255 > PassNum and Left_LED_22_Check255 > PassNum and Left_LED_23_Check255 > PassNum and Left_LED_26_Check255 > PassNum and Left_LED_27_Check255 > PassNum and Left_LED_28_Check255 > PassNum and Left_LED_30_Check255 > PassNum:
        PASS = 1
    else:
        print(Left_LED_01_Check255, Left_LED_02_Check255, Left_LED_04_Check255, Left_LED_05_Check255,
              Left_LED_06_Check255, Left_LED_07_Check255, Left_LED_08_Check255, Left_LED_09_Check255,
              Left_LED_10_Check255, Left_LED_11_Check255, Left_LED_12_Check255, Left_LED_13_Check255,
              Left_LED_14_Check255, Left_LED_15_Check255, Left_LED_16_Check255, Left_LED_17_Check255,
              Left_LED_18_Check255, Left_LED_19_Check255, Left_LED_20_Check255, Left_LED_21_Check255,
              Left_LED_22_Check255, Left_LED_23_Check255, Left_LED_26_Check255, Left_LED_27_Check255,
              Left_LED_28_Check255, Left_LED_30_Check255)

        FAIL = 1
    return PASS, FAIL