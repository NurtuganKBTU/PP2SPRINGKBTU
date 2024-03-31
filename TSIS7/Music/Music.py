import os, time, pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
musics = os.listdir("/Users/acer/OneDrive/Рабочий стол/Everything/2nd Semester/PP2/LAB1/TSIS7/Music/Playlist")
path = "/Users/acer/OneDrive/Рабочий стол/Everything/2nd Semester/PP2/LAB1/TSIS7/Music/Playlist/{}"
idx = 0
pygame.mixer.music.load(path.format(musics[idx]))
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play()
running = True
mus = True
while running:
   time.sleep(0.1)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
   pressed = pygame.key.get_pressed()
   if pressed[pygame.K_SPACE]:
      if mus == False:
         pygame.mixer.music.unpause()
         mus = True
      else:
         pygame.mixer.music.pause()
         mus = False
   
   if pressed[pygame.K_q]:
      pygame.mixer.music.stop()
   if pressed[pygame.K_RIGHT]:
      idx += 1
      if idx == len(musics):
         idx = 0
      pygame.mixer.music.load(path.format(musics[idx]))
      pygame.mixer.music.play()
   if pressed[pygame.K_LEFT]:
      idx -= 1
      if idx == -1:
         idx = len(musics)
      pygame.mixer.music.load(path.format(musics[idx]))
      pygame.mixer.music.play()
      pygame.display.flip()
