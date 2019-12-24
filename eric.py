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
    if find_pic_inscreen('登录过期'):
        find_pic_andclick('登录过期')
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



if __name__ == '__main__':
    while True:
        # get_out()
        log_in()


 