import os
import json
import sys
import requests

def getURL(num):
    
    url = "https://testm.10jqka.com.cn/tg_templates/doubleone/2018/kycUserProfile/index.php"
    querystring = {"con":"survey","act":"uploadAnswers"}
    payload = "answers[]="+str(int(num[0])+1)+"&answers[]="+str(int(num[1])+1)+"&answers[]="+str(int(num[2])+1)+"&answers[]="+str(int(num[3])+1)+"&answers[]="+str(int(num[4])+1)+"&answers[]="+str(int(num[5])+1)+"&answers[]="+str(int(num[6])+1)+"&answers[]="+str(int(num[7])+1)+"&answers[]="+str(int(num[8])+1)+"&answers[]="+str(int(num[9])+1)+"&answers[]="+str(int(num[10])+1)+"&answers[]="+str(int(num[11])+1)+"&answers[]="+str(int(num[12])+1)+"&answers[]="+str(int(num[13])+1)+"&answers[]="+str(int(num[14])+1)+"&answers[]="+str(int(num[15])+1)+"&answers[]="+str(int(num[16])+1)+"&answers[]="+str(int(num[17])+1)+"&answers[]="+str(int(num[18])+1)+"&answers[]="+str(int(num[19])+1)+"&answers[]="+str(int(num[20])+1)+"&answers[]="+str(int(num[21])+1)+"&answers[]="+str(int(num[22])+1)+"&isBreakPoint=0&type=23"
    
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    return json.loads(response.text)["data"]


def DecConversion(dec,n):
    # 存放输出数据初始化
    result = ''
    # 判断数据是否为空
    if dec:
        # 递归调用进制数据转换函数
        result = DecConversion(dec // n,n)
        # 输出转换后的结果
        return result + str(dec % n)
    else:
        return result

def getSOC(num):
    #change = DecConversion(num,5).zfill(23)
    #print(change[5])
    change = num
    N = (int(change[5])+int(change[1])+int(change[7])+int(change[3])+int(change[12])+5)/5
    E = (int(change[0])+int(change[6])+int(change[2])+int(change[8])+4)/4
    O = (int(change[9])+int(change[10])-int(change[11])+int(change[4])+int(change[13])+6+5)/5
    A = (18-int(change[14])-int(change[15])-int(change[16])+int(change[17])-2)/4
    C = (18+int(change[18])+int(change[19])-int(change[20])-int(change[21])-int(change[22])-1)/5
    list = []
    list.append(getClassN(N))
    list.append(getClassE(E))
    list.append(getClassA(A))
    list.append(getClassO(O))
    list.append(getClassC(C))
    '''
    print(N)
    print(E)
    print(A)
    print(O)
    print(C)
    
    print(getClassN(N))
    print(getClassE(E))
    print(getClassA(A))
    print(getClassO(O))
    print(getClassC(C))
    '''
    return sorted(list)
    
    
    


def getClassN(soc):
    if soc<1.2:
        return 0    #N1
    elif soc < 1.8:
        return 10   #N2
    elif soc < 2.3:
        return 25    #N3
    elif soc < 2.7:
        return 18    #N4
    else:
        return 8    #N5
    

def getClassE(soc):
    if soc<2.0:
        return 9    #E1
    elif soc < 2.5:
        return 19    #E2
    elif soc < 2.9:
        return 25    #E3
    elif soc < 3.2:
        return 14   #E4
    else:
        return 4    #E5

def getClassA(soc):
    if soc<2.3:
        return 1    #A1
    elif soc < 2.6:
        return 11   #A2
    elif soc < 2.9:
        return 25   #A3
    elif soc < 3.2:
        return 17   #A4
    else:
        return 7   #A5


def getClassO(soc):
    if soc<2.2:
        return 5    #O1
    elif soc < 2.6:
        return 15   #O2
    elif soc < 2.9:
        return 25   #O3
    elif soc < 3.2:
        return 13   #O4
    else:
        return 3    #o5


def getClassC(soc):
    if soc<2.3:
        return 2    #C1
    elif soc < 2.8:
        return 12   #C2
    elif soc < 3.3:
        return 25   #C3
        #return
    elif soc < 3.6:
        return 16   #C4
    else:
        return 6   #C5


def result(list):
    result = []
    if list[1]==25:
        #print("宜人性：友好、诚实、同情")   #A5
        result.insert(1,"A5")
        if list[0]==25:            
            print("开放性：实干、保守、规范")   #O1
            result.insert(0,"O1")
        else:
            #print(duiying(list[0]))
            result.insert(0,duiying(list[0]))
    else:
        #print(duiying(list[0]))
        result.insert(0,duiying(list[0]))
        #print(duiying(list[1]))
        result.insert(1,duiying(list[1]))
    return result

'''
def duiying(n):
    if n == 0 or n == 10:
        return "神经质：冷静、理性、自制"   #N1/N2
    elif n == 1 or n == 11:
        return "宜人性：强硬、客观、独立"   #A1/A2
    elif n == 2 or n == 12:
        return "尽责性：冲动、草率、随性"   #C1/C2
    elif n == 3 or n == 13:
        return "开放性：想象、新奇、思辨"   #O4/O5
    elif n == 4 or n == 14:
        return "外向性：健谈、热情、乐观"   #E4/E5
    elif n == 5 or n == 15:
        return "开放性：实干、保守、规范"   #O1/O2
    elif n == 6 or n == 16:
        return "尽责性：高效、精力、纪律"   #C4/C5
    elif n == 7 or n == 17:
        return "宜人性：友好、诚实、同情"   #A4/A5
    elif n == 8 or n == 18:
        return "神经质：焦虑、紧张、冲动"   #N4/N5
    elif n == 9 or n == 19:
        return "外向性：沉静、谦逊、谨慎"   #E1/E2
'''
def duiying(n):
    if n == 0:
        #return "神经质：冷静、理性、自制"   #N1/N2
        return "N1"
    elif n == 1:
        #return "宜人性：强硬、客观、独立"   #A1/A2
        return "A1"
    elif n == 2:
        #return "尽责性：冲动、草率、随性"   #C1/C2
        return "C1"
    elif n == 3:
        #return "开放性：想象、新奇、思辨"   #O4/O5
        return "O5"
    elif n == 4:
        #return "外向性：健谈、热情、乐观"   #E4/E5
        return "E5"
    elif n == 5:
        #return "开放性：实干、保守、规范"   #O1/O2
        return "O1"
    elif n == 6:
        #return "尽责性：高效、精力、纪律"   #C4/C5
        return "C5"
    elif n == 7:
        #return "宜人性：友好、诚实、同情"   #A4/A5
        return "A5"
    elif n == 8:
        #return "神经质：焦虑、紧张、冲动"   #N4/N5
        return "N5"
    elif n == 9:
        #return "外向性：沉静、谦逊、谨慎"   #E1/E2
        return "E1"
    elif n == 10:
        #return "神经质：冷静、理性、自制"   #N1/N2
        return "N2"
    elif n == 11:
        #return "宜人性：强硬、客观、独立"   #A1/A2
        return "A2"
    elif n == 12:
        #return "尽责性：冲动、草率、随性"   #C1/C2
        return "C2"
    elif n == 13:
        #return "开放性：想象、新奇、思辨"   #O4/O5
        return "O4"
    elif n == 14:
        #return "外向性：健谈、热情、乐观"   #E4/E5
        return "E4"
    elif n == 15:
        #return "开放性：实干、保守、规范"   #O1/O2
        return "O2"
    elif n == 16:
        #return "尽责性：高效、精力、纪律"   #C4/C5
        return "C4"
    elif n == 17:
        #return "宜人性：友好、诚实、同情"   #A4/A5
        return "A4"
    elif n == 18:
        #return "神经质：焦虑、紧张、冲动"   #N4/N5
        return "N4"
    elif n == 19:
        #return "外向性：沉静、谦逊、谨慎"   #E1/E2
        return "E2"


fo = open("foo.txt", "w+")
for i in range(11920928955078124,0,-1):
    j =  str(DecConversion(i,5).zfill(23))
    a = getURL(j)
    b = result(getSOC(j))
    print(i)
    print(j)
    if a != b:
        print("预期是"+str(b))
        print("实际是"+str(a))
        fo.write( str(i)+":"+str(j)+"\n")
        fo.write( "预期是"+str(b)+";"+"实际是"+str(a)+"\n")
fo.close()

#print(DecConversion(11920928955078124,5)[0])

#print(result(getSOC(int(sys.argv[1]))))
#print(getSOC(int(sys.argv[1])))
a = str(DecConversion(11920928955078124,5).zfill(23))
print(getURL(a))
print(result(getSOC(a)))