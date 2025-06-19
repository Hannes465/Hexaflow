import pygame,sys,time,math
s_lvl2 = False
h_win = False
r1 = False
r2 = False
sperre1 = False
sperre2 = False
show_rectangles = False
saved_key = "k_p"
scounter1 = 0
scounter2 = 0
r1counter = 0
r2counter = 0
l2money = 200
oncer = 0
oncerlast = 1
SCREEN_HIGHT = 900
SCREEN_WHITH = 1600
endlesstimer = 0
pygame.init()
start = True
volume = 0.5
screen = pygame.display.set_mode((SCREEN_WHITH, SCREEN_HIGHT),pygame.FULLSCREEN)
FS = True
pygame.display.set_caption("Hexaflow")
pygame.mixer.init()
level2 = "lvl2m.mp3"
menu = "menu.mp3"
rick = "rick roll.mp3"
lvl1s = "lvl1.mp3"
hardcorem = "Hardcore.mp3"
lvl1h = "lvl1h.mp3"
lvl2h = "lvl2h.mp3"
endlessm = "endless.mp3"
hardcore = False
num = 1
pygame.mixer.music.set_volume(volume)
def spiele_musik(datei):
    pygame.mixer.music.load(datei)
    pygame.mixer.music.play(-1,0,0)
 
clock = pygame.time.Clock()
cooldown =  0.2
last_click_time = 0
last_click_time2 = 0
lvl1lives = 200
spawnedlvl1= 0
spawnlvl1 = 0
healertimer = 0
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255,0,0)
gray = (130,130,130)
GRAY = (200, 200, 200)
lightgray = (160,160,160)
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)
DARK_BLUE = (0, 90, 200)
TEXT_COLOR = (255, 255, 255)
new_tower = (0,0)
 
 
 
font_large = pygame.font.SysFont("Georgia", 72)
font = pygame.font.SysFont("Georgia", 32)
font_small = pygame.font.SysFont(None, 36)
font_extra = pygame.font.SysFont("Georgia", 120)
fontnor = pygame.font.SysFont("Georgia", 54)
ec = 0

 
 
 
start_text1 = font_large.render("Hannes Entertainment", True, red)
start_text2 = font_small.render("presents", True, white)
main_text = font_extra.render("Hexaflow", True, red)
hexa = font_large.render("Hexaflow",True,red)
 
hexa = hexa.convert_alpha()
start_text1 = start_text1.convert_alpha()
start_text2 = start_text2.convert_alpha()
main_text_rect = main_text.get_rect(center=(SCREEN_WHITH/2, SCREEN_HIGHT/2))
setting = font_large.render("Settings", True, red)
win = False
w_lvl1 = False
w_lvl2 = False
lvl1speicher = False
lvl2speicher = False
endless = False
s_endlessend = False
lvl2time = 0
 
image = pygame.image.load("planet06.png").convert_alpha()
image_scaled = pygame.transform.scale(image, (SCREEN_HIGHT, SCREEN_HIGHT))
planet01 = pygame.image.load("planet01.png").convert_alpha()
planet01 = pygame.transform.scale(planet01, (SCREEN_HIGHT, SCREEN_HIGHT))
planet04 = pygame.image.load("planet04.png").convert_alpha()
planet04 = pygame.transform.scale(planet04, (SCREEN_HIGHT, SCREEN_HIGHT))
stars = pygame.image.load("stars.jpg").convert_alpha()
stars = pygame.transform.scale(stars, (SCREEN_WHITH, SCREEN_HIGHT))
settings = pygame.image.load("gear.jpg").convert_alpha()
settings = pygame.transform.scale(settings, (90, 90))
pause = pygame.image.load("pause.png").convert_alpha()
pause = pygame.transform.scale(pause,(70,70))
space = pygame.image.load("lvl1.jpg").convert_alpha()
space = pygame.transform.scale(space,(SCREEN_WHITH+85,SCREEN_HIGHT-75))
enemy1 = pygame.image.load("planet01.png").convert_alpha()
enemy1 = pygame.transform.scale(enemy1, (70, 70))
wall = pygame.image.load("wall.png").convert_alpha()
wall = pygame.transform.scale(wall, (30, 70))
live = pygame.image.load("live.png").convert_alpha()
live = pygame.transform.scale(live,(30,30))
enemy2 = pygame.image.load("planet02.png").convert_alpha()
enemy2 = pygame.transform.scale(enemy2, (70, 70))
enemy3 = pygame.image.load("planet03.png").convert_alpha()
enemy3 = pygame.transform.scale(enemy3, (70, 70))
enemy4 = pygame.image.load("planet04.png").convert_alpha()
enemy4 = pygame.transform.scale(enemy4, (70, 70))
healer1 = pygame.image.load("healer1.png").convert_alpha()
healer1 = pygame.transform.scale(healer1, (70, 70))
healer2 = pygame.image.load("healer2.png").convert_alpha()
healer2 = pygame.transform.scale(healer2, (70, 70))
laser = pygame.image.load("tower3.png").convert_alpha()
laser = pygame.transform.scale(laser, (50, 70))
laser2 = pygame.transform.rotate(laser, 180)
laser3 = pygame.image.load("tower3.png").convert_alpha()
laser3 = pygame.transform.scale(laser3, (50,70))
money = pygame.image.load("tower4 1.png").convert_alpha()
money = pygame.transform.scale(money, (70,30))
money2 = pygame.image.load("tower4 2.png").convert_alpha()
money2 = pygame.transform.scale(money2, (70,30))
lvl2 = pygame.image.load("lvl2.png").convert_alpha()
lvl2 = pygame.transform.scale(lvl2, (SCREEN_WHITH+600, SCREEN_HIGHT))
lock = pygame.image.load("lock.png").convert_alpha()
lock = pygame.transform.scale(lock, (40, 40))
enemy5 = pygame.image.load("planet05.png").convert_alpha()
enemy5 = pygame.transform.scale(enemy5, (70, 70))
enemy6 = pygame.image.load("planet06.png").convert_alpha()
enemy6 = pygame.transform.scale(enemy6, (70, 70))
enemy7 = pygame.image.load("planet07.png").convert_alpha()
enemy7 = pygame.transform.scale(enemy7, (70, 70))
enemy8 = pygame.image.load("planet07.png").convert_alpha()
enemy8 = pygame.transform.scale(enemy8, (70, 70))
enemy9 = pygame.image.load("planet07.png").convert_alpha()
enemy9 = pygame.transform.scale(enemy9, (70, 70))
 
left_pos = (SCREEN_WHITH-SCREEN_WHITH, SCREEN_HIGHT/2)
right_pos = (SCREEN_WHITH, SCREEN_HIGHT/2)
 
 
angle = 0
last = 0
 
alpha = 0
fade_in = True
show_startscreen = True
show_screenidk2 = False
 
show_screen3 = False
show_screen4 = False
s_lvl1 = False
s_settings = False
erststart = True
rickroll = False
placemode = False
settings2 = False
start_time = pygame.time.get_ticks()
lvl1time = 0
killed = 0
healers1 = 0
h2 = False
l2 = False
laser1t = 0
#Menu
buttons = [
    {"rect": pygame.Rect(SCREEN_WHITH/2-150, SCREEN_HIGHT/2, 300, 70), "text": "Level 1"},
    {"rect": pygame.Rect(SCREEN_WHITH/2-150, SCREEN_HIGHT/2+90, 300, 70), "text": "Level 2"},
    {"rect": pygame.Rect(SCREEN_WHITH/2-150, SCREEN_HIGHT/2+180, 300, 70), "text": "Beenden"},
    {"rect": pygame.Rect(SCREEN_WHITH-120, 30, 90, 90), "text": " "},
    {"rect": pygame.Rect(SCREEN_WHITH/2+180, SCREEN_HIGHT/2, 70, 70), "text": "Reset"},
    {"rect": pygame.Rect(SCREEN_WHITH/2+180, SCREEN_HIGHT/2+90, 70, 70), "text": " Reset "},
    {"rect": pygame.Rect(20,200, 70, 70), "text": "Back"}
   # {"rect": pygame.Rect(SCREEN_WHITH/2+180, SCREEN_HIGHT/2+90, 70, 70), "text": "  Reset  "}
]
buttons2 = [
    {"rect": pygame.Rect(SCREEN_WHITH/2-80-32, 250, 32, 32), "text": "-"},
    {"rect": pygame.Rect(SCREEN_WHITH/2+80, 250, 32, 32), "text": "+"},
    {"rect": pygame.Rect(30, 30, 140, 50), "text": "Zurück"},
    {"rect": pygame.Rect(SCREEN_WHITH/2-115/2, 300, 115, 50), "text": "Mute"},
    {"rect": pygame.Rect(SCREEN_WHITH/2-160/2, SCREEN_HIGHT-80, 160, 50), "text": "Cheats"},
    {"rect": pygame.Rect(SCREEN_WHITH/2-180/2, 500, 180, 50), "text": "Window"}
 
]
buttons3 = [
    {"rect": pygame.Rect(50, 50, 70, 70), "text": "  "},
    {"rect": pygame.Rect(200, 50, 70, 70), "text": " "},
    {"rect": pygame.Rect(320, 50, 70, 70), "text": "   "},
    {"rect": pygame.Rect(440, 50, 70, 70), "text": "    "}
]
 
 
buttons4 = [
    {"rect": pygame.Rect(SCREEN_WHITH/2-150, SCREEN_HIGHT/2-50, 300, 100), "text": "Start"}
]
 
 
 
WHITE = (255, 255, 255)
RED = (200, 50, 50)
class Enemy:
    def __init__(self, path):
        self.path = path
        self.path_index = 0
        self.x, self.y = self.path[self.path_index]
        self.speed = 5
        self.moneyget = 0
        self.lives = 10
        self.maxlives = 10
        self.cooldown = 0
        self.livetime = 0
        self.indic = 0
       
    def move(self):
        self.cooldown +=1
        self.livetime += 1
        target_x, target_y = self.path[self.path_index]
        dx, dy = target_x - self.x, target_y - self.y
        dist = max(1, (dx**2 + dy**2) ** 0.5)
 
        if abs(dx) < 2 and abs(dy) < 2:
            self.path_index = (self.path_index + 1) % len(self.path)
        else:
            self.x += self.speed * dx / dist
            self.y += self.speed * dy / dist
    def take_dmg(self,amount):
        if self.cooldown > 15:
            self.lives -= amount
            self.cooldown = 0      
        if self.lives <= 0:
            enemies.remove(self)
            self.moneyget = self.maxlives
    def get_position(self):
        return (self.x, self.y)
    def get_dmg(self):
        return (self.lives)
    def getmoney(self):
        return (self.moneyget)
   
 
    def getindic(self,indi):
        if self.livetime <3:
            self.indic = indi
       
 
       
 
       
    def draw(self, surface):
        pygame.draw.circle(surface, RED, (int(self.x), int(self.y)), 10)
        if self.indic == 0:
            screen.blit(enemy1,(self.x-35,self.y-35))
            if self.livetime <3:
                self.lives = 10
                self.maxlives = 10
        if self.indic == 1:
            screen.blit(enemy2,(self.x-35,self.y-35))
            if self.livetime <3:
                self.lives = 20
                self.maxlives = 20
        if self.indic == 2:
            screen.blit(enemy3,(self.x-35,self.y-35))
            if self.livetime <3:
                self.lives = 30
                self.maxlives = 30
        if self.indic == 3:
            screen.blit(enemy4,(self.x-35,self.y-35))
            if self.livetime <3:
                self.lives = 40
                self.maxlives = 40
        if self.indic == 4:
            screen.blit(enemy5,(self.x-35,self.y-35))
            if self.livetime <3:
                self.lives = 60
                self.maxlives = 50
        if self.indic == 5:
            screen.blit(enemy6,(self.x-35,self.y-35))
            if self.livetime <3:
                self.lives = 80
                self.maxlives = 60
        if self.indic == 6:
            screen.blit(enemy7,(self.x-35,self.y-35))
            if self.livetime <3:
                self.lives = 100
                self.maxlives = 70
        if self.indic == 7:
            screen.blit(enemy8,(self.x-35,self.y-35))
            if self.livetime <3:
                self.lives = 120
                self.maxlives = 80
        if self.indic >= 8:
            screen.blit(enemy9,(self.x-35,self.y-35))
            if self.livetime <3:
                self.lives = 140
                self.maxlives = 90
        
 
 
square_path = [
    (-10, 200), (SCREEN_WHITH-100, 200),
    (170, SCREEN_HIGHT-100), (SCREEN_WHITH+6, SCREEN_HIGHT-40)
]
money = 1000
tower_price = 300
 
towers = []
towers2 = []
towers3 = []
hitboxes = []
hitboxes2 = []
 
l2enemies = []
l2towers = []
l2towers2 = []
l2towers3 = []
spawnedlvl2 = 0
spawnlvl2 = 0
money2 = 1000
lvl2lives = 200
 
placing_tower = False
placing_tower2 = False
placing_tower3 = False
tower_position = (0, 0)
tower_position2 = (0, 0)
tower_position3 = (0, 0)
 
 
 
def draw_tower(tower):
    pygame.draw.circle(screen, RED, (tower[0], tower[1]), 30)
    pygame.draw.circle(screen, BLACK, (tower[0], tower[1]), 30, 3)  
 
 
def check_collision(new_tower):
    for tower in towers:
        dist = math.hypot(tower[0] - new_tower[0], tower[1] - new_tower[1])
        if dist < 60:
            return True
    for tower2 in towers2:
        dist2 = math.hypot(tower2[0] - new_tower[0], tower2[1] - new_tower[1])
        if dist2 < 60:
            return True
    for tower3 in towers3:
        dist3 = math.hypot(tower3[0] - new_tower[0], tower3[1] - new_tower[1])
        if dist3 < 60:
            return True
   
    return False
   
 
 
def check_collision2(new_tower2):
    for tower in towers:
        dist12 = math.hypot(tower[0] - new_tower2[0], tower[1] - new_tower2[1])
        if dist12 < 60:
            return True
    for tower2 in towers2:
        dist22 = math.hypot(tower2[0] - new_tower2[0], tower2[1] - new_tower2[1])
        if dist22 < 60:
            return True
    for tower3 in towers3:
        dist32 = math.hypot(tower3[0] - new_tower2[0], tower3[1] - new_tower2[1])
        if dist32 < 60:
            return True
    return False
 
 
def check_collision3(new_tower3):
    for tower in towers:
        dist13 = math.hypot(tower[0] - new_tower3[0], tower[1] - new_tower3[1])
        if dist13 < 60:
            return True
    for tower2 in towers2:
        dist23 = math.hypot(tower2[0] - new_tower3[0], tower2[1] - new_tower3[1])
        if dist23 < 60:
            return True
    for tower3 in towers3:
        dist33 = math.hypot(tower3[0] - new_tower3[0], tower3[1] - new_tower3[1])
        if dist33 < 60:
            return True
    return False
 
enemies = []
spawn_timer = 0
spawn_interval = 250  #ms
death = False
once = True
show_startscreen= True
running = True
w_lvl1 = False
w_lvl2 = True
while running:
    if w_lvl2:
        buttons4 = [
            {"rect": pygame.Rect(SCREEN_WHITH/2-150, SCREEN_HIGHT/2-210, 300, 100), "text": "Start"},
            {"rect": pygame.Rect(SCREEN_WHITH/2-150, SCREEN_HIGHT/2-90, 300, 100), "text": "Hardcore"},
            {"rect": pygame.Rect(SCREEN_WHITH/2-150, SCREEN_HIGHT/2+30, 300, 100), "text": "Endless"},
            {"rect": pygame.Rect(SCREEN_WHITH/2-150, SCREEN_HIGHT/2+150, 300, 100), "text": "Beenden"}
        ]
   
    screen.fill(black)
    now = pygame.time.get_ticks()
 
    for event in pygame.event.get():
        if start:
            start = False
            time.sleep(2)
            spiele_musik(menu)
    if show_startscreen:
        pygame.mouse.set_visible(False)
        screen.blit(stars,(0,0))
        if fade_in:
            alpha += 2
            if alpha >= 255:
                alpha = 255
                fade_in = False
        else:
            alpha -= 2
            if alpha <= 0:
                alpha = 0
                fade_in = True
 
 
        start_text1.set_alpha(alpha)
        start_text2.set_alpha(alpha)
 
        screen.blit(start_text1, start_text1.get_rect(center=(SCREEN_WHITH/2, SCREEN_HIGHT/2-50)))
        screen.blit(start_text2, start_text2.get_rect(center=(SCREEN_WHITH/2, SCREEN_HIGHT/2+50)))
 
        if now - start_time > 6000:
            show_startscreen = False
            show_screenidk2 = True
   
    if show_screenidk2 == True:
        angle += 0.05
       
        screen.blit(stars,(0,0))
       
        fade_in = True
        if fade_in:
            alpha += 2
            if alpha >= 255:
                alpha = 255
                fade_in = False
       
        rotated_left = pygame.transform.rotate(image_scaled, angle)
        rotated_right = pygame.transform.rotate(image_scaled, -angle)
 
        screen.blit(rotated_left, rotated_left.get_rect(center=left_pos))
        screen.blit(rotated_right, rotated_right.get_rect(center=right_pos))
        main_text.set_alpha(alpha)
        screen.blit(main_text, main_text_rect)
 
        if now - start_time > 12000:
            show_screenidk2 = False
            show_screen3 = True
    if show_screen3:
        pygame.mouse.set_visible(True)
        screen.fill(black)
        screen.blit(stars,(0,0))
        screen.blit(planet01, (SCREEN_WHITH/2-SCREEN_HIGHT/2,SCREEN_HIGHT-SCREEN_HIGHT))
        mouse_pos = pygame.mouse.get_pos()
        for btn in buttons4:
            color = DARK_BLUE if btn["rect"].collidepoint(mouse_pos) else BLUE
            pygame.draw.rect(screen, color, btn["rect"])
            text_surf = font_large.render(btn["text"], True, red)
            text_rect = text_surf.get_rect(center=btn["rect"].center)
            screen.blit(text_surf, text_rect)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in buttons4:
                if btn["rect"].collidepoint(event.pos):
                    label = btn["text"]
                    if label == "Start":
                        show_screen4 = True
                        show_screen3 = False
                        hardcore = False
                    elif label == "Hardcore":
                        show_screen4 = True
                        show_screen3 = False
                        hardcore = True
                        w_lvl1 = False
                        spiele_musik(hardcorem)
                    elif label == "Endless":
                        endless = True
                        hardcore = False
                        spiele_musik(endlessm)
                    elif label == "Beenden":
                        running = False
                        
       
    if show_screen4:
        mouse_pos = pygame.mouse.get_pos()
        pygame.mixer.music.set_volume(volume)
        screen.fill(black)
        screen.blit(stars, (0, 0))
        screen.blit(planet01, (SCREEN_WHITH / 2 - SCREEN_HIGHT / 2, 0))
        if hardcore:
            screen.blit(planet04, (SCREEN_WHITH / 2 - SCREEN_HIGHT / 2, 0))  
        screen.blit(hexa, hexa.get_rect(center=(SCREEN_WHITH / 2, SCREEN_HIGHT / 2 -50)))
        reset1 = font.render("Du hast Level 1 zurückgestezt",True,red)
        reset2 = font.render("Du hast Level 2 zurückgestezt",True,red)
        s1 = font.render("Bitte beende oder resette erst Level 1",True,red)
        s2 = font.render("Bitte beende oder resette erst Level 2",True,red)
        if r1:
            screen.blit(reset1,(SCREEN_WHITH/2+270, SCREEN_HIGHT/2-90+20, 70, 70))
            r1counter +=1
            if r1counter > 100:
                r1counter = 0
                r1 = False
        if r2:
            screen.blit(reset2,(SCREEN_WHITH/2+270, SCREEN_HIGHT/2+20, 70, 70))
            r2counter +=1
            if r2counter > 100:
                r2counter = 0
                r2 = False
        for btn in buttons:
            color = DARK_BLUE if btn["rect"].collidepoint(mouse_pos) else BLUE
            pygame.draw.rect(screen, color, btn["rect"])
            text_surf = font.render(btn["text"], True, TEXT_COLOR)
            text_rect = text_surf.get_rect(center=btn["rect"].center)
            screen.blit(text_surf, text_rect)
 
        screen.blit(settings, (SCREEN_WHITH - 120, 30))
        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in buttons:
                if btn["rect"].collidepoint(event.pos):
                    label = btn["text"]
                    if erststart == False:
                        if label == "Beenden":
                            pygame.quit()
                            sys.exit()
                        elif label == "Level 1" and s_settings == False and lvl2speicher == False:
                            lvl1speicher = True
                            s_lvl1 = True
                            show_screen4 = False
                            spiele_musik(lvl1s)
                            if hardcore:
                                spiele_musik(lvl1h)
                            menu_running = False
                        elif label == "Level 2" and s_settings ==  False and w_lvl1 == True and lvl1speicher == False:
                            lvl2speicher = True
                            s_lvl2 = True
                            spiele_musik(level2)
                            if hardcore:
                                spiele_musik(lvl2h)
                            show_screen4 = False
                        elif label == " " and s_settings == False:
                            menu_running = False
                            time.sleep(1)
                            s_settings = True
                        elif label == "Reset" and s_settings == False:
                            enemies = []
                            towers = []
                            towers2 = []
                            towers3 = []
                            spawnedlvl1 = 0
                            spawnlvl1 = 0
                            money = 1000
                            lvl1speicher = False
                            r1 = True
                            lvl1lives = 200
                        elif label == " Reset " and s_settings == False:
                            lvl2speicher = False
                            enemies = []
                            towers = []
                            towers2 = []
                            towers3 = []
                            spawnedlvl1 = 0
                            spawnlvl1 = 0
                            money = 1000
                            lvl1lives = 200
                            r2 = True
                        elif label == "Back":
                            show_screen3  = True
                            show_screen4 = False
                            if hardcore:
                                spiele_musik(menu)
                    elif erststart == True:
                        time.sleep(0.1)
                        erststart = False
        helper = font.render("Um ein Level2 zu starten musst du zuerst Level1 resetten und umgekehrt. Spielstände werden gespeichert",True,red)
        screen.blit(helper, helper.get_rect(center=(SCREEN_WHITH/2, SCREEN_HIGHT-50)))
        if not w_lvl1:
            screen.blit(lock,(SCREEN_WHITH/2-20, SCREEN_HIGHT/2+110, 300, 70))
    if s_settings:
        mouse_pos = pygame.mouse.get_pos()
 
        screen.fill(black)
        screen.blit(stars, (0, 0))
        screen.blit(planet01, (SCREEN_WHITH / 2 - SCREEN_HIGHT / 2, 0))
        if hardcore:
            screen.blit(planet04, (SCREEN_WHITH / 2 - SCREEN_HIGHT / 2, 0))
        screen.blit(setting, setting.get_rect(center=(SCREEN_WHITH / 2, 40 )))
        volume = (round(volume*100))/100
        if volume < 0:
            volume = 0
        if volume > 1:
            volume = 1
        laut = volume*100
        laut = str(laut)
        text3 = font.render(laut,True,red)
        volumetext = font_large.render("Sound",True,red)
        screen.blit(volumetext,(SCREEN_WHITH/2-100,130))
        tex = font_large.render("Window",True,red)
        screen.blit(tex,(SCREEN_WHITH/2-130,380))
        screen.blit(text3,(SCREEN_WHITH/2-30,250))
        for btn in buttons2:
            color = DARK_BLUE if btn["rect"].collidepoint(mouse_pos) else BLUE
            pygame.draw.rect(screen, color, btn["rect"])
            text_surf = font.render(btn["text"], True, TEXT_COLOR)
            text_rect = text_surf.get_rect(center=btn["rect"].center)
            screen.blit(text_surf, text_rect)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in buttons2:
                if btn["rect"].collidepoint(event.pos):
                    label = btn["text"]
                    if label == "Zurück":
                        s_settings = False
                        show_screen4 = True
                        menu_running = False
                    elif label == "+":
                        current_time2 = time.time()
                        if current_time2 - last_click_time2 >= cooldown:
                            last_click_time2 = current_time2
                            volume += 0.1
                               
                    elif label == "-" and rickroll == False:
                        current_time = time.time()
                        if current_time - last_click_time >= cooldown:
                            last_click_time = current_time
                            volume -= 0.1
                    elif label == "Mute" and rickroll == False:
                        volume = 0
                    elif label == "Cheats":
                        spiele_musik(rick)
                        volume = 1
                        print("Rick Roll")
                        rickroll = True
                    elif label == "Window" and FS:
                        screen = pygame.display.set_mode((SCREEN_WHITH, SCREEN_HIGHT))
                        FS = False
                        buttons2 = [
                            {"rect": pygame.Rect(SCREEN_WHITH/2-80-32, 250, 32, 32), "text": "-"},
                            {"rect": pygame.Rect(SCREEN_WHITH/2+80, 250, 32, 32), "text": "+"},
                            {"rect": pygame.Rect(30, 30, 140, 50), "text": "Zurück"},
                            {"rect": pygame.Rect(SCREEN_WHITH/2-115/2, 300, 115, 50), "text": "Mute"},
                            {"rect": pygame.Rect(SCREEN_WHITH/2-160/2, SCREEN_HIGHT-80, 160, 50), "text": "Cheats"},
                            {"rect": pygame.Rect(SCREEN_WHITH/2-180/2, 500, 180, 50), "text": "Fullscreen"}
                        ]
                        pygame.display.flip()
                    elif label == "Fullscreen" and not FS:
                        screen = pygame.display.set_mode((SCREEN_WHITH, SCREEN_HIGHT),pygame.FULLSCREEN)
                        FS = True
                        buttons2 = [
                            {"rect": pygame.Rect(SCREEN_WHITH/2-80-32, 250, 32, 32), "text": "-"},
                            {"rect": pygame.Rect(SCREEN_WHITH/2+80, 250, 32, 32), "text": "+"},
                            {"rect": pygame.Rect(30, 30, 140, 50), "text": "Zurück"},
                            {"rect": pygame.Rect(SCREEN_WHITH/2-115/2, 300, 115, 50), "text": "Mute"},
                            {"rect": pygame.Rect(SCREEN_WHITH/2-160/2, SCREEN_HIGHT-80, 160, 50), "text": "Cheats"},
                            {"rect": pygame.Rect(SCREEN_WHITH/2-180/2, 500, 180, 50), "text": "Window"}
                       
                        ]
                        pygame.display.flip()
 
    if hardcore:
        multi = 1.5
    if not hardcore:
        multi = 1
    if s_lvl1:
        square_path = [
        (-10, 200), (SCREEN_WHITH-100, 200),
        (170, SCREEN_HIGHT-100), (SCREEN_WHITH+6, SCREEN_HIGHT-40)]
        lvl1time +=1
        hitboxes2 = towers3
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(black)
        screen.blit(space,(0,75))
       
        dt = clock.tick(60)
        spawn_timer += dt
        laser1t += 1
        if laser1t >= 50:
            l2 = True
            for eny in enemies:
                positioEn = Enemy.get_position(self = eny)
                for hibox in hitboxes2:
                    pygame.draw.rect(screen,red,(hibox[0],hibox[1]+40,20,90))
                    if (hibox[0] < positioEn[0]+35 < (hibox[0]+20)) and (hibox[1]+40 < positioEn[1]+35 < (hibox[1]+160)):
                        Enemy.take_dmg(self = eny,amount = 10/multi)
                money += Enemy.getmoney(self = eny)/2
           
        else:
            for eny in enemies:
                positioEn = Enemy.get_position(self = eny)
                for hibox in hitboxes2:
                    pygame.draw.rect(screen,red,(hibox[0],hibox[1]-150,20,90))
                    if (hibox[0] < positioEn[0]+35 < (hibox[0]+20)) and (hibox[1]-150 < positioEn[1]+35 < (hibox[1]+40)):
                        Enemy.take_dmg(self = eny,amount = 10/multi)
                money += Enemy.getmoney(self = eny)/2
           
        if laser1t >= 100:
 
            laser1t = 0
            l2 = False
        hintergrund = pygame.draw.rect(screen,lightgray,pygame.Rect(0,0,SCREEN_WHITH+100,150))

            

        
                       
        if spawn_timer >= spawn_interval:
 
            enemies.append(Enemy(square_path))
            spawn_timer = 0
        mouse_x,mouse_y = pygame.mouse.get_pos()
        
       
        for btn in buttons3:
            color = DARK_BLUE if btn["rect"].collidepoint(mouse_pos) else BLUE
            pygame.draw.rect(screen, color, btn["rect"])
            text_surf = font.render(btn["text"], True, TEXT_COLOR)
            text_rect = text_surf.get_rect(center=btn["rect"].center)
            screen.blit(text_surf, text_rect)
        screen.blit(pause,(50,50))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons3:
                    if btn["rect"].collidepoint(event.pos):
                        label = btn["text"]
                        if label == "  ":
                            s_lvl1 = False
                            show_screen4 = True
                            spiele_musik(menu)
                            if hardcore:
                                spiele_musik(hardcorem)
                        if label == " " and money - 300 >= 0:
                                lvl1time = 0
                                placing_tower=True
                                new_tower = (mouse_x, mouse_y)
                        if label == "   " and money - 500 >= 0:
                                lvl1time = 0
                                placing_tower2=True
                                new_tower2 = (mouse_x, mouse_y)
                        if label == "    " and money - 400 >= 0:
                                lvl1time = 0
                                placing_tower3=True
                                new_tower3 = (mouse_x, mouse_y)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    placing_tower = False
                    placing_tower2 = False
                    placing_tower3 = False
                if event.key == pygame.K_p:

                    show_rectangles = not show_rectangles
        if show_rectangles:
            for enemy in enemies:
                x, y = enemy.get_position()
                pygame.draw.rect(screen, red, (x - 25, y - 30, 60, 60))
        for enemy in enemies:
            enemy.move()
 
        for enemy in enemies:
            enemy.draw(screen)
 
                           
        if placing_tower:
            new_tower = (mouse_x, mouse_y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl1time >= 10:
                    placing_tower = False
                    placemode = False
                    if not check_collision(new_tower):
                        towers.append(new_tower)
                        money-=300
        if placing_tower:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tower_position = (mouse_x, mouse_y)
 
 
        for tower in towers:
            screen.blit(wall,(tower[0]-15,tower[1]-45))
 
        if placing_tower:
            screen.blit(wall,(tower_position[0]-15,tower_position[1]-45))
        moneyfont = pygame.font.SysFont("Arial", 30)
        money_text = moneyfont.render(f"Money: ${money}", True, BLACK)
        screen.blit(money_text, (10, 10))
        for eny in enemies:
            positioEn = Enemy.get_position(self=eny)
            if positioEn[0]>= SCREEN_WHITH:
                nowdmg = Enemy.get_dmg(self=eny)
                if hardcore:
                    nowdmg = nowdmg*10
                nowdmg = round(nowdmg)
                lvl1lives -= nowdmg
               
                Enemy.take_dmg(self=eny,amount=9999999)
        lvl1livestxt = str(lvl1lives)
        livesfont = moneyfont.render(lvl1livestxt,False,red)
        screen.blit(livesfont,(300,10))
        screen.blit(live,(370,10))
        hitboxes = towers
        for eny in enemies:
            positioEn = Enemy.get_position(self = eny)
            for hbox in hitboxes:
                if (hbox[0]-5 < positioEn[0]+35 < (hbox[0]+35)) and (hbox[1]-5 < positioEn[1]+35 < (hbox[1]+75)):
                    Enemy.take_dmg(self = eny,amount = 5/multi)
            money += (Enemy.getmoney(self = eny))/2
        if lvl1lives <= 0:
            lvl1lives = 0
            s_lvl1 = False
            death = True
            spiele_musik(menu)
        spawnlvl1 += 1
        if spawnlvl1 >= 60:
            spawnlvl1 = 0
            spawnedlvl1 +=1
        if placing_tower2:
            new_tower2 = (mouse_x, mouse_y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl1time >= 10:
                    placing_tower2 = False
                    placemode2 = False
                    if not check_collision2(new_tower2):
                        towers2.append(new_tower2)
                        money-=500
                        healers1 += 1
        if placing_tower2:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tower_position2 = (mouse_x, mouse_y)
 
 
        for tower2 in towers2:
            if not h2:
                screen.blit(healer1,(tower2[0]-15,tower2[1]-45))
 
        if placing_tower2:
            screen.blit(healer1,(tower_position2[0]-15,tower_position2[1]-45))
 
 
 
 
 
        if placing_tower3:
            new_tower3 = (mouse_x, mouse_y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl1time >= 10:
                    placing_tower3 = False
                    placemode3 = False
                    if not check_collision3(new_tower3):
                        towers3.append(new_tower3)
                        money-=400
                        healers1 += 1
 
 
 
        if placing_tower3:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tower_position3 = (mouse_x, mouse_y)
 
 
        for tower3 in towers3:
            if not l2:
                screen.blit(laser,(tower3[0]-15,tower3[1]-45))
            if l2:
                screen.blit(laser2,(tower3[0]-15,tower3[1]-45))
 
        if placing_tower3:
            screen.blit(laser,(tower_position3[0]-15,tower_position3[1]-45))
           
       
        if placing_tower or placing_tower2 or placing_tower3:
            esc = font.render("Drücke Esc um platzieren zu beenden",True,red)
            screen.blit(esc,(SCREEN_WHITH-550,150))
 
 
        if spawnedlvl1 >= 21:
            for eny in enemies:
               Enemy.getindic(self = eny, indi = 1)
        if spawnedlvl1 >= 42:
            for eny in enemies:
                Enemy.getindic(self = eny, indi = 2)
        if spawnedlvl1 >= 64:
            for eny in enemies:
                Enemy.getindic(self = eny, indi = 3)
        if spawnedlvl1 >= 80:
            win = True
            s_lvl1 = False
        screen.blit(wall,(220,50))
        screen.blit(healer1,(320,50))
        screen.blit(laser3,(450,50))
        if healertimer >= 140:
            h2 = True
            for h in towers2:
                screen.blit(healer2,(h[0]-15,h[1]-45))
                           
                if once:
                    lvl1lives += healers1
                    once = False
            if healertimer >= 180:
                healertimer = 0
                once = True
                h2 = False
        healertimer += 1
       
 
       
        costfont = pygame.font.SysFont("Georgia", 20)
        t1 = costfont.render("300$",True,red)
        t2 = costfont.render("500$",True,red)
        t3 = costfont.render("400$",True,red)
        screen.blit(t1,(210,120))
        screen.blit(t2,(330,120))
        screen.blit(t3,(450,120))
           
 
   
    if win:
        screen.fill(black)
        spiele_musik(menu)
        if hardcore:
            spiele_musik(hardcorem)
        screen.blit(stars,(0,0))
        deathfont = font_large.render("Du hast gewonnen",False,red)
        screen.blit(deathfont,(SCREEN_WHITH/2-300,SCREEN_HIGHT/2-20))
        enemies = []
        towers = []
        towers2 = []
        towers3 = []
        spawnedlvl1 = 0
        spawnlvl1 = 0
        s_lvl1 = False
        money = 1000
        lvl1lives = 200
        pygame.display.flip()
        time.sleep(2)
        win = False
        show_screen4 = True
        w_lvl1 = True
        lvl1speicher = False
             
    if death:
        s_lvl1 = False
        show_screen3 = True
        if hardcore:
            spiele_musik(hardcorem)
        screen.fill(black)
        screen.blit(stars,(0,0))
        deathfont = font_large.render("Du bist gestorben",False,red)
        screen.blit(deathfont,(SCREEN_WHITH/2-320,SCREEN_HIGHT/2-20))
        enemies = []
        towers = []
        towers2 = []
        towers3 = []
        spawnedlvl1 = 0
        spawnlvl1 = 0
        money = 1000
        lvl1lives = 200
        pygame.display.flip()
        time.sleep(2)
        death = False
        show_screen3 = True
   
 
    if s_lvl2:
        square_path = [
        (-10, 200), (SCREEN_WHITH+100, SCREEN_HIGHT+80),
]
        lvl1time +=1
        hitboxes2 = towers3
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(black)
        screen.blit(lvl2,(-200,0))
       
        dt = clock.tick(60)
        spawn_timer += dt
        laser1t += 1
        if laser1t >= 50:
            l2 = True
            for eny in enemies:
                positioEn = Enemy.get_position(self = eny)
                for hibox in hitboxes2:
                    pygame.draw.rect(screen,red,(hibox[0],hibox[1]+40,20,90))
                    if (hibox[0] < positioEn[0]+35 < (hibox[0]+20)) and (hibox[1]+40 < positioEn[1]+35 < (hibox[1]+160)):
                        Enemy.take_dmg(self = eny,amount = 10/multi)
                money += Enemy.getmoney(self = eny)/2
           
        else:
            for eny in enemies:
                positioEn = Enemy.get_position(self = eny)
                for hibox in hitboxes2:
                    pygame.draw.rect(screen,red,(hibox[0],hibox[1]-150,20,90))
                    if (hibox[0] < positioEn[0]+35 < (hibox[0]+20)) and (hibox[1]-150 < positioEn[1]+35 < (hibox[1]+40)):
                        Enemy.take_dmg(self = eny,amount = 10/multi)
                money += Enemy.getmoney(self = eny)/2
           
        if laser1t >= 100:
 
            laser1t = 0
            l2 = False
        hintergrund = pygame.draw.rect(screen,lightgray,pygame.Rect(0,0,SCREEN_WHITH+100,150))
 
            

                        

        

        if spawn_timer >= spawn_interval:
            enemies.append(Enemy(square_path))
            spawn_timer = 0
        mouse_x,mouse_y = pygame.mouse.get_pos()
        
       
        for btn in buttons3:
            color = DARK_BLUE if btn["rect"].collidepoint(mouse_pos) else BLUE
            pygame.draw.rect(screen, color, btn["rect"])
            text_surf = font.render(btn["text"], True, TEXT_COLOR)
            text_rect = text_surf.get_rect(center=btn["rect"].center)
            screen.blit(text_surf, text_rect)
        screen.blit(pause,(50,50))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons3:
                    if btn["rect"].collidepoint(event.pos):
                        label = btn["text"]
                        if label == "  ":
                            s_lvl2 = False
                            show_screen4 = True
                            spiele_musik(menu)
                            if hardcore:
                                spiele_musik(hardcorem)
                        if label == " " and money - 300 >= 0:
                                lvl1time = 0
                                placing_tower=True
                                new_tower = (mouse_x, mouse_y)
                        if label == "   " and money - 500 >= 0:
                                lvl1time = 0
                                placing_tower2=True
                                new_tower2 = (mouse_x, mouse_y)
                        if label == "    " and money - 400 >= 0:
                                lvl1time = 0
                                placing_tower3=True
                                new_tower3 = (mouse_x, mouse_y)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    placing_tower = False
                    placing_tower2 = False
                    placing_tower3 = False
                if event.key == pygame.K_p:
                    show_rectangles = not show_rectangles
            if show_rectangles:
                for enemy in enemies:
                    x, y = enemy.get_position()
                    pygame.draw.rect(screen, red, (x - 25, y - 30, 60, 60))
        for enemy in enemies:
            enemy.move()
 
        for enemy in enemies:
            enemy.draw(screen)
                    
                           
        if placing_tower:
            new_tower = (mouse_x, mouse_y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl1time >= 10:
                    placing_tower = False
                    placemode = False
                    if not check_collision(new_tower):
                        towers.append(new_tower)
                        money-=300
        if placing_tower:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tower_position = (mouse_x, mouse_y)
 
 
        for tower in towers:
            screen.blit(wall,(tower[0]-15,tower[1]-45))
 
        if placing_tower:
            screen.blit(wall,(tower_position[0]-15,tower_position[1]-45))
        moneyfont = pygame.font.SysFont("Arial", 30)
        money_text = moneyfont.render(f"Money: ${money}", True, BLACK)
        screen.blit(money_text, (10, 10))
        for eny in enemies:
            positioEn = Enemy.get_position(self=eny)
            if positioEn[0]>= SCREEN_WHITH:
                nowdmg = Enemy.get_dmg(self=eny)
                if hardcore:
                    nowdmg = nowdmg*10
                nowdmg = round(nowdmg)
                lvl1lives -= nowdmg
                Enemy.take_dmg(self=eny,amount=9999999)
        lvl1livestxt = str(lvl1lives)
        livesfont = moneyfont.render(lvl1livestxt,False,red)
        screen.blit(livesfont,(300,10))
        screen.blit(live,(370,10))
        hitboxes = towers
        for eny in enemies:
            positioEn = Enemy.get_position(self = eny)
            for hbox in hitboxes:
                if (hbox[0]-5 < positioEn[0]+35 < (hbox[0]+35)) and (hbox[1]-5 < positioEn[1]+35 < (hbox[1]+75)):
                    Enemy.take_dmg(self = eny,amount = 5/multi)
            money += Enemy.getmoney(self = eny)/2
        if lvl1lives <= 0:
            lvl1lives = 0
            s_lvl1 = False
            death = True
            spiele_musik(menu)
        spawnlvl1 += 1
        if spawnlvl1 >= 60:
            spawnlvl1 = 0
            spawnedlvl1 +=1
        if placing_tower2:
            new_tower2 = (mouse_x, mouse_y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl1time >= 10:
                    placing_tower2 = False
                    placemode2 = False
                    if not check_collision2(new_tower2):
                        towers2.append(new_tower2)
                        money-=500
                        healers1 += 1
        if placing_tower2:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tower_position2 = (mouse_x, mouse_y)
 
 
        for tower2 in towers2:
            if not h2:
                screen.blit(healer1,(tower2[0]-15,tower2[1]-45))
 
        if placing_tower2:
            screen.blit(healer1,(tower_position2[0]-15,tower_position2[1]-45))
 
 
 
 
 
        if placing_tower3:
            new_tower3 = (mouse_x, mouse_y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl1time >= 10:
                    placing_tower3 = False
                    placemode3 = False
                    if not check_collision3(new_tower3):
                        towers3.append(new_tower3)
                        money-=400
                        healers1 += 1
 
 
 
        if placing_tower3:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tower_position3 = (mouse_x, mouse_y)
 
 
        for tower3 in towers3:
            if not l2:
                screen.blit(laser,(tower3[0]-15,tower3[1]-45))
            if l2:
                screen.blit(laser2,(tower3[0]-15,tower3[1]-45))
 
        if placing_tower3:
            screen.blit(laser,(tower_position3[0]-15,tower_position3[1]-45))
           
       
        if placing_tower or placing_tower2 or placing_tower3:
            esc = font.render("Drücke Esc um platzieren zu beenden",True,red)
            screen.blit(esc,(SCREEN_WHITH-550,150))
 
 
        if spawnedlvl1 >= 21:
            for eny in enemies:
               Enemy.getindic(self = eny, indi = 1)
        if spawnedlvl1 >= 42:
            for eny in enemies:
                Enemy.getindic(self = eny, indi = 2)
        if spawnedlvl1 >= 64:
            for eny in enemies:
                Enemy.getindic(self = eny, indi = 3)
        if spawnedlvl1 >= 100:
            win = True
            s_lvl1 = False
        screen.blit(wall,(220,50))
        screen.blit(healer1,(320,50))
        screen.blit(laser3,(450,50))
        if healertimer >= 140:
            h2 = True
            for h in towers2:
                screen.blit(healer2,(h[0]-15,h[1]-45))
                           
                if once:
                    lvl1lives += healers1
                    once = False
            if healertimer >= 180:
                healertimer = 0
                once = True
                h2 = False
        healertimer += 1
       
 
       
        costfont = pygame.font.SysFont("Georgia", 20)
        t1 = costfont.render("300$",True,red)
        t2 = costfont.render("500$",True,red)
        t3 = costfont.render("400$",True,red)
        screen.blit(t1,(210,120))
        screen.blit(t2,(330,120))
        screen.blit(t3,(450,120))
           
 
   
    if win:
        screen.fill(black)
        spiele_musik(menu)
        screen.blit(stars,(0,0))
        deathfont = font_large.render("Du hast gewonnen",False,red)
        screen.blit(deathfont,(SCREEN_WHITH/2-300,SCREEN_HIGHT/2-20))
        enemies = []
        towers = []
        towers2 = []
        towers3 = []
        s_lvl2 = False
        spawnedlvl1 = 0
        spawnlvl1 = 0
        money = 1000
        lvl1lives = 200
        pygame.display.flip()
        time.sleep(2)
        win = False
        if not hardcore:
            show_screen3 = True
            w_lvl2= True
        else:
            h_win = True
            start_time2 = 0
        lvl2speicher = False
             
    if death:
        s_lvl2 = False
       
        if hardcore:
            spiele_musik(hardcorem)
        screen.fill(black)
        screen.blit(stars,(0,0))
        deathfont = font_large.render("Du bist gestorben",False,red)
        screen.blit(deathfont,(SCREEN_WHITH/2-250,SCREEN_HIGHT/2-20))
        enemies = []
        towers = []
        towers2 = []
        towers3 = []
        spawnedlvl1 = 0
        spawnlvl1 = 0
        money = 1000
        lvl1lives = 200
        pygame.display.flip()
        time.sleep(2)
        death = False
        show_screen3 = True
       
 
    if h_win:
        start_time2 += 1
        pygame.mouse.set_visible(False)
        screen.blit(stars,(0,0))
        if fade_in:
            alpha += 2
            if alpha >= 255:
                alpha = 255
                fade_in = False
        else:
            alpha -= 2
            if alpha <= 0:
                alpha = 0
                fade_in = True
 
        ende = font_large.render("Hexaflow by Hannes",True,red)
        ende2 = font.render("Ende",True,WHITE)
        ende.set_alpha(alpha)
        ende2.set_alpha(alpha)
 
        screen.blit(ende, start_text1.get_rect(center=(SCREEN_WHITH/2, SCREEN_HIGHT/2-50)))
        screen.blit(ende2, start_text2.get_rect(center=(SCREEN_WHITH/2, SCREEN_HIGHT/2+50)))
        if start_time2 > 120:
            show_screen3 = True

    if endless:
        square_path = [
        (-10, 200), (SCREEN_WHITH-100, 200),
        (170, SCREEN_HIGHT-100), (SCREEN_WHITH+6, SCREEN_HIGHT-40)]
        lvl1time +=1
        hitboxes2 = towers3
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(black)
        screen.blit(space,(0,75))
       
        dt = clock.tick(60)
        spawn_timer += dt
        laser1t += 1
        if laser1t >= 50:
            l2 = True
            for eny in enemies:
                positioEn = Enemy.get_position(self = eny)
                for hibox in hitboxes2:
                    pygame.draw.rect(screen,red,(hibox[0],hibox[1]+40,20,90))
                    if (hibox[0] < positioEn[0]+35 < (hibox[0]+20)) and (hibox[1]+40 < positioEn[1]+35 < (hibox[1]+160)):
                        Enemy.take_dmg(self = eny,amount = 10/multi)
                money += Enemy.getmoney(self = eny)/2
           
        else:
            for eny in enemies:
                positioEn = Enemy.get_position(self = eny)
                for hibox in hitboxes2:
                    pygame.draw.rect(screen,red,(hibox[0],hibox[1]-150,20,90))
                    if (hibox[0] < positioEn[0]+35 < (hibox[0]+20)) and (hibox[1]-150 < positioEn[1]+35 < (hibox[1]+40)):
                        Enemy.take_dmg(self = eny,amount = 10/multi)
                money += Enemy.getmoney(self = eny)/2
           
        if laser1t >= 100:
 
            laser1t = 0
            l2 = False
        hintergrund = pygame.draw.rect(screen,lightgray,pygame.Rect(0,0,SCREEN_WHITH+100,150))
 


        if show_rectangles:
            for enemy in enemies:
                x, y = enemy.get_position()
                pygame.draw.rect(screen, red, (x - 25, y - 30, 60, 60))
                       
        if spawn_timer >= spawn_interval:
 
            enemies.append(Enemy(square_path))
            spawn_timer = 0
        mouse_x,mouse_y = pygame.mouse.get_pos()
        
       
        for btn in buttons3:
            color = DARK_BLUE if btn["rect"].collidepoint(mouse_pos) else BLUE
            pygame.draw.rect(screen, color, btn["rect"])
            text_surf = font.render(btn["text"], True, TEXT_COLOR)
            text_rect = text_surf.get_rect(center=btn["rect"].center)
            screen.blit(text_surf, text_rect)
        screen.blit(pause,(50,50))
        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in buttons3:
                if btn["rect"].collidepoint(event.pos):
                    label = btn["text"]
                    if label == "  ":
                        endless = False
                        s_endlessend = True
                        endlesstimer = 0
                        spiele_musik(menu)
                    if label == " " and money - 300 >= 0:
                            lvl1time = 0
                            placing_tower=True
                            new_tower = (mouse_x, mouse_y)
                    if label == "   " and money - 500 >= 0:
                            lvl1time = 0
                            placing_tower2=True
                            new_tower2 = (mouse_x, mouse_y)
                    if label == "    " and money - 400 >= 0:
                            lvl1time = 0
                            placing_tower3=True
                            new_tower3 = (mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                placing_tower = False
                placing_tower2 = False
                placing_tower3 = False
            if event.key == pygame.K_p:

                show_rectangles = not show_rectangles
        if show_rectangles:
            for enemy in enemies:
                x, y = enemy.get_position()
                pygame.draw.rect(screen, red, (x - 25, y - 30, 60, 60))
        for enemy in enemies:
            enemy.move()
 
        for enemy in enemies:
            enemy.draw(screen)
 
                           
        if placing_tower:
            new_tower = (mouse_x, mouse_y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl1time >= 10:
                    placing_tower = False
                    placemode = False
                    if not check_collision(new_tower):
                        towers.append(new_tower)
                        money-=300
        if placing_tower:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tower_position = (mouse_x, mouse_y)
 
 
        for tower in towers:
            screen.blit(wall,(tower[0]-15,tower[1]-45))
 
        if placing_tower:
            screen.blit(wall,(tower_position[0]-15,tower_position[1]-45))
        moneyfont = pygame.font.SysFont("Arial", 30)
        money_text = moneyfont.render(f"Money: ${money}", True, BLACK)
        screen.blit(money_text, (10, 10))
        for eny in enemies:
            positioEn = Enemy.get_position(self=eny)
            if positioEn[0]>= SCREEN_WHITH:
                nowdmg = Enemy.get_dmg(self=eny)
                if hardcore:
                    nowdmg = nowdmg*10
                nowdmg = round(nowdmg)
                lvl1lives -= nowdmg
               
                Enemy.take_dmg(self=eny,amount=9999999)
        lvl1livestxt = str(lvl1lives)
        livesfont = moneyfont.render(lvl1livestxt,False,red)
        screen.blit(livesfont,(300,10))
        screen.blit(live,(370,10))
        hitboxes = towers
        for eny in enemies:
            positioEn = Enemy.get_position(self = eny)
            for hbox in hitboxes:
                if (hbox[0]-5 < positioEn[0]+35 < (hbox[0]+35)) and (hbox[1]-5 < positioEn[1]+35 < (hbox[1]+75)):
                    Enemy.take_dmg(self = eny,amount = 5/multi)
            money += (Enemy.getmoney(self = eny))/2
        if lvl1lives <= 0:
            lvl1lives = 0
            s_lvl1 = False
            death = True
            spiele_musik(menu)
        spawnlvl1 += 1
        if spawnlvl1 >= 60:
            spawnlvl1 = 0
            spawnedlvl1 +=1
        if placing_tower2:
            new_tower2 = (mouse_x, mouse_y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl1time >= 10:
                    placing_tower2 = False
                    placemode2 = False
                    if not check_collision2(new_tower2):
                        towers2.append(new_tower2)
                        money-=500
                        healers1 += 1
        if placing_tower2:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tower_position2 = (mouse_x, mouse_y)
 
 
        for tower2 in towers2:
            if not h2:
                screen.blit(healer1,(tower2[0]-15,tower2[1]-45))
 
        if placing_tower2:
            screen.blit(healer1,(tower_position2[0]-15,tower_position2[1]-45))
 
 
 
 
 
        if placing_tower3:
            new_tower3 = (mouse_x, mouse_y)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl1time >= 10:
                    placing_tower3 = False
                    placemode3 = False
                    if not check_collision3(new_tower3):
                        towers3.append(new_tower3)
                        money-=400
                        healers1 += 1
 
 
 
        if placing_tower3:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tower_position3 = (mouse_x, mouse_y)
 
 
        for tower3 in towers3:
            if not l2:
                screen.blit(laser,(tower3[0]-15,tower3[1]-45))
            if l2:
                screen.blit(laser2,(tower3[0]-15,tower3[1]-45))
 
        if placing_tower3:
            screen.blit(laser,(tower_position3[0]-15,tower_position3[1]-45))
           
       
        if placing_tower or placing_tower2 or placing_tower3:
            esc = font.render("Drücke Esc um platzieren zu beenden",True,red)
            screen.blit(esc,(SCREEN_WHITH-550,150))
 

        if spawnedlvl1 >= last+21:
            last += 21
            if oncer == 0 and oncerlast == 0:
                ec += 1
                oncer = 1
            oncerlast = oncer
            oncer = 1
        for eny in enemies:
            Enemy.getindic(self = eny, indi = ec)
        else:
            oncer = 0
            oncerlast = 0
    
        wellen = ec
        wellent = font.render(f"Welle: {wellen}",True,red)
        screen.blit(wellent,(SCREEN_WHITH-200,50))
        screen.blit(wall,(220,50))
        screen.blit(healer1,(320,50))
        screen.blit(laser3,(450,50))
        if healertimer >= 140:
            h2 = True
            for h in towers2:
                screen.blit(healer2,(h[0]-15,h[1]-45))
                           
                if once:
                    lvl1lives += healers1
                    once = False
            if healertimer >= 180:
                healertimer = 0
                once = True
                h2 = False
        healertimer += 1
       
 
       
        costfont = pygame.font.SysFont("Georgia", 20)
        t1 = costfont.render("300$",True,red)
        t2 = costfont.render("500$",True,red)
        t3 = costfont.render("400$",True,red)
        screen.blit(t1,(210,120))
        screen.blit(t2,(330,120))
        screen.blit(t3,(450,120))
    wellen = ec
    if s_endlessend:
        endlesstimer += 1
        screen.fill(black)
        screen.blit(stars,(0,0))
        endlesstext = font_large.render(f"Du hast {wellen} Wellen überlebt",True,red)
        screen.blit(endlesstext,endlesstext.get_rect(center = (SCREEN_WHITH/2, SCREEN_HIGHT/2)))
        if endlesstimer >= 300:
            s_endlessend = False
            show_screen3 = True
            enemies = []
            ec = 0
            wellen = 0
            oncer = 0
            oncerlast = 0
            last = 0
            towers = []
            towers2 = []
            towers3 = []
            spawnedlvl1 = 0
            spawnlvl1 = 0
            money = 1000
            lvl1speicher = False
            r1 = True
            lvl1lives = 200


       
       
 
    pygame.display.flip()
    clock.tick(60)
 
 
 
 
 
 
pygame.quit()
sys.exit()