import pygame
from Car import Car

 # 우리의 어플리케이션!
class App:
    # 게임 내부 초기화 이전에 해야할 작업들
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

         # 게임의 창 크기, 바꿔보세요!
        self.size = self.weight, self.height = 640, 400

    # 게임을 초기화 할 때 해야할 작업들
    def on_init(self):
        pygame.init()
         
        # 디스플레이 모드 설정, 디스플레이 데이터를 screen이라는 변수에 담는다
        self.screen = pygame.display.set_mode(self.size, 0, 16)

        # 창 색깔 설정, 바꿔보세요!
        self.screen.fill((255, 255, 255))

        # 창 이름 설정, 바꿔보세요!
        pygame.display.set_caption("Hello Pygame!")

        # running flag 초기화
        # flag란? 단순 참/거짓 값을 통해 프로그램을 제어하기 위한 변수
        # 이 프로그램에선 running = True 일 때만 게임이 실행되도록 한다
        self.running = True

        # 게임의 모든 sprite를 포함하는 변수
        self.sprites = pygame.sprite.Group()

        # playerCar에 Car라는 sprite를 만들어 담는다.
        # Car 색깔 바꿔보세요!
        # EX) (255, 0, 0) -> (0, 255, 0)
        self.playerCar = Car((0, 255, 0), 100, 30)
        self.playerCar.rect.x = 0
        self.playerCar.rect.y = 0

        # playerCar를 게임 sprite 관리 그룹에 추가한다.
        self.sprites.add(self.playerCar)

    # 이벤트가 발생할 때 해야할 작업들
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                self.playerCar.moveRight()
            elif event.key==pygame.K_LEFT:
                self.playerCar.moveLeft()
            elif event.key==pygame.K_UP:
                self.playerCar.moveUp()
            elif event.key==pygame.K_DOWN:
                self.playerCar.moveDown()

    # 매 반복시마다 해야할 작업들
    def on_loop(self):
        # 게임의 sprite들에 대한 정보를 업데이트한다
        self.sprites.update()

    # 화면을 보여줄 때 마다 해야할 작업들
    def on_render(self):
        # 바탕그리기
        self.screen.fill((255, 255, 255))
        
        # 게임의 sprite들을 screen에 그린다
        self.sprites.draw(self.screen)

    # 게임을 종료할 때 해야할 작업들
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        # 이 코드는 무시하셔도 좋습니다.
        if self.on_init() == False:
            self.running = False

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

             # 화면이 몇 초에 한번씩 바뀔 것인가를 설정
            self.clock.tick(60)

             # 화면 업데이트
            pygame.display.flip()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
