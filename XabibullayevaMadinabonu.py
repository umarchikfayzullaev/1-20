import cv2
import numpy as np
from collections import deque
from enum import Enum
import time
import pyautogui

# инициализируем
video = cv2.VideoCapture(1) # id устройства камеры
hands_haar_cascade = cv2.CascadeClassifier("rpalm.xml")

# цикл

class Moves(Enum):
	LEFT = 1
	TOP = 2
	RIGHT = 3
	DOWN = 4

moves_queue = deque([0]*4, maxlen=4)
last_vertical, last_horizontal = 0, 0
ACTION_DELAY = 500 # ms
last_action_time = time.perf_counter_ns()
while True:
	_r, frame = video.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	hands = hands_haar_cascade.detectMultiScale(gray, 1.3, 4)

	if len(hands):
		for x, y, w, h in hands:
			cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)

			if ((time.perf_counter_ns() - last_action_time) // 1_000_000) > ACTION_DELAY:
				if last_vertical or last_horizontal:
					# get diff
					diff_vertical = y - last_vertical
					diff_horizontal = x - last_horizontal

					if abs(diff_vertical) > abs(diff_horizontal):
						# vertical movement
						if diff_vertical < 0:
							moves_queue.appendleft(Moves.TOP)
						else:
							moves_queue.appendleft(Moves.DOWN)
					else:
						# horizontal movement
						if diff_horizontal > 0:
							moves_queue.appendleft(Moves.LEFT)
						else:
							moves_queue.appendleft(Moves.RIGHT)

				# save last known pos
				last_vertical = y
				last_horizontal = x

				# check for action
				move_made = False
				if all(m == Moves.LEFT for m in moves_queue):
					# LEFT
					print("LEFT")
					move_made = True
					pyautogui.keyDown('left')
					pyautogui.keyUp('left')
				elif all(m == Moves.TOP for m in moves_queue):
					# TOP
					print("TOP")
					move_made = True
					pyautogui.keyDown('up')
					pyautogui.keyUp('up')
				elif all(m == Moves.RIGHT for m in moves_queue):
					# RIGHT
					print("RIGHT")
					move_made = True
					pyautogui.keyDown('right')
					pyautogui.keyUp('right')
				elif all(m == Moves.DOWN for m in moves_queue):
					# DOWN
					print("DOWN")
					move_made = True
					pyautogui.keyDown('down')
					pyautogui.keyUp('down')

				if move_made:
					last_action_time = time.perf_counter_ns()
					last_horizontal = 0
					last_vertical = 0
					moves_queue = deque([0]*4, maxlen=4)


	frame = cv2.resize(frame, (1280//2, 720//2))
	cv2.imshow("Test", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# завершение
video.release()
cv2.destroyAllWindows()