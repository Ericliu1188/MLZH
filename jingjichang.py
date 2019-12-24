from mlzhlc import *
import time


def jingjichang_action_after_findpic(shangdian=False):
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
    find_pic_andclick('竞技场商店', (322, -183), 1, 0)
    find_pic_andclick('关闭', (-1, 1), 1, 0)
    #find_pic_andclick('战斗胜利红水', (-177, 130), 0, 0)
    print('完成了一次检测~~, 休息一会')


if __name__ == '__main__':
    while True:
        #click_in_safe()
        #click_in_safe()
        jingjichang_action_after_findpic()

