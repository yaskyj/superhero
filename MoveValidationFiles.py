import os
import shutil

heroes = ['ant_man', 'super_man', 'iron_man', 'bat_man', 'captain_america', 
'spider_man', 'hulk', 'avengers', 'black_panther', 'cat_woman', 'aqua_man', 'ghostrider']

# Create folders for each breed
for i in heroes:
    directory = './CAX_Superhero_Train_Original/train/' + i
    if not os.path.exists(directory):
        os.makedirs(directory)

for i in heroes:
    directory = './CAX_Superhero_Train_Original/test/' + i
    if not os.path.exists(directory):
        os.makedirs(directory)

# train_totals = []
# validation_totals = []

# for i in heroes:
#     directory = './CAX_Superhero_Train_Original/' + i
#     print int(round((len(os.listdir(directory))-1)*.8))
#     train_totals.append(int(round((len(os.listdir(directory))-1)*.8)))
#     print int(round(len(os.listdir(directory))))-1-int(round((len(os.listdir(directory))-1)*.8))
#     validation_totals.append(int(round(len(os.listdir(directory))))-1-int(round((len(os.listdir(directory))-1)*.7)))

# print sum(train_totals)
# print sum(validation_totals)
# print sum(train_totals) + sum(validation_totals)

for i in heroes:
    directory = './CAX_Superhero_Train_Original/' + i
    src_files = os.listdir(directory)
    for x in range(1, int(round(len(os.listdir(directory))))):
        if x < int(round(len(os.listdir(directory))*.9)):
            print x
            dest = './CAX_Superhero_Train_Original/train/' + i + '/' + src_files[x]
            print dest
            shutil.copy(directory + '/' + src_files[x], dest)
        else:
            print x
            dest = './CAX_Superhero_Train_Original/test/' + i + '/' + src_files[x]
            print dest
            shutil.copy(directory + '/' + src_files[x], dest)
            
