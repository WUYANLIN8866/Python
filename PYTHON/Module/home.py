import data
data.video_to_image("D:\\PROGRAM\\CBSR_database\\test_release\\test_release", "D:\\PROGRAM\\python photo\\alignment")
data.face_alignment("D:\\PROGRAM\\python photo\\alignment", "C:\\dlib\\dlib-master\\python_examples\\shape_predictor_68_face_landmarks.dat")
data.screen_shot("D:\\PROGRAM\\python photo\\alignment")
exit()
#input1f = "D:\\PROGRAM\\CBSR_database\\test_release\\test_release"    # 輸入的資料夾
#output = "D:\\PROGRAM\\python photo\\alignment"  # 儲存資料夾
#align = "C:\\dlib\\dlib-master\\python_examples\\shape_predictor_68_face_landmarks.dat"  # 對齊檔