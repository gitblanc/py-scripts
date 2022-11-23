'''
Programa que lista todos los contenidos de un repositorio de Github

Eduardo Blanco Bielsa - gitblanc
'''
import os
from importlib.metadata import files

from github import Github
images = []
g = Github(input("Introduce your github access token: "))

repo = g.get_repo("gitblanc/Obsidian-Notes")
contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        if file_content.name != ".obsidian" and "img":
            contents.extend(repo.get_contents(file_content.path))
            print("--- Carpeta - " + file_content.name + " ---")
    else:
        if  file_content.name != ".DS_Store":
            if ".png" in file_content.name:
                images.append(file_content.name)
            else:
                print("\t" + file_content.name)

print("imágenes")
print(images)