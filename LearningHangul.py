import pygame
import random
import time
import sys
from pygame import mixer
import os
import pandas

os.chdir("")  #Directory with additional needed files
  
Hangul = ["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ","ㅏ","ㅑ","ㅓ","ㅕ", "ㅗ","ㅛ","ㅜ","ㅠ","ㅡ", "ㅣ","ㄲ","ㄸ","ㅃ",  "ㅉ","ㅆ","ㅢ", "ㅚ", "ㅐ","ㅟ","ㅔ","ㅒ", "ㅖ","ㅘ", "ㅝ", "ㅙ","ㅞ"]
English = ["g","n","d", "r", "m","b", "s","",  "j","ch","k","t", "p","h","a","ya","eo","yeo","o","yo","u","yu","eu","i","gg","dd","bb","jj","ss","ui","oe","ae","wi","e","yae","ye","wa","wo","wae","we"]

df = pandas.read_csv("") #Directory of csv to track mistakes
pygame.init()

score = 0
mistakeCount = 0
  
clock = pygame.time.Clock()
mixer.init()

correct = pygame.mixer.Sound("correct.mp3")
incorrect = pygame.mixer.Sound("incorrect.mp3")

correct.set_volume(0.2)
incorrect.set_volume(0.2)

def playCorrectSound():
    pygame.mixer.Sound.play(correct)

def playIncorrectSound():
    pygame.mixer.Sound.play(incorrect)

    

  
screen = pygame.display.set_mode([700, 700])
  
base_font = pygame.font.Font(None, 42)
hangul_font = pygame.font.Font("arial-unicode-ms.ttf", 400)
user_text = ''
letter = random.choice(Hangul)

hint = ""

# create rectangle
input_rect = pygame.Rect(250, 500, 200, 50)
  
color_passive = pygame.Color('grey')
color = color_passive
  
active = False
  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                if user_text in English:
                    if English.index(user_text) == Hangul.index(letter):
                        score+=1
                        user_text = ""
                        letter = random.choice(Hangul)
                        mistakeCount = 0
                        playCorrectSound()
                        flashGreen()
                        hint = ""
                    else:
                        score = 0
                        playIncorrectSound()
                        flashRed()
                        mistakeCount+=1
                        df.iloc[Hangul.index(letter), 1] 
                        df.to_csv("C:/Users/fabik/OneDrive/Desktop/aaa/mistakes.csv", index=False)
                        if mistakeCount == 2:
                            hint = English[Hangul.index(letter)]
                else:
                    score = 0
                    playIncorrectSound()
                    flashRed()
                    mistakeCount+=1
                    df.iloc[Hangul.index(letter), 1] += 1
                    df.to_csv("C:/Users/fabik/OneDrive/Desktop/aaa/mistakes.csv", index=False)
                    if mistakeCount == 2:
                            hint = English[Hangul.index(letter)]
            else:
                user_text += event.unicode
            if len(user_text) > 3:
                user_text = user_text[:-1]
            
            


    screen.fill((255, 255, 255))
  
    pygame.draw.rect(screen, color, input_rect)
  
    text_surface = base_font.render(user_text, True, (0, 0, 0))
    text_letter = hangul_font.render(letter, True, (0, 0, 0))
    text_score = base_font.render("Streak: "+str(score), True,(0,0,0))
    text_hint = base_font.render(hint, True, (0,0,0))


    screen.blit(text_letter, text_letter.get_rect(center = (700/2, 250)))
    screen.blit(text_surface, text_surface.get_rect(center = (700/2, 525)))
    screen.blit(text_score, text_score.get_rect(center = (70, 680)))
    screen.blit(text_hint, text_hint.get_rect(center = (670, 680)))


    
      
    def draw_rect(color):
        pygame.draw.rect(screen, color,(250, 500, 200, 50))

    def flashRed():
        draw_rect("red")
        pygame.display.flip()
        time.sleep(0.2)  
        draw_rect("grey")
        pygame.display.flip()

    def flashGreen():
        draw_rect("green")
        pygame.display.flip()
        time.sleep(0.2)  
        draw_rect("grey")
        pygame.display.flip()
        

    pygame.display.flip()
      

    clock.tick(60)