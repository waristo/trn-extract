import sys

if (len(sys.argv) != 3) :
  print("usage: python extract.py [all set file name] [minus set file name]")

cmp = []

allSet = open(sys.argv[2], 'rt')
while True :
  line = allSet.readline()
  if not line :
    break
  cmp.append(line.split(' :: ')[0])
allSet.close()

minusSet = open(sys.argv[1], 'rt')
otherSet = open('other.trn', 'wt')

while True :
  line = minusSet.readline()
  if not line :
    break
  if line.split(' :: ')[0] not in cmp :
    otherSet.write(line)

minusSet.close()
otherSet.close()