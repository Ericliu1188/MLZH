from mlzhlc import *
import time


def shilianta_action_after_findpic(shangdian=False):
    find_pic_andclick('战斗胜利红水', (-177, 100), 1, 0)
    find_pic_andclick('战斗胜利红水', (-177, 100), 1, 0)
    # find_pic_andclick('战斗胜利红水', (-177, 170))
    find_pic_andclick('召唤石确认', (-1, 1), 0, 0)
    find_pic_andclick('世界地图', (-386, -130), 0, 0)
    find_pic_andclick('开始战斗啦', pause=0, qianzhi=0)
    
    print('完成了一次检测~~, 休息一会')


if __name__ == '__main__':
    while True:
        #click_in_safe()
        #click_in_safe()
        shilianta_action_after_findpic()
