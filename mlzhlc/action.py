import pyautogui as pag
import os
import pyscreeze
import time
import pyperclip
from random import randint

from . import mlzhpath

pag.PAUSE = 0.25
pic_path = mlzhpath.__file__[:-11] + 'pic\\'
sav_path = mlzhpath.__file__[:-11] + 'sav\\'


def ppaste(astr):
    pyperclip.copy(astr)
    pag.hotkey('ctrl', 'v')


def click_at_point(position: tuple):
    assert isinstance(position, tuple)
    position = position[0] + randint(-3, 3), position[1] + randint(-3, 3)
    pag.moveTo(position, tween=pag.easeInQuad, duration=0.5)
    pag.click()
    pag.moveTo(position, pause=0.25)


def rand_choose(zuobiao_pack):
    '''zuobiao_pack : [(x,y),weight,hight]'''
    atuple, weight, hight = zuobiao_pack
    x = atuple[0] + randint(0, weight)
    y = atuple[1] + randint(0, hight)
    return (x, y)


def click_in_block(position_block):
    '''[(x,y),weight,hight]'''
    position = rand_choose(position_block)
    pag.moveTo(position, tween=pag.easeInQuad, duration=0.33, pause=0.2)
    pag.click()

    position = rand_choose(position_block)
    pag.moveTo(position, duration=0.25, pause=0.25)


def click_in_block2(position_block):
    '''[(x,y),weight,hight]'''
    position = rand_choose(position_block)
    pag.moveTo(position, pause=0)
    pag.click(pause=0)


def find_pic_inscreen(pic_name: str):
    return pag.locateOnScreen(pic_path + pic_name + '.png', grayscale=True)


def find_pic_andclick(pic_name, moveXY=(0, 0),
                      pause=0.5, qianzhi=0.5):
    time.sleep(qianzhi)
    findres = find_pic_inscreen(pic_name)
    if findres:
        print('Log--mlzh :::   发现 %s' % pic_name)
        position_block = [(findres.left + moveXY[0], findres.top + moveXY[1]),
                          findres.width, findres.height]
        click_in_block(position_block)
        time.sleep(pause)  # 如果发现了，休息一秒
    else:
        print('Log--mlzh ::: 未发现 %s' % pic_name)


def save_screen(picname=False):
    time.sleep(2)
    if picname:
        pag.screenshot().save(sav_path + str(picname) + '.png')
    else:
        pag.screenshot().save(sav_path + str(randint(1, 8)) + '.png')
