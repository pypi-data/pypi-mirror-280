from ftplib import FTP
import io
import sys

def get():
    ftp = FTP('sent1ntg.beget.tech')
    ftp.login(user='sent1ntg_base', passwd='Amdlover345!')
    ftp.encoding = 'utf-8'  # Устанавливаем кодировку UTF-8

    method = input("Выберите метод (write или read): ")

    if method.lower() == "write":
        filename = input("Введите имя файла для записи: ")
        print("Введите текст. Для окончания ввода нажмите Ctrl + D")
        data = sys.stdin.read()
        data_ftp = io.BytesIO(data.encode())
        ftp.storbinary(f'STOR {filename}.html', data_ftp)
        print(f"Файл {filename}.html успешно записан на FTP сервер")
    elif method.lower() == "read":
        files = [file for file in ftp.nlst() if file.endswith('.html')]
        print("Список файлов формата HTML на FTP сервере:")
        for idx, file in enumerate(files):
            print(f"{idx + 1}. {file}")
        choice = int(input("Выберите файл для чтения (введите номер): "))
        if 1 <= choice <= len(files):
            filename = files[choice - 1]
            data = bytearray()

            def write_data(buf):
                data.extend(buf)

            ftp.retrbinary(f"RETR {filename}", write_data)

            content = data.decode('utf-8')
            print(f"Содержимое файла {filename}:")
            print(content)
            print(f"Файл {filename} успешно скачан с FTP сервера")
        else:
            print("Неверный выбор файла.")
    else:
        print("Неверный метод. Пожалуйста, выберите WRITE или READ.")

    ftp.quit()

get()
input("Press Enter to exit...")