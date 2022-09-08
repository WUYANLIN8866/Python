import random
import sys
import time
import pygame
from pygame.locals import *
from collections import deque

SCREEN_WIDTH = 600      # 屏幕寬度
SCREEN_HEIGHT = 480     # 屏幕高度
SIZE = 20               # 小方格大小
LINE_WIDTH = 1          # 網格線寬度

# 遊戲區域的坐標範圍
SCOPE_X = (0, SCREEN_WIDTH // SIZE - 1)
SCOPE_Y = (2, SCREEN_HEIGHT // SIZE - 1)

# 食物的分值及顏色
FOOD_STYLE_LIST = [(10, (255, 100, 100)), (20, (100, 255, 100)), (30, (100, 100, 255))]

LIGHT = (100, 100, 100)
DARK = (200, 200, 200)      # 蛇的顏色
BLACK = (0, 0, 0)           # 網格線顏色
RED = (200, 30, 30)         # 紅色，GAME OVER 的字體顏色
BGCOLOR = (40, 40, 60)      # 背景色


def print_text(screen, font, x, y, text, fcolor=(255, 255, 255)):
  imgText = font.render(text, True, fcolor)
  screen.blit(imgText, (x, y))


# 初始化蛇
def init_snake():
  snake = deque()
  snake.append((2, SCOPE_Y[0]))
  snake.append((1, SCOPE_Y[0]))
  snake.append((0, SCOPE_Y[0]))
  return snake


def create_food(snake):
  food_x = random.randint(SCOPE_X[0], SCOPE_X[1])
  food_y = random.randint(SCOPE_Y[0], SCOPE_Y[1])
  while (food_x, food_y) in snake:
      # 如果食物出現在蛇身上，則重來
      food_x = random.randint(SCOPE_X[0], SCOPE_X[1])
      food_y = random.randint(SCOPE_Y[0], SCOPE_Y[1])
  return food_x, food_y


def get_food_style():
  return FOOD_STYLE_LIST[random.randint(0, 2)]


def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption('貪吃蛇')

  font1 = pygame.font.SysFont('SimHei', 24)  # 得分的字體
  font2 = pygame.font.Font(None, 72)  # GAME OVER 的字體
  fwidth, fheight = font2.size('GAME OVER')

  # 如果蛇正在向右移動，那麼快速點擊向下向左，由於程序刷新沒那麼快，向下事件會被向左覆蓋掉，導致蛇後退，直接GAME OVER
  # b 變量就是用於防止這種情況的發生
  b = True

  # 蛇
  snake = init_snake()
  # 食物
  food = create_food(snake)
  food_style = get_food_style()
  # 方向
  pos = (1, 0)

  game_over = True
  start = False  # 是否開始，當start = True，game_over = True 時，才顯示 GAME OVER
  score = 0  # 得分
  orispeed = 0.5  # 原始速度
  speed = orispeed
  last_move_time = None
  pause = False  # 暫停

  while True:
      for event in pygame.event.get():
          if event.type == QUIT:
              sys.exit()
          elif event.type == KEYDOWN:
              if event.key == K_RETURN:
                  if game_over:
                      start = True
                      game_over = False
                      b = True
                      snake = init_snake()
                      food = create_food(snake)
                      food_style = get_food_style()
                      pos = (1, 0)
                      # 得分
                      score = 0
                      last_move_time = time.time()
              elif event.key == K_SPACE:
                  if not game_over:
                      pause = not pause
              elif event.key in (K_w, K_UP):
                  # 这个判断是为了防止蛇向上移时按了向下键，导致直接 GAME OVER
                  if b and not pos[1]:
                      pos = (0, -1)
                      b = False
              elif event.key in (K_s, K_DOWN):
                  if b and not pos[1]:
                      pos = (0, 1)
                      b = False
              elif event.key in (K_a, K_LEFT):
                  if b and not pos[0]:
                      pos = (-1, 0)
                      b = False
              elif event.key in (K_d, K_RIGHT):
                  if b and not pos[0]:
                      pos = (1, 0)
                      b = False

      # 填充背景色
      screen.fill(BGCOLOR)
      # 画网格线 竖线
      for x in range(SIZE, SCREEN_WIDTH, SIZE):
          pygame.draw.line(screen, BLACK, (x, SCOPE_Y[0] * SIZE), (x, SCREEN_HEIGHT), LINE_WIDTH)
      # 画网格线 横线
      for y in range(SCOPE_Y[0] * SIZE, SCREEN_HEIGHT, SIZE):
          pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y), LINE_WIDTH)

      if not game_over:
          curTime = time.time()
          if curTime - last_move_time > speed:
              if not pause:
                  b = True
                  last_move_time = curTime
                  next_s = (snake[0][0] + pos[0], snake[0][1] + pos[1])
                  if next_s == food:
                      # 吃到了食物
                      snake.appendleft(next_s)
                      score += food_style[0]
                      speed = orispeed - 0.03 * (score // 100)
                      food = create_food(snake)
                      food_style = get_food_style()
                  else:
                      if SCOPE_X[0] <= next_s[0] <= SCOPE_X[1] and SCOPE_Y[0] <= next_s[1] <= SCOPE_Y[1] \
                              and next_s not in snake:
                          snake.appendleft(next_s)
                          snake.pop()
                      else:
                          game_over = True

      # 画食物
      if not game_over:
          # 避免 GAME OVER 的时候把 GAME OVER 的字给遮住了
          pygame.draw.rect(screen, food_style[1], (food[0] * SIZE, food[1] * SIZE, SIZE, SIZE), 0)

      # 画蛇
      for s in snake:
          pygame.draw.rect(screen, DARK, (s[0] * SIZE + LINE_WIDTH, s[1] * SIZE + LINE_WIDTH,
                                          SIZE - LINE_WIDTH * 2, SIZE - LINE_WIDTH * 2), 0)

      print_text(screen, font1, 30, 7, f'speed: {score//100}')
      print_text(screen, font1, 450, 7, f'point: {score}')

      if game_over:
          if start:
              print_text(screen, font2, (SCREEN_WIDTH - fwidth) // 2, (SCREEN_HEIGHT - fheight) // 2, 'GAME OVER', RED)

      pygame.display.update()


if __name__ == '__main__':
  main()