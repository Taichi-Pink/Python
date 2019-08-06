import os,shutil

tone = 'ReinhardDevlinTMO'
for i in range(1,9):
    directory1 = '/home/ziyi/Desktop/ToneMapped/scene'+str(i)+'/Multi-Face/'+tone+'/'
    directory2 = '/home/ziyi/Desktop/ToneMapped/scene' + str(i) + '/One-Face/'+tone+'/'
    # if not os.path.exists(directory1):
    #     os.makedirs(directory1)
    # if not os.path.exists(directory2):
    #     os.makedirs(directory2)
    if os.path.exists(directory1):
        shutil.rmtree(directory1)
    if os.path.exists(directory2):
        shutil.rmtree(directory2)