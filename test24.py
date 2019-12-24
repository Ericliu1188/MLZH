from mlzhlc import *
import time
from random import choice
from datetime import datetime

# randomlist = [1] * 155 + [987] * 3
# yijielist = [1] * 50 + [2] * 20 + [3, 4, 5] * 5
# print(randomlist)

def log_in():
    find_pic_andclick('登录1')
    if find_pic_inscreen('登录密码'):
        find_pic_andclick('登录密码')
        pag.typewrite('lpy111888')
        find_pic_andclick('点击登录')
    # if find_pic_inscreen('登录过期'):
        # find_pic_andclick('登录过期')
    find_pic_andclick('再试一次')
    find_pic_andclick('取消')
    find_pic_andclick('认证失败')
    # while not find_pic_inscreen('登录1'):
        # pag.press('esc',pause=0.5)
    #     if find_pic_inscreen("战斗图标"):
    #         break
    

# def get_out():
#     while not find_pic_inscreen('战斗图标'):
#         find_pic_andclick('不结束游戏')
#         pag.press('esc', pause=0.5)
#         # click_in_safe()
#         # find_pic_andclick('关闭限时道具确定')
#         find_pic_andclick('不结束游戏')

def ugfight():
    while not find_pic_inscreen('战斗图标'):
        pag.press('esc')
    find_pic_andclick('战斗图标')
    find_pic_andclick('地下城')
    find_pic_andclick('龙')
    find_pic_andclick('龙10')
    find_pic_andclick("开始战斗啦")

def jingjichang_action_after_findpic(shangdian=False):
    while not find_pic_inscreen('战斗图标'):
        pag.press('esc')
    find_pic_andclick("JJC小翅膀")
    find_pic_andclick('竞技场战斗图标', (-1, 1), 2, 0)
    find_pic_andclick('JJC开始战斗', pause=10, qianzhi=0)
    find_pic_andclick('自动打怪按钮', (-1, 1), 0, 0)
    find_pic_andclick('战斗胜利红水JJC', (-177, 100), 1, 0)
    find_pic_andclick('自己头像', (-1, 1), 1, 0)
    find_pic_andclick('确认按钮', (-1, 1), 1, 0)
    find_pic_andclick('刷新列表', (-1, 1), 1, 0)

    find_pic_andclick('刷新列表2', (-1, 1), 1, 0)
    # find_pic_andclick('战斗胜利红水', (-177, 170))

    find_pic_andclick('世界地图', (-318, -100), 0, 0)
    # find_pic_andclick('竞技场商店', (322, -183), 1, 0)
    # find_pic_andclick('关闭', (-1, 1), 1, 0)
    #find_pic_andclick('战斗胜利红水', (-177, 130), 0, 0)
    print('完成了一次检测~~, 休息一会')

if __name__ == '__main__':
	while True:
	    while find_pic_inscreen('点击登录'):
	        # get_out()
	        log_in()
	        time.sleep(1800)
	    while find_pic_inscreen("商店图标"):
	        jingjichang_action_after_findpic()
	    while find_pic_inscreen("竞技场商店"):
	        ugfight()

 