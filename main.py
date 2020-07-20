import play, json, os
a = open('config.json', 'r')
b = json.load(a)
ballinfo = b['ball']
boxinfo = b['box']
textinfo = b['text']
balls = []


paused = False
text1 = play.new_text('X: 0, Y: 0', x = play.screen.left + 100, y = play.screen.top - 20, font_size = 30)
text2 = play.new_text(f'ObjCount: {len(play.all_sprites) - 1}', x = play.screen.left + 85, y = play.screen.top - 40, font_size = 30)
text3 = play.new_text(f'', x = play.screen.left + 120, y = play.screen.top - 60, font_size = 30)
text4 = play.new_text(f'', x = play.screen.left + 80, y = play.screen.top - 80, font_size = 30)
obj = 0
@play.when_key_pressed('b')
def make_ball(key):
		for ball in balls:
			if play.mouse.is_touching(ball):
				return
		ball = play.new_circle(color=play.random_color(), y=play.mouse.y, x=play.mouse.x, radius=ballinfo['radius'])
		print(f"New Ball obj spawned at x = {play.mouse.x}, y = {play.mouse.y} with size = {ballinfo['radius']},\nbounce = {ballinfo['bounce']}, mass = {ballinfo['mass']}, friction = {ballinfo['friction']}\n")
		ball.start_physics(bounciness=ballinfo['bounce'], mass=ballinfo['mass'], friction=ballinfo['friction'])
		ball.is_being_dragged = False

		@ball.when_clicked
		def click_ball():
			print(f'Ball obj clicked at x = {play.mouse.x}, y = {play.mouse.y}\n')
			text3.words = f'Color: {ball.color}'
			text3.show()
			text4.words = f"Mass: {ballinfo['mass']}"
			text4.show()
			ball.is_being_dragged = True

		@play.mouse.when_click_released
		def release_ball():
				for ball in balls:
						ball.is_being_dragged = False
						text3.hide()
						text4.hide()

		balls.append(ball)

@play.when_key_pressed('c')
def make_box(key):
		for ball in balls:
			if play.mouse.is_touching(ball):
				return
		
		ball = play.new_box(color=play.random_color(), y=play.mouse.y, x=play.mouse.x, width=boxinfo['width'], height=boxinfo['height'])
		print(f"New Box obj spawned at x = {play.mouse.x}, y = {play.mouse.y} with width = {boxinfo['width']},\nheight={boxinfo['height']}, bounce = {boxinfo['bounce']}, mass = {boxinfo['mass']}, friction = {boxinfo['friction']}\n")
		ball.start_physics(bounciness=boxinfo['bounce'], mass=boxinfo['mass'], friction=boxinfo['friction'])
		ball.is_being_dragged = False

		@ball.when_clicked
		def click_ball():
			print(f'Box obj clicked at x = {play.mouse.x}, y = {play.mouse.y}\n')
			text3.words = f'Color: {ball.color}'
			text3.show()
			text4.words = f"Mass: {boxinfo['mass']}"
			text4.show()
			ball.is_being_dragged = True


		@play.mouse.when_click_released
		def release_ball():
				for ball in balls:
						ball.is_being_dragged = False
						text3.hide()
						text4.hide()

		balls.append(ball)

@play.when_key_pressed('t')
def make_text(key):
		for ball in balls:
			if play.mouse.is_touching(ball):
				return
		words = input('Enter text: ')
		ball = play.new_text(words=words, color=play.color.color_name_to_rgb("black"), y=play.mouse.y, x=play.mouse.x)
		print(f"New Text obj spawned at x = {play.mouse.x}, y = {play.mouse.y} with text = {words}", end = "")
		if textinfo['move'] == True:
			ball.start_physics(bounciness=boxinfo['bounce'], mass=boxinfo['mass'], friction=boxinfo['friction'])
			print(f" ,physics = {textinfo['move']}, bounce = {textinfo['bounce']}, mass = {textinfo['mass']}, friction = {textinfo['friction']}\n")
		else:
			print("\n")
			pass
		ball.is_being_dragged = False

		@ball.when_clicked
		def click_ball():
			print(f'Box obj clicked at x = {play.mouse.x}, y = {play.mouse.y}\n')
			text3.words = f'Color: {ball.color}'
			text3.show()
			text4.words = f"Mass: {boxinfo['mass']}"
			text4.show()
			ball.is_being_dragged = True


		@play.mouse.when_click_released
		def release_ball():
				for ball in balls:
						ball.is_being_dragged = False
						text3.hide()
						text4.hide()

		balls.append(ball)

@play.when_key_pressed('z')
def press_space(key):
		print('Mix event\n')
		for ball in balls:
				ball.physics.y_speed = play.random_number(80, 100)
				ball.physics.x_speed = play.random_number(-30, 30)

@play.when_key_pressed('r')
def change_color(key):
	print('Change Color event\n')
	for ball in balls:
		ball.color = play.random_color()

@play.when_key_pressed(' ')
def reset(key):
	play.all_sprites.clear()
	balls.clear()
	play.all_sprites.append(text1)
	play.all_sprites.append(text2)
	play.all_sprites.append(text3)
	os.system("clear")
	print("Reset event")

def setup():
	os.system('clear')
	print('Program Start event')

play.when_program_starts(setup)

@play.repeat_forever
def loop():
		text1.words = f'X: {round(play.mouse.x)}, Y:{round(play.mouse.y)}'
		objcount = len(balls)
		text2.words = f'ObjCount: {objcount}'
		for ball in balls:
				if ball.is_being_dragged:
						ball.physics.x_speed = play.mouse.x - ball.x
						ball.physics.y_speed = play.mouse.y - ball.y
play.start_program()
