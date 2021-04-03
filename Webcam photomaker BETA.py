# -*- coding: utf-8 -*-
import cv2, time, zipfile, os, smtplib

stream = cv2.VideoCapture(0)
stream.set(cv2.CAP_PROP_FPS, 24) 
stream.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 768) 

os.chdir('C:\\')   
n = 0
key = input('Чтобы сделать фото, введи «1». \nУ тебя будет 10 секунд на то, чтобы принять нужную позу. \nВнимание! Чтобы фотографии сохранились, обязательно заверши программу командой «2»\n')
zip = zipfile.ZipFile('Фотосессия.zip', 'w')

while (stream.isOpened()):

    if key == '1':
        print('\nПредставь, что ты фотомодель — приготовься.')
        for i in range(10):
            time.sleep(1)
            print(f'{10-i}...')
        status, photo = stream.read()
        print('Попался, красавчик!')
        cv2.imshow('SEXUALITY = 100%', photo)
        if cv2.waitKey(10) == 27:
            break
        key = input('Чтобы сохранить фотографию, введи  «1». Если не хочешь ее сохранять, введи «2».\n') 
        if key == '1':            
            cv2.imwrite(f'{n}.jpg', photo)
            json = open(f'{n}.json', 'w+')
            json.write('[1, [0, 0, 0, 0]]')
            json.close()
            zip.write(f'{n}.jpg')
            os.remove(f'C:\{n}.jpg')        
            zip.write(f'{n}.json')
            os.remove(f'C:\{n}.json')        
            n+=1
            print('\nА у тебя есть вкус <3\n')                   
        else:
             print('\nТы чево наделол..\n')    

        key = input('\n- Снова нажми «1», чтобы сделать ещё фото; \n- Нажми «2», чтобы закончить и сохранить фотосессию.\n')             
        
    elif key == '2':
        zip.close()    
        print('\nСохранено!\nИщи свои фото по адресу C:/Фотосессия.zip\n')
        
        break
        
    elif key == '3':
        print('\nСворачиваемся...\n')
        break        

    else:
        key = input('\nНе-а, только «1» или «2»\n')       
        
stream.release()
cv2.destroyAllWindows()        

input()
