import pyxel as py

scene_start = 0
scene_stage_1 = 1
scene_stage_2 = 2
scene_stage_3 = 3
scene_stage_4 = 4
scene_stage_5 = 5
scene_stage_6 = 6
scene_death = 7
scene_win = 8


screen_x = 500
screen_y = 250
now_1 = 0
now_2 = 0
now_enemy = 0
now_main_1 = 0
now_main_2 = 0
camera_x = 0
camera_y = 0        

class Character:
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.w = 35
        self.h = 61
        self.speed = 1
        self.is_alive = alive
        self.is_hided = True
        self.is_running = False
        self.side = True
        self.is_walking = False
        self.show_walking = 1
        self.show_running = 1
        self.power_invi = False
        self.is_invi = False
        self.used_invi = False
        self.now_invi = 0
        self.power_tiny = False
        self.is_tiny = False

    def stairs(self, position_i, position_f, direction, h_max, h_min):
        if self.x in range(position_i+10,position_f-10):
            self.speed = 1
            if py.btn(py.KEY_A):
                self.is_walking = True
                if direction == True:
                    self.y += self.speed
                else:
                    self.y -= self.speed
            elif py.btn(py.KEY_D):
                self.is_walking = True
                if direction == True:
                    self.y -= self.speed
                else:
                    self.y += self.speed
        elif self.x in range(position_i,position_i+10) and self.y != h_min:
            self.y = h_max
        elif self.x in range(position_f-10,position_f) and self.y != h_max:
            self.y = h_min
            
    def running(self):
        if self.is_running == True and self.is_invi == False:
            self.is_walking = False
            self.speed = 5
        else:
            self.speed = 1 
    
    def hiding(self, scene):
        if self.is_tiny == True:
            y = screen_y - 30
        else:
            y = screen_y - 87
            
        if py.pget(screen_x/2,y) == 0 and py.pget(screen_x/2+17,y) == 0 and scene!=scene_stage_6:
            self.is_hided = True
        elif self.power_invi == True and self.is_invi:
            self.is_hided = True
        elif scene==scene_stage_6:
            if py.pget(screen_x/2,y) == 0 and py.pget(screen_x/2+20,y) == 0:
                self.is_hided = False
            else:
                self.is_hided = True
        else:
            self.is_hided = False
    
    def update(self):
        global now_main_1, now_main_2
        if py.btnp(py.KEY_Q):
            py.quit()
        if py.btn(py.KEY_A):
            self.x -= self.speed
            self.side = False
            self.is_walking = True
        elif py.btn(py.KEY_D):
            self.x += self.speed
            self.side = True
            self.is_walking = True
        else:
            self.is_walking = False
            
        if py.btn(py.KEY_W) and py.pget(self.x,self.y) == 3 and py.pget(self.x+self.w,self.y)==3:
            self.y -= self.speed
        if py.btn(py.KEY_S) and self.y != screen_y-20 and py.pget(self.x-1,self.y)==3 and py.pget(self.x+21,self.y)==3:
            self.y += self.speed

        if py.btn(py.KEY_SHIFT) and (py.btn(py.KEY_A) or py.btn(py.KEY_D)):
            self.is_running = True
        else:
            self.is_running = False
            
        self.running()
        
        if py.btnp(py.KEY_E) and self.power_invi == True and self.used_invi == False:
            self.is_invi = True
            self.now_invi = py.frame_count
        if self.now_invi+300 <= py.frame_count and self.is_invi == True:
            self.is_invi = False
            self.used_invi = True
            self.now_invi = py.frame_count
        if self.now_invi+400 <= py.frame_count and self.used_invi == True:
            self.used_invi = False

        if py.btn(py.KEY_CTRL) and self.power_tiny == True:
            self.is_tiny = True
            self.is_invi = False
            self.used_invi = True
        else:
            self.is_tiny = False

        if py.frame_count>=now_main_1+15 and self.show_walking == 1:
            self.show_walking = 2
            now_main_1 = py.frame_count
        elif py.frame_count>=now_main_1+15 and self.show_walking == 2:
            self.show_walking = 1
            now_main_1 = py.frame_count
            
        if py.frame_count>=now_main_2+5 and self.show_running == 1:
            self.show_running = 2
            now_main_2 = py.frame_count
        elif py.frame_count>=now_main_2+5 and self.show_running == 2:
            self.show_running = 1
            now_main_2 = py.frame_count
            
    def draw(self):
        if self.side == True:
            if self.is_walking == True:
                if self.show_walking == 1:
                    if self.is_invi == True:
                        py.blt(self.x, self.y, 1, 68, 141, 35, 61, 9)
                    elif self.is_tiny == True:
                        py.blt(self.x, self.y+26, 1, 0, 141, 17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 0, 0, 35, 61, 9)
                else:
                    if self.is_invi == True:
                        py.blt(self.x, self.y, 1, 104, 141, 35, 61, 9)
                    elif self.is_tiny == True:
                        py.blt(self.x, self.y+26, 1, 17, 141, 17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 36, 0, 35, 61, 9)
            elif self.is_running == True:
                if self.show_running == 1:
                    if self.is_tiny == True:
                        py.blt(self.x, self.y+26, 1, 34, 141, 17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 72, 0, 35, 61,  9)
                else:
                    if self.is_tiny == True:
                        py.blt(self.x, self.y+26, 1, 51, 141, 17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 107, 0, 35, 61,  9) 
            else:
                if self.is_invi == True:
                    py.blt(self.x, self.y, 1, 68, 141, 35, 61, 9)
                elif self.is_tiny == True:
                    py.blt(self.x, self.y+26, 1, 0, 141, 17, 35, 9)
                else:
                    py.blt(self.x, self.y, 1, 0, 0, 35, 61, 9)
        else:
            if self.is_walking == True:
                if self.show_walking == 1:
                    if self.is_invi == True: 
                        py.blt(self.x, self.y, 1, 68, 141, -35, 61, 9)
                    elif self.is_tiny == True:
                        py.blt(self.x, self.y+26, 1, 0, 141, -17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 0, 0, -35, 61, 9)
                else:
                    if self.is_invi == True:
                        py.blt(self.x, self.y, 1, 104, 141, -35, 61, 9)
                    elif self.is_tiny == True:
                        py.blt(self.x, self.y+26, 1, 17, 141, -17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 36, 0, -35, 61, 9)
            elif self.is_running == True:
                if self.show_running == 1:
                    if self.is_tiny == True:
                        py.blt(self.x, self.y+26, 1, 34, 141, -17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 72, 0, -35, 61,  9)
                else:
                    if self.is_tiny == True:
                        py.blt(self.x, self.y+26, 1, 51, 141, -17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 107, 0, -35, 61,  9)
            else:
                if self.is_invi == True:
                    py.blt(self.x, self.y, 1, 68, 141, -35, 61, 9)
                elif self.is_tiny == True:
                    py.blt(self.x, self.y+26, 1, 0, 141, -17, 35, 9)
                else:
                    py.blt(self.x, self.y, 1, 0, 0, -35, 61, 9)

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 1.5
        self.side = True
        self.is_chasing = False
        self.is_hearing = False
        self.is_walking = 1
        
    def update(self):
        global now_enemy, now_1
        if self.is_hearing == True:
            self.speed = 0
            if py.frame_count >= now_1+30:
                self.side = not self.side
                self.is_hearing = False
                now_1 = 0
        else:
            if self.is_chasing == True:
                if self.side == True:
                    self.speed = 8
                else:
                    self.speed = -8
            else:
                if self.side == True:
                    self.speed = 1.5
                else:
                    self.speed = -1.5
        
        if self.x >= camera_x+600 or self.x >= 740:
            self.speed = -1.5
            self.side = False
            if self.x >= camera_x+700:
                self.speed = -4
        elif self.x <= camera_x-200 or self.x <= 0:
            self.speed = 1.5
            self.side = True
            if self.x <= camera_x-300:
                self.speed = 4
            
        if self.is_walking == 1 and py.frame_count>=now_enemy+20:
            now_enemy = py.frame_count
            self.is_walking = 2
        elif self.is_walking == 2 and py.frame_count>=now_enemy+20:
            self.is_walking = 1
            now_enemy = py.frame_count
            
        self.x += self.speed
        
    def draw(self):
        if self.is_chasing == False:
            if self.side == True:
                if self.is_walking == 1:
                    py.blt(self.x, self.y, 0, 0, 0, 106, 142, 7)
                else:
                    py.blt(self.x-5, self.y, 0, 109, 0, 110, 142, 7)
            else:
                if self.is_walking == 1:
                    py.blt(self.x, self.y, 0, 0, 0, -106, 142, 7)
                else:
                    py.blt(self.x, self.y, 0, 109, 0, -110, 142, 7)
        else:
            if self.side == True:
                py.blt(self.x, self.y+30, 0, 0, 144, 170, 112, 7)
            else:
                py.blt(self.x, self.y+30, 0, 0, 144, -170, 112, 7)
        
class Objects:
    def __init__(self):
        
        self.safes_1 = [[190,146],[70,402]]
        self.safes_2 = [[550,152],[320,408]]
        self.safes_3 = [[70,159],[400,159],[230,415],[435,415]]
        
        self.obj_1 = (1, 0, 63, 124, 78, 9)
        self.obj_2 = (1, 124, 69, 81, 72, 9)
        self.obj_3 = (1, 144, 1, 55, 66, 9)
        
        self.door = (1, 205, 0, 16, 126, 9)
        self.doors_xy_left = [[0,98],[0,354],[0,866]]
        self.doors_xy_right = [[2000,98],[2000,354],[1265,258],[2032,610]]
        
        self.torches = [[1000,351],[1050,351],[1100,351],[1150,351],[1200,351]]
        
        self.spikes = (1, 224, 160, 32, 32, 9)
        self.fire = True
        
    def draw_tochas(self):
        for i in range(len(self.torches)):
            py.blt(self.torches[i][0], self.torches[i][1],1,211,127,12,33,9)
    
    def draw_spikes_fase3(self, h):
        for i in range(1568,2000,32):
            py.blt(i,h,self.spikes[0],self.spikes[1],self.spikes[2],self.spikes[3],self.spikes[4],self.spikes[5])
            py.rect(i,220,32,h-220,0)
            
    def draw_door(self):
        for i in range(len(self.doors_xy_right)):
                py.blt(self.doors_xy_right[i][0], self.doors_xy_right[i][1], self.door[0], self.door[1], self.door[2], self.door[3], self.door[4], self.door[5])
        for i in range(len(self.doors_xy_left)):
                py.blt(self.doors_xy_left[i][0], self.doors_xy_left[i][1], self.door[0], self.door[1], self.door[2], -self.door[3], self.door[4], self.door[5])
         
    def draw_hide(self):
        for i in range(len(self.safes_1)):
            py.blt(self.safes_1[i][0], self.safes_1[i][1], self.obj_1[0], self.obj_1[1], self.obj_1[2], self.obj_1[3], self.obj_1[4], self.obj_1[5])
        for i in range(len(self.safes_2)):
            py.blt(self.safes_2[i][0], self.safes_2[i][1], self.obj_2[0], self.obj_2[1], self.obj_2[2], self.obj_2[3], self.obj_2[4], self.obj_2[5])
        for i in range(len(self.safes_3)):
            py.blt(self.safes_3[i][0], self.safes_3[i][1], self.obj_3[0], self.obj_3[1], self.obj_3[2], self.obj_3[3], self.obj_3[4], self.obj_3[5])

    def draw_back(self):
        py.rect(camera_x, 0, screen_x, 50, 1)
        py.rect(0, 220, screen_x, 30, 1)
        py.rect(-300, 0, 300, 800, 0)
        py.rect(2013,300,300,700,0)

class Boss:
    def __init__(self):
        self.x = 300
        self.y = 550
        self.up_down = False
        self.image = (2,143,95,112 ,160,7)
    
    def update(self):
        global now_1
        if now_1+20 <= py.frame_count:
            now_1 = py.frame_count
            self.up_down = not(self.up_down)
        if self.up_down == True:
            self.y += 1
        else:
            self.y -= 1
    
    def draw(self):
        py.blt(self.x, self.y, self.image[0], self.image[1], self.image[2], self.image[3], self.image[4],self.image[5])
        py.blt(self.x+self.image[3], self.y, self.image[0], self.image[1], self.image[2], -self.image[3], self.image[4], self.image[5])
        
class App:
    def __init__(self):  
        self.main = Character(screen_x/2-18, screen_y-87, True)
        self.vilain = Enemy(screen_x/2-106,screen_y-175)
        self.cenary = Objects()
        self.boss = Boss()
        
        self.passed_2 = False
        self.start_shaking = False
        self.is_shaking = False
        self.spikes_y = 220
           
        py.init(screen_x,screen_y, title="Don't let he see you", fps=60)
        self.scene = scene_start
        py.load("ASSETS.pyxres")
        
        py.run(self.update,self.draw)
       
    def sumir_fase_2(self,current_1,current_2,current_3,vilain_side,vilain_x):
            self.cenary.safes_1 = current_1
            self.cenary.safes_2 = current_2
            self.cenary.safes_3 = current_3
            self.vilain.side = vilain_side
            if self.vilain.is_chasing == False:
                self.vilain.x = vilain_x
                          
    def update(self):
        if py.btn(py.KEY_Q):
            py.quit()
            
        if self.scene == scene_start:    
            self.update_start()

        elif self.scene == scene_death:
            self.update_death()        
        
        elif self.scene == scene_win:
            self.update_win()
                        
        elif self.scene == scene_stage_1:
            self.update_stage_1()
            
        elif self.scene == scene_stage_2:
            self.update_stage_2()
            
        elif self.scene == scene_stage_3:
            self.update_stage_3()
            
        elif self.scene == scene_stage_4:
            self.update_stage_4()
            
        elif self.scene == scene_stage_5:
            self.update_stage_5()
            
        elif self.scene == scene_stage_6:
            self.update_stage_6()
                       
    def update_start(self):
        if py.btnp(py.KEY_RETURN) or py.btnp(py.GAMEPAD1_BUTTON_X):
            self.scene = scene_stage_1
            
    def update_stage_1(self):
        global camera_x, camera_y, now_1
        self.main.update()
        self.main.hiding(self.scene)
        self.vilain.update()

        if self.main.x >= 220 and self.main.x <= 250 and self.main.y == 419 and self.passed_2 == False:
            self.scene = scene_stage_2
            now_1 = py.frame_count
        if self.main.x <= 4 and self.main.y == 419:
            self.main.x = 2000-self.main.w
            self.scene = scene_stage_3
            now_1 = 0
        if self.main.x <= 4 and self.main.y == 163:
            self.scene = scene_stage_4
            self.main.x = 1975
        if self.main.x >= 1252 and self.main.y == 323:
            now_1 = py.frame_count
            self.start_shaking = False
            self.scene = scene_stage_5
            self.main.x = 10
            self.main.y = 931
            self.tremendo = 0
        if self.main.x < self.vilain.x and self.vilain.side == 0 and self.main.is_hided == False and (
        self.vilain.x < camera_x+450) and self.main.y == 163:
            self.vilain.is_chasing = True
        if self.main.x > self.vilain.x and self.vilain.side == 1 and self.main.is_hided == False and (
        self.vilain.x > camera_x-50) and self.main.y == 163:
            self.vilain.is_chasing = True
        if self.vilain.is_chasing == True and self.main.x in range(int(self.vilain.x),int(self.vilain.x+100)):
            self.main.is_alive = False

        if (self.main.x+20 < self.vilain.x and self.main.x > self.vilain.x-100 and py.btn(py.KEY_SHIFT) and self.vilain.side == True) or (
            self.main.x > self.vilain.x+100 and self.main.x < self.vilain.x+200 and py.btn(py.KEY_SHIFT) and self.vilain.side == False):
            if now_1 == 0:
                self.vilain.is_hearing = True
                now_1 = py.frame_count
                
        camera_x = self.main.x-242
        camera_y = self.main.y-163
        
        if self.main.y>=163 and self.main.y<=323:
            self.main.stairs(728, 910, False, 163, 323)
        if self.main.y>=323 and self.main.y<=500:
            self.main.stairs(527, 643, True, 419, 323)

        if self.main.x>=643 and self.main.x<=910:
            if self.main.y <= 325 and self.main.y >=322 and (not py.btn(py.KEY_W) or (self.main.x>=740 and self.main.x<=894)):
                self.main.y = 323
        elif self.main.x <= 642 and self.main.y <= 170 and self.main.y >= 150:
            self.main.y = 163
                
        self.main.y = max(self.main.y, 0)
        self.main.y = min(self.main.y, 1000)
        if self.main.is_alive == False:
            self.scene = scene_death
            now_1 = py.frame_count
            self.tremendo = 0
        self.cenary.draw_hide()
    
    def update_stage_2(self):
        global camera_x, camera_y, now_1
        self.main.update()
        self.main.hiding(self.scene)
        self.vilain.update()
        self.main.x = min(self.main.x, 500) 
        if self.main.is_alive == False:
            self.scene = scene_death
            now_1 = py.frame_count
            self.tremendo = 0
        camera_x = self.main.x-242
        camera_y = self.main.y-163

        if self.main.x < self.vilain.x and self.vilain.side == 0 and self.main.is_hided == False and self.main.y == 419 and (
        self.vilain.x < camera_x+450) and self.vilain.y == 319:
            self.vilain.is_chasing = True
        if self.main.x > self.vilain.x and self.vilain.side == 1 and self.main.is_hided == False and self.main.y == 419 and self.vilain.y == 319:
            self.vilain.is_chasing = True
        if self.vilain.is_chasing == True and self.main.x in range(int(self.vilain.x),int(self.vilain.x+100)):
            self.main.is_alive = False

        if now_1+600 >= py.frame_count:
            self.main.is_running = False
            self.main.is_walking = False
            self.main.x = 244
        elif now_1+700 >= py.frame_count:
            self.vilain.y = 319
            self.main.x = 244
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],True,30)           
        elif now_1+900 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],False,30)           
        elif now_1+1000 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[435,415]],False,30)           
        elif now_1+1200 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[435,415]],True,30)           
        elif now_1+1300 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],False,30) 
        elif now_1+1450 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[0,0]],[[230,415]],False,30)
        elif now_1+1650 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[0,0]],[[230,415]],True,30)
        elif now_1+1750 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],False,30)
        elif now_1+1900 >= py.frame_count:
            self.sumir_fase_2([[0,0]],[[320,408]],[[435,415]],False,30)
        elif now_1+2100 >= py.frame_count:
            self.sumir_fase_2([[0,0]],[[320,408]],[[435,415]],True,30)
        elif now_1+2200 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],False,30)
        elif now_1+2350 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[0,0]],[[0,0]],False,30)
        elif now_1+2550 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[0,0]],[[0,0]],True,30)
        elif now_1+2650 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],False,30)
        elif now_1+2800 >= py.frame_count:
            self.sumir_fase_2([[0,0]],[[0,0]],[[435,415]],False,30)
        elif now_1+3000 >= py.frame_count:
            self.sumir_fase_2([[0,0]],[[0,0]],[[435,415]],True,30)
        elif now_1+3200 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],False,450)
        else:
            self.passed_2 = True
            self.scene = scene_stage_1
            self.vilain.x = 0
            self.vilain.y = 80
            self.vilain.is_chasing = False
            self.cenary.safes_1 = [[190,146],[70,402]]
            self.cenary.safes_2 = [[550,152],[320,408]]
            self.cenary.safes_3 = [[70,159],[400,159],[230,415],[435,415]]
            now_1 = 0

    def update_stage_3(self):
        global camera_x, camera_y, now_1
        camera_x = 1542
        camera_y = 256
        self.main.x = max(self.main.x, 1568)
        self.main.update()
        self.main.hiding(self.scene)
        self.vilain.update()
        if self.main.x+self.main.w >= 2002:
            self.scene = scene_stage_1
            self.main.x = 5
            self.cenary.safes_1 = [[190,146],[70,402]]
            self.cenary.safes_2 = [[550,152],[320,408]]
            self.cenary.safes_3 = [[70,159],[400,159],[230,415],[435,415]]
            now_1 = 0
        if self.main.x <= 1785:
            self.main.power_tiny = True
        if self.spikes_y+32 >= self.main.y and self.main.is_tiny == False:
            self.scene = scene_death
            now_1 = py.frame_count
            self.tremendo = 0
        
    def update_stage_4(self):
        global camera_x, camera_y, now_1
        self.main.update()
        self.main.hiding(self.scene)
        self.main.x = max(self.main.x, 1568)
        self.vilain.update()
        if self.main.x <= 1645:
            self.main.power_invi = True
        if self.main.x >= 1980:
            self.scene = scene_stage_1
            self.main.x = 5
            self.main.y = screen_y-87
            self.vilain.x = 300
            self.vilain.side = True
            self.cenary.safes_1 = [[190,146],[70,402]]
            self.cenary.safes_2 = [[550,152],[320,408]]
            self.cenary.safes_3 = [[70,159],[400,159],[230,415],[435,415]]
            self.vilain.is_chasing = False
            camera_x = self.main.x-242
            camera_y = screen_y-250 
            now_1 = 0
        if self.main.x >= 1753 and self.main.x <= 1848 and self.main.is_tiny == False:
            self.scene = scene_death
            now_1 = py.frame_count
            self.tremendo = 0
        camera_x = 1542
        camera_y = 0
        
    def update_stage_5(self):
        global camera_x, camera_y, now_1, now_2
        if self.start_shaking == False:
            camera_x = self.main.x-242
            camera_y = self.main.y-163
        self.main.update()
        self.main.is_hided = True
        self.cenary.draw_hide()
        self.cenary.draw_door()
        if self.main.x >= 396:
            self.main.x = 397
            self.start_shaking = True
            if self.is_shaking == True:
                camera_x += 10
            else:
                camera_x -= 10
            self.tremendo += 1
        if self.main.x <= 3:
            self.scene = scene_stage_1
            self.main.x = 1245
            self.main.y = 323
            self.vilain.x = 300
            self.vilain.side = True
            self.cenary.safes_1 = [[190,146],[70,402]]
            self.cenary.safes_2 = [[550,152],[320,408]]
            self.cenary.safes_3 = [[70,159],[400,159],[230,415],[435,415]]
            self.vilain.is_chasing = False
            now_1 = 0

        if now_1+5 <= py.frame_count:
            self.is_shaking = not(self.is_shaking)
            now_1 = py.frame_count
        if self.tremendo >= 100:
            self.scene = scene_stage_6
            self.main.y = 675
            self.boss.y = 550
            now_2 = py.frame_count
           
    def update_stage_6(self):
        global camera_x, camera_y, now_1
        camera_x = self.main.x-242
        camera_y = self.main.y-163
        if self.main.is_hided == False:
            self.scene = scene_death
            self.tremendo = 0
            now_1 = py.frame_count
        if self.main.x >= 2005:
            self.scene = scene_win
        self.main.x = max(self.main.x, 150)
        self.boss.x = self.main.x - 97
        self.boss.update()
        self.main.update()
        self.main.hiding(self.scene)
        
    def update_death(self):
        global camera_x, camera_y, now_1, now_2
        camera_x = 0
        camera_y = 0
        self.boss.x = 130
        self.boss.y = 60
        if now_1+5 <= py.frame_count:
            self.is_shaking = not(self.is_shaking)
            now_1 = py.frame_count
        if self.is_shaking == True:
            camera_x += 10
        else:
            camera_x -= 10
        self.tremendo += 1
        if self.tremendo >= 100:
            if py.btnp(py.KEY_RETURN) or py.btnp(py.GAMEPAD1_BUTTON_X):
                now_1 = 0
                self.main.x = screen_x/2-18
                self.main.y = screen_y-87
                self.vilain.x = 200
                self.vilain.y = 80
                self.vilain.side = True
                self.main.is_alive = True
                self.vilain.is_chasing = False
                self.cenary.safes_1 = [[190,146],[70,402]]
                self.cenary.safes_2 = [[550,152],[320,408]]
                self.cenary.safes_3 = [[70,159],[400,159],[230,415],[435,415]]
                self.scene = scene_stage_1
            
    def update_win(self):
        global camera_x, camera_y, now_1
        self.main.x = 245
        self.main.y = 150
        self.main.side = True
        camera_x = 0
        camera_y = 0
        if py.btnp(py.KEY_RETURN) or py.btnp(py.GAMEPAD1_BUTTON_X):
            now_1 = 0
            self.scene = scene_stage_1
            self.main.x = screen_x/2-18
            self.main.y = screen_y-87
            self.vilain.x = 0
            self.vilain.y = 80
            self.main.is_alive = True
            self.vilain.is_chasing = False
            self.cenary.safes_1 = [[190,146],[70,402]]
            self.cenary.safes_2 = [[550,152],[320,408]]
            self.cenary.safes_3 = [[70,159],[400,159],[230,415],[435,415]]

            
    def draw(self):
        py.cls(0)
        py.camera(camera_x,camera_y)
        if self.scene == scene_start:
            self.draw_start()

        elif self.scene == scene_death:
            self.draw_death()
        
        elif self.scene == scene_win:
            self.draw_win()
                    
        elif self.scene == scene_stage_1:
            self.draw_stage_1()
            
        elif self.scene == scene_stage_2:
            self.draw_stage_2()
            
        elif self.scene == scene_stage_3:
            self.draw_stage_3()
            
        elif self.scene == scene_stage_4:
            self.draw_stage_4()
            
        elif self.scene == scene_stage_5:
            self.draw_stage_5()
            
        elif self.scene == scene_stage_6:
            self.draw_stage_6()
            
    def draw_start(self):
        py.text(35, 66, "Don't let he see you.", 13)
        py.text(31, 126, "- PRESS ENTER -", 13)
        py.blt(386,60,2,142,95,114,161,7)
    
    def draw_stage_1(self):
        
        self.cenary.draw_back()
        py.bltm(0, 0, 0, 0, 0, 2100, 700, 9)
        self.vilain.draw()
        self.cenary.draw_hide()
        self.cenary.draw_door()
        self.main.draw()
        self.cenary.draw_tochas()

    def draw_stage_2(self):
        global now_2
        self.cenary.draw_back()
        py.bltm(0, 0, 0, 0, 0, 1000, 1000, 9)
        self.vilain.draw()
        self.cenary.draw_hide()
        self.cenary.draw_door()
        self.main.draw()
        if now_2+15 <= py.frame_count:
            self.cenary.fire = not(self.cenary.fire)
            now_2 = py.frame_count
        
        if now_1+300 >= py.frame_count:
            py.rect(self.main.x-37,self.main.y-112,124,34,7)
            py.rect(self.main.x-35,self.main.y-110,120,30,0)
            py.text(self.main.x-25,self.main.y-100,'I see you down stairs...', 7)
        elif now_1+400 >= py.frame_count:
            py.rect(self.main.x-37,self.main.y-112,124,34,7)
            py.rect(self.main.x-35,self.main.y-110,120,30,0)
            py.text(self.main.x-25,self.main.y-100,'...', 7)
        elif now_1+600 >= py.frame_count:
            py.rect(self.main.x-37,self.main.y-112,124,34,7)
            py.rect(self.main.x-35,self.main.y-110,120,30,0)
            py.text(self.main.x-25,self.main.y-100,"let's play a game...", 7)
            
        elif now_1+800 <= py.frame_count and now_1+900 >= py.frame_count:
            if self.cenary.fire == True:
                py.blt(228,460,2,0,0,59,25,7)
            else:
                py.blt(228,460,2,0,26,59,25,7) 
        elif now_1+1200 <= py.frame_count and now_1+1300 >= py.frame_count:
            if self.cenary.fire == True:
                py.blt(433,460,2,0,0,59,25,7)
                py.blt(314,460,2,59,0,92,26,7)
            else:
                py.blt(433,460,2,0,26,59,25,7)
                py.blt(314,460,2,59,28,92,26,7)
        elif now_1+1650 <= py.frame_count and now_1+1750 >= py.frame_count:
            if self.cenary.fire == True:
                py.blt(228,460,2,0,0,59,25,7)
                py.blt(64,460,2,0,53,130,24,7)
            else:
                py.blt(228,460,2,0,26,59,25,7)
                py.blt(64,460,2,0,77,130,24,7)
        elif now_1+2100 <= py.frame_count and now_1+2200 >= py.frame_count:
            if self.cenary.fire == True:
                py.blt(228,460,2,0,0,59,25,7)
                py.blt(433,460,2,0,0,59,25,7)
                py.blt(314,460,2,59,0,92,26,7)
            else:
                py.blt(228,460,2,0,26,59,25,7) 
                py.blt(433,460,2,0,26,59,25,7)
                py.blt(314,460,2,59,28,92,26,7)
        elif now_1+2550 <= py.frame_count and now_1+2650 >= py.frame_count:
            if self.cenary.fire == True:
                py.blt(228,460,2,0,0,59,25,7)
                py.blt(314,460,2,59,0,92,26,7)
                py.blt(64,460,2,0,53,130,24,7)
            else:
                py.blt(228,460,2,0,26,59,25,7) 
                py.blt(314,460,2,59,28,92,26,7)
                py.blt(64,460,2,0,77,130,24,7)
        elif now_1+3000 <= py.frame_count and now_1+3200 >= py.frame_count:
            py.rect(self.main.x-22,self.main.y-130,170,34,7)
            py.rect(self.main.x-20,self.main.y-128,166,30,0)
            py.text(self.main.x-10,self.main.y-118,'hm... must have returned back upstairs', 7)
            
    def draw_stage_3(self):
        global now_1
        self.cenary.draw_back()
        py.bltm(0, 0, 0, 0, 0, 2500, 2500, 9)
        self.vilain.draw()
        self.cenary.draw_hide()
        self.cenary.draw_door()
        self.main.draw()
        if self.main.power_tiny == True:
            if now_1 <= py.frame_count and self.spikes_y<=415:
                self.spikes_y+=1
                now_1 = py.frame_count
            py.rect(camera_x+188,camera_y+214,134,34,7)
            py.rect(camera_x+190,camera_y+216,130,30,0)
            py.text(camera_x+200,camera_y+226,'Hold CTRL to get tiny.', 7)
                
            self.cenary.draw_spikes_fase3(self.spikes_y)
        else:
            py.blt(1785,410,1,197,146,14,14,9)
             
    def draw_stage_4(self):
        self.cenary.draw_back()
        self.vilain.draw()
        py.bltm(0, 0, 0, 0, 0, 2100, 2100, 9)
        self.main.draw()
        if self.main.power_invi == False:
            py.blt(1657,153,1,183,146,14,14,9)
        else:
            py.rect(camera_x+178,camera_y+214,154,34,7)
            py.rect(camera_x+180,camera_y+216,150,30,0)
            py.text(camera_x+190,camera_y+226,'Press E to get invisible.', 7)
        self.cenary.draw_hide()
        self.cenary.draw_door()
        
    def draw_stage_5(self):
        self.cenary.draw_back()
        py.bltm(0, 0, 0, 0, 0, 2100, 2100, 9)
        self.cenary.draw_hide()
        self.cenary.draw_door()
        self.main.draw()
        
    def draw_stage_6(self):
        self.boss.draw()
        self.cenary.draw_back()
        py.bltm(0, 0, 0, 0, 0, 2100, 2100, 9)
        self.cenary.draw_hide()
        self.cenary.draw_door()
        self.main.draw()
        if now_2+150 >= py.frame_count:
            py.rect(self.main.x-37,self.main.y-112,124,34,7)
            py.rect(self.main.x-35,self.main.y-110,120,30,0)
            py.text(self.main.x-25,self.main.y-100,'ENOUGH!!!', 7)
        elif now_2+300 >= py.frame_count:
            py.rect(self.main.x-37,self.main.y-112,124,34,7)
            py.rect(self.main.x-35,self.main.y-110,120,30,0)
            py.text(self.main.x-25,self.main.y-100,'I AM TIRED OF YOU!', 7)
        elif now_2+450 >= py.frame_count:
            py.rect(self.main.x-37,self.main.y-112,150,34,7)
            py.rect(self.main.x-35,self.main.y-110,146,30,0)
            py.text(self.main.x-25,self.main.y-100,'You will not escape from here.', 7)
        
    def draw_death(self):
        if self.tremendo <= 100:
            self.boss.draw()
        else:
            py.camera()
            py.text(225, 50, "GAME OVER", 8)
            py.text(210, 90, "- PRESS ENTER -", 13)
        
    def draw_win(self):
        py.camera()
        self.main.draw()
        self.main.is_invi = False
        self.main.is_tiny = False
        py.text(225, 50, "YOU WIN", 3)
        py.text(215, 90, "- PRESS ENTER -", 13)
App()
