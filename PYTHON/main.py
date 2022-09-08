import cv2
import mediapipe as mp
import math

mp_face_detection1 = mp.solutions.face_detection
mp_drawing1 = mp.solutions.drawing_utils
mp_drawing2 = mp_drawing1
mp_drawing_styles2 = mp.solutions.drawing_styles
mp_face_mesh2 = mp.solutions.face_mesh
drawing_spec2 = mp_drawing2.DrawingSpec(thickness=1, circle_radius=1)
mp_drawing_hand = mp.solutions.drawing_utils
mp_drawing_styles_hand = mp.solutions.drawing_styles
mp_hands_hand = mp.solutions.hands

# 根據兩點的座標，計算角度
def vector_2d_angle(v1, v2):
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_= math.degrees(math.acos((v1_x*v2_x+v1_y*v2_y)/(((v1_x**2+v1_y**2)**0.5)*((v2_x**2+v2_y**2)**0.5))))
    except:
        angle_ = 180
    return angle_

# 根據傳入的 21 個節點座標，得到該手指的角度
def hand_angle(hand_):
    angle_list = []
    # thumb 大拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[2][0])),(int(hand_[0][1])-int(hand_[2][1]))),
        ((int(hand_[3][0])- int(hand_[4][0])),(int(hand_[3][1])- int(hand_[4][1])))
        )
    angle_list.append(angle_)
    # index 食指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])-int(hand_[6][0])),(int(hand_[0][1])- int(hand_[6][1]))),
        ((int(hand_[7][0])- int(hand_[8][0])),(int(hand_[7][1])- int(hand_[8][1])))
        )
    angle_list.append(angle_)
    # middle 中指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[10][0])),(int(hand_[0][1])- int(hand_[10][1]))),
        ((int(hand_[11][0])- int(hand_[12][0])),(int(hand_[11][1])- int(hand_[12][1])))
        )
    angle_list.append(angle_)
    # ring 無名指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[14][0])),(int(hand_[0][1])- int(hand_[14][1]))),
        ((int(hand_[15][0])- int(hand_[16][0])),(int(hand_[15][1])- int(hand_[16][1])))
        )
    angle_list.append(angle_)
    # pink 小拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0])- int(hand_[18][0])),(int(hand_[0][1])- int(hand_[18][1]))),
        ((int(hand_[19][0])- int(hand_[20][0])),(int(hand_[19][1])- int(hand_[20][1])))
        )
    angle_list.append(angle_)
    return angle_list

# 根據手指角度的串列內容，返回對應的手勢名稱
def hand_pos(finger_angle):
    f1 = finger_angle[0]   # 大拇指角度
    f2 = finger_angle[1]   # 食指角度
    f3 = finger_angle[2]   # 中指角度
    f4 = finger_angle[3]   # 無名指角度
    f5 = finger_angle[4]   # 小拇指角度
    # 小於 50 表示手指伸直，大於等於 50 表示手指捲縮
    if f1<40 and f2>=40 and f3>=40 and f4>=40 and f5>=40:
        return 'Yes'
    elif f1>=50 and f2>=50 and f3<50 and f4>=50 and f5>=50:
        return 'Fxxk'
    elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5>=50:
        return '0'
    elif f1>=50 and f2>=50 and f3>=50 and f4>=50 and f5<50:
        return 'No'
    elif f1>=50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return '1'
    elif f1>=50 and f2<50 and f3<50 and f4>=50 and f5>=50:
        return '2'
    elif f1>=50 and f2>=50 and f3<50 and f4<50 and f5<50:
        return 'ok'
    elif f1>=50 and f2<50 and f3<50 and f4<50 and f5>50:
        return '3'
    elif f1>=50 and f2<50 and f3<50 and f4<50 and f5<50:
        return '4'
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5<50:
        return '5'
    elif f1<50 and f2>=50 and f3>=50 and f4>=50 and f5<50:
        return '6'
    elif f1<50 and f2<50 and f3>=50 and f4>=50 and f5>=50:
        return '7'
    elif f1<50 and f2<50 and f3<50 and f4>=50 and f5>=50:
        return '8'
    elif f1<50 and f2<50 and f3<50 and f4<50 and f5>=50:
        return '9'
    else:
        return ''

cap = cv2.VideoCapture(0)
fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 印出文字的字型
lineType = cv2.LINE_AA               # 印出文字的邊框

with mp_hands_hand.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    with mp_face_detection1.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        with mp_face_mesh2.FaceMesh(max_num_faces=10,refine_landmarks=True,min_detection_confidence=0.5,min_tracking_confidence=0.5) as face_mesh:
            if not cap.isOpened():
                print("Cannot open camera")
                exit()
            w, h = 1400, 700
            while True:
                ret, img = cap.read()
                if not ret:
                    print("Cannot receive frame")
                    break
                results = hands.process(img)  # 偵測手勢
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        finger_points = []  # 記錄手指節點座標的串列
                        for i in hand_landmarks.landmark:
                            # 將 21 個節點換算成座標，記錄到 finger_points
                            x = i.x*w
                            y = i.y*h
                            finger_points.append((x, y))
                        if finger_points:
                            finger_angle = hand_angle(finger_points)  # 計算手指角度，回傳長度為 5 的串列
                            print(finger_angle)  # 印出角度 ( 有需要就開啟註解 )
                            text = hand_pos(finger_angle)  # 取得手勢所回傳的內容
                            cv2.putText(img, text, (30, 120), fontFace, 3, (255, 255, 255), 10, lineType)  # 印出文字
                results_hand = hands.process(img)  # 偵測手掌
                if results_hand.multi_hand_landmarks:
                    for hand_landmarks in results_hand.multi_hand_landmarks:
                        mp_drawing_hand.draw_landmarks(img, hand_landmarks, mp_hands_hand.HAND_CONNECTIONS,mp_drawing_styles_hand.get_default_hand_landmarks_style(),mp_drawing_styles_hand.get_default_hand_connections_style())
                results1 = face_detection.process(img)
                if results1.detections:
                    for detection in results1.detections:
                        mp_drawing1.draw_detection(img, detection)
                results2 = face_mesh.process(img)
                if results2.multi_face_landmarks:
                    for face_landmarks in results2.multi_face_landmarks:
                        mp_drawing2.draw_landmarks(image=img,landmark_list=face_landmarks,connections=mp_face_mesh2.FACEMESH_TESSELATION,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles2.get_default_face_mesh_tesselation_style())
                        mp_drawing2.draw_landmarks(image=img,landmark_list=face_landmarks,connections=mp_face_mesh2.FACEMESH_CONTOURS,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles2.get_default_face_mesh_contours_style())
                        mp_drawing2.draw_landmarks(image=img,landmark_list=face_landmarks,connections=mp_face_mesh2.FACEMESH_IRISES,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles2.get_default_face_mesh_iris_connections_style())
                cv2.imshow('Mediapipe', img)
                if cv2.waitKey(1) == ord('z'):
                    break    # 按下 z 鍵停止
cap.release()
cv2.destroyAllWindows()