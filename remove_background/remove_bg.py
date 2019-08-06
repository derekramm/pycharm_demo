from removebg import RemoveBg
import os

rmbg = RemoveBg('DNPfUtzXVwGtqTatMzu2q8MK', 'error.log')

path = f'{os.getcwd()}/images'
for img in os.listdir(path):
    rmbg.remove_background_from_img_file(f'{path}/{img}')
