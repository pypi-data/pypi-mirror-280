#!/usr/bin/env python3
# Author Mr. manimal

class Corso:

	def __init__(self, nome, durata, link):
		self.nome = nome
		self.durata = durata
		self.link = link

	def __repr__(self):
		return f"{self.nome} [{self.durata} ORE] ({self.link})"


corsi = [

	Corso("Corso Hacking Etico", 60, "https://www.youtube.com/playlist?list=PLKZZXjqZrqQtKGgJuAYhzYczf1KIdswvO"),
	Corso("Corso Linux", 15, "https://www.youtube.com/playlist?list=PLKZZXjqZrqQvfAhgY7Nit5ynpK3kN_3tx"),
	Corso("Corso Personalizazione Linux", 3, "https://www.youtube.com/playlist?list=PLKZZXjqZrqQslOV4EyEl40ZPxo7bpFHQE"),
	Corso("Corso Python Offensive", 50, "https://www.youtube.com/playlist?list=PLKZZXjqZrqQu7qZkgSsdU3lRpR7oISMXh")
	]

def lista_corsi():
	for corso in corsi:
		print(corso)

def cerca_corso_by_nome(nome):
	for corso in corsi:
		if corso.nome == nome:
			return corso
	return None
