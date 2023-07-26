# ファイル出力
fname = 'sample.txt'

f = open(fname, "w")
f.write('Hello World!\nGoodBye!')

f.close()

# ファイル入力
f = open(fname, "r")

for line in f:
  print(line)

f.close()
