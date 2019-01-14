
def show_magicians(names):
    for name in names:
        print(name.title())

def make_great(mag_names, new_mag=''):
    if new_mag != '':
        while mag_names:
            cur_mag = mag_names.pop()
            print('Great ' + cur_mag)
            new_mag.append(cur_mag)
    else:
        for name in mag_names:
            print('Great ' + name.title())

mag_names = ['alice', 'bob', 'mike']
new_mag = []

'''
show_magicians(mag_names)
make_great(mag_names)
'''

make_great(mag_names[:], new_mag)
make_great(mag_names)