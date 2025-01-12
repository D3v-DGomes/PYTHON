'''
Add size and brand attributes to the Television class. Create two Television objects 
and assign them different sizes and brands. Then print the values of these
attributes to confirm that the values of each instance (object) are independent.
'''

# Code:
class Television:
    def __init__(self):
        self.connected = False
        self.channel = 2
        self.size = 0
        self.brand = ''

tv_room = Television()
print(tv_room.connected)
print(tv_room.channel)

tv_living_room = Television()
tv_living_room.connected = True
tv_living_room.channel = 4
print(tv_living_room.channel)

# Answer:
tv_room.size = 24
tv_room.brand = 'LG'
print(f'TV size = {tv_room.size}, TV brand = {tv_room.brand}')

tv_living_room.size = 44
tv_living_room.brand = 'TCL'
print(f'TV size = {tv_living_room.size}, TV brand = {tv_living_room.brand}')



