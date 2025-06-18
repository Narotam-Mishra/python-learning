file = open('youtube.txt', 'w')

try:
    file.write('working on youtube manager')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('using python')