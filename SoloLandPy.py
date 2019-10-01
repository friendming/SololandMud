#SoloLandPy
#Produced by Quming
#Latest edit:20190928 19:24

plot_progress = ''  #全局变量 剧情进度
gamer_place = ''    #角色所在位置

class Persion:
    name = "TestPeople"
    age = 10
    exp = 0
    hp = 0      #血量
    mp = 0      #魂力
    jsl = 0     #精神力

def showPlot(progress): #剧情显示函数
    plot_path = './plot/ch/' + str(progress) + '.slmp'
    if (int(progress) <= 1):
        fplot = open(plot_path,encoding = 'utf-8',mode = 'r')
        ls = fplot.readlines()
        #ls_len = len(ls)
        for i in ls:
            if (i[0] == '/'):
                print("Command Mode")
                commandi = i.strip('/')
                eval(commandi)
            else:
                print(i)
        fplot.close()

def getCommand(): #获取指令并操作的函数 返回输入的指令
    com = input('')
    ####指令判别####
    if (com == 'map'):
        print('Map output') #--这里应输出地图！读取地图文件--
    elif (com == 'go to e'):
        print('东方')
    elif (com == 'go to w'):
        print('西方')
    elif (com == 'go to n'):
        print('北方')
    elif (com == 'go to s'):
        print('南方')
    elif (com == 'end game'):
        exit()
    elif (com == 'help'):
        printHelp()
    else:
        print('未知指令')
    ####判别 END####
    return com

def setPlot(next): #剧情进度设定函数
    global plot_progress
    if next == '+':
        plot_progress = plot_progress + 1
    else:
        plot_progress = next
    fplotp = open('./udata/plot_progress.slmd', mode = 'w')   #修改进度文件
    fplotp.write(str(plot_progress))
    fplotp.close()

def printHelp():
    fhelp = open('./bin/files/help.slmf',encoding = 'utf-8',mode = 'r')
    print(fhelp.read())
    fhelp.close

def battleInit():
    fbattle_info = open('./udata/gamer/battle_info.slmd',mode = 'r')
    ls = fbattle_info.readlines()
    hp = ls[0].strip('hp=')
    mp = ls[1].strip('mp=')
    jsl = ls[2].strip('jsl=')
    watt = ls[3].strip('watt=')
    fatt = ls[4].strip('fatt=')
    wpro = ls[5].strip('wpro=')
    fpro = ls[6].strip('fpro=')

def init():
    fplotp = open('./udata/plot_progress.slmd', mode = 'r')     #获取剧情进度
    flstp = open('./udata/last_place.slmd', mode = 'r')         #获取剧情进度
    global plot_progress                                        #全局变量 剧情进度
    global gamer_place
    plot_progress = fplotp.read()
    gamer_place = flstp.read()
    fplotp.close()
    flstp.close()
    print(plot_progress)#显示剧情序号



init()
showPlot(plot_progress)
while(1):
    getCommand()
