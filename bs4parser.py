#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def populateSubInfo(url):
	response = requests.get(url)
	htmlcontent = response.content
	soup = BeautifulSoup(htmlcontent)
	resultItemDivs = soup("div", class_="subitem")

	subInfos = []

	for resultItem in resultItemDivs:
		subInfo = {}

		subTitle = resultItem("a", class_="introtitle")[0].get_text()
		subInfo["subTitle"] = subTitle 

		infoTags = resultItem.find_all("li")
		for infoTag in infoTags:
			
			tagText = infoTag.get_text().strip()

			if tagText.startswith(u"格式"):
				subFormat = tagText.split(u"：")[1].strip()
				subInfo["subFormat"] = subFormat
				continue
			elif tagText.startswith(u"语言"):
				subLang = tagText.split(u"：")[1].strip()
				subInfo["subLang"] = subLang
				continue
			elif tagText.startswith(u"制作"):
				subMaker = tagText.split(u"：")[1].strip()
				subInfo["subMaker"] = subMaker
				continue
			elif tagText.startswith(u"校订"):
				subChecker = tagText.split(u"：")[1].strip()
				subInfo["subChecker"] = subChecker
				continue
			elif tagText.startswith(u"上载"):
				subUploader = tagText.split(u"：")[1].strip()
				subInfo["subUploader"] = subUploader
				continue
			elif tagText.startswith(u"来源"):
				subSource = tagText.split(u"：")[1].strip()
				subInfo["subSource"] = subSource
				continue
			elif tagText.startswith(u"日期"):
				subDate = tagText.split(u"：")[1].strip()
				subInfo["subDate"] = subDate
				continue
			elif tagText.startswith(u"查阅次数"):
				subViewCount = tagText.split(u"：")[1].strip()
				subInfo["subViewCount"] = subViewCount
				continue
			elif tagText.startswith(u"下载次数"):
				subDownloadCount = tagText.split(u"：")[1].strip()
				subInfo["subDownloadCount"] = subDownloadCount
				continue
			elif tagText.startswith(u"翻译质量"):
				subQuality = tagText.split(u"：")[1].strip()
				subInfo["subQuality"] = subQuality
				continue
		
		subInfos.append(subInfo)

	return subInfos

populateSubInfo('http://www.shooter.cn/search2/lucy/')