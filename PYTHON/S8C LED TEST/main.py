from tkinter import *
from PIL import Image
from functools import partial
from time import sleep
import xml.etree.ElementTree as XET,StartLedTest,cv2,os
class loadinfsplash:
    def __init__(self):
        def loadinganimate():
            for i in range(2):
                for j in range(11):
                    Label(self.root2, bg="#fff2cc", width=2, height=1).place(x=(j + 2) * 22, y=70)
                    sleep(0.1)
                    self.root2.update_idletasks()
                    Label(self.root2, bg="#f6b26b", width=2, height=1).place(x=(j + 2) * 22, y=70)
                if i == 2 :
                    break
            else:
                self.root2.destroy()


        self.root2 = Tk()
        self.root2.configure(bg="#eeeeee")
        self.root2.overrideredirect(True)
        self.root2.title("Testing")
        self.root2.geometry("320x120+565+300")
        Label(self.root2, text="Testing . . .", font="Bahnschrift 15").place(x=120, y=20)
        for i in range(11):
            Label(self.root2, bg="#f6b26b", width=2, height=1).place(x=(i + 2) * 22, y=70)

        self.root2.update()
        loadinganimate()
class Start:
    def __init__(self):
        def loadinganimate():
            for i in range(3):
                for j in range(11):
                    Label(self.root2, bg="#fff2cc", width=2, height=1).place(x=(j + 2) * 22, y=70)
                    sleep(0.1)
                    self.root2.update_idletasks()
                    Label(self.root2, bg="#f6b26b", width=2, height=1).place(x=(j + 2) * 22, y=70)
                if i == 3:
                    break
            else:
                self.root2.destroy()


        self.root2 = Tk()
        self.root2.configure(bg="#eeeeee")
        self.root2.overrideredirect(True)
        self.root2.title("S8C Led test")
        self.root2.geometry("320x120+565+300")
        Label(self.root2, text="Initialization . . .", font="Bahnschrift 15").place(x=100, y=20)
        for i in range(11):
            Label(self.root2, bg="#f6b26b", width=2, height=1).place(x=(i + 2) * 22, y=70)

        self.root2.update()
        loadinganimate()
try:
    xmlpath = "D:\\Pycharm\\S8C_led_test_v1\\info.xml"
    Start()
    root = Tk()
    root.resizable(False,False)
    XMLDATA = XET.parse(xmlpath)
    XMLDATA = XMLDATA.getroot()
    root.geometry(str(XMLDATA[3].text))
    root.title(str(XMLDATA[4].text))
except: None
def Initialization():
    global TESTING
    if not os.path.exists(str(XMLDATA[2].text+"TEST")):
        os.mkdir(str(XMLDATA[2].text+"TEST"))
    else:
        donothing = 1
    TESTING = [0, 0, 0, 0, 0, 0, 0, 0]
    mycanvas1 = Canvas(root, width=320, height=370)
    mycanvas1.place(x=2, y=20)
    mycanvas1.create_rectangle(2, 10, 318, 355, outline='black')
    mycanvas2 = Canvas(root, width=320, height=370)
    mycanvas2.place(x=322, y=20)
    mycanvas2.create_rectangle(2, 10, 318, 355, outline='black')
    mycanvas3 = Canvas(root, width=320, height=370)
    mycanvas3.place(x=642, y=20)
    mycanvas3.create_rectangle(2, 10, 318, 355, outline='black')
    mycanvas4 = Canvas(root, width=320, height=370)
    mycanvas4.place(x=960, y=20)
    mycanvas4.create_rectangle(2, 10, 318, 355, outline='black')
    mycanvas5 = Canvas(root, width=320, height=370)
    mycanvas5.place(x=2, y=380)
    mycanvas5.create_rectangle(2, 10, 318, 355, outline='black')
    mycanvas6 = Canvas(root, width=320, height=370)
    mycanvas6.place(x=322, y=380)
    mycanvas6.create_rectangle(2, 10, 318, 355, outline='black')
    mycanvas7 = Canvas(root, width=320, height=370)
    mycanvas7.place(x=642, y=380)
    mycanvas7.create_rectangle(2, 10, 318, 355, outline='black')
    mycanvas8 = Canvas(root, width=320, height=370)
    mycanvas8.place(x=960, y=380)
    mycanvas8.create_rectangle(2, 10, 318, 355, outline='black')
def fixture_1():
    global img1, img2, img3, img4, img5, img6, img7, img8, IMG1, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, TMP1, TMP2, TMP3, TMP4, TMP5, TMP6, TMP7, TMP8, FINDRUNNUM, TESTING
    global TestStatus1, TestStatus1btn1, TestStatus1btn2, Reviewlable1
    global TestStatus2, TestStatus2btn1, TestStatus2btn2, Reviewlable2
    global TestStatus3, TestStatus3btn1, TestStatus3btn2, Reviewlable3
    global TestStatus4, TestStatus4btn1, TestStatus4btn2, Reviewlable4
    global TestStatus5, TestStatus5btn1, TestStatus5btn2, Reviewlable5
    global TestStatus6, TestStatus6btn1, TestStatus6btn2, Reviewlable6
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus8, TestStatus8btn1, TestStatus8btn2, Reviewlable8
    SN1 = str(XMLDATA[5].text)
    Alreadypass = 0
    FixtureNumber1 = XMLDATA[0][0].get("fixturenumber")
    text1_sn = Label(root, text="SN : " + SN1)
    text1_sn.place(x=10, y=270)
    # FixtureNumber
    FixtureNumber1 = "FixtureNumber : " + str(FixtureNumber1)
    text1_fix = Label(root, text=FixtureNumber1)
    text1_fix.place(x=10, y=290)
    # Test Status
    TestStatus1result = ""
    if TestStatus1result != "PASS" and TestStatus1result != "FAIL":
        TestStatus1result = str(XMLDATA[5].text)
    TestStatus1 = "Test Status : " + str(TestStatus1result)
    TestStatus1 = Label(root, text=TestStatus1)
    TestStatus1.place(x=10, y=310)
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][0].get("fixturenumber")) + ".run"):
        loadinfsplash()

        TESTING[0] = 1
        FINDRUNNUM[0] = 1
        print("SN1 Get")
        with open(str(XMLDATA[2].text) + str(XMLDATA[0][0].get("fixturenumber")) + ".run", 'r') as file:
            SN1 = file.readlines()[0]
        Fixture1Photo = str(XMLDATA[2].text) + str(SN1) + ".png"
        Fixture1Photo_copy = cv2.imread(str(XMLDATA[2].text) + str(SN1) + ".png")
        Fixture1Photo_copy = cv2.imwrite(str(XMLDATA[2].text) + "TEST\\" + str(SN1) + "_copy.png", Fixture1Photo_copy)
        Fixture1Photo_copy = str(XMLDATA[2].text) + "TEST\\" + str(SN1) + "_copy.png"
        img1 = Image.open(Fixture1Photo_copy)
        try:
            img1 = img1.resize((300, 224), Image.ANTIALIAS)
            img1.save(Fixture1Photo_copy, "png")
        except:
            donothing = 1
        img1 = PhotoImage(file=Fixture1Photo_copy)
        IMG1 = Label(root, image=img1)
        IMG1.place(x=10, y=40)
    else:
        try:
            IMG1.destroy()
        except:
            donothing = 1
    if TESTING[0] == 1:
        if Alreadypass == 0:
            CheckUpSevenSegmentDisplayNumber = StartLedTest.CheckUpSevenSegmentDisplayNumber(str(XMLDATA[1].text), SN1, xmlpath)
            if CheckUpSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestRightLed(str(XMLDATA[1].text), SN1, 0, 0)[0]
                if PASS == 1:
                    TestStatus1result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus1result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            CheckDownSevenSegmentDisplayNumber = StartLedTest.CheckDownSevenSegmentDisplayNumber(str(XMLDATA[1].text),
                                                                                                 SN1, xmlpath)
            if CheckDownSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestLeftLed(str(XMLDATA[1].text), SN1, 0, 0)[0]
                if PASS == 1:
                    TestStatus1result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus1result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            TestStatus1result = "FAIL"
    if TestStatus1result != "PASS" and TestStatus1result != "FAIL":
        TestStatus1result = str(XMLDATA[5].text)
    if TestStatus1result == "FAIL":
        Reviewlable1 = Label(root, text=str(XMLDATA[6].text), fg="RED", font=3)
        Reviewlable1.place(x=10, y=330)
        TestStatus1btn1 = Button(root, text="PASS", command=partial(SN1reviewPASS, SN1), font=3, fg="Green")
        TestStatus1btn1.place(x=210, y=270, width=100, height=50)
        TestStatus1btn2 = Button(root, text="FAIL", command=partial(SN1reviewFAIL, SN1), font=3, fg="RED")
        TestStatus1btn2.place(x=210, y=320, width=100, height=50)
    elif TestStatus1result == "PASS":
        TMP1 = open(str(XMLDATA[2].text) + str(XMLDATA[0][0].get("fixturenumber")) + ".tmp", 'w')
        TMP1.write("SN:" + SN1 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][0].get("fixturenumber")))
        TMP1.close()
        TESTING[0] = 0
        try:
            os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][0].get("fixturenumber")) + ".run")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN1) + "_copy.png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN1) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN1) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN1) + ".png")
        except:
            donothing = 1
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][0].get("fixturenumber")) + ".tmp"):
        FINDRUNNUM[0] = 0
        img1 = PhotoImage(file="")
        IMG1 = Label(root, image=img1)
        IMG1.place(x=10, y=40)
def SN1reviewPASS(SN1):
    TMP1 = open(str(XMLDATA[2].text) + str(XMLDATA[0][0].get("fixturenumber")) + ".tmp", 'w')
    TMP1.write("SN:" + SN1 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][0].get("fixturenumber")))
    TMP1.close()
    TestStatus1.config(text="Test Status : PASS")
    TestStatus1btn1.place_forget()
    TestStatus1btn2.place_forget()
    Reviewlable1.place_forget()
    TESTING[0] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][0].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN1) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN1) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN1) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN1) + ".png")
    except:
        donothing = 1
def SN1reviewFAIL(SN1):
    TMP1 = open(str(XMLDATA[2].text) + str(XMLDATA[0][0].get("fixturenumber")) + ".tmp", 'w')
    TMP1.write("SN:" + SN1 + "\nRESULT:FAIL\nFixtureID:" + str(XMLDATA[0][0].get("fixturenumber")))
    TMP1.close()
    TestStatus1.config(text="Test Status : FAIL")
    TestStatus1btn1.place_forget()
    TestStatus1btn2.place_forget()
    Reviewlable1.place_forget()
    TESTING[0] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][0].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN1) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN1) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN1) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN1) + ".png")
    except:
        donothing = 1
def fixture_2():
    global img1, img2, img3, img4, img5, img6, img7, img8, IMG1, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, TMP1, TMP2, TMP3, TMP4, TMP5, TMP6, TMP7, TMP8, FINDRUNNUM
    global TestStatus1, TestStatus1btn1, TestStatus1btn2, Reviewlable1
    global TestStatus2, TestStatus2btn1, TestStatus2btn2, Reviewlable2
    global TestStatus3, TestStatus3btn1, TestStatus3btn2, Reviewlable3
    global TestStatus4, TestStatus4btn1, TestStatus4btn2, Reviewlable4
    global TestStatus5, TestStatus5btn1, TestStatus5btn2, Reviewlable5
    global TestStatus6, TestStatus6btn1, TestStatus6btn2, Reviewlable6
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus8, TestStatus8btn1, TestStatus8btn2, Reviewlable8
    SN2 = str(XMLDATA[5].text)
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][1].get("fixturenumber")) + ".run"):
        loadinfsplash()
        FINDRUNNUM[1] = 1
        TESTING[1] = 1
        print("SN2 Get")
        with open(str(XMLDATA[2].text) + str(XMLDATA[0][1].get("fixturenumber")) + ".run", 'r') as file:
            SN2 = file.readlines()[0]
    Alreadypass = 0
    FixtureNumber2 = XMLDATA[0][1].get("fixturenumber")
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][1].get("fixturenumber")) + ".run"):
        Fixture2Photo = str(XMLDATA[2].text) + str(SN2) + ".png"
        Fixture2Photo_copy = cv2.imread(str(XMLDATA[2].text) + str(SN2) + ".png")
        Fixture2Photo_copy = cv2.imwrite(str(XMLDATA[2].text) + "TEST\\" + str(SN2) + "_copy.png", Fixture2Photo_copy)
        Fixture2Photo_copy = str(XMLDATA[2].text) + "TEST\\" + str(SN2) + "_copy.png"
        img2 = Image.open(Fixture2Photo_copy)
        try:
            img2 = img2.resize((300, 224), Image.ANTIALIAS)
            img2.save(Fixture2Photo_copy, "png")
        except:
            donothing = 2
        img2 = PhotoImage(file=Fixture2Photo_copy)
        IMG2 = Label(root, image=img2)
        IMG2.place(x=10 + 320 * 1, y=40)
    else:
        try:
            IMG2.destroy()
        except:
            donothing = 2
    text2_sn = Label(root, text="SN : " + SN2)
    text2_sn.place(x=10 + 320 * 1, y=270)
    # FixtureNumber
    FixtureNumber2 = "FixtureNumber : " + str(FixtureNumber2)
    text2_fix = Label(root, text=FixtureNumber2)
    text2_fix.place(x=10 + 320 * 1, y=290)
    # Test Status
    TestStatus2result = ""
    if TESTING[1] == 1:
        if Alreadypass == 0:
            CheckUpSevenSegmentDisplayNumber = StartLedTest.CheckUpSevenSegmentDisplayNumber(str(XMLDATA[1].text), SN2, xmlpath)
            if CheckUpSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestRightLed(str(XMLDATA[1].text), SN2, 0, 0)[0]
                if PASS == 1:
                    TestStatus2result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus2result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            CheckDownSevenSegmentDisplayNumber = StartLedTest.CheckDownSevenSegmentDisplayNumber(str(XMLDATA[1].text),
                                                                                                 SN2, xmlpath)
            if CheckDownSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestLeftLed(str(XMLDATA[1].text), SN2, 0, 0)[0]
                if PASS == 1:
                    TestStatus2result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus2result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            TestStatus2result = "FAIL"
    if TestStatus2result != "PASS" and TestStatus2result != "FAIL":
        TestStatus2result = str(XMLDATA[5].text)
    TestStatus2 = "Test Status : " + str(TestStatus2result)
    TestStatus2 = Label(root, text=TestStatus2)
    TestStatus2.place(x=10 + 320 * 1, y=310)
    if TestStatus2result == "FAIL":
        Reviewlable2 = Label(root, text=str(XMLDATA[6].text), fg="RED", font=3)
        Reviewlable2.place(x=10 + 320 * 1, y=330)
        TestStatus2btn1 = Button(root, text="PASS", command=partial(SN2reviewPASS, SN2), font=3, fg="Green")
        TestStatus2btn1.place(x=210 + 320 * 1, y=270, width=100, height=50)
        TestStatus2btn2 = Button(root, text="FAIL", command=partial(SN2reviewFAIL, SN2), font=3, fg="RED")
        TestStatus2btn2.place(x=210 + 320 * 1, y=320, width=100, height=50)
    elif TestStatus2result == "PASS":
        TMP2 = open(str(XMLDATA[2].text) + str(XMLDATA[0][1].get("fixturenumber")) + ".tmp", 'w')
        TMP2.write("SN:" + SN2 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][1].get("fixturenumber")))
        TMP2.close()
        FINDRUNNUM[1] = 0
        try:
            os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][1].get("fixturenumber")) + ".run")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN2) + "_copy.png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN2) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN2) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN2) + ".png")
        except:
            donothing = 1
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][1].get("fixturenumber")) + ".tmp"):
        FINDRUNNUM[1] = 0
        img2 = PhotoImage(file="")
        IMG2 = Label(root, image=img2)
        IMG2.place(x=10 + 320 * 1, y=40)
def SN2reviewPASS(SN2):
    TMP2 = open(str(XMLDATA[2].text) + str(XMLDATA[0][1].get("fixturenumber")) + ".tmp", 'w')
    TMP2.write("SN:" + SN2 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][1].get("fixturenumber")))
    TMP2.close()
    TestStatus2.config(text="Test Status : PASS")
    TestStatus2btn1.place_forget()
    TestStatus2btn2.place_forget()
    Reviewlable2.place_forget()
    TESTING[1] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][1].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN2) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN2) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN2) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN2) + ".png")
    except:
        donothing = 1
def SN2reviewFAIL(SN2):

    TMP2 = open(str(XMLDATA[2].text) + str(XMLDATA[0][1].get("fixturenumber")) + ".tmp", 'w')
    TMP2.write("SN:" + SN2 + "\nRESULT:FAIL\nFixtureID:" + str(XMLDATA[0][1].get("fixturenumber")))
    TMP2.close()
    TestStatus2.config(text="Test Status : FAIL")
    TestStatus2btn1.place_forget()
    TestStatus2btn2.place_forget()
    Reviewlable2.place_forget()
    TESTING[1] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][1].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN2) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN2) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN2) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN2) + ".png")
    except:
        donothing = 1
def fixture_3():
    global img1, img2, img3, img4, img5, img6, img7, img8, IMG1, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, TMP1, TMP2, TMP3, TMP4, TMP5, TMP6, TMP7, TMP8, FINDRUNNUM
    global TestStatus1, TestStatus1btn1, TestStatus1btn2, Reviewlable1
    global TestStatus2, TestStatus2btn1, TestStatus2btn2, Reviewlable2
    global TestStatus3, TestStatus3btn1, TestStatus3btn2, Reviewlable3
    global TestStatus4, TestStatus4btn1, TestStatus4btn2, Reviewlable4
    global TestStatus5, TestStatus5btn1, TestStatus5btn2, Reviewlable5
    global TestStatus6, TestStatus6btn1, TestStatus6btn2, Reviewlable6
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus8, TestStatus8btn1, TestStatus8btn2, Reviewlable8
    SN3 = str(XMLDATA[5].text)
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][2].get("fixturenumber")) + ".run"):
        loadinfsplash()
        FINDRUNNUM[2] = 1
        TESTING[2] = 1
        print("SN3 Get")
        with open(str(XMLDATA[2].text) + str(XMLDATA[0][2].get("fixturenumber")) + ".run", 'r') as file:
            SN3 = file.readlines()[0]
    Alreadypass = 0
    FixtureNumber3 = XMLDATA[0][2].get("fixturenumber")
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][2].get("fixturenumber")) + ".run"):
        Fixture3Photo = str(XMLDATA[2].text) + str(SN3) + ".png"
        Fixture3Photo_copy = cv2.imread(str(XMLDATA[2].text) + str(SN3) + ".png")
        Fixture3Photo_copy = cv2.imwrite(str(XMLDATA[2].text) + "TEST\\" + str(SN3) + "_copy.png", Fixture3Photo_copy)
        Fixture3Photo_copy = str(XMLDATA[2].text) + "TEST\\" + str(SN3) + "_copy.png"
        img3 = Image.open(Fixture3Photo_copy)
        try:
            img3 = img3.resize((300, 224), Image.ANTIALIAS)
            img3.save(Fixture3Photo_copy, "png")
        except:
            donothing = 3
        img3 = PhotoImage(file=Fixture3Photo_copy)
        IMG3 = Label(root, image=img3)
        IMG3.place(x=10 + 320 * 2, y=40)
    else:
        try:
            IMG3.destroy()
        except:
            donothing = 3
    text3_sn = Label(root, text="SN : " + SN3)
    text3_sn.place(x=10 + 320 * 2, y=270)
    # FixtureNumber
    FixtureNumber3 = "FixtureNumber : " + str(FixtureNumber3)
    text3_fix = Label(root, text=FixtureNumber3)
    text3_fix.place(x=10 + 320 * 2, y=290)
    # Test Status
    TestStatus3result = ""
    if TESTING[2] == 1:
        if Alreadypass == 0:
            CheckUpSevenSegmentDisplayNumber = StartLedTest.CheckUpSevenSegmentDisplayNumber(str(XMLDATA[1].text), SN3, xmlpath)
            if CheckUpSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestRightLed(str(XMLDATA[1].text), SN3, 0, 0)[0]
                if PASS == 1:
                    TestStatus3result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus3result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            CheckDownSevenSegmentDisplayNumber = StartLedTest.CheckDownSevenSegmentDisplayNumber(str(XMLDATA[1].text),
                                                                                                 SN3, xmlpath)
            if CheckDownSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestLeftLed(str(XMLDATA[1].text), SN3, 0, 0)[0]
                if PASS == 1:
                    TestStatus3result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus3result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            TestStatus3result = "FAIL"
    if TestStatus3result != "PASS" and TestStatus3result != "FAIL":
        TestStatus3result = str(XMLDATA[5].text)
    TestStatus3 = "Test Status : " + str(TestStatus3result)

    TestStatus3 = Label(root, text=TestStatus3)
    TestStatus3.place(x=10 + 320 * 2, y=310)
    if TestStatus3result == "FAIL":
        FINDRUNNUM[2] = 1
        Reviewlable3 = Label(root, text=str(XMLDATA[6].text), fg="RED", font=3)
        Reviewlable3.place(x=10 + 320 * 2, y=330)
        TestStatus3btn1 = Button(root, text="PASS", command=partial(SN3reviewPASS, SN3), font=3, fg="Green")
        TestStatus3btn1.place(x=210 + 320 * 2, y=270, width=100, height=50)
        TestStatus3btn2 = Button(root, text="FAIL", command=partial(SN3reviewFAIL, SN3), font=3, fg="RED")
        TestStatus3btn2.place(x=210 + 320 * 2, y=320, width=100, height=50)
    elif TestStatus3result == "PASS":
        TMP3 = open(str(XMLDATA[2].text) + str(XMLDATA[0][2].get("fixturenumber")) + ".tmp", 'w')
        TMP3.write("SN:" + SN3 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][2].get("fixturenumber")))
        TMP3.close()
        FINDRUNNUM[2] = 0
        try:
            os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][2].get("fixturenumber")) + ".run")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN3) + "_copy.png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN3) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN3) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN3) + ".png")
        except:
            donothing = 1
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][2].get("fixturenumber")) + ".tmp"):
        FINDRUNNUM[2] = 0
        img3 = PhotoImage(file="")
        IMG3 = Label(root, image=img3)
        IMG3.place(x=10 + 320 * 2, y=40)
def SN3reviewPASS(SN3):

    TMP3 = open(str(XMLDATA[2].text) + str(XMLDATA[0][2].get("fixturenumber")) + ".tmp", 'w')
    TMP3.write("SN:" + SN3 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][2].get("fixturenumber")))
    TMP3.close()
    TestStatus3.config(text="Test Status : PASS")
    TestStatus3btn1.place_forget()
    TestStatus3btn2.place_forget()
    Reviewlable3.place_forget()
    TESTING[2] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][2].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN3) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN3) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN3) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN3) + ".png")
    except:
        donothing = 1
def SN3reviewFAIL(SN3):

    TMP3 = open(str(XMLDATA[2].text) + str(XMLDATA[0][2].get("fixturenumber")) + ".tmp", 'w')
    TMP3.write("SN:" + SN3 + "\nRESULT:FAIL\nFixtureID:" + str(XMLDATA[0][2].get("fixturenumber")))
    TMP3.close()
    TestStatus3.config(text="Test Status : FAIL")
    TestStatus3btn1.place_forget()
    TestStatus3btn2.place_forget()
    Reviewlable3.place_forget()
    TESTING[2] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][2].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN3) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN3) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN3) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN3) + ".png")
    except:
        donothing = 1
def fixture_4():
    global img1, img2, img3, img4, img5, img6, img7, img8, IMG1, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, TMP1, TMP2, TMP3, TMP4, TMP5, TMP6, TMP7, TMP8, FINDRUNNUM
    global TestStatus1, TestStatus1btn1, TestStatus1btn2, Reviewlable1
    global TestStatus2, TestStatus2btn1, TestStatus2btn2, Reviewlable2
    global TestStatus3, TestStatus3btn1, TestStatus3btn2, Reviewlable3
    global TestStatus4, TestStatus4btn1, TestStatus4btn2, Reviewlable4
    global TestStatus5, TestStatus5btn1, TestStatus5btn2, Reviewlable5
    global TestStatus6, TestStatus6btn1, TestStatus6btn2, Reviewlable6
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus8, TestStatus8btn1, TestStatus8btn2, Reviewlable8
    SN4 = str(XMLDATA[5].text)
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][3].get("fixturenumber")) + ".run"):
        loadinfsplash()
        FINDRUNNUM[3] = 1
        TESTING[3] = 1
        print("SN4 Get")
        with open(str(XMLDATA[2].text) + str(XMLDATA[0][3].get("fixturenumber")) + ".run", 'r') as file:
            SN4 = file.readlines()[0]
    Alreadypass = 0
    FixtureNumber4 = XMLDATA[0][3].get("fixturenumber")
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][3].get("fixturenumber")) + ".run"):
        Fixture4Photo = str(XMLDATA[2].text) + str(SN4) + ".png"
        Fixture4Photo_copy = cv2.imread(str(XMLDATA[2].text) + str(SN4) + ".png")
        Fixture4Photo_copy = cv2.imwrite(str(XMLDATA[2].text) + "TEST\\" + str(SN4) + "_copy.png", Fixture4Photo_copy)
        Fixture4Photo_copy = str(XMLDATA[2].text) + "TEST\\" + str(SN4) + "_copy.png"
        img4 = Image.open(Fixture4Photo_copy)
        try:
            img4 = img4.resize((300, 224), Image.ANTIALIAS)
            img4.save(Fixture4Photo_copy, "png")
        except:
            donothing = 3
        img4 = PhotoImage(file=Fixture4Photo_copy)
        IMG4 = Label(root, image=img4)
        IMG4.place(x=10 + 320 * 3, y=40)
    else:
        try:
            IMG4.destroy()
        except:
            donothing = 3
    text4_sn = Label(root, text="SN : " + SN4)
    text4_sn.place(x=10 + 320 * 3, y=270)
    # FixtureNumber
    FixtureNumber4 = "FixtureNumber : " + str(FixtureNumber4)
    text4_fix = Label(root, text=FixtureNumber4)
    text4_fix.place(x=10 + 320 * 3, y=290)
    # Test Status
    TestStatus4result = ""
    if TESTING[3] == 1:
        if Alreadypass == 0:
            CheckUpSevenSegmentDisplayNumber = StartLedTest.CheckUpSevenSegmentDisplayNumber(str(XMLDATA[1].text), SN4, xmlpath)
            if CheckUpSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestRightLed(str(XMLDATA[1].text), SN4, 0, 0)[0]
                if PASS == 1:
                    TestStatus4result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus4result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            CheckDownSevenSegmentDisplayNumber = StartLedTest.CheckDownSevenSegmentDisplayNumber(str(XMLDATA[1].text),
                                                                                                 SN4, xmlpath)
            if CheckDownSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestLeftLed(str(XMLDATA[1].text), SN4, 0, 0)[0]
                if PASS == 1:
                    TestStatus4result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus4result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            TestStatus4result = "FAIL"
    if TestStatus4result != "PASS" and TestStatus4result != "FAIL":
        TestStatus4result = str(XMLDATA[5].text)
    TestStatus4 = "Test Status : " + str(TestStatus4result)
    TestStatus4 = Label(root, text=TestStatus4)
    TestStatus4.place(x=10 + 320 * 3, y=310)
    if TestStatus4result == "FAIL":
        FINDRUNNUM[3] = 1
        Reviewlable4 = Label(root, text=str(XMLDATA[6].text), fg="RED", font=3)
        Reviewlable4.place(x=10 + 320 * 3, y=330)
        TestStatus4btn1 = Button(root, text="PASS", command=partial(SN4reviewPASS, SN4), font=3, fg="Green")
        TestStatus4btn1.place(x=210 + 320 * 3, y=270, width=100, height=50)
        TestStatus4btn2 = Button(root, text="FAIL", command=partial(SN4reviewFAIL, SN4), font=3, fg="RED")
        TestStatus4btn2.place(x=210 + 320 * 3, y=320, width=100, height=50)
    elif TestStatus4result == "PASS":
        TMP4 = open(str(XMLDATA[2].text) + str(XMLDATA[0][3].get("fixturenumber")) + ".tmp", 'w')
        TMP4.write("SN:" + SN4 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][3].get("fixturenumber")))
        TMP4.close()
        FINDRUNNUM[3] = 0
        try:
            os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][3].get("fixturenumber")) + ".run")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN4) + "_copy.png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN4) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN4) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN4) + ".png")
        except:
            donothing = 1
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][3].get("fixturenumber")) + ".tmp"):
        FINDRUNNUM[3] = 0
        img4 = PhotoImage(file="")
        IMG4 = Label(root, image=img4)
        IMG4.place(x=10 + 320 * 3, y=40)
def SN4reviewPASS(SN4):
    TestStatus4btn1.place_forget()
    TestStatus4btn2.place_forget()
    Reviewlable4.place_forget()
    TMP4 = open(str(XMLDATA[2].text) + str(XMLDATA[0][3].get("fixturenumber")) + ".tmp", 'w')
    TMP4.write("SN:" + SN4 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][3].get("fixturenumber")))
    TMP4.close()
    TestStatus4.config(text="Test Status : PASS")
    TESTING[3] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][3].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text)+"TEST\\"+str(SN4)+"_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text)+"TEST\\result_"+str(SN4)+".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text)+"TEST\\Right_LED_"+str(SN4)+".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text)+"TEST\\Left_LED_"+str(SN4)+".png")
    except:
        donothing = 1
def SN4reviewFAIL(SN4):
    TMP4 = open(str(XMLDATA[2].text) + str(XMLDATA[0][3].get("fixturenumber")) + ".tmp", 'w')
    TMP4.write("SN:" + SN4 + "\nRESULT:FAIL\nFixtureID:" + str(XMLDATA[0][3].get("fixturenumber")))
    TMP4.close()
    TestStatus4.config(text="Test Status : FAIL")
    TestStatus4btn1.place_forget()
    TestStatus4btn2.place_forget()
    Reviewlable4.place_forget()
    TESTING[3] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][3].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text)+"TEST\\"+str(SN4)+"_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text)+"TEST\\result_"+str(SN4)+".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text)+"TEST\\Right_LED_"+str(SN4)+".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text)+"TEST\\Left_LED_"+str(SN4)+".png")
    except:
        donothing = 1
def fixture_5():
    global img1, img2, img3, img4, img5, img6, img7, img8, IMG1, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, TMP1, TMP2, TMP3, TMP4, TMP5, TMP6, TMP7, TMP8, FINDRUNNUM
    global TestStatus1, TestStatus1btn1, TestStatus1btn2, Reviewlable1
    global TestStatus2, TestStatus2btn1, TestStatus2btn2, Reviewlable2
    global TestStatus3, TestStatus3btn1, TestStatus3btn2, Reviewlable3
    global TestStatus4, TestStatus4btn1, TestStatus4btn2, Reviewlable4
    global TestStatus5, TestStatus5btn1, TestStatus5btn2, Reviewlable5
    global TestStatus6, TestStatus6btn1, TestStatus6btn2, Reviewlable6
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus8, TestStatus8btn1, TestStatus8btn2, Reviewlable8
    SN5 = str(XMLDATA[5].text)
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][4].get("fixturenumber")) + ".run"):
        loadinfsplash()
        FINDRUNNUM[4] = 1
        TESTING[4] = 1
        print("SN5 Get")
        with open(str(XMLDATA[2].text) + str(XMLDATA[0][4].get("fixturenumber")) + ".run", 'r') as file:
            SN5 = file.readlines()[0]
    Alreadypass = 0
    FixtureNumber5 = XMLDATA[0][4].get("fixturenumber")
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][4].get("fixturenumber")) + ".run"):
        Fixture5Photo = str(XMLDATA[2].text) + str(SN5) + ".png"
        Fixture5Photo_copy = cv2.imread(str(XMLDATA[2].text) + str(SN5) + ".png")
        Fixture5Photo_copy = cv2.imwrite(str(XMLDATA[2].text) + "TEST\\" + str(SN5) + "_copy.png", Fixture5Photo_copy)
        Fixture5Photo_copy = str(XMLDATA[2].text) + "TEST\\" + str(SN5) + "_copy.png"
        img5 = Image.open(Fixture5Photo_copy)
        try:
            img5 = img5.resize((300, 224), Image.ANTIALIAS)
            img5.save(Fixture5Photo_copy, "png")
        except:
            donothing = 5
        img5 = PhotoImage(file=Fixture5Photo_copy)
        IMG5 = Label(root, image=img5)
        IMG5.place(x=10, y=400)
    else:
        try:
            IMG5.destroy()
        except:
            donothing = 5
    SN5 = str(SN5)
    text5_sn = Label(root, text="SN : " + SN5)
    text5_sn.place(x=10, y=630)
    # FixtureNumber
    FixtureNumber5 = "FixtureNumber : " + str(FixtureNumber5)
    text5_fix = Label(root, text=FixtureNumber5)
    text5_fix.place(x=10, y=650)
    # Test Status
    TestStatus5result = ""
    if TESTING[4] == 1:
        if Alreadypass == 0:
            CheckUpSevenSegmentDisplayNumber = StartLedTest.CheckUpSevenSegmentDisplayNumber(str(XMLDATA[1].text), SN5, xmlpath)
            if CheckUpSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestRightLed(str(XMLDATA[1].text), SN5, 0, 0)[0]
                if PASS == 1:
                    TestStatus5result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus5result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            CheckDownSevenSegmentDisplayNumber = StartLedTest.CheckDownSevenSegmentDisplayNumber(str(XMLDATA[1].text),
                                                                                                 SN5, xmlpath)
            if CheckDownSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestLeftLed(str(XMLDATA[1].text), SN5, 0, 0)[0]
                if PASS == 1:
                    TestStatus5result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus5result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            TestStatus5result = "FAIL"
    if TestStatus5result != "PASS" and TestStatus5result != "FAIL":
        TestStatus5result = str(XMLDATA[5].text)
    TestStatus5 = "Test Status : " + str(TestStatus5result)
    TestStatus5 = Label(root, text=TestStatus5)
    TestStatus5.place(x=10, y=670)
    if TestStatus5result == "FAIL":
        FINDRUNNUM[4] = 1
        Reviewlable5 = Label(root, text=str(XMLDATA[6].text), fg="RED", font=3)
        Reviewlable5.place(x=10, y=690)
        TestStatus5btn1 = Button(root, text="PASS", command=partial(SN5reviewPASS, SN5), font=3, fg="Green")
        TestStatus5btn1.place(x=210, y=630, width=100, height=50)
        TestStatus5btn2 = Button(root, text="FAIL", command=partial(SN5reviewFAIL, SN5), font=3, fg="RED")
        TestStatus5btn2.place(x=210, y=680, width=100, height=50)
    elif TestStatus5result == "PASS":
        TMP5 = open(str(XMLDATA[2].text) + str(XMLDATA[0][4].get("fixturenumber")) + ".tmp", 'w')
        TMP5.write("SN:" + SN5 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][4].get("fixturenumber")))
        TMP5.close()
        FINDRUNNUM[4] = 0
        try:
            os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][4].get("fixturenumber")) + ".run")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN5) + "_copy.png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN5) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN5) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN5) + ".png")
        except:
            donothing = 1
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][4].get("fixturenumber")) + ".tmp"):
        FINDRUNNUM[4] = 0
        img5 = PhotoImage(file="")
        IMG5 = Label(root, image=img5)
        IMG5.place(x=10, y=400)
def SN5reviewPASS(SN5):
    TestStatus5btn1.place_forget()
    TestStatus5btn2.place_forget()
    Reviewlable5.place_forget()
    TMP5 = open(str(XMLDATA[2].text) + str(XMLDATA[0][4].get("fixturenumber")) + ".tmp", 'w')
    TMP5.write("SN:" + SN5 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][4].get("fixturenumber")))
    TMP5.close()
    TestStatus5.config(text="Test Status : PASS")
    TESTING[4] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][4].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN5) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN5) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN5) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN5) + ".png")
    except:
        donothing = 1
def SN5reviewFAIL(SN5):

    TMP5 = open(str(XMLDATA[2].text) + str(XMLDATA[0][4].get("fixturenumber")) + ".tmp", 'w')
    TMP5.write("SN:" + SN5 + "\nRESULT:FAIL\nFixtureID:" + str(XMLDATA[0][4].get("fixturenumber")))
    TMP5.close()
    TestStatus5.config(text="Test Status : FAIL")
    TestStatus5btn1.place_forget()
    TestStatus5btn2.place_forget()
    Reviewlable5.place_forget()
    TESTING[4] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][4].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN5) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN5) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN5) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN5) + ".png")
    except:
        donothing = 1
def fixture_6():
    global img1, img2, img3, img4, img5, img6, img7, img8, IMG1, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, TMP1, TMP2, TMP3, TMP4, TMP5, TMP6, TMP7, TMP8, FINDRUNNUM
    global TestStatus1, TestStatus1btn1, TestStatus1btn2, Reviewlable1
    global TestStatus2, TestStatus2btn1, TestStatus2btn2, Reviewlable2
    global TestStatus3, TestStatus3btn1, TestStatus3btn2, Reviewlable3
    global TestStatus4, TestStatus4btn1, TestStatus4btn2, Reviewlable4
    global TestStatus5, TestStatus5btn1, TestStatus5btn2, Reviewlable5
    global TestStatus6, TestStatus6btn1, TestStatus6btn2, Reviewlable6
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus8, TestStatus8btn1, TestStatus8btn2, Reviewlable8
    SN6 = str(XMLDATA[5].text)
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][5].get("fixturenumber")) + ".run"):
        loadinfsplash()
        FINDRUNNUM[5] = 1
        TESTING[5] = 1
        print("SN6 Get")
        with open(str(XMLDATA[2].text) + str(XMLDATA[0][5].get("fixturenumber")) + ".run", 'r') as file:
            SN6 = file.readlines()[0]
    Alreadypass = 0
    FixtureNumber6 = XMLDATA[0][5].get("fixturenumber")
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][5].get("fixturenumber")) + ".run"):
        Fixture6Photo = str(XMLDATA[2].text) + str(SN6) + ".png"
        Fixture6Photo_copy = cv2.imread(str(XMLDATA[2].text) + str(SN6) + ".png")
        Fixture6Photo_copy = cv2.imwrite(str(XMLDATA[2].text) + "TEST\\" + str(SN6) + "_copy.png", Fixture6Photo_copy)
        Fixture6Photo_copy = str(XMLDATA[2].text) + "TEST\\" + str(SN6) + "_copy.png"
        img6 = Image.open(Fixture6Photo_copy)
        try:
            img6 = img6.resize((300, 224), Image.ANTIALIAS)
            img6.save(Fixture6Photo_copy, "png")
        except:
            donothing = 6
        img6 = PhotoImage(file=Fixture6Photo_copy)
        IMG6 = Label(root, image=img6)
        IMG6.place(x=10 + 320 * 1, y=400)
    else:
        try:
            IMG6.destroy()
        except:
            donothing = 6
    text6_sn = Label(root, text="SN : " + SN6)
    text6_sn.place(x=10 + 320 * 1, y=630)
    # FixtureNumber
    FixtureNumber6 = "FixtureNumber : " + str(FixtureNumber6)
    text6_fix = Label(root, text=FixtureNumber6)
    text6_fix.place(x=10 + 320 * 1, y=650)
    # Test Status
    TestStatus6result = ""
    if TESTING[5] == 1:
        if Alreadypass == 0:
            CheckUpSevenSegmentDisplayNumber = StartLedTest.CheckUpSevenSegmentDisplayNumber(str(XMLDATA[1].text), SN6, xmlpath)
            if CheckUpSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestRightLed(str(XMLDATA[1].text), SN6, 0, 0)[0]
                if PASS == 1:
                    TestStatus6result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus6result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            CheckDownSevenSegmentDisplayNumber = StartLedTest.CheckDownSevenSegmentDisplayNumber(str(XMLDATA[1].text),
                                                                                                 SN6, xmlpath)
            if CheckDownSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestLeftLed(str(XMLDATA[1].text), SN6, 0, 0)[0]
                if PASS == 1:
                    TestStatus6result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus6result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            TestStatus6result = "FAIL"
    if TestStatus6result != "PASS" and TestStatus6result != "FAIL":
        TestStatus6result = str(XMLDATA[5].text)
    TestStatus6 = "Test Status : " + str(TestStatus6result)
    TestStatus6 = Label(root, text=TestStatus6)
    TestStatus6.place(x=10 + 320 * 1, y=670)
    if TestStatus6result == "FAIL":
        FINDRUNNUM[5] = 1
        Reviewlable6 = Label(root, text=str(XMLDATA[6].text), fg="RED", font=3)
        Reviewlable6.place(x=10 + 320 * 1, y=690)
        TestStatus6btn1 = Button(root, text="PASS", command=partial(SN6reviewPASS, SN6), font=3, fg="Green")
        TestStatus6btn1.place(x=210 + 320 * 1, y=630, width=100, height=50)
        TestStatus6btn2 = Button(root, text="FAIL", command=partial(SN6reviewFAIL, SN6), font=3, fg="RED")
        TestStatus6btn2.place(x=210 + 320 * 1, y=680, width=100, height=50)
    elif TestStatus6result == "PASS":
        TMP6 = open(str(XMLDATA[2].text) + str(XMLDATA[0][5].get("fixturenumber")) + ".tmp", 'w')
        TMP6.write("SN:" + SN6 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][5].get("fixturenumber")))
        TMP6.close()
        FINDRUNNUM[5] = 0
        try:
            os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][5].get("fixturenumber")) + ".run")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN6) + "_copy.png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN6) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN6) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN6) + ".png")
        except:
            donothing = 1
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][5].get("fixturenumber")) + ".tmp"):
        FINDRUNNUM[5] = 0
        img6 = PhotoImage(file="")
        IMG6 = Label(root, image=img6)
        IMG6.place(x=10 + 320 * 1, y=400)
def SN6reviewPASS(SN6):
    TestStatus6btn1.place_forget()
    TestStatus6btn2.place_forget()
    Reviewlable6.place_forget()
    TMP6 = open(str(XMLDATA[2].text) + str(XMLDATA[0][5].get("fixturenumber")) + ".tmp", 'w')
    TMP6.write("SN:" + SN6 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][5].get("fixturenumber")))
    TMP6.close()
    TestStatus6.config(text="Test Status : PASS")
    TESTING[5] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][5].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN6) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN6) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN6) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN6) + ".png")
    except:
        donothing = 1
def SN6reviewFAIL(SN6):
    TMP6 = open(str(XMLDATA[2].text) + str(XMLDATA[0][5].get("fixturenumber")) + ".tmp", 'w')
    TMP6.write("SN:" + SN6 + "\nRESULT:FAIL\nFixtureID:" + str(XMLDATA[0][5].get("fixturenumber")))
    TMP6.close()
    TestStatus6.config(text="Test Status : FAIL")
    TestStatus6btn1.place_forget()
    TestStatus6btn2.place_forget()
    Reviewlable6.place_forget()
    TESTING[5] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][5].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN6) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN6) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN6) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN6) + ".png")
    except:
        donothing = 1
def fixture_7():
    global img1, img2, img3, img4, img5, img6, img7, img8, IMG1, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, TMP1, TMP2, TMP3, TMP4, TMP5, TMP6, TMP7, TMP8, FINDRUNNUM
    global TestStatus1, TestStatus1btn1, TestStatus1btn2, Reviewlable1
    global TestStatus2, TestStatus2btn1, TestStatus2btn2, Reviewlable2
    global TestStatus3, TestStatus3btn1, TestStatus3btn2, Reviewlable3
    global TestStatus4, TestStatus4btn1, TestStatus4btn2, Reviewlable4
    global TestStatus5, TestStatus5btn1, TestStatus5btn2, Reviewlable5
    global TestStatus6, TestStatus6btn1, TestStatus6btn2, Reviewlable6
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus8, TestStatus8btn1, TestStatus8btn2, Reviewlable8
    SN7 = str(XMLDATA[5].text)
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][6].get("fixturenumber")) + ".run"):
        loadinfsplash()
        FINDRUNNUM[6] = 1
        TESTING[6] = 1
        print("SN7 Get")
        with open(str(XMLDATA[2].text) + str(XMLDATA[0][6].get("fixturenumber")) + ".run", 'r') as file:
            SN7 = file.readlines()[0]
    Alreadypass = 0
    FixtureNumber7 = XMLDATA[0][6].get("fixturenumber")
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][6].get("fixturenumber")) + ".run"):
        Fixture7Photo = str(XMLDATA[2].text) + str(SN7) + ".png"
        Fixture7Photo_copy = cv2.imread(str(XMLDATA[2].text) + str(SN7) + ".png")
        Fixture7Photo_copy = cv2.imwrite(str(XMLDATA[2].text) + "TEST\\" + str(SN7) + "_copy.png", Fixture7Photo_copy)
        Fixture7Photo_copy = str(XMLDATA[2].text) + "TEST\\" + str(SN7) + "_copy.png"
        img7 = Image.open(Fixture7Photo_copy)
        try:
            img7 = img7.resize((300, 224), Image.ANTIALIAS)
            img7.save(Fixture7Photo_copy, "png")
        except:
            donothing = 7
        img7 = PhotoImage(file=Fixture7Photo_copy)
        IMG7 = Label(root, image=img7)
        IMG7.place(x=10 + 320 * 2, y=400)
    else:
        try:
            IMG7.destroy()
        except:
            donothing = 7
    text7_sn = Label(root, text="SN : " + SN7)
    text7_sn.place(x=10 + 320 * 2, y=630)
    # FixtureNumber
    FixtureNumber7 = "FixtureNumber : " + str(FixtureNumber7)
    text7_fix = Label(root, text=FixtureNumber7)
    text7_fix.place(x=10 + 320 * 2, y=650)
    # Test Status
    TestStatus7result = ""
    if TESTING[6] == 1:
        if Alreadypass == 0:
            CheckUpSevenSegmentDisplayNumber = StartLedTest.CheckUpSevenSegmentDisplayNumber(str(XMLDATA[1].text), SN7, xmlpath)
            if CheckUpSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestRightLed(str(XMLDATA[1].text), SN7, 0, 0)[0]
                if PASS == 1:
                    TestStatus7result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus7result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            CheckDownSevenSegmentDisplayNumber = StartLedTest.CheckDownSevenSegmentDisplayNumber(str(XMLDATA[1].text),
                                                                                                 SN7, xmlpath)
            if CheckDownSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestLeftLed(str(XMLDATA[1].text), SN7, 0, 0)[0]
                if PASS == 1:
                    TestStatus7result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus7result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            TestStatus7result = "FAIL"
    if TestStatus7result != "PASS" and TestStatus7result != "FAIL":
        TestStatus7result = str(XMLDATA[5].text)
    TestStatus7 = "Test Status : " + str(TestStatus7result)

    TestStatus7 = Label(root, text=TestStatus7)
    TestStatus7.place(x=10 + 320 * 2, y=670)
    if TestStatus7result == "FAIL":
        FINDRUNNUM[6] = 1
        Reviewlable7 = Label(root, text=str(XMLDATA[6].text), fg="RED", font=3)
        Reviewlable7.place(x=10 + 320 * 2, y=690)
        TestStatus7btn1 = Button(root, text="PASS", command=partial(SN7reviewPASS, SN7), font=3, fg="Green")
        TestStatus7btn1.place(x=210 + 320 * 2, y=630, width=100, height=50)
        TestStatus7btn2 = Button(root, text="FAIL", command=partial(SN7reviewFAIL, SN7), font=3, fg="RED")
        TestStatus7btn2.place(x=210 + 320 * 2, y=680, width=100, height=50)
    elif TestStatus7result == "PASS":
        TMP7 = open(str(XMLDATA[2].text) + str(XMLDATA[0][6].get("fixturenumber")) + ".tmp", 'w')
        TMP7.write("SN:" + SN7 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][6].get("fixturenumber")))
        TMP7.close()
        FINDRUNNUM[6] = 0
        try:
            os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][6].get("fixturenumber")) + ".run")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN7) + "_copy.png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN7) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN7) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN7) + ".png")
        except:
            donothing = 1
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][6].get("fixturenumber")) + ".tmp"):
        FINDRUNNUM[6] = 0
        img7 = PhotoImage(file="")
        IMG7 = Label(root, image=img7)
        IMG7.place(x=10 + 320 * 2, y=400)
def SN7reviewPASS(SN7):
    TestStatus7btn1.place_forget()
    TestStatus7btn2.place_forget()
    Reviewlable7.place_forget()
    TMP7 = open(str(XMLDATA[2].text) + str(XMLDATA[0][6].get("fixturenumber")) + ".tmp", 'w')
    TMP7.write("SN:" + SN7 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][6].get("fixturenumber")))
    TMP7.close()
    TestStatus7.config(text="Test Status : PASS")
    TESTING[6] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][6].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN7) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN7) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN7) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN7) + ".png")
    except:
        donothing = 1
def SN7reviewFAIL(SN7):

    TMP7 = open(str(XMLDATA[2].text) + str(XMLDATA[0][6].get("fixturenumber")) + ".tmp", 'w')
    TMP7.write("SN:" + SN7 + "\nRESULT:FAIL\nFixtureID:" + str(XMLDATA[0][6].get("fixturenumber")))
    TMP7.close()
    TestStatus7.config(text="Test Status : FAIL")
    TestStatus7btn1.place_forget()
    TestStatus7btn2.place_forget()
    Reviewlable7.place_forget()
    TESTING[6] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][6].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN7) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN7) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN7) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN7) + ".png")
    except:
        donothing = 1
def fixture_8():
    global img1, img2, img3, img4, img5, img6, img7, img8, IMG1, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, TMP1, TMP2, TMP3, TMP4, TMP5, TMP6, TMP7, TMP8, FINDRUNNUM
    global TestStatus1, TestStatus1btn1, TestStatus1btn2, Reviewlable1
    global TestStatus2, TestStatus2btn1, TestStatus2btn2, Reviewlable2
    global TestStatus3, TestStatus3btn1, TestStatus3btn2, Reviewlable3
    global TestStatus4, TestStatus4btn1, TestStatus4btn2, Reviewlable4
    global TestStatus5, TestStatus5btn1, TestStatus5btn2, Reviewlable5
    global TestStatus6, TestStatus6btn1, TestStatus6btn2, Reviewlable6
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus8, TestStatus8btn1, TestStatus8btn2, Reviewlable8
    SN8 = str(XMLDATA[5].text)
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][7].get("fixturenumber")) + ".run"):
        loadinfsplash()
        FINDRUNNUM[7] = 1
        TESTING[7] = 1
        print("SN8 Get")
        with open(str(XMLDATA[2].text) + str(XMLDATA[0][7].get("fixturenumber")) + ".run", 'r') as file:
            SN8 = file.readlines()[0]
    Alreadypass = 0
    FixtureNumber8 = XMLDATA[0][7].get("fixturenumber")
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][7].get("fixturenumber")) + ".run"):
        Fixture8Photo = str(XMLDATA[2].text) + str(SN8) + ".png"
        Fixture8Photo_copy = cv2.imread(str(XMLDATA[2].text) + str(SN8) + ".png")
        Fixture8Photo_copy = cv2.imwrite(str(XMLDATA[2].text) + "TEST\\" + str(SN8) + "_copy.png", Fixture8Photo_copy)
        Fixture8Photo_copy = str(XMLDATA[2].text) + "TEST\\" + str(SN8) + "_copy.png"
        img8 = Image.open(Fixture8Photo_copy)
        try:
            img8 = img8.resize((300, 224), Image.ANTIALIAS)
            img8.save(Fixture8Photo_copy, "png")
        except:
            donothing = 8
        img8 = PhotoImage(file=Fixture8Photo_copy)
        IMG8 = Label(root, image=img8)
        IMG8.place(x=10 + 320 * 3, y=400)
    else:
        try:
            IMG8.destroy()
        except:
            donothing = 8
    text8_sn = Label(root, text="SN : " + SN8)
    text8_sn.place(x=10 + 320 * 3, y=630)
    # FixtureNumber
    FixtureNumber8 = "FixtureNumber : " + str(FixtureNumber8)
    text8_fix = Label(root, text=FixtureNumber8)
    text8_fix.place(x=10 + 320 * 3, y=650)
    # Test Status
    TestStatus8result = ""
    if TESTING[7] == 1:
        if Alreadypass == 0:
            CheckUpSevenSegmentDisplayNumber = StartLedTest.CheckUpSevenSegmentDisplayNumber(str(XMLDATA[1].text), SN8, xmlpath)
            if CheckUpSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestRightLed(str(XMLDATA[1].text), SN8, 0, 0)[0]
                if PASS == 1:
                    TestStatus8result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus8result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            CheckDownSevenSegmentDisplayNumber = StartLedTest.CheckDownSevenSegmentDisplayNumber(str(XMLDATA[1].text),
                                                                                                 SN8, xmlpath)
            if CheckDownSevenSegmentDisplayNumber == 2:
                PASS = StartLedTest.TestLeftLed(str(XMLDATA[1].text), SN8, 0, 0)[0]
                if PASS == 1:
                    TestStatus8result = "PASS"
                    Alreadypass = 1
                else:
                    TestStatus8result = "FAIL"
                    Alreadypass = 0
        if Alreadypass == 0:
            TestStatus8result = "FAIL"
    if TestStatus8result != "PASS" and TestStatus8result != "FAIL":
        TestStatus8result = str(XMLDATA[5].text)
    TestStatus8 = "Test Status : " + str(TestStatus8result)

    TestStatus8 = Label(root, text=TestStatus8)
    TestStatus8.place(x=10 + 320 * 3, y=670)
    if TestStatus8result == "FAIL":
        FINDRUNNUM[7] = 1
        Reviewlable8 = Label(root, text=str(XMLDATA[6].text), fg="RED", font=3)
        Reviewlable8.place(x=10 + 320 * 3, y=690)
        TestStatus8btn1 = Button(root, text="PASS", command=partial(SN8reviewPASS, SN8), font=3, fg="Green")
        TestStatus8btn1.place(x=210 + 320 * 3, y=630, width=100, height=50)
        TestStatus8btn2 = Button(root, text="FAIL", command=partial(SN8reviewFAIL, SN8), font=3, fg="RED")
        TestStatus8btn2.place(x=210 + 320 * 3, y=680, width=100, height=50)
    elif TestStatus8result == "PASS":
        TMP8 = open(str(XMLDATA[2].text) + str(XMLDATA[0][7].get("fixturenumber")) + ".tmp", 'w')
        TMP8.write("SN:" + SN8 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][7].get("fixturenumber")))
        TMP8.close()
        FINDRUNNUM[7] = 0
        try:
            os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][7].get("fixturenumber")) + ".run")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN8) + "_copy.png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN8) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN8) + ".png")
        except:
            donothing = 1
        try:
            os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN8) + ".png")
        except:
            donothing = 1
    if os.path.isfile(str(XMLDATA[2].text) + str(XMLDATA[0][7].get("fixturenumber")) + ".tmp"):
        FINDRUNNUM[7] = 0
        img8 = PhotoImage(file="")
        IMG8 = Label(root, image=img8)
        IMG8.place(x=10 + 320 * 3, y=400)
def SN8reviewPASS(SN8):
    TestStatus8btn1.place_forget()
    TestStatus8btn2.place_forget()
    Reviewlable8.place_forget()
    TMP8 = open(str(XMLDATA[2].text) + str(XMLDATA[0][7].get("fixturenumber")) + ".tmp", 'w')
    TMP8.write("SN:" + SN8 + "\nRESULT:PASS\nFixtureID:" + str(XMLDATA[0][7].get("fixturenumber")))
    TMP8.close()
    TestStatus8.config(text="Test Status : PASS")
    TESTING[7] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][7].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN8) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN8) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN8) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN8) + ".png")
    except:
        donothing = 1
def SN8reviewFAIL(SN8):

    TMP8 = open(str(XMLDATA[2].text) + str(XMLDATA[0][7].get("fixturenumber")) + ".tmp", 'w')
    TMP8.write("SN:" + SN8 + "\nRESULT:FAIL\nFixtureID:" + str(XMLDATA[0][7].get("fixturenumber")))
    TMP8.close()
    TestStatus8.config(text="Test Status : FAIL")
    TestStatus8btn1.place_forget()
    TestStatus8btn2.place_forget()
    Reviewlable8.place_forget()
    TESTING[7] = 0
    try:
        os.remove(str(XMLDATA[2].text) + str(XMLDATA[0][7].get("fixturenumber")) + ".run")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\" + str(SN8) + "_copy.png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\result_" + str(SN8) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Right_LED_" + str(SN8) + ".png")
    except:
        donothing = 1
    try:
        os.remove(str(XMLDATA[2].text) + "TEST\\Left_LED_" + str(SN8) + ".png")
    except:
        donothing = 1
def main():
    root.update()
    global img1, img2, img3, img4, img5, img6, img7, img8, IMG1, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, TMP1, TMP2, TMP3, TMP4, TMP5, TMP6, TMP7, TMP8, FINDRUNNUM, TESTING
    global TestStatus1, TestStatus1btn1, TestStatus1btn2, Reviewlable1
    global TestStatus2, TestStatus2btn1, TestStatus2btn2, Reviewlable2
    global TestStatus3, TestStatus3btn1, TestStatus3btn2, Reviewlable3
    global TestStatus4, TestStatus4btn1, TestStatus4btn2, Reviewlable4
    global TestStatus5, TestStatus5btn1, TestStatus5btn2, Reviewlable5
    global TestStatus6, TestStatus6btn1, TestStatus6btn2, Reviewlable6
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus7, TestStatus7btn1, TestStatus7btn2, Reviewlable7
    global TestStatus8, TestStatus8btn1, TestStatus8btn2, Reviewlable8
    FINDRUNNUM = [0, 0, 0, 0, 0, 0, 0, 0]
    if TESTING[0] == 0:fixture_1()
    if TESTING[1] == 0:fixture_2()
    if TESTING[2] == 0:fixture_3()
    if TESTING[3] == 0:fixture_4()
    if TESTING[4] == 0:fixture_5()
    if TESTING[5] == 0:fixture_6()
    if TESTING[6] == 0:fixture_7()
    if TESTING[7] == 0:fixture_8()
    time = 3000
    for i in range(len(FINDRUNNUM)):
        time = time + FINDRUNNUM[i] * 1000
    root.after(time, main)
Initialization()
main()
root.mainloop()