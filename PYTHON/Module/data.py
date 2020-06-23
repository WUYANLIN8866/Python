import cv2
import numpy as np
import dlib
import os
import logging
logging.basicConfig(level=logging.WARNING, format='%(message)s')  #  %(asctime)s - %(name)s - %(levelname)s -
logger = logging.getLogger()
detector = dlib.get_frontal_face_detector()


def video_to_image(input_folder, output_image_folder):
    items = os.listdir(input_folder)  # 取得指定目錄中所有的檔案與子目錄名稱取得指定目錄中所有的檔案與子目錄名稱
    for i in range(len(items)):
        items[i] = '{0}\\{1}'.format(input_folder, items[i])
    while len(items) > 0:
        item = items.pop(0)
        if os.path.isdir(item):
            sub_items = os.listdir(item)  # 取得指定目錄中所有的檔案與子目錄名稱取得指定目錄中所有的檔案與子目錄名稱
            for i in range(len(sub_items)): items.append('{0}\\{1}'.format(item, sub_items[i]))
        elif os.path.isfile(item):
            logger.warning("file: %s ", item)
            new_folder = item[:item.rfind('\\')].replace(input_folder, output_image_folder)
            filename_face = item[item.rfind('\\') + 1:item.rfind('.avi')]
            if not os.path.exists(new_folder): os.makedirs(new_folder)
            cap = cv2.VideoCapture(item)
            frame_no = 1
            while cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    face_rects, scores, idx = detector.run(frame, 0)  # 取出所有偵測的結果
                    for i, d in enumerate(face_rects):
                        crop_img = frame[d.top():d.bottom(), d.left():d.right()]
                        cv2.imwrite('{0}\\{1}_{2:0>1d}.png'.format(new_folder, filename_face, frame_no), crop_img)
                else:
                    break
                frame_no = frame_no + 1
    return 0


def face_alignment(input_folder, align):
    sp = dlib.shape_predictor(align)
    items = os.listdir(input_folder)
    for i in range(1,len(items)+1):
        for (root, dirs, files) in os.walk(input_folder+"\\"+str(i)):
            for f in files:
                path = os.path.join(root, f)
                Q = cv2.imread(path)
                if Q is None:break
                dets = detector(cv2.cvtColor(Q, cv2.COLOR_BGR2RGB), 1)
                faces = dlib.full_object_detections()
                for det in dets:
                    faces.append(sp(cv2.cvtColor(Q, cv2.COLOR_BGR2RGB), det))
                    images = dlib.get_face_chips(cv2.cvtColor(Q, cv2.COLOR_BGR2RGB), faces, size=300)
                    for image in images:
                        cv_bgr_image = cv2.cvtColor(np.array(image).astype(np.uint8), cv2.COLOR_RGB2BGR)
                        cv2.imwrite(input_folder+"\\"+str(i)+"\\"+ str(f),cv_bgr_image)
        if i > len(items)+1:break
    return 0


def screen_shot(folder):
    A = 1;j=40
    while (A < 31):
        A1 = 1
        while (A1 < 13):
            A2 = 1
            while(A2<A2+1):
                cap = cv2.imread(folder+"\\" + str(A) + "\\" + str(A1) + "_" + str(A2) + ".png")
                if cap is None: break
                face_rects, scores, idx = detector.run(cap, 0)
                for i, d in enumerate(face_rects):
                    crop_img = cap[d.top() + j:d.bottom() - j, d.left() + j:d.right() - j]
                    res = cv2.resize(crop_img, (320, 320), interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(folder+"\\" + str(A) + "\\" + str(A1) + "_" + str(A2) + ".png", res)

                A2 += 1
            A1 += 1
        A += 1
    return 0