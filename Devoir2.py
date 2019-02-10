#coding: utf-8

import json
import csv
import requests

fichier = "laBanq.csv"

url = "http://collections.banq.qc.ca/api/service-notice?handle=52327/"

entete = {
	"User-Agent":"Thomas Dufour: journaliste",
	"From":"thomasdufour4@gmail.com"
}

p = ["Handle", "Titre", "Créateur", "Date de création", "Description du matériel", "URL"]

henri = open(fichier,"a")

bourassa = csv.writer(henri)

bourassa.writerow(p)



for x in range(1000, 2001):
	
	req = requests.get(url + str(x), headers=entete)

	if req.status_code == 200:

		doc = req.json()

		s = []

		if doc["type"] == "audio":

			title = doc["titre"].split(" /")

			s.append(x)

			s.append(title[0])

			s.append(doc["createurs"][0])

			s.append(doc["dateCreation"])

			s.append(doc["descriptionMat"])

			s.append(doc["noticeComplete"][0]["liens"][0]["url"])

			print(s)

			henri = open(fichier,"a")

			bourassa = csv.writer(henri)
		
			bourassa.writerow(s)

			