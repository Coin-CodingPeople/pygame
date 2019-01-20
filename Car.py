import pygame

# 모든 pygame Sprite는 pygame.sprite.Sprite를 상속받아야 한다
class Car(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # 차의 공간을 결정한다
        # self.image = pygame.Surface([width, height])

        # 차의 모습을 결정한다.
        # color에는 차의 색이 담긴다
        # EX) (255, 0, 0): 빨강, (0, 255, 0): 초록, (0, 0, 255): 파랑
        # pygame.draw.rect(self.image, color, [0, 0, width, height])

        # 차 그림을 가져온다
        self.image = pygame.image.load("./car.jpeg")

        # 차 그림의 크기를 정한다
        self.image = pygame.transform.scale(self.image, (width, height))

        # pygame에서 사용될 이미지 데이터를 rect 변수에 저장한다
        self.rect = self.image.get_rect()
    
    def moveRight(self):
        self.rect.x += 10

    def moveLeft(self):
        self.rect.x -= 10

    def moveUp(self):
        self.rect.y -= 10

    def moveDown(self):
        self.rect.y += 10
