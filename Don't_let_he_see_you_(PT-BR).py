import pyxel as py

cena_inicio = 0
cena_fase1 = 1
cena_fase2 = 2
cena_fase3 = 3
cena_fase4 = 4
cena_fase5 = 5
cena_fase6 = 6
cena_morte = 7
cena_vitoria = 8


tela_x = 500
tela_y = 250
agora = 0
agora1 = 0
now_e = 0
now_m1 = 0
now_m2 = 0
camerax = 0
cameray = 0        

class Character:
    def __init__(self, x, y, vivo):
        self.x = x
        self.y = y
        self.w = 35
        self.h = 61
        self.speed = 1
        self.vivo = vivo
        self.hided = True
        self.is_running = False
        self.lado = True
        self.is_walking = False
        self.mostra_caminha = 1
        self.mostra_corre = 1
        self.power_invi = False
        self.is_invi = False
        self.usou_invi = False
        self.agora_invi = 0
        self.power_dimi = False
        self.is_dimi = False

    def stairs(self, position_i, position_f, direction, alt_max, alt_min):
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
        elif self.x in range(position_i,position_i+10) and self.y != alt_min:
            self.y = alt_max
        elif self.x in range(position_f-10,position_f) and self.y != alt_max:
            self.y = alt_min
            
    def running(self):
        if self.is_running == True and self.is_invi == False:
            self.is_walking = False
            self.speed = 5
        else:
            self.speed = 1 
    
    def hiding(self, cena):
        if self.is_dimi == True:
            y = tela_y - 30
        else:
            y = tela_y - 87
            
        if py.pget(tela_x/2,y) == 0 and py.pget(tela_x/2+17,y) == 0 and cena!=cena_fase6:
            self.hided = True
        elif self.power_invi == True and self.is_invi:
            self.hided = True
        elif cena==cena_fase6:
            if py.pget(tela_x/2,y) == 0 and py.pget(tela_x/2+20,y) == 0:
                self.hided = False
            else:
                self.hided = True
        else:
            self.hided = False
    
    def update(self):
        global now_m1, now_m2
        if py.btnp(py.KEY_Q):
            py.quit()
        if py.btn(py.KEY_A):
            self.x -= self.speed
            self.lado = False
            self.is_walking = True
        elif py.btn(py.KEY_D):
            self.x += self.speed
            self.lado = True
            self.is_walking = True
        else:
            self.is_walking = False
            
        if py.btn(py.KEY_W) and py.pget(self.x,self.y) == 3 and py.pget(self.x+self.w,self.y)==3:
            self.y -= self.speed
        if py.btn(py.KEY_S) and self.y != tela_y-20 and py.pget(self.x-1,self.y)==3 and py.pget(self.x+21,self.y)==3:
            self.y += self.speed

        if py.btn(py.KEY_SHIFT) and (py.btn(py.KEY_A) or py.btn(py.KEY_D)):
            self.is_running = True
        else:
            self.is_running = False
            
        self.running()
        
        if py.btnp(py.KEY_E) and self.power_invi == True and self.usou_invi == False:
            self.is_invi = True
            self.agora_invi = py.frame_count
        if self.agora_invi+300 <= py.frame_count and self.is_invi == True:
            self.is_invi = False
            self.usou_invi = True
            self.agora_invi = py.frame_count
        if self.agora_invi+400 <= py.frame_count and self.usou_invi == True:
            self.usou_invi = False

        if py.btn(py.KEY_CTRL) and self.power_dimi == True:
            self.is_dimi = True
            self.is_invi = False
            self.usou_invi = True
        else:
            self.is_dimi = False

        if py.frame_count>=now_m1+15 and self.mostra_caminha == 1:
            self.mostra_caminha = 2
            now_m1 = py.frame_count
        elif py.frame_count>=now_m1+15 and self.mostra_caminha == 2:
            self.mostra_caminha = 1
            now_m1 = py.frame_count
            
        if py.frame_count>=now_m2+5 and self.mostra_corre == 1:
            self.mostra_corre = 2
            now_m2 = py.frame_count
        elif py.frame_count>=now_m2+5 and self.mostra_corre == 2:
            self.mostra_corre = 1
            now_m2 = py.frame_count
            
    def draw(self):
        if self.lado == True:
            if self.is_walking == True:
                if self.mostra_caminha == 1:
                    if self.is_invi == True:
                        py.blt(self.x, self.y, 1, 68, 141, 35, 61, 9)
                    elif self.is_dimi == True:
                        py.blt(self.x, self.y+26, 1, 0, 141, 17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 0, 0, 35, 61, 9)
                else:
                    if self.is_invi == True:
                        py.blt(self.x, self.y, 1, 104, 141, 35, 61, 9)
                    elif self.is_dimi == True:
                        py.blt(self.x, self.y+26, 1, 17, 141, 17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 36, 0, 35, 61, 9)
            elif self.is_running == True:
                if self.mostra_corre == 1:
                    if self.is_dimi == True:
                        py.blt(self.x, self.y+26, 1, 34, 141, 17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 72, 0, 35, 61,  9)
                else:
                    if self.is_dimi == True:
                        py.blt(self.x, self.y+26, 1, 51, 141, 17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 107, 0, 35, 61,  9) 
            else:
                if self.is_invi == True:
                    py.blt(self.x, self.y, 1, 68, 141, 35, 61, 9)
                elif self.is_dimi == True:
                    py.blt(self.x, self.y+26, 1, 0, 141, 17, 35, 9)
                else:
                    py.blt(self.x, self.y, 1, 0, 0, 35, 61, 9)
        else:
            if self.is_walking == True:
                if self.mostra_caminha == 1:
                    if self.is_invi == True: 
                        py.blt(self.x, self.y, 1, 68, 141, -35, 61, 9)
                    elif self.is_dimi == True:
                        py.blt(self.x, self.y+26, 1, 0, 141, -17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 0, 0, -35, 61, 9)
                else:
                    if self.is_invi == True:
                        py.blt(self.x, self.y, 1, 104, 141, -35, 61, 9)
                    elif self.is_dimi == True:
                        py.blt(self.x, self.y+26, 1, 17, 141, -17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 36, 0, -35, 61, 9)
            elif self.is_running == True:
                if self.mostra_corre == 1:
                    if self.is_dimi == True:
                        py.blt(self.x, self.y+26, 1, 34, 141, -17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 72, 0, -35, 61,  9)
                else:
                    if self.is_dimi == True:
                        py.blt(self.x, self.y+26, 1, 51, 141, -17, 35, 9)
                    else:
                        py.blt(self.x, self.y, 1, 107, 0, -35, 61,  9)
            else:
                if self.is_invi == True:
                    py.blt(self.x, self.y, 1, 68, 141, -35, 61, 9)
                elif self.is_dimi == True:
                    py.blt(self.x, self.y+26, 1, 0, 141, -17, 35, 9)
                else:
                    py.blt(self.x, self.y, 1, 0, 0, -35, 61, 9)

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speed = 1.5
        self.lado = True
        self.chasing = False
        self.hearing = False
        self.walking = 1
        
    def update(self):
        global now_e, agora
        if self.hearing == True:
            self.speed = 0
            if py.frame_count >= agora+30:
                self.lado = not self.lado
                self.hearing = False
                agora = 0
        else:
            if self.chasing == True:
                if self.lado == True:
                    self.speed = 8
                else:
                    self.speed = -8
            else:
                if self.lado == True:
                    self.speed = 1.5
                else:
                    self.speed = -1.5
        
        if self.x >= camerax+600 or self.x >= 740:
            self.speed = -1.5
            self.lado = False
            if self.x >= camerax+700:
                self.speed = -4
        elif self.x <= camerax-200 or self.x <= 0:
            self.speed = 1.5
            self.lado = True
            if self.x <= camerax-300:
                self.speed = 4
            
        if self.walking == 1 and py.frame_count>=now_e+20:
            now_e = py.frame_count
            self.walking = 2
        elif self.walking == 2 and py.frame_count>=now_e+20:
            self.walking = 1
            now_e = py.frame_count
            
        self.x += self.speed
        
    def draw(self):
        if self.chasing == False:
            if self.lado == True:
                if self.walking == 1:
                    py.blt(self.x, self.y, 0, 0, 0, 106, 142, 7)
                else:
                    py.blt(self.x-5, self.y, 0, 109, 0, 110, 142, 7)
            else:
                if self.walking == 1:
                    py.blt(self.x, self.y, 0, 0, 0, -106, 142, 7)
                else:
                    py.blt(self.x, self.y, 0, 109, 0, -110, 142, 7)
        else:
            if self.lado == True:
                py.blt(self.x, self.y+30, 0, 0, 144, 170, 112, 7)
            else:
                py.blt(self.x, self.y+30, 0, 0, 144, -170, 112, 7)
        
class Objects:
    def __init__(self):
        
        self.safes1 = [[190,146],[70,402]]
        self.safes2 = [[550,152],[320,408]]
        self.safes3 = [[70,159],[400,159],[230,415],[435,415]]
        
        self.obj1 = (1, 0, 63, 124, 78, 9)
        self.obj2 = (1, 124, 69, 81, 72, 9)
        self.obj3 = (1, 144, 1, 55, 66, 9)
        
        self.porta = (1, 205, 0, 16, 126, 9)
        self.portasxy_esq = [[0,98],[0,354],[0,866]]
        self.portasxy_dir = [[2000,98],[2000,354],[1265,258],[2032,610]]
        
        self.tochas = [[1000,351],[1050,351],[1100,351],[1150,351],[1200,351]]
        
        self.spikes = (1, 224, 160, 32, 32, 9)
        self.fogo = True
        
        self.colunas = [45, 230, 415]
        self.win = 1000
        self.fase1 = 0
        self.fase4 = 3
    def draw_tochas(self):
        for i in range(len(self.tochas)):
            py.blt(self.tochas[i][0], self.tochas[i][1],1,211,127,12,33,9)
    
    def draw_spikes_fase3(self, altura):
        for i in range(1568,2000,32):
            py.blt(i,altura,self.spikes[0],self.spikes[1],self.spikes[2],self.spikes[3],self.spikes[4],self.spikes[5])
            py.rect(i,220,32,altura-220,0)
            
    def draw_door(self):
        for i in range(len(self.portasxy_dir)):
                py.blt(self.portasxy_dir[i][0], self.portasxy_dir[i][1], self.porta[0], self.porta[1], self.porta[2], self.porta[3], self.porta[4], self.porta[5])
        for i in range(len(self.portasxy_esq)):
                py.blt(self.portasxy_esq[i][0], self.portasxy_esq[i][1], self.porta[0], self.porta[1], self.porta[2], -self.porta[3], self.porta[4], self.porta[5])
         
    def draw_hide(self):
        for i in range(len(self.safes1)):
            py.blt(self.safes1[i][0], self.safes1[i][1], self.obj1[0], self.obj1[1], self.obj1[2], self.obj1[3], self.obj1[4], self.obj1[5])
        for i in range(len(self.safes2)):
            py.blt(self.safes2[i][0], self.safes2[i][1], self.obj2[0], self.obj2[1], self.obj2[2], self.obj2[3], self.obj2[4], self.obj2[5])
        for i in range(len(self.safes3)):
            py.blt(self.safes3[i][0], self.safes3[i][1], self.obj3[0], self.obj3[1], self.obj3[2], self.obj3[3], self.obj3[4], self.obj3[5])

    def draw_back(self):
        py.rect(camerax, 0, tela_x, 50, 1)
        py.rect(0, 220, tela_x, 30, 1)
        py.rect(-300, 0, 300, 800, 0)
        py.rect(2013,300,300,700,0)

class Boss:
    def __init__(self):
        self.x = 300
        self.y = 550
        self.sobe_desce = False
        self.angry = False
        self.imagem = (2,143,95,112 ,160,7)
    
    def update(self):
        global agora
        if agora+20 <= py.frame_count:
            agora = py.frame_count
            self.sobe_desce = not(self.sobe_desce)
        if self.sobe_desce == True:
            self.y += 1
        else:
            self.y -= 1
    
    def draw(self):
        py.blt(self.x, self.y, self.imagem[0], self.imagem[1], self.imagem[2], self.imagem[3], self.imagem[4],self.imagem[5])
        py.blt(self.x+self.imagem[3], self.y, self.imagem[0], self.imagem[1], self.imagem[2], -self.imagem[3], self.imagem[4], self.imagem[5])
        
class App:
    def __init__(self):  
        self.main = Character(tela_x/2-18, tela_y-87, True)
        self.vilain = Enemy(tela_x/2-106,tela_y-175)
        self.cenary = Objects()
        self.boss = Boss()
        
        self.passou_2 = False
        self.inicio_treme = False
        self.treme = False
        self.spikes_y = 220
           
        py.init(tela_x,tela_y,'Não deixe que ele te veja',60)
        self.cena = cena_inicio
        py.load("ASSETS.pyxres")
        
        py.run(self.update,self.draw)
       
    def sumir_fase_2(self,atual1,atual2,atual3,vilao_lado,vilao_x):
            self.cenary.safes1 = atual1
            self.cenary.safes2 = atual2
            self.cenary.safes3 = atual3
            self.vilain.lado = vilao_lado
            if self.vilain.chasing == False:
                self.vilain.x = vilao_x
                          
    def update(self):
        print(self.main.power_invi, self.cena)
        if py.btn(py.KEY_Q):
            py.quit()
            
        if self.cena == cena_inicio:    
            self.update_inicio()

        elif self.cena == cena_morte:
            self.update_morte()        
        
        elif self.cena == cena_vitoria:
            self.update_vitoria()
                        
        elif self.cena == cena_fase1:
            self.update_fase1()
            
        elif self.cena == cena_fase2:
            self.update_fase2()
            
        elif self.cena == cena_fase3:
            self.update_fase3()
            
        elif self.cena == cena_fase4:
            self.update_fase4()
            
        elif self.cena == cena_fase5:
            self.update_fase5()
            
        elif self.cena == cena_fase6:
            self.update_fase6()
                       
    def update_inicio(self):
        if py.btnp(py.KEY_RETURN) or py.btnp(py.GAMEPAD1_BUTTON_X):
            self.cena = cena_fase1
            
    def update_fase1(self):
        global camerax, cameray, agora
        self.main.update()
        self.main.hiding(self.cena)
        self.vilain.update()

        if self.main.x >= 220 and self.main.x <= 250 and self.main.y == 419 and self.passou_2 == False:
            self.cena = cena_fase2
            agora = py.frame_count
        if self.main.x <= 4 and self.main.y == 419:
            self.main.x = 2000-self.main.w
            self.cena = cena_fase3
            agora = 0
        if self.main.x <= 4 and self.main.y == 163:
            self.cena = cena_fase4
            self.main.x = 1975
        if self.main.x >= 1252 and self.main.y == 323:
            agora = py.frame_count
            self.inicio_treme = False
            self.cena = cena_fase5
            self.main.x = 10
            self.main.y = 931
            self.tremendo = 0
        if self.main.x < self.vilain.x and self.vilain.lado == 0 and self.main.hided == False and (
        self.vilain.x < camerax+450) and self.main.y == 163:
            self.vilain.chasing = True
        if self.main.x > self.vilain.x and self.vilain.lado == 1 and self.main.hided == False and (
        self.vilain.x > camerax-50) and self.main.y == 163:
            self.vilain.chasing = True
        if self.vilain.chasing == True and self.main.x in range(int(self.vilain.x),int(self.vilain.x+100)):
            self.main.vivo = False

        if (self.main.x+20 < self.vilain.x and self.main.x > self.vilain.x-100 and py.btn(py.KEY_SHIFT) and self.vilain.lado == True) or (
            self.main.x > self.vilain.x+100 and self.main.x < self.vilain.x+200 and py.btn(py.KEY_SHIFT) and self.vilain.lado == False):
            if agora == 0:
                self.vilain.hearing = True
                agora = py.frame_count
                
        camerax = self.main.x-242
        cameray = self.main.y-163
        
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
        if self.main.vivo == False:
            self.cena = cena_morte
            agora = py.frame_count
            self.tremendo = 0
        self.cenary.draw_hide()
    
    def update_fase2(self):
        global camerax, cameray, agora
        self.main.update()
        self.main.hiding(self.cena)
        self.vilain.update()
        self.main.x = min(self.main.x, 500) 
        if self.main.vivo == False:
            self.cena = cena_morte
            agora = py.frame_count
            self.tremendo = 0
        camerax = self.main.x-242
        cameray = self.main.y-163

        if self.main.x < self.vilain.x and self.vilain.lado == 0 and self.main.hided == False and self.main.y == 419 and (
        self.vilain.x < camerax+450) and self.vilain.y == 319:
            self.vilain.chasing = True
        if self.main.x > self.vilain.x and self.vilain.lado == 1 and self.main.hided == False and self.main.y == 419 and self.vilain.y == 319:
            self.vilain.chasing = True
        if self.vilain.chasing == True and self.main.x in range(int(self.vilain.x),int(self.vilain.x+100)):
            self.main.vivo = False

        if agora+600 >= py.frame_count:
            self.main.is_running = False
            self.main.is_walking = False
            self.main.x = 244
        elif agora+700 >= py.frame_count:
            self.vilain.y = 319
            self.main.x = 244
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],True,30)           
        elif agora+900 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],False,30)           
        elif agora+1000 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[435,415]],False,30)           
        elif agora+1200 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[435,415]],True,30)           
        elif agora+1300 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],False,30) 
        elif agora+1450 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[0,0]],[[230,415]],False,30)
        elif agora+1650 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[0,0]],[[230,415]],True,30)
        elif agora+1750 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],False,30)
        elif agora+1900 >= py.frame_count:
            self.sumir_fase_2([[0,0]],[[320,408]],[[435,415]],False,30)
        elif agora+2100 >= py.frame_count:
            self.sumir_fase_2([[0,0]],[[320,408]],[[435,415]],True,30)
        elif agora+2200 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],False,30)
        elif agora+2350 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[0,0]],[[0,0]],False,30)
        elif agora+2550 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[0,0]],[[0,0]],True,30)
        elif agora+2650 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],False,30)
        elif agora+2800 >= py.frame_count:
            self.sumir_fase_2([[0,0]],[[0,0]],[[435,415]],False,30)
        elif agora+3000 >= py.frame_count:
            self.sumir_fase_2([[0,0]],[[0,0]],[[435,415]],True,30)
        elif agora+3200 >= py.frame_count:
            self.sumir_fase_2([[70,402]],[[320,408]],[[230,415],[435,415]],False,450)
        else:
            self.passou_2 = True
            self.cena = cena_fase1
            self.vilain.x = 0
            self.vilain.y = 80
            self.vilain.chasing = False
            self.cenary.safes1 = [[190,146],[70,402]]
            self.cenary.safes2 = [[550,152],[320,408]]
            self.cenary.safes3 = [[70,159],[400,159],[230,415],[435,415]]
            agora = 0

    def update_fase3(self):
        global camerax, cameray, agora
        camerax = 1542
        cameray = 256
        self.main.x = max(self.main.x, 1568)
        self.main.update()
        self.main.hiding(self.cena)
        self.vilain.update()
        if self.main.x+self.main.w >= 2002:
            self.cena = cena_fase1
            self.main.x = 5
            self.cenary.safes1 = [[190,146],[70,402]]
            self.cenary.safes2 = [[550,152],[320,408]]
            self.cenary.safes3 = [[70,159],[400,159],[230,415],[435,415]]
            agora = 0
        if self.main.x <= 1785:
            self.main.power_dimi = True
        if self.spikes_y+32 >= self.main.y and self.main.is_dimi == False:
            self.cena = cena_morte
            agora = py.frame_count
            self.tremendo = 0
        
    def update_fase4(self):
        global camerax, cameray, agora
        self.main.update()
        self.main.hiding(self.cena)
        self.main.x = max(self.main.x, 1568)
        self.vilain.update()
        if self.main.x <= 1645:
            self.main.power_invi = True
        if self.main.x >= 1980:
            self.cena = cena_fase1
            self.main.x = 5
            self.main.y = tela_y-87
            self.vilain.x = 300
            self.vilain.lado = True
            self.cenary.safes1 = [[190,146],[70,402]]
            self.cenary.safes2 = [[550,152],[320,408]]
            self.cenary.safes3 = [[70,159],[400,159],[230,415],[435,415]]
            self.vilain.chasing = False
            camerax = self.main.x-242
            cameray = tela_y-250 
            agora = 0
        if self.main.x >= 1753 and self.main.x <= 1848 and self.main.is_dimi == False:
            self.cena = cena_morte
            agora = py.frame_count
            self.tremendo = 0
        camerax = 1542
        cameray = 0
        
    def update_fase5(self):
        global camerax, cameray, agora, agora1
        if self.inicio_treme == False:
            camerax = self.main.x-242
            cameray = self.main.y-163
        self.main.update()
        self.main.hided = True
        self.cenary.draw_hide()
        self.cenary.draw_door()
        if self.main.x >= 396:
            self.main.x = 397
            self.inicio_treme = True
            if self.treme == True:
                camerax += 10
            else:
                camerax -= 10
            self.tremendo += 1
        if self.main.x <= 3:
            self.cena = cena_fase1
            self.main.x = 1245
            self.main.y = 323
            self.vilain.x = 300
            self.vilain.lado = True
            self.cenary.safes1 = [[190,146],[70,402]]
            self.cenary.safes2 = [[550,152],[320,408]]
            self.cenary.safes3 = [[70,159],[400,159],[230,415],[435,415]]
            self.vilain.chasing = False
            agora = 0

        if agora+5 <= py.frame_count:
            self.treme = not(self.treme)
            agora = py.frame_count
        if self.tremendo >= 100:
            self.cena = cena_fase6
            self.main.y = 675
            self.boss.y = 550
            agora1 = py.frame_count
           
    def update_fase6(self):
        global camerax, cameray, agora
        camerax = self.main.x-242
        cameray = self.main.y-163
        if self.main.hided == False:
            self.cena = cena_morte
            self.tremendo = 0
            agora = py.frame_count
        if self.main.x >= 2005:
            self.cena = cena_vitoria
        self.main.x = max(self.main.x, 150)
        self.boss.x = self.main.x - 97
        self.boss.update()
        self.main.update()
        self.main.hiding(self.cena)
        
    def update_morte(self):
        global camerax, cameray, agora, agora1
        camerax = 0
        cameray = 0
        self.boss.x = 130
        self.boss.y = 60
        if agora+5 <= py.frame_count:
            self.treme = not(self.treme)
            agora = py.frame_count
        if self.treme == True:
            camerax += 10
        else:
            camerax -= 10
        self.tremendo += 1
        if self.tremendo >= 100:
            if py.btnp(py.KEY_RETURN) or py.btnp(py.GAMEPAD1_BUTTON_X):
                agora = 0
                self.main.x = tela_x/2-18
                self.main.y = tela_y-87
                self.vilain.x = 200
                self.vilain.y = 80
                self.vilain.lado = True
                self.main.vivo = True
                self.vilain.chasing = False
                self.cenary.safes1 = [[190,146],[70,402]]
                self.cenary.safes2 = [[550,152],[320,408]]
                self.cenary.safes3 = [[70,159],[400,159],[230,415],[435,415]]
                self.cena = cena_fase1
            
    def update_vitoria(self):
        global camerax, cameray, agora
        self.main.x = 245
        self.main.y = 150
        self.main.lado = True
        camerax = 0
        cameray = 0
        if py.btnp(py.KEY_RETURN) or py.btnp(py.GAMEPAD1_BUTTON_X):
            agora = 0
            self.cena = cena_fase1
            self.main.x = tela_x/2-18
            self.main.y = tela_y-87
            self.vilain.x = 0
            self.vilain.y = 80
            self.main.vivo = True
            self.vilain.chasing = False
            self.cenary.safes1 = [[190,146],[70,402]]
            self.cenary.safes2 = [[550,152],[320,408]]
            self.cenary.safes3 = [[70,159],[400,159],[230,415],[435,415]]

            
    def draw(self):
        py.cls(0)
        py.camera(camerax,cameray)
        if self.cena == cena_inicio:
            self.draw_inicio()

        elif self.cena == cena_morte:
            self.draw_morte()
        
        elif self.cena == cena_vitoria:
            self.draw_vitoria()
                    
        elif self.cena == cena_fase1:
            self.draw_fase1()
            
        elif self.cena == cena_fase2:
            self.draw_fase2()
            
        elif self.cena == cena_fase3:
            self.draw_fase3()
            
        elif self.cena == cena_fase4:
            self.draw_fase4()
            
        elif self.cena == cena_fase5:
            self.draw_fase5()
            
        elif self.cena == cena_fase6:
            self.draw_fase6()
            
    def draw_inicio(self):
        py.text(35, 66, "Nao deixe que ele te veja.", 13)
        py.text(31, 126, "- PRESSIONE ENTER -", 13)
        py.blt(386,60,2,142,95,114,161,7)
    
    def draw_fase1(self):
        
        self.cenary.draw_back()
        py.bltm(0, 0, 0, 0, 0, 2100, 700, 9)
        self.vilain.draw()
        self.cenary.draw_hide()
        self.cenary.draw_door()
        self.main.draw()
        self.cenary.draw_tochas()

    def draw_fase2(self):
        global agora1
        self.cenary.draw_back()
        py.bltm(0, 0, 0, 0, 0, 1000, 1000, 9)
        self.vilain.draw()
        self.cenary.draw_hide()
        self.cenary.draw_door()
        self.main.draw()
        if agora1+15 <= py.frame_count:
            self.cenary.fogo = not(self.cenary.fogo)
            agora1 = py.frame_count
        
        if agora+300 >= py.frame_count:
            py.rect(self.main.x-37,self.main.y-112,124,34,7)
            py.rect(self.main.x-35,self.main.y-110,120,30,0)
            py.text(self.main.x-25,self.main.y-100,'eu te vejo ai embaixo...', 7)
        elif agora+400 >= py.frame_count:
            py.rect(self.main.x-37,self.main.y-112,124,34,7)
            py.rect(self.main.x-35,self.main.y-110,120,30,0)
            py.text(self.main.x-25,self.main.y-100,'...', 7)
        elif agora+600 >= py.frame_count:
            py.rect(self.main.x-37,self.main.y-112,124,34,7)
            py.rect(self.main.x-35,self.main.y-110,120,30,0)
            py.text(self.main.x-25,self.main.y-100,'vamos jogar um jogo...', 7)
            
        elif agora+800 <= py.frame_count and agora+900 >= py.frame_count:
            if self.cenary.fogo == True:
                py.blt(228,460,2,0,0,59,25,7)
            else:
                py.blt(228,460,2,0,26,59,25,7) 
        elif agora+1200 <= py.frame_count and agora+1300 >= py.frame_count:
            if self.cenary.fogo == True:
                py.blt(433,460,2,0,0,59,25,7)
                py.blt(314,460,2,59,0,92,26,7)
            else:
                py.blt(433,460,2,0,26,59,25,7)
                py.blt(314,460,2,59,28,92,26,7)
        elif agora+1650 <= py.frame_count and agora+1750 >= py.frame_count:
            if self.cenary.fogo == True:
                py.blt(228,460,2,0,0,59,25,7)
                py.blt(64,460,2,0,53,130,24,7)
            else:
                py.blt(228,460,2,0,26,59,25,7)
                py.blt(64,460,2,0,77,130,24,7)
        elif agora+2100 <= py.frame_count and agora+2200 >= py.frame_count:
            if self.cenary.fogo == True:
                py.blt(228,460,2,0,0,59,25,7)
                py.blt(433,460,2,0,0,59,25,7)
                py.blt(314,460,2,59,0,92,26,7)
            else:
                py.blt(228,460,2,0,26,59,25,7) 
                py.blt(433,460,2,0,26,59,25,7)
                py.blt(314,460,2,59,28,92,26,7)
        elif agora+2550 <= py.frame_count and agora+2650 >= py.frame_count:
            if self.cenary.fogo == True:
                py.blt(228,460,2,0,0,59,25,7)
                py.blt(314,460,2,59,0,92,26,7)
                py.blt(64,460,2,0,53,130,24,7)
            else:
                py.blt(228,460,2,0,26,59,25,7) 
                py.blt(314,460,2,59,28,92,26,7)
                py.blt(64,460,2,0,77,130,24,7)
        elif agora+3000 <= py.frame_count and agora+3200 >= py.frame_count:
            py.rect(self.main.x-22,self.main.y-130,154,34,7)
            py.rect(self.main.x-20,self.main.y-128,150,30,0)
            py.text(self.main.x-10,self.main.y-118,'hm... deve ter voltado para cima', 7)
            
    def draw_fase3(self):
        global agora
        self.cenary.draw_back()
        py.bltm(0, 0, 0, 0, 0, 2500, 2500, 9)
        self.vilain.draw()
        self.cenary.draw_hide()
        self.cenary.draw_door()
        self.main.draw()
        if self.main.power_dimi == True:
            if agora <= py.frame_count and self.spikes_y<=415:
                self.spikes_y+=1
                agora = py.frame_count
            py.rect(camerax+188,cameray+214,134,34,7)
            py.rect(camerax+190,cameray+216,130,30,0)
            py.text(camerax+200,cameray+226,'Pressione CTRL para diminuir.', 7)
                
            self.cenary.draw_spikes_fase3(self.spikes_y)
        else:
            py.blt(1785,410,1,197,146,14,14,9)
             
    def draw_fase4(self):
        self.cenary.draw_back()
        self.vilain.draw()
        py.bltm(0, 0, 0, 0, 0, 2100, 2100, 9)
        self.main.draw()
        if self.main.power_invi == False:
            py.blt(1657,153,1,183,146,14,14,9)
        else:
            py.rect(camerax+178,cameray+214,154,34,7)
            py.rect(camerax+180,cameray+216,150,30,0)
            py.text(camerax+190,cameray+226,'Pressione E para ficar invisivel.', 7)
        self.cenary.draw_hide()
        self.cenary.draw_door()
        
    def draw_fase5(self):
        self.cenary.draw_back()
        py.bltm(0, 0, 0, 0, 0, 2100, 2100, 9)
        self.cenary.draw_hide()
        self.cenary.draw_door()
        self.main.draw()
        
    def draw_fase6(self):
        self.boss.draw()
        self.cenary.draw_back()
        py.bltm(0, 0, 0, 0, 0, 2100, 2100, 9)
        self.cenary.draw_hide()
        self.cenary.draw_door()
        self.main.draw()
        if agora1+150 >= py.frame_count:
            py.rect(self.main.x-37,self.main.y-112,124,34,7)
            py.rect(self.main.x-35,self.main.y-110,120,30,0)
            py.text(self.main.x-25,self.main.y-100,'CHEGA!!!', 7)
        elif agora1+300 >= py.frame_count:
            py.rect(self.main.x-37,self.main.y-112,124,34,7)
            py.rect(self.main.x-35,self.main.y-110,120,30,0)
            py.text(self.main.x-25,self.main.y-100,'EU CANSEI DE VOCE!', 7)
        elif agora1+450 >= py.frame_count:
            py.rect(self.main.x-37,self.main.y-112,124,34,7)
            py.rect(self.main.x-35,self.main.y-110,120,30,0)
            py.text(self.main.x-25,self.main.y-100,'Voce nao ira fugir daqui.', 7)
        
    def draw_morte(self):
        if self.tremendo <= 100:
            self.boss.draw()
        else:
            py.camera()
            py.text(225, 50, "VOCE PERDEU", 8)
            py.text(210, 90, "- PRESSIONE ENTER -", 13)
        
    def draw_vitoria(self):
        py.camera()
        self.main.draw()
        self.main.is_invi = False
        self.main.is_dimi = False
        py.text(225, 50, "VOCE VENCEU", 3)
        py.text(215, 90, "- PRESSIONE ENTER -", 13)
App()