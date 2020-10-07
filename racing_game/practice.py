import pygame
import random
import time
import os

"""
REFERENCE : 이수안컴퓨터연구소 - 파이썬 레이싱 자동차 게임 만들기(2019)
"""
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
class Car:
    # 자동차 이미지 초이스를 위한 리스트
    image_car = os.listdir('assets/comp')

    def __init__(self, x = 0, y = 0, dx = 0, dy = 0):
        self.image = ""
        self.x = x # coord
        self.y = y
        self.dx = dx # direction
        self.dy = dy
        self.base_dir = "assets/comp/"

    def load_image(self):
        self.image = pygame.image.load(self.base_dir + random.choice(self.image_car))
        self.width = self.image.get_rect().size[0]
        self.height = self.image.get_rect().size[1]

    def draw_image(self):
        screen.blit(self.image, [self.x, self.y]) # 그리기
    def move_x(self):
        self.x += self.dx # 방향만큼 더해준다
    def move_y(self):
        self.y += self.dy

    def check_out_of_screen(self):
        # 화면을 넘어가는지 체크
        if self.x + self.width > WINDOW_WIDTH or self.x < 0:
            self.x -= self.dx
    def check_crash(self, car):
        # 현재 내 자동차와 다른 자동차가 부딪히지 않았는가
        if (self.x+self.width > car.x) and (self.x < car.x+car.width) and (self.y < car.y+car.height) and (self.y+self.height>car.y):
            return True
        else:
            return False

def draw_main_menu():
    draw_x = (WINDOW_WIDTH / 2) -200
    draw_y = WINDOW_HEIGHT / 2
    image_intro = pygame.image.load("assets/parrot_main.png") # 인트로 이미지

    screen.blit(image_intro, [draw_x, draw_y - 280])
    font_40 = pygame.font.SysFont("FixedSys", 40, True, False)
    font_30 = pygame.font.SysFont("FixedSys", 30, True, False)

    text_title = font_40.render("PyCar: Racing Car Game", True, BLACK)
    screen.blit(text_title, [draw_x, draw_y])
    text_score = font_40.render("Score: " + str(score), True, WHITE)
    text_start = font_30.render("Press Space Key to Start !", True, GRAY)
    screen.blit(text_start, [draw_x, draw_y + 140])
    pygame.display.flip()

# 게임중에 점수 띄우기
def draw_score():
    font_30 = pygame.font.SysFont("FixedSys", 30, True, False)
    text_score = font_30.render("Score: " + str(score), True, BLACK)
    screen.blit(text_score, [15, 15])


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("pycar : racing car game")
    clock = pygame.time.Clock()

    # sound
    # pygame.mixer.music.load("file dir.wav")
    # sound_crash = pygame.mixer.Sound("crash.wav")
    # sound_engine = pygame.mixer.Sound("engine.wav")

    # 초기위치 --> 중앙으로
    player = Car(WINDOW_WIDTH/2, WINDOW_HEIGHT-150, 0, 0)
    player.load_image()

    # 다른 플레이어들
    cars = []
    car_count = 3
    for i in range(car_count):
        x = random.randrange(0, WINDOW_WIDTH-55)
        y = random.randrange(-150, -50)
        car = Car(x, y, 0, random.randint(5, 10)) # direction 속도 조정
        car.load_image()
        cars.append(car)

    # 차선
    lanes = []
    lane_width = 10
    lane_height = 80
    lane_margin = 20 # 여백
    lane_count = 20
    lane_x = (WINDOW_WIDTH - lane_width)/2
    lane_y = -10

    for i in range(lane_count):
        lanes.append([lane_x, lane_y])
        lane_y += lane_height + lane_margin

    score = 0
    # 이벤트 처리용 바이트 연산
    crash = True
    game_on = True

    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            if crash:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # 게임을 다시 시작하고 싶다(SPACE)
                    crash = False
                    # 장애물 다시 세팅
                    for i in range(car_count):
                        cars[i].x = random.randrange(0, WINDOW_WIDTH-cars[i].width)
                        cars[i].y = random.randrange(-150, -50)
                        cars[i].load_image()
                    # 플레이어 재시작
                    player.load_image()
                    player.x = WINDOW_WIDTH / 2
                    player.dx = 0
                    score = 0
                    pygame.mouse.set_visible(False)
                    # sound_engine.play()
                    time.sleep(5)
                    # pygame.mixer.music.play(-1)
            if not crash:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        player.dx = 4 # 속도 변경 가능
                    if event.key == pygame.K_LEFT:
                        player.dx = -4
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        player.dx = 0 # 속도 변경 가능
                    if event.key == pygame.K_LEFT:
                        player.dx = 0
        screen.fill(GRAY)
        if not crash:
            for i in range(lane_count):
                pygame.draw.rect(screen, WHITE, [lanes[i][0], lanes[i][1], lane_width, lane_height])
                lanes[i][1] += 10 # 속도 변경
                if lanes[i][1] > WINDOW_HEIGHT: # 넘어갔을 때
                    lanes[i][1] = -40-lane_height
            player.draw_image()
            player.move_x()
            # 뒤로도 움직일 수 있게 해주고 싶으면 move_y 사용해도 됨
            player.check_out_of_screen()

            for i in range(car_count):
                cars[i].draw_image()
                cars[i].y += cars[i].dy # 컴퓨터 자동차들은 위 아래로 움직임
                if cars[i].y > WINDOW_HEIGHT:
                    score += 10 # 장애물을 피했으므로 점수 부여
                    cars[i].x = random.randrange(0, WINDOW_WIDTH - cars[i].width)
                    cars[i].y = random.randrange(-150, -50)
                    cars[i].dy = random.randint(5, 10)
                    cars[i].load_image()
            for i in range(car_count):
                if player.check_crash(cars[i]):
                    # 자동차와 충돌되었는가
                    crash = True
                    # pygame.mixer.music.stop()
                    # sound_crash.play()
                    time.sleep(2)
                    pygame.mouse.set_visible(True)
                    break
            draw_score() # 만들어야함
            pygame.display.flip()
        else:
            draw_main_menu() # 만들어야함
        clock.tick(60)
    pygame.quit()
