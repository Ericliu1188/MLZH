from mlzhlc import *
import time

'''
def huangouliang(num=15):
    ysj = find_pic_inscreen('右上角')
    ysj = ysj.left + ysj.width / 2, ysj.top + ysj.height / 2

    pxy = find_pic_inscreen('左下角')
    pxy = pxy.left + pxy.width / 2, pxy.top + pxy.height / 2

    for i in range(num):
        pag.click(ysj, duration=0.5, pause=0.11)
        pag.dragTo(pxy, duration=0.5, pause=0.11)

    find_pic_andclick('空白格子', (-250, 0))
    find_pic_andclick('空白格子', (-107, 0))
    find_pic_andclick('空白格子', (-177, 40))

    find_pic_andclick('黑色青蛙', (-180, 0))
    find_pic_andclick('黑色青蛙', (-60, 0))
    find_pic_andclick('黑色青蛙', (-120, 0))
'''

def daigouliang(shangdian=True):
    # save_screen()
    #click_in_safe()
    #click_in_safe()

    find_pic_andclick('战斗胜利红水', (-260, 200), 1, 0)
    find_pic_andclick('战斗胜利红水', (-260, 200), 1, 0)
    find_pic_andclick('战斗胜利红水', (-260, 145), 1, 0)
    find_pic_andclick('战斗胜利红水', (-260, 145), 1, 0)
    #find_pic_andclick('获得符石道具', (-1, -1), 0, 0)
    #find_pic_andclick('确认获得材料', (-1, -1), 0, 0)
    #find_pic_andclick('战斗死亡', (320, -1), 0, 0)
    #find_pic_andclick('确认卖出符文', (0, 0), 0, 0)
    #find_pic_andclick('开始战斗啦', (-1, -1), 0, 0)
    #find_pic_andclick('关闭图标')
    #find_pic_andclick('出售', (-1, -1), 1, 0)
    #find_pic_andclick('礼物箱', (-1, -1), 0, 0)
    find_pic_andclick('世界地图', (-260, -142), 0, 0)
    #time.sleep(1)
    #pag.moveTo(1400,230)
    #pag.click()


    
    if find_pic_inscreen('商店图标'):
        if find_pic_inscreen('礼物箱图标'):
            find_pic_andclick('礼物箱图标')
            find_pic_andclick('收取礼物箱闪电')
            find_pic_andclick('关闭礼物箱')
            find_pic_andclick('世界地图', (-260, -145))
        else:
            find_pic_andclick('商店图标')
            find_pic_andclick('钻石能量')
            find_pic_andclick('确认钻石能量')
            find_pic_andclick('购买完毕')
            find_pic_andclick('关闭购买框')
    '''        
    if find_pic_inscreen('开始战斗啦'):
        huangouliang()
        find_pic_andclick('开始战斗啦')
        pass
    '''

if __name__ == '__main__':
    # huangouliang()
    while True:
        daigouliang(0)
