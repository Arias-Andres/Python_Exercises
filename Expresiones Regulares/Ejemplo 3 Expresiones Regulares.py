import re
man = open('mbox-short.txt')
for linea in man:
    linea = linea.rstrip()
    if re.search('F..m:', linea):
        print(linea)
