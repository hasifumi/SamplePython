#coding: utf-8
import sys, os, pygame
from pygame.locals import * #定数などの呼び出しを楽に

pygame.init() #pygameの初期化

size = 480, 360
screen = pygame.display.set_mode(size) #スクリーンサイズを設定し、ウィンドウ表示

running = True
while running:
    for event in pygame.event.get(): #イベントをキューから取り出し
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            #もしウィンドウクローズか、エスケープキーが押されたらループを抜ける
            running = False
sys.exit()
