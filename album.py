"""import urllib.request
import os
import vk_api
import time
import errno
import math
import re
access_token = 'vk1.a.OPgHolyWlbubzsCS7swFowiq2mOrjRxVjrZ6a1JM4n_5N_9fdaimHFAPnxN7RkIEWA4QomCPh7dLLOfrt04H9D8RUPz_wbVNQzzDJt9JeCjKsSxDFsQJ9__nrIePWsOx-oNlaNDDZHnKchBSg4WuATmUp9vPOJPu2ykpTxFZlGrO-a1eHUsYNUxj6uGkaQ_vzK-Dxpeo46NC4SXF1CqlTg'
vk_session = vk_api.VkApi(token=access_token)
vkapi = vk_session.get_api()

link_album = 'https://vk.com/albums-42869722?z=photo-42869722_457242454%2Fphotos-42869722'

match = re.search(r'album(-?\d+)_(\d+)', link_album)
if match:
    o_id = match.group(1)
    a_id = match.group(2)
else:
    print("Неверная ссылка на альбом")
    o_id = a_id = None

if o_id and a_id:
    p_enumerator = vkapi.photos.getAlbums(owner_id=o_id, album_id=a_id)["count"]
    c_pr = 0
    t_timer = time.time()

    if not os.path.exists('vk_photos'):
        os.mkdir('vk_photos')
    savefolder = 'vk_photos/album{0}_{1}'.format(o_id, a_id)
    if not os.path.exists(savefolder):
        os.mkdir(savefolder)

    iter = 0
    for j in range(math.ceil(p_enumerator / 1000)):
        photos = vkapi.photos.get(owner_id=o_id, album_id=a_id, count=1000, offset=j * 1000)["items"]
        for photo in photos:
            c_pr += 1
            url = photo['sizes'][-1]['url']
            print('Загрузка фото № {} из {}. Загружено: {:.2f}%'.format(c_pr, p_enumerator, iter))
            iter = round(50 / p_enumerator * c_pr, 2)

            try:
                urllib.request.urlretrieve(url, savefolder + "/" + os.path.split(url)[1])
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

    print('Загрузка завершена. Время выполнения: {} сек.'.format(round(time.time() - t_timer, 2)))
"""

import urllib.request
import os
import vk_api
import time
import errno
import math
import re
access_token = 'vk1.a.OPgHolyWlbubzsCS7swFowiq2mOrjRxVjrZ6a1JM4n_5N_9fdaimHFAPnxN7RkIEWA4QomCPh7dLLOfrt04H9D8RUPz_wbVNQzzDJt9JeCjKsSxDFsQJ9__nrIePWsOx-oNlaNDDZHnKchBSg4WuATmUp9vPOJPu2ykpTxFZlGrO-a1eHUsYNUxj6uGkaQ_vzK-Dxpeo46NC4SXF1CqlTg'
vk_session = vk_api.VkApi(token=access_token)
vkapi = vk_session.get_api()

link_album = input('Nhập đường dẫn album VK: ') # đường dẫn đầy đủ đến album VK
a_id = link_album.split('/')[-1].split('_')[1]
o_id = link_album.split('/')[-1].split('_')[0].replace('album', '')






p_enumerator = vkapi.photos.getAlbums(owner_id=o_id, album_id=a_id)["count"]
c_pr = 0
t_timer = time.time()

if not os.path.exists('vk_photos'):
    os.mkdir('vk_photos')
savefolder = 'vk_photos/album{0}_{1}'.format(o_id, a_id)
if not os.path.exists(savefolder):
    os.mkdir(savefolder)

iter = 0
for j in range(math.ceil(p_enumerator / 1000)):
    photos = vkapi.photos.get(owner_id=o_id, album_id=a_id, count=1000, offset=j * 1000)["items"]
    for photo in photos:
        c_pr += 1
        url = photo['sizes'][-1]['url']
        print('Загрузка фото № {} из {}. Загружено: {:.2f}%'.format(c_pr, p_enumerator, iter))
        iter = round(100 / p_enumerator * c_pr, 2)

        try:
            urllib.request.urlretrieve(url, savefolder + "/" + os.path.split(url)[1])
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

print('Загрузка завершена. Время выполнения: {} сек.'.format(round(time.time() - t_timer, 2)))

