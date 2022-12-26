# from random import randint
# dice_imgs = ['0','0','0','0','0','0']
# dice_num = randint(1,6)
# print(dice_imgs[dice_num])


###solved👇
from random import randint
dice_imgs = ['0','0','0','0','0','0']
# dice_num = 6       error
dice_num = randint(0,5)

print(dice_imgs[dice_num])