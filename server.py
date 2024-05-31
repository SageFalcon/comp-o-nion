import socket
import os
import pandas as pd
import webbrowser
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
server.bind((socket.gethostbyname_ex(hostname)[-1][-1], 1234))
print(socket.gethostbyname_ex(hostname)[-1][-1])
server.listen()

while True:
    user, addr = server.accept()
    print("connect")

    while True:
        data = user.recv(1024).decode("utf-8").lower()
        print(data)

        # Функция для сканирования дисков и сбора информации
        def scan_disks(directory, file_formats):
            disk_info = []
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_extension = os.path.splitext(file)[1]
                    if file_extension.lower() in file_formats:
                        # Получаем размер файла
                        file_size = os.path.getsize(file_path)
                        # Добавляем информацию о файле в список
                        disk_info.append({'File': file, 'Path': file_path, 'Size': file_size, 'Format': file_extension})
            return disk_info

        if data == "scan":
            # Сканирование диска и сохранение в CSV файл
            directory_to_scan = 'C:/Users/Simon/Downloads'
            file_formats_to_scan = ['.pdf', '.doc', '.xml', '.ptx', '.jpg', '.png']
            output_csv_file = 'scanned_files.csv'
            disks_data = scan_disks(directory_to_scan, file_formats_to_scan)
            df = pd.DataFrame(disks_data)

            # Преобразуем DataFrame в строку JSON
            files_json = df.to_json(orient='records')

            # Отправляем данные клиенту
            user.send(files_json.encode("utf-8"))

            print("scanning")
        elif data == "web":
            while True:
                data = user.recv(1024).decode("utf-8").lower()
                if data == "close":
                    break
                else:
                    webbrowser.open(f"https://www.{data}")

        elif data == "open":
            while True:
                data = user.recv(1024).decode("utf-8").lower()
                if data == f"{data}":
                    os.startfile(f"{data}")
                elif data == "edge":
                    os.startfile("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")

                elif data == "close":
                    break

        elif data == "exit":
            server.close()
