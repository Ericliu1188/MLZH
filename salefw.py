from mlzhlc import *
import time

def daigouliang(shangdian=True):
    # save_screen()
    #click_in_safe()
    #click_in_safe()

    # find_pic_andclick('五星符文', (-1, -1), 0, 0)
    #find_pic_andclick('确认获得材料', (-1, -1), 0, 0)
    #find_pic_andclick('战斗死亡', (320, -1), 0, 0)
    #find_pic_andclick('确认卖出符文', (0, 0), 0, 0)
    #find_pic_andclick('开始战斗啦', (-1, -1), 0, 0)
    #find_pic_andclick('关闭图标')
    #find_pic_andclick('出售', (-1, -1), 1, 0)
    #find_pic_andclick('礼物箱', (-1, -1), 0, 0)
    #find_pic_andclick('世界地图', (-260, -142), 0, 0)
    #time.sleep(1)
    #pag.moveTo(1400,230)
    #pag.click()


    
    #if find_pic_inscreen('4星符文'):
    find_pic_andclick('拉菲斯',(405,426),0,0)
    find_pic_andclick('出售符文')
    find_pic_andclick('确认出售符文')
    find_pic_andclick('确认出售符文')
    time.sleep(1)
    #if find_pic_inscreen('5星判定'):
        #return False

    '''        
    if find_pic_inscreen('开始战斗啦'):
        huangouliang()
        find_pic_andclick('开始战斗啦')
        pass
    '''

if __name__ == '__main__':
    # huangouliang()
    i = 0
    while i < 30:
        daigouliang(0)
        i += 1