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

class WorldPlace:
    def __init__(self,name,x,y,w,e,s,n):
        self.name = name
        self.x = x
        self.y = y
        self.w = w
        self.e = e
        self.s = s
        self.n = n
    
    def getWorldPlaceDic():
        return {'name':name,'x':x,'y':y,'w':w,'e':e,'s':s,'n':n}

def showPlot(progress): #剧情显示函数
    plot_path = './plot/ch/' + str(progress) + '.slmp'
    if (int(progress) <= 2):
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
    elif (com[0:11] == 'battle with'):  #进入战斗
        com1 = com.lstrip('battle ')
        com2 = com1.lstrip('with')
        com3 = com2.lstrip(' ')
        battleInit(com3)
    elif (com[0:7] == 'move to'):
        com1 = com.lstrip('move ')
        com2 = com1.lstrip('to')
        com3 = com2.lstrip(' ')
        print('移动到' + com3)
    else:
        print('\033[1;31;40m未知指令\033[0m')
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
    print('---')
    print('\033[1;34m帮助：\033[0m')
    fhelp = open('./bin/files/help.slmf',encoding = 'utf-8',mode = 'r')
    print(fhelp.read())
    fhelp.close
    print('---')

def battleInit(enemy):      #战斗初始化
    print(enemy)
    ls_info_me = battleReadFiles('./udata/gamer/battle_info.slmd')
    enemy_url = './bin/battleperson/normal/' + enemy + '.slmd'
    print(enemy_url)
    ls_info_enemy = battleReadFiles(enemy_url)
    if(ls_info_enemy == 0):
        print('\033[1;31m错误,未找到人物！\033[0m')
        return
    print(ls_info_enemy)
    print(ls_info_me)
    print('----------\033[1;33m战斗开始\033[0m----------')
    '''
    hp = ls_info_me[0]
    mp = ls_info_me[1]
    jsl = ls_info_me[2]
    watt = ls_info_me[3]
    fatt = ls_info_me[4]
    wpro = ls_info_me[5]
    fpro = ls_info_me[6]
    '''

def battleReadFiles(url):  #读取战斗数据
    try:
        fbattle_info = open(url,mode = 'r')
        ls = fbattle_info.readlines()
        ls[0] = ls[0].strip('hp=')
        ls[1] = ls[1].strip('mp=')
        ls[2] = ls[2].strip('jsl=')
        ls[3] = ls[3].strip('watt=')
        ls[4] = ls[4].strip('fatt=')
        ls[5] = ls[5].strip('wpro=')
        ls[6] = ls[6].strip('fpro=')
        fbattle_info.close()
        return ls
    except IOError:
        return 0

def readMap(place):
    total_place = 0
    all_area = (0,0)
    if(place == 'map all'):
        print('输出全部地图功能暂未上线，请直接输入map获得地图')
    else:
        url_name = './bin/world/map/' + place + '/name.slmd'
        url_lj = './bin/world/map/' + place + '/adjacency.slmd'
        map_name = open(url_name,encoding = 'utf-8', mode = 'r')
        map_lj = open(url_lj, mode = 'r')
        ls_name = map_name.readlines()
        ls_lj = map_lj.readlines()

        for i in range(int(3)):
            for i2 in range(int (3)):
                

'''
def movePlace(place):
    if (place == e):
        
    elif (place == w):

    elif (place == s):

    elif (place == n):

    else:
        print('移动到->' + place)
'''
def init():
    fplotp = open('./udata/plot_progress.slmd', mode = 'r')     #获取剧情进度
    flstp = open('./udata/last_place.slmd', mode = 'r')         #获取剧情进度
    global plot_progress                                        #全局变量 剧情进度
    global gamer_place
    plot_progress = fplotp.read()
    gamer_place = flstp.read()
    fplotp.close()
    flstp.close()
    print(plot_progress)                                        #显示剧情序号

init()
showPlot(plot_progress)
while(1):
    getCommand()