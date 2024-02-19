# file : ds29_osFileList.py
# date : 20240219
# desc : 윈도우 파일 리스트

import os

fnameAry = []
folderName = 'C:/Sources/ds-and-algorithm-2024/day06'

for dirName, subDirlist, fnames in os.walk(folderName):
    for fname in fnames:
        fnameAry.append(fname)

print(fnameAry)
print(len(fnameAry))

fnameAry.sort(reverse=True) # 역순으로 정렬
print(fnameAry)