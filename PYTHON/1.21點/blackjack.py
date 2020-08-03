import random
while(1):
    i=input("請輸入籌碼:")
    i1=input("請下注:")
    c = random.randrange(10)+1
    d = random.randrange(10)+1
    f = random.randrange(10)+1
    f1 = random.randrange(10)+1
    f2 = random.randrange(10)+1
    print("你的牌是:%d %d" % (c,d))
    print("是否加牌?1=yes/0=no")
    yn=input("")
    if yn == 1:
        if (c+d+f)>21:
            print("你的牌是 %d %d %d    你輸了!"%(c,d,f))
            i=i-i1
            print("剩餘籌碼:%d"%i)
        else:
            print("你的牌是 %d %d %d"%(c,d,f))
            yn=input("是否加牌?1=yes/0=no")
            if yn == 1:
                if (c+d+f+f1)>21:
                    print("你的牌是 %d %d %d %d   你輸了!"%(c,d,f,f1))
                    i=i-i1;
                    print("剩餘籌碼:%d"%i);
                else:
                    print("你的牌是 %d %d %d %d"%(c,d,f,f1))
                    print("你的牌是 %d %d %d"%(c,d,f))
                    yn=input("")
                    if yn == 1:
                        if (c+d+f+f1+f2)>21:
                            print("你的牌是 %d %d %d %d %d   你輸了!"%(c,d,f,f1,f2))
                            i=i-i1;
                            print("剩餘籌碼:%d\n\n"%i)
                        else:
                            print("你的牌是 %d %d %d %d %d  ( 五 龍 ) 你贏了!"%(c,d,f,f1,f2))
                            i=i+i1;
                            print("剩餘籌碼:%d"%i)
                    else:
                        t=c+d+f+f1;
                        print("你的牌是 %d %d %d %d  共%d點"%(c,d,f,f1,t))
                        com=random.randrange(20)+1
                        if(com<16):com=com+6;
                        if(com<16):com=com+6;
                        print("你的點數是%d    電腦的點數是:%d"%(t,com))
                        if(c+d+f+f1)<com:
                           print("你輸了");
                           i=i-i1;
                           print("剩餘籌碼:%d"%i);
                        elif((c+d+f+f1)>com):
                            print("你贏了\n\n");
                            i=i+i1;
                            print("剩餘籌碼:%d"%i);
                        else:
                            print("平手")
                            print("剩餘籌碼:%d"%i)
            else:
                t=c+d+f;
                print("你的牌是 %d %d %d  共%d點"%(c,d,f,t))
                com=random.randrange(20)+1
                if(com<16):com=com+6;
                    print("你的點數是%d    電腦的點數是:%d"%(t,com))
                if((c+d+f)<com):
                    print("你輸了");
                    i=i-i1;
                    print("剩餘籌碼:%d"%i)
                elif((c+d+f)>com):
                    print("你贏了");
                    i=i+i1;
                    print("剩餘籌碼:%d"%i)
                else:print("平手")
    else:
        t=c+d;
        print("你的牌是 %d %d   共%d點"%(c,d,t))
        com=random.randrange(20)+1
        if(com<15):com=com+6;
        print("你的點數是%d    電腦的點數是:%d"%(t,com))
        if((c+d)<com):
            print("你輸了");
            i=i-i1;
            print("剩餘籌碼:%d"%i);
        elif((c+d)>com):
            print("你贏了\n\n");
            i=i+i1;
            print("剩餘籌碼:%d",i);
        else:print("平手");
