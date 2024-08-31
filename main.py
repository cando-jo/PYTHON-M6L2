#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Uzay Yolculuğu"
FPS = 30

# Değişkanler ve Nesneler
gemi = Actor("gemi", (300, 400))
uzay = Actor("uzay")

#gemiler 150 300 450
gemi1 = Actor('gemi1', (150, 225))
gemi2 = Actor('gemi2', (300, 225))
gemi3 = Actor('gemi3', (450, 225))


dusmanlar = []
gezegenler = [Actor("gezegen1", (random.randint(0, 600), -100)), Actor("gezegen2", (random.randint(0, 600), -100)), Actor("gezegen3", (random.randint(0, 600), -100))]
meteorlar = []
mod = 'menu'

# Düşmanlar listesini oluşturmak
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    dusman = Actor("düşman", (x, y))
    dusman.speed = random.randint(2, 8)
    dusmanlar.append(dusman)
    
# Meteorlar listesini oluşturmak
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    meteor = Actor("meteor", (x, y))
    meteor.speed = random.randint(2, 10)
    meteorlar.append(meteor)

# Çizimler
def draw():
    # Oyun Modu
    if mod == 'oyun':
        uzay.draw()
        gezegenler[0].draw()
        # Meteorların Çizilmesi
        for i in range(len(meteorlar)):
            meteorlar[i].draw()
        gemi.draw()
        # Düşmanların Çizilmesi
        for i in range(len(dusmanlar)):
            dusmanlar[i].draw()
    # Oyun Bitti ekranı
    elif mod == 'son':
        uzay.draw()
        screen.draw.text("OYUN BİTTİ!", center = (300, 200), color = "white", fontsize = 36)
        
    elif mod == 'menu':
        uzay.draw()
        gemi1.draw()
        gemi2.draw()
        gemi3.draw()
        screen.draw.text("Choose your spaceship!!", center = (300, 100), color = "white", fontsize = 36)
    
# Kontroller
def on_mouse_move(pos):
    gemi.pos = pos

# Yeni Düşmanların Eklenmesi
def yeni_dusman():
    x = random.randint(0, 400)
    y = -50
    dusman = Actor("düşman", (x, y))
    dusman.speed = random.randint(2, 8)
    dusmanlar.append(dusman)

# Düşmanların Hareketleri
def dusman_gemisi():
    for i in range(len(dusmanlar)):
        if dusmanlar[i].y < 650:
            dusmanlar[i].y = dusmanlar[i].y + dusmanlar[i].speed
        else:
            dusmanlar.pop(i)
            yeni_dusman()

# Gezegenlerin Hareketleri
def gezegen():
    if gezegenler[0].y < 550:
            gezegenler[0].y = gezegenler[0].y + 1
    else:
        gezegenler[0].y = -100
        gezegenler[0].x = random.randint(0, 600)
        birinci = gezegenler.pop(0)
        gezegenler.append(birinci)

# Meteorların Hareketleri
def meteorlar_hareket():
    for i in range(len(meteorlar)):
        if meteorlar[i].y < 450:
            meteorlar[i].y = meteorlar[i].y + meteorlar[i].speed
        else:
            meteorlar[i].x = random.randint(0, 600)
            meteorlar[i].y = -20
            meteorlar[i].speed = random.randint(2, 10)

# Çarpışmalar
def carpismalar():
    global mod
    for i in range(len(dusmanlar)):
        if gemi.colliderect(dusmanlar[i]):
            mod = 'son'

def update(dt):
    if mod == 'oyun':
        dusman_gemisi()
        carpismalar()
        gezegen()
        meteorlar_hareket()
        
def on_mouse_down(button, pos):
    global mod
    if mod == 'menu':
        if button == mouse.LEFT:
            if gemi1.collidepoint(pos):
                gemi.image = gemi1.image
                mod = 'oyun'
            elif gemi2.collidepoint(pos):
                gemi.image = gemi2.image
                mod = 'oyun'
            elif gemi3.collidepoint(pos):
                gemi.image = gemi3.image
                mod = 'oyun'
                
