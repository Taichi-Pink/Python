import os




# Delete_path = '/home/ziyi/Desktop/ToneMapped/Delete/' + tone + '/'
#
# for i in os.listdir(Delete_path):
#     imagePath = os.path.join(Delete_path, i)
#     filename = os.path.splitext(os.path.basename(imagePath))[0]
#     file = filename.split('_', 2)
#     file = file[0]
#     rename = os.path.join(Delete_path, (file + '_' + tone + '.png'))
#     os.rename(imagePath, rename)

tone = 'TumblinTMO'

for index in range(1,9):
    multi_path = '/home/ziyi/Desktop/ToneMapped/scene'+str(index)+'/Multi-Face/'+tone+'/'
    one_path = '/home/ziyi/Desktop/ToneMapped/scene'+str(index)+'/One-Face/'+tone+'/'
    # Delete_path = '/home/ziyi/Desktop/ToneMapped/scene'+str(index)+'/Delete/'+tone+'/'

    for i in os.listdir(multi_path):
        imagePath = os.path.join(multi_path, i)
        filename = os.path.splitext(os.path.basename(imagePath))[0]
        file = filename.split('_',2)
        file = file[0]+'_'+file[1]
        rename = os.path.join(multi_path, (file+'_'+tone+'.png'))
        os.rename(imagePath, rename)

    for i in os.listdir(one_path):
        imagePath = os.path.join(one_path, i)
        filename = os.path.splitext(os.path.basename(imagePath))[0]
        file = filename.split('_',2)
        file = file[0]+'_'+file[1]
        rename = os.path.join(one_path, (file+'_'+tone+'.png'))
        os.rename(imagePath, rename)

#     for i in os.listdir(Delete_path):
#         imagePath = os.path.join(Delete_path, i)
#         filename = os.path.splitext(os.path.basename(imagePath))[0]
#         file = filename.split('_',2)
#         file = file[0]
#         rename = os.path.join(Delete_path, (file+'_'+tone+'.png'))
#         os.rename(imagePath, rename)