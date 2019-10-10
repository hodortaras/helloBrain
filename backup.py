import os
import time
import zipfile

sourse = ['C:\\Users\Tarar\123']
target_dit = 'C:\\Backup'
today = target_dit + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

coment = input('Введите коментарий:')
if len(coment)==0:
    target = today + os.sep + now +'.zip'
else:
    target = today + os.sep + now + ' ' + coment.replace(' ','_') +'.zip'
if not os.path.exists(today):
    os.mkdir(today)
print('Каталог успешно создан', today)

zip_comand=' -c {0} {1}'.format(target, ' '.join(sourse))

if zipfile.ZipFile(zip_comand)==0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось')
