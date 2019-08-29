import csv

path = "./characterList/"
charaList = [
			"alisa", "anna", "amking", "asuka", "bob", "bryan",
			"claudio", "dragunov", "eddy", "eliza", "feng",
			"geese", "gigas", "gouki", "heihachi", "jack7", "jin",
			"julia", "katarina", "kazumi", "kazuya", "king", "kuma",
			"lars", "lee", "lei", "leo", "lili", "lucky",
			"marduk", "miguel", "negan", "nina", "noctis", "paul",
			"shaheen", "steve", "xiaoyu","yoshimitsu"
			]

for file in charaList:
	with open(path + file + "List.csv", "r+w", encoding='utf-8') as f:
		reader = csv.reader(f)
		for row in reader:
			del row[-2:]
			print(row)
		