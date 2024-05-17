# import socket
# import webbrowser
# import os
# import pandas as pd
# from pathlib import Path
#
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# hostname = socket.gethostname()
# server.bind((socket.gethostbyname_ex(hostname)[-1][-1], 1234))
# print(socket.gethostbyname_ex(hostname)[-1][-1])
# server.listen()
#
# while True:
#     user, addr = server.accept()
#     print("connect")
#
#     while True:
#         data = user.recv(1024).decode("utf-8").lower()
#         print(data)
#
#
#         def bits_to_kilobytes_or_megabytes(bits):
#             # Конвертация бит в байты
#             bytes = bits / 8
#             # Конвертация байтов в килобайты
#             kilobytes = bytes / 1024
#
#             # Если количество килобайтов меньше 1024, возвращаем килобайты
#             if kilobytes < 1024:
#                 return f"{kilobytes:.2f} KB"
#             # Иначе конвертируем килобайты в мегабайты и возвращаем
#             else:
#                 megabytes = kilobytes / 1024
#                 return f"{megabytes:.2f} MB"
#         # Функция для сканирования дисков
#         def get_available_drives(drive_list):
#             """Проверяет доступность предопределенных дисков в системе."""
#             available_drives = []
#             for drive in drive_list:
#                 if os.path.exists(drive):
#                     available_drives.append(drive)
#             return available_drives
#
#         def scan_disks(directory, file_formats, special_directories, excluded_extensions):
#             disk_info = []
#             exe_files = []
#
#             for root, dirs, files in os.walk(directory):
#                 current_dir_is_special = any(root.startswith(special_dir) for special_dir in special_directories)
#
#                 # Исключаем специальные директории для общего сканирования, но сканируем в них .exe файлы
#                 if current_dir_is_special:
#                     # Сканируем только .exe файлы в специальных директориях
#                     for file in files:
#                         file_path = os.path.join(root, file)
#                         file_extension = os.path.splitext(file)[1].lower()
#                         if file_extension == '.exe':
#                             file_size = os.path.getsize(file_path)
#                             formatted_size = bits_to_kilobytes_or_megabytes(file_size * 8)
#                             file_info = {'File': file, 'Path': file_path, 'Size': formatted_size,
#                                          'Format': file_extension}
#                             exe_files.append(file_info)
#                     continue
#
#                 # Обрабатываем файлы во всех других директориях, исключая .exe и другие нежелательные расширения
#                 for file in files:
#                     file_path = os.path.join(root, file)
#                     file_extension = os.path.splitext(file)[1].lower()
#
#                     if file_extension in file_formats and file_extension not in excluded_extensions:
#                         file_size = os.path.getsize(file_path)
#                         formatted_size = bits_to_kilobytes_or_megabytes(file_size * 8)
#                         file_info = {'File': file, 'Path': file_path, 'Size': formatted_size, 'Format': file_extension}
#                         disk_info.append(file_info)
#
#             return disk_info, exe_files
#
#
#         drive_list = ['A:', 'B:', 'C:', 'D:', 'F:', 'G:', 'H:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', ]
#
#         if data == "scan":
#             # Сканирование диска и сохранение в CSV файл
#             directory_to_scan = get_available_drives(drive_list)
#             file_formats_to_scan = ['.pdf', '.doc', '.xml', '.ptx', '.jpg', '.png', '.mp3', '.gif', '.webm', '.mp4']
#             special_directories = ['K:SteamLibrary', 'K:epp', 'K:build', 'K:lol', 'K:gegegeg', 'K:nox', 'K:Новая папка',
#                                    'C:Program Files', 'C:Program Files (x86)', 'C:Windows', 'C:system.sav',
#                                    'J:EpicGames', 'J:project unit', 'J:soft', 'J:SteamLibrary',
#                                    'Q:SteamLibrary']
#             excluded_extensions = ['.tmp', '.log', '.exe']  # Исключаем .exe для общего сканирования
#             output_csv_file = 'scanned_files.csv'
#             output_exe_file = 'exe_files.csv'
#
#             disks_data, exe_data = scan_disks(directory_to_scan, file_formats_to_scan, special_directories,
#                                               excluded_extensions)
#
#             # Сохранение результатов сканирования
#             df = pd.DataFrame(disks_data)
#             df.to_csv(output_csv_file, index=False)
#             print("Scanned and saved general files.")
#
#             df_exe = pd.DataFrame(exe_data)
#             df_exe.to_csv(output_exe_file, index=False)
#             print("Scanned and saved .exe files separately.")
#
#         elif data == "web":
#             while True:
#                 data = user.recv(1024).decode("utf-8").lower()
#                 if data == "close":
#                     continue
#                 else:
#                     webbrowser.open(f"https://www.{data}")
#         elif data == "file":
#             while True:
#                 data = user.recv(1024).decode("utf-8").lower()
#                 if data == "close":
#                     continue
#                 else:
#                     os.startfile(f"{data}")
#
#
#         elif data == "exit":
#             server.close()

import socket
import webbrowser
import os
import pandas as pd
import psutil
import pickle
import time
def format_size(bytes):
    # Функция для форматирования байт в более читаемые единицы
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} PB"
def system_info():
    # Сбор информации о системе

    memory = psutil.virtual_memory()
    memory_usage_percent = memory.percent

    disk = psutil.disk_usage('/')
    disk_usage_percent = disk.percent

    network = psutil.net_io_counters()
    download_speed = network.bytes_recv
    upload_speed = network.bytes_sent

    info = {}
    info['cpu_usage_percent'] = psutil.cpu_percent(interval=1)
    info['memory_usage'] = f"{memory_usage_percent}%", f"Total: {format_size(memory.total)}"
    info['disk_usage'] = f"{disk_usage_percent}%", f"Total:{format_size(disk.total)}"
    info['network_speed'] = f"Download: {format_size(download_speed)}", f"Upload: {format_size(upload_speed)}"
    return info


#
# # Вывод информации
# print(f"CPU Usage: {cpu_usage_percent}%")
# print(f"Memory Usage: {memory_usage_percent}% of {format_size(memory.total)}")
# print(f"Disk Usage: {disk_usage_percent}% of {format_size(disk.total)}")
# print(f"Network Speed - Download: {format_size(download_speed)}/s, Upload: {format_size(upload_speed)}/s")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
server.bind((socket.gethostbyname_ex(hostname)[-1][-1], 1234))
print(socket.gethostbyname_ex(hostname)[-1][-1])
server.listen()

while True:
    user, addr = server.accept()
    print("connect")
    # Получение информации о системе
    info = system_info()

    # Сериализация данных
    data = pickle.dumps(info)

    # Отправка данных клиенту
    user.sendall(data)

    # Пауза в 5 секунд перед следующим сбором и отправкой данных
    time.sleep(5)
    while True:
        data = user.recv(1024).decode("utf-8").lower()
        print(data)


        def bits_to_kilobytes_or_megabytes(bits):
            # Конвертация бит в байты
            bytes = bits / 8
            # Конвертация байтов в килобайты
            kilobytes = bytes / 1024

            # Если количество килобайтов меньше 1024, возвращаем килобайты
            if kilobytes < 1024:
                return f"{kilobytes:.2f} KB"
            # Иначе конвертируем килобайты в мегабайты и возвращаем
            else:
                megabytes = kilobytes / 1024
                return f"{megabytes:.2f} MB"
        # Функция для сканирования дисков
        # def get_available_drives(drive_list):
        #     """Проверяет доступность предопределенных дисков в системе."""
        #     available_drives = []
        #     for drive in drive_list:
        #         if os.path.exists(drive):
        #             available_drives.append(drive)
        #     return available_drives
        def get_available_drives(drive_list):
            """Проверяет доступность предопределенных дисков и системных папок в системе."""
            available_drives = []
            for drive in drive_list:
                if os.path.exists(drive):
                    available_drives.append(drive)

            # Добавление стандартных системных папок
            user_profile = os.environ.get('USERPROFILE', '')  # Получаем путь к домашнему каталогу пользователя
            standard_paths = [
                os.path.join(user_profile, 'Desktop'),  # Рабочий стол
                os.path.join(user_profile, 'Downloads'),  # Загрузки
                os.path.join(user_profile, 'Documents')  # Документы
            ]
            for path in standard_paths:
                if os.path.exists(path):
                    available_drives.append(path)

            return available_drives


        def scan_disks(directory, file_formats, special_directories, excluded_extensions):
            disk_info = []
            exe_files = []

            for root, dirs, files in os.walk(directory):
                current_dir_is_special = any(
                    root.startswith(os.path.join(directory, special_dir)) for special_dir in special_directories)
                # Сканирование файлов в текущей директории
                for file in files:
                    file_path = os.path.join(root, file)
                    file_extension = os.path.splitext(file)[1].lower()

                    if current_dir_is_special:
                        # Если текущая директория является специальной, сканируем только .exe файлы
                        if file_extension == '.exe':
                            file_size = os.path.getsize(file_path)
                            formatted_size = bits_to_kilobytes_or_megabytes(file_size * 8)
                            file_info = {'File': file, 'Path': file_path, 'Size': formatted_size,
                                         'Format': file_extension}
                            exe_files.append(file_info)
                    else:
                        # Во всех остальных директориях сканируем файлы согласно указанным форматам, исключая .exe и другие нежелательные расширения
                        if file_extension in file_formats and file_extension not in excluded_extensions:
                            file_size = os.path.getsize(file_path)
                            formatted_size = bits_to_kilobytes_or_megabytes(file_size * 8)
                            file_info = {'File': file, 'Path': file_path, 'Size': formatted_size,
                                         'Format': file_extension}
                            disk_info.append(file_info)

            return disk_info, exe_files


        if data == "scan":
            # Получение списка доступных дисков и системных папок
            drive_list = ['A:', 'B:', 'C:', 'D:', 'F:', 'G:', 'H:', 'J:', 'K:', 'L:', 'M:','N:','O:','P:','Q:', 'R:']  # Пример списка дисков
            drives_to_scan = get_available_drives(drive_list)
            file_formats_to_scan = ['.pdf', '.doc', '.xml', '.ptx', '.jpg', '.png', '.mp3', '.gif', '.webm', '.mp4', '.txt']
            special_directories = ['SteamLibrary', 'epp', 'build', 'lol', 'gegegeg', 'nox', 'Новая папка', 'Program Files', 'Program Files (x86)', 'Windows', 'project unit', 'soft', 'EpicGames']
            excluded_extensions = ['.tmp', '.log', '.exe']
            output_csv_file = 'scanned_files.csv'
            output_exe_file = 'exe_files.csv'
            all_disks_data = []
            all_exe_data = []

            for directory_to_scan in drives_to_scan:
                disks_data, exe_data = scan_disks(directory_to_scan, file_formats_to_scan, special_directories,
                                                  excluded_extensions)
                all_disks_data.extend(disks_data)
                all_exe_data.extend(exe_data)

            # Сохранение результатов сканирования
            df = pd.DataFrame(all_disks_data)
            df.to_csv(output_csv_file, index=False)
            print("Scanned and saved general files.")
            df_exe = pd.DataFrame(all_exe_data)
            df_exe.to_csv(output_exe_file, index=False)
            print("Scanned and saved .exe files separately.")
            continue

        # Предопределённый список дисков для проверки
        # drive_list = ['A:', 'B:', 'C:', 'D:', 'F:', 'G:', 'H:', 'J:', 'K:', 'L:', 'M:','N:','O:','P:','Q:', 'R:', './Users' , './Пользователи']
        #
        # if data == "scan":
        #     # Получение списка доступных дисков из предопределенного списка
        #     drives_to_scan = get_available_drives(drive_list)
        #     file_formats_to_scan = ['.pdf', '.doc', '.xml', '.ptx', '.jpg', '.png', '.mp3', '.gif', '.webm', '.mp4']
        #     special_directories = ['SteamLibrary', 'epp', 'build', 'lol', 'gegegeg', 'nox', 'Новая папка',
        #                            'Program Files', 'Program Files (x86)', 'Windows',
        #                            'EpicGames', 'project unit', 'soft']
        #     excluded_extensions = ['.tmp', '.log', '.exe']  # Исключаем .exe для общего сканирования
        #     output_csv_file = 'scanned_files.csv'
        #     output_exe_file = 'exe_files.csv'
        #     all_disks_data = []
        #     all_exe_data = []
        #
        #     # Сканирование каждого доступного диска
        #     for directory_to_scan in drives_to_scan:
        #         disks_data, exe_data = scan_disks(directory_to_scan, file_formats_to_scan, special_directories,
        #                                           excluded_extensions)
        #         all_disks_data.extend(disks_data)
        #         all_exe_data.extend(exe_data)
        #
        #     # Сохранение результатов сканирования
        #     df = pd.DataFrame(all_disks_data)
        #     df.to_csv(output_csv_file, index=False)
        #     print("Scanned and saved general files.")
        #
        #     df_exe = pd.DataFrame(all_exe_data)
        #     df_exe.to_csv(output_exe_file, index=False)
        #     print("Scanned and saved .exe files separately.")

        # if data == "scan":
        #     # Сканирование диска и сохранение в CSV файл
        #     directory_to_scan = '.'
        #     file_formats_to_scan = ['.pdf', '.doc', '.xml', '.ptx', '.jpg', '.png', '.mp3', '.gif', '.webm', '.mp4']
        #     special_directories = ['K:SteamLibrary', 'K:epp', 'K:build', 'K:lol', 'K:gegegeg', 'K:nox', 'K:Новая папка',
        #                            'C:Program Files', 'C:Program Files (x86)', 'C:Windows', 'C:system.sav',
        #                            'J:EpicGames', 'J:project unit', 'J:soft', 'J:SteamLibrary',
        #                            'Q:SteamLibrary']
        #     excluded_extensions = ['.tmp', '.log', '.exe']  # Исключаем .exe для общего сканирования
        #     output_csv_file = 'scanned_files.csv'
        #     output_exe_file = 'exe_files.csv'
        #
        #     disks_data, exe_data = scan_disks(directory_to_scan, file_formats_to_scan, special_directories,
        #                                       excluded_extensions)
        #
        #     # Сохранение результатов сканирования
        #     df = pd.DataFrame(disks_data)
        #     df.to_csv(output_csv_file, index=False)
        #     print("Scanned and saved general files.")
        #
        #     df_exe = pd.DataFrame(exe_data)
        #     df_exe.to_csv(output_exe_file, index=False)
        #     print("Scanned and saved .exe files separately.")

        elif data == "web":
            while True:
                data = user.recv(1024).decode("utf-8").lower()
                if data == "close":
                    break
                else:
                    webbrowser.open(f"https://www.{data}")
        elif data == "file":
            while True:
                data = user.recv(1024).decode("utf-8").lower()
                if data == "close":
                    break
                else:
                    os.startfile(f"{data}")


        elif data == "exit":
            server.close()
