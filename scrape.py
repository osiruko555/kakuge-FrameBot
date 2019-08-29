import urllib3
import csv
import time
from bs4 import BeautifulSoup

basicUrl = "http://geppopotamus.info/game/tekken7fr/"
data = "/data.htm"
charaList = [
			"alisa", "anna", "amking", "asuka", "bob", "bryan",
			"claudio", "dragunov", "eddy", "eliza", "feng",
			"geese", "gigas", "gouki", "heihachi", "jack7", "jin",
			"julia", "katarina", "kazumi", "kazuya", "king", "kuma",
			"lars", "lee", "lei", "leo", "lili", "lucky",
			"marduk", "miguel", "negan", "nina", "noctis", "paul",
			"shaheen", "steve", "xiaoyu","yoshimitsu"
			]

commandList = {
				"../1.bmp":"1", "../2.bmp":"2", "../3.bmp":"3", "../4.bmp":"4",
				"../6.bmp":"6", "../7.bmp":"7", "../8.bmp":"9", "../lp.bmp":"LP",
				"../rp.bmp":"RP", "../lk.bmp":"LK", "../rk.bmp":"RK", "../p.bmp":"LP+RP",
				"../k.bmp":"LK+RK", "../rpk.bmp":"RP+LK"
				}

http = urllib3.PoolManager()
#html = http.request('GET', basicUrl + charaList[0] + data)
#soup = BeautifulSoup(html.data, "html.parser")


for fighter in charaList:
	print("crawling...")
	html = http.request('GET', basicUrl + fighter + data)
	soup = BeautifulSoup(html.data, "html.parser")
	table = soup.findAll("table", {"class":"fr"})[0]
	rows = table.findAll("tr")
	with open("./characterList/" + fighter + "List.csv", "w", encoding="utf-8-sig", newline="") as file:
		writer = csv.writer(file)
		for row in rows:
			csvRow = []
			command = []
			for tag in row.findAll(['img']):
				img = tag.find(['img'])
				print(tag)
				print(img.get['src'])
				'''
				if img.get('src') in commandList:
					command.append(commandList[img.get('src')])
				'''
				print(command)
				print("sleep")
				time.sleep(1)
			for cell in row.findAll(['td']):
				csvRow.append(cell.get_text())
			writer.writerow(csvRow)
	print("sleeping...")
	time.sleep(3)
