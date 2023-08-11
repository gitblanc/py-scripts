import os
import re
import urllib.parse

def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    updated_content = re.sub(r'!\[\[(.*?)\]\]', replace_image_tag, content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

def replace_image_tag(match):
    img_name = match.group(1)
    img_name = img_name.replace(' ', '%20')
    return f'![](./img/{img_name})'

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                process_markdown_file(file_path)

def main():
    target_folder = input("Ingrese la ruta de la carpeta a procesar: ")

    if not os.path.exists(target_folder):
        print("La ruta especificada no existe.")
        return

    process_directory(target_folder)
    print("Procesamiento completado.")

if __name__ == "__main__":
    main()
