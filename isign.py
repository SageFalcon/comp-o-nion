# # import flet as ft
# # from flet import ElevatedButton, TextField, Column, Card, Text, IconButton, AppBar, icons
# #
# # def main(page: ft.Page):
# #     page.title = "Comp-O-nion"
# #     page.theme_mode = 'dark'
# #     page.vertical_alignment = ft.MainAxisAlignment.CENTER
# #     page.background_color = ft.colors.ORANGE_200
# #
# #     def open_website(e):
# #         page.navigator.push(website_page)
# #
# #     def open_file(e):
# #         page.navigator.push(file_page)
# #
# #     def open_app(e):
# #         page.navigator.push(app_page)
# #
# #     # Создаем AppBar
# #     app_bar = AppBar(
# #         bgcolor=ft.colors.ORANGE_500,
# #         title=Text("Comp-O-nion", style="headlineMedium"),
# #         actions=[IconButton(icon=icons.RADAR, on_click=lambda e: print('IconButton pressed'))]
# #     )
# #
# #     # Кнопки
# #     button_website = ElevatedButton(text="Открыть веб сайт", on_click=open_website, width=391)
# #     button_file = ElevatedButton(text="Открыть файл", on_click=open_file, width=391)
# #     button_app = ElevatedButton(text="Открыть приложение", on_click=open_app, width=391)
# #
# #     # Карточка для отображения состояния устройства
# #     card = Card(
# #         content=Text("Состояние устройства"),
# #         width=369,
# #         height=257,
# #         color=ft.colors.GREY_600
# #
# #     )
# #
# #     # Колонка для вертикального размещения виджетов
# #     col = Column(
# #         controls=[
# #             button_website,
# #             button_file,
# #             button_app,
# #             card
# #         ]
# #     )
# #
# #     # Добавляем AppBar и колонку на страницу
# #     page.add(app_bar, col)
# # def website_page(page: ft.Page):
# #     page.title = "Открыть Вебсайт"
# #     page.background_color = ft.colors.ORANGE_200
# #
# #     app_bar = AppBar(
# #         bgcolor=ft.colors.ORANGE_500,
# #         title=Text("Открыть Вебсайт", style="headlineMedium"),
# #         actions=[IconButton(icon=icons.ARROW_LEFT, on_click=lambda e: print('IconButton pressed'))]
# #     )
# #     data = Text("GEEG")
# #     website_input = TextField(label="Введите название/ссылку сайта", width=200)
# #
# #     def open_web(e):
# #         data.value = f"{website_input.value}!"
# #         page.update()
# #
# #     send_button = ElevatedButton(text="Отправить", on_click=open_web)
# #     col = Column([
# #         data,
# #         website_input,
# #         send_button,
# #     ], expand=True)
# #
# #     page.add(col)
# #
# # def file_page(page: ft.Page):
# #     page.title = "Открыть Вебсайт"
# #     page.background_color = ft.colors.ORANGE_200
# #
# #     app_bar = AppBar(
# #         bgcolor=ft.colors.ORANGE_500,
# #         title=Text("Открыть Вебсайт", style="headlineMedium"),
# #         actions=[IconButton(icon=icons.POINT_OF_SALE_SHARP, on_click=lambda e: print('IconButton pressed'))]
# #     )
# #     data = Text("GEEG")
# #     website_input = TextField(label="Введите название/ссылку сайта", width=200)
# #
# #     def open_web(e):
# #         data.value = f"{website_input.value}!"
# #         page.update()
# #
# #     send_button = ElevatedButton(text="Отправить", on_click=open_web)
# #     col = Column([
# #         data,
# #         website_input,
# #         send_button,
# #     ], expand=True)
# #
# #     page.add(col)
# #
# #
# # def app_page(page: ft.Page):
# #     page.title = "Открыть Вебсайт"
# #     page.background_color = ft.colors.ORANGE_200
# #
# #     app_bar = AppBar(
# #         bgcolor=ft.colors.ORANGE_500,
# #         title=Text("Открыть Вебсайт", style="headlineMedium"),
# #         actions=[IconButton(icon=icons.POINT_OF_SALE_SHARP, on_click=lambda e: print('IconButton pressed'))]
# #     )
# #     data = Text("GEEG")
# #     website_input = TextField(label="Введите название/ссылку сайта", width=200)
# #
# #     def open_web(e):
# #         data.value = f"{website_input.value}!"
# #         page.update()
# #
# #     send_button = ElevatedButton(text="Отправить", on_click=open_web)
# #     col = Column([
# #         data,
# #         website_input,
# #         send_button,
# #     ], expand=True)
# #
# #     page.add(col)
# #
# # ft.app(target=main_page)
#
#
# # import socket
# # import webbrowser
# # import os
# # import pandas as pd
# # from pathlib import Path
# #
# #
# # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # hostname = socket.gethostname()
# # server.bind((socket.gethostbyname_ex(hostname)[-1][-1], 1234))
# # print(socket.gethostbyname_ex(hostname)[-1][-1])
# # server.listen()
# #
# # while True:
# #     user, addr = server.accept()
# #     print("connect")
# #
# #     while True:
# #         data = user.recv(1024).decode("utf-8").lower()
# #         print(data)
# #
# #
# #         def bits_to_kilobytes_or_megabytes(bits):
# #             # Конвертация бит в байты
# #             bytes = bits / 8
# #             # Конвертация байтов в килобайты
# #             kilobytes = bytes / 1024
# #
# #             # Если количество килобайтов меньше 1024, возвращаем килобайты
# #             if kilobytes < 1024:
# #                 return f"{kilobytes:.2f} KB"
# #             # Иначе конвертируем килобайты в мегабайты и возвращаем
# #             else:
# #                 megabytes = kilobytes / 1024
# #                 return f"{megabytes:.2f} MB"
# #         # Функция для сканирования дисков
# #         def get_available_drives(drive_list):
# #             """Проверяет доступность предопределенных дисков в системе."""
# #             available_drives = []
# #             for drive in drive_list:
# #                 if os.path.exists(drive):
# #                     available_drives.append(drive)
# #             return available_drives
# #
# #         def scan_disks(directory, file_formats, special_directories, excluded_extensions):
# #             disk_info = []
# #             exe_files = []
# #
# #             for root, dirs, files in os.walk(directory):
# #                 current_dir_is_special = any(root.startswith(special_dir) for special_dir in special_directories)
# #
# #                 # Исключаем специальные директории для общего сканирования, но сканируем в них .exe файлы
# #                 if current_dir_is_special:
# #                     # Сканируем только .exe файлы в специальных директориях
# #                     for file in files:
# #                         file_path = os.path.join(root, file)
# #                         file_extension = os.path.splitext(file)[1].lower()
# #                         if file_extension == '.exe':
# #                             file_size = os.path.getsize(file_path)
# #                             formatted_size = bits_to_kilobytes_or_megabytes(file_size * 8)
# #                             file_info = {'File': file, 'Path': file_path, 'Size': formatted_size,
# #                                          'Format': file_extension}
# #                             exe_files.append(file_info)
# #                     continue
# #
# #                 # Обрабатываем файлы во всех других директориях, исключая .exe и другие нежелательные расширения
# #                 for file in files:
# #                     file_path = os.path.join(root, file)
# #                     file_extension = os.path.splitext(file)[1].lower()
# #
# #                     if file_extension in file_formats and file_extension not in excluded_extensions:
# #                         file_size = os.path.getsize(file_path)
# #                         formatted_size = bits_to_kilobytes_or_megabytes(file_size * 8)
# #                         file_info = {'File': file, 'Path': file_path, 'Size': formatted_size, 'Format': file_extension}
# #                         disk_info.append(file_info)
# #
# #             return disk_info, exe_files
# #
# #
# #         drive_list = ['A:', 'B:', 'C:', 'D:', 'F:', 'G:', 'H:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', ]
# #
# #         if data == "scan":
# #             # Сканирование диска и сохранение в CSV файл
# #             directory_to_scan = get_available_drives(drive_list)
# #             file_formats_to_scan = ['.pdf', '.doc', '.xml', '.ptx', '.jpg', '.png', '.mp3', '.gif', '.webm', '.mp4']
# #             special_directories = ['K:SteamLibrary', 'K:epp', 'K:build', 'K:lol', 'K:gegegeg', 'K:nox', 'K:Новая папка',
# #                                    'C:Program Files', 'C:Program Files (x86)', 'C:Windows', 'C:system.sav',
# #                                    'J:EpicGames', 'J:project unit', 'J:soft', 'J:SteamLibrary',
# #                                    'Q:SteamLibrary']
# #             excluded_extensions = ['.tmp', '.log', '.exe']  # Исключаем .exe для общего сканирования
# #             output_csv_file = 'scanned_files.csv'
# #             output_exe_file = 'exe_files.csv'
# #
# #             disks_data, exe_data = scan_disks(directory_to_scan, file_formats_to_scan, special_directories,
# #                                               excluded_extensions)
# #
# #             # Сохранение результатов сканирования
# #             df = pd.DataFrame(disks_data)
# #             df.to_csv(output_csv_file, index=False)
# #             print("Scanned and saved general files.")
# #
# #             df_exe = pd.DataFrame(exe_data)
# #             df_exe.to_csv(output_exe_file, index=False)
# #             print("Scanned and saved .exe files separately.")
# #
# #         elif data == "web":
# #             while True:
# #                 data = user.recv(1024).decode("utf-8").lower()
# #                 if data == "close":
# #                     continue
# #                 else:
# #                     webbrowser.open(f"https://www.{data}")
# #         elif data == "file":
# #             while True:
# #                 data = user.recv(1024).decode("utf-8").lower()
# #                 if data == "close":
# #                     continue
# #                 else:
# #                     os.startfile(f"{data}")
# #
# #
# #         elif data == "exit":
# #             server.close()
#
# # import os
# # import tkinter as tk
# # from tkinter import messagebox
# #
# #
# # def get_drives():
# #     drives = []
# #     for drive in range(65, 91):
# #         drive_letter = chr(drive)
# #         if os.path.exists(f"{drive_letter}:\\"):
# #             drives.append(f"{drive_letter}:\\")
# #     return drives
# #
# #
# # def select_disks():
# #     def on_ok():
# #         selected = [drive for drive, var in checkboxes.items() if var.get()]
# #         if selected:
# #             root.selected_disks = selected
# #             root.quit()
# #         else:
# #             messagebox.showwarning("Выбор дисков", "Выберите хотя бы один диск.")
# #
# #     root = tk.Tk()
# #     root.title("Выбор дисков")
# #
# #     checkboxes = {}
# #     drives = get_drives()
# #
# #     for drive in drives:
# #         var = tk.BooleanVar()
# #         chk = tk.Checkbutton(root, text=drive, variable=var)
# #         chk.pack(anchor=tk.W)
# #         checkboxes[drive] = var
# #
# #     ok_button = tk.Button(root, text="OK", command=on_ok)
# #     ok_button.pack()
# #
# #     root.selected_disks = []
# #     root.mainloop()
# #     return root.selected_disks
# #
# #
# # def scan_directory(directory):
# #     for root, dirs, files in os.walk(directory):
# #         for file in files:
# #             print(os.path.join(root, file))  # Вывести полный путь к файлу
# #
# #
# # if __name__ == "__main__":
# #     selected_disks = select_disks()
# #     if selected_disks:
# #         print(f"Выбранные диски: {', '.join(selected_disks)}")
# #         for disk in selected_disks:
# #             print(f"Сканирование диска {disk}...")
# #             scan_directory(disk)
# #     else:
# #         print("Диски не выбраны.")
#
# #
# # import os
# # import socket
# # import tkinter as tk
# # from tkinter import messagebox
# # import pystray
# # from PIL import Image, ImageDraw
# # import threading
# # import socketserver
# # import time
# #
# #
# # class WidgetApp:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("WidgetApp")
# #         self.root.geometry("300x250")
# #         self.root.protocol("WM_DELETE_WINDOW", self.hide_window)
# #
# #         self.create_tray_icon()
# #
# #         # Создание простого интерфейса
# #         self.label = tk.Label(root, text="Выберите диски для сканирования:")
# #         self.label.pack(pady=10)
# #
# #         self.select_button = tk.Button(root, text="Выбрать диски", command=self.select_disks)
# #         self.select_button.pack(pady=10)
# #
# #         self.scan_button = tk.Button(root, text="Начать сканирование", command=self.start_scan, state=tk.DISABLED)
# #         self.scan_button.pack(pady=10)
# #
# #         self.result_text = tk.Text(root, height=5, width=40)
# #         self.result_text.pack(pady=10)
# #
# #         self.restart_button = tk.Button(root, text="Перезагрузить сервер", command=self.restart_server)
# #         self.restart_button.pack(pady=10)
# #
# #     def create_tray_icon(self):
# #         # Создание значка для трея
# #         self.image = self.create_image()
# #         self.menu = pystray.Menu(pystray.MenuItem('Открыть', self.show_window),
# #                                  pystray.MenuItem('Выход', self.exit_app))
# #         self.icon = pystray.Icon("test", self.image, "WidgetApp", self.menu)
# #
# #         # Запуск иконки трея в отдельном потоке
# #         threading.Thread(target=self.icon.run, daemon=True).start()
# #
# #     def create_image(self):
# #         # Создание изображения для иконки трея
# #         image = Image.new('RGB', (64, 64), (255, 255, 255))
# #         dc = ImageDraw.Draw(image)
# #         dc.rectangle((0, 0, 64, 64), fill=(0, 0, 0))
# #         return image
# #
# #     def hide_window(self):
# #         self.root.withdraw()
# #         self.icon.visible = True
# #
# #     def show_window(self, icon, item):
# #         self.root.deiconify()
# #         self.icon.visible = False
# #
# #     def close_window(self):
# #         self.icon.stop()
# #         self.root.destroy()
# #
# #     def exit_app(self, icon, item):
# #         self.icon.stop()
# #         self.root.destroy()
# #
# #     def get_drives(self):
# #         drives = []
# #         for drive in range(65, 91):
# #             drive_letter = chr(drive)
# #             if os.path.exists(f"{drive_letter}:\\"):
# #                 drives.append(f"{drive_letter}:\\")
# #         return drives
# #
# #     def select_disks(self):
# #         def on_ok():
# #             selected = [drive for drive, var in checkboxes.items() if var.get()]
# #             if selected:
# #                 self.selected_disks = selected
# #                 selection_window.destroy()
# #                 self.scan_button.config(state=tk.NORMAL)
# #             else:
# #                 messagebox.showwarning("Выбор дисков", "Выберите хотя бы один диск.")
# #
# #         selection_window = tk.Toplevel(self.root)
# #         selection_window.title("Выбор дисков")
# #
# #         checkboxes = {}
# #         drives = self.get_drives()
# #
# #         for drive in drives:
# #             var = tk.BooleanVar()
# #             chk = tk.Checkbutton(selection_window, text=drive, variable=var)
# #             chk.pack(anchor=tk.W)
# #             checkboxes[drive] = var
# #
# #         ok_button = tk.Button(selection_window, text="OK", command=on_ok)
# #         ok_button.pack()
# #
# #     def start_scan(self):
# #         self.result_text.delete(1.0, tk.END)
# #         if hasattr(self, 'selected_disks') and self.selected_disks:
# #             for disk in self.selected_disks:
# #                 self.result_text.insert(tk.END, f"Сканирование диска {disk}...\n")
# #                 self.scan_directory(disk)
# #         else:
# #             messagebox.showwarning("Сканирование", "Сначала выберите диски для сканирования.")
# #
# #     def scan_directory(self, directory):
# #         for root, dirs, files in os.walk(directory):
# #             for file in files:
# #                 self.result_text.insert(tk.END, f"{os.path.join(root, file)}\n")
# #         self.result_text.insert(tk.END, "Сканирование завершено.\n")
# #
# #     def restart_server(self):
# #         try:
# #             with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
# #                 s.connect(('localhost', 12345))  # Адрес и порт вашего серверного приложения
# #                 s.sendall(b'restart')  # Отправка команды перезагрузки серверу
# #                 response = s.recv(1024).decode()
# #                 self.result_text.insert(tk.END, f"Сервер: {response}\n")
# #         except ConnectionRefusedError:
# #             messagebox.showerror("Ошибка", "Не удалось подключиться к серверу.")
# #         except Exception as e:
# #             messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")
# #
# #
# # class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
# #     def handle(self):
# #         self.data = self.request.recv(1024).strip()
# #         print(f"{self.client_address[0]} wrote: {self.data.decode()}")
# #         if self.data.decode() == 'restart':
# #             self.server.restart_flag = True
# #             self.request.sendall(b'Server is restarting...')
# #         else:
# #             self.request.sendall(b'Unknown command')
# #
# #
# # class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
# #     daemon_threads = True
# #     allow_reuse_address = True
# #     restart_flag = False
# #
# #
# # def restart_server(server):
# #     server.shutdown()
# #     server.server_close()
# #     time.sleep(1)  # wait for the server to shut down
# #     server.restart_flag = False
# #     start_server()
# #
# #
# # def start_server():
# #     HOST, PORT = "localhost", 12345
# #     server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
# #     server_thread = threading.Thread(target=server.serve_forever)
# #     server_thread.daemon = True
# #     server_thread.start()
# #     print(f"Server loop running in thread: {server_thread.name}")
# #
# #     while True:
# #         time.sleep(1)
# #         if server.restart_flag:
# #             print("Restarting server...")
# #             restart_server(server)
# #
# #
# # if __name__ == "__main__":
# #     server_thread = threading.Thread(target=start_server)
# #     server_thread.daemon = True
# #     server_thread.start()
# #
# #     root = tk.Tk()
# #     app = WidgetApp(root)
# #     root.mainloop()
#
#
# import os
# import socket
# import socketserver
# import tkinter as tk
# from tkinter import messagebox
# import pystray
# from PIL import Image, ImageDraw
# import threading
# import psutil
# import pickle
# import time
# import pandas as pd
# import webbrowser
#
#
# class WidgetApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("WidgetApp")
#         self.root.geometry("400x400")
#         self.root.protocol("WM_DELETE_WINDOW", self.hide_window)
#
#         self.create_tray_icon()
#
#         # Создание простого интерфейса
#         self.label = tk.Label(root, text="Выберите диски для сканирования:")
#         self.label.pack(pady=10)
#
#         self.select_button = tk.Button(root, text="Выбрать диски", command=self.select_disks)
#         self.select_button.pack(pady=10)
#
#         self.scan_button = tk.Button(root, text="Начать сканирование", command=self.start_scan, state=tk.DISABLED)
#         self.scan_button.pack(pady=10)
#
#         self.sys_info_button = tk.Button(root, text="Системная информация", command=self.show_system_info)
#         self.sys_info_button.pack(pady=10)
#
#         self.web_button = tk.Button(root, text="Открыть веб-сайт", command=self.open_website)
#         self.web_button.pack(pady=10)
#
#         self.file_button = tk.Button(root, text="Открыть файл", command=self.open_file)
#         self.file_button.pack(pady=10)
#
#         self.restart_button = tk.Button(root, text="Перезагрузить сервер", command=self.restart_server)
#         self.restart_button.pack(pady=10)
#
#         self.result_text = tk.Text(root, height=10, width=50)
#         self.result_text.pack(pady=10)
#
#     def create_tray_icon(self):
#         # Создание значка для трея
#         self.image = self.create_image()
#         self.menu = pystray.Menu(pystray.MenuItem('Открыть', self.show_window),
#                                  pystray.MenuItem('Выход', self.exit_app),
#                                  pystray.MenuItem('Disk', self.select_disks),
#                                  pystray.MenuItem('save', self.start_scan))
#         self.icon = pystray.Icon("test", self.image, "WidgetApp", self.menu)
#
#         # Запуск иконки трея в отдельном потоке
#         threading.Thread(target=self.icon.run, daemon=True).start()
#
#     def create_image(self):
#         # Создание изображения для иконки трея
#         image = Image.new('RGB', (64, 64), (255, 255, 255))
#         dc = ImageDraw.Draw(image)
#         dc.rectangle((0, 0, 64, 64), fill=(0, 0, 0))
#         return image
#
#     def hide_window(self):
#         self.root.withdraw()
#         self.icon.visible = True
#
#     def show_window(self, icon, item):
#         self.root.deiconify()
#         self.icon.visible = False
#
#     def close_window(self):
#         self.icon.stop()
#         self.root.destroy()
#
#     def exit_app(self, icon, item):
#         self.icon.stop()
#         self.root.destroy()
#
#     def get_drives(self):
#         drives = []
#         for drive in range(65, 91):
#             drive_letter = chr(drive)
#             if os.path.exists(f"{drive_letter}:\\"):
#                 drives.append(f"{drive_letter}:\\")
#         return drives
#
#     def select_disks(self):
#         def on_ok():
#             selected = [drive for drive, var in checkboxes.items() if var.get()]
#             if selected:
#                 self.selected_disks = selected
#                 selection_window.destroy()
#                 self.scan_button.config(state=tk.NORMAL)
#             else:
#                 messagebox.showwarning("Выбор дисков", "Выберите хотя бы один диск.")
#
#         selection_window = tk.Toplevel(self.root)
#         selection_window.title("Выбор дисков")
#
#         checkboxes = {}
#         drives = self.get_drives()
#
#         for drive in drives:
#             var = tk.BooleanVar()
#             chk = tk.Checkbutton(selection_window, text=drive, variable=var)
#             chk.pack(anchor=tk.W)
#             checkboxes[drive] = var
#
#         ok_button = tk.Button(selection_window, text="OK", command=on_ok)
#         ok_button.pack()
#
#     def start_scan(self):
#         self.result_text.delete(1.0, tk.END)
#         if hasattr(self, 'selected_disks') and self.selected_disks:
#             for disk in self.selected_disks:
#                 self.result_text.insert(tk.END, f"Сканирование диска {disk}...\n")
#                 self.scan_directory(disk)
#         else:
#             messagebox.showwarning("Сканирование", "Сначала выберите диски для сканирования.")
#
#     def scan_directory(self, directory):
#         file_formats_to_scan = ['.pdf', '.doc', '.xml', '.ptx', '.jpg', '.png', '.mp3', '.gif', '.webm', '.mp4', '.txt']
#         special_directories = ['SteamLibrary', 'epp', 'build', 'lol', 'gegegeg', 'nox', 'Новая папка', 'Program Files',
#                                'Program Files (x86)', 'Windows', 'project unit', 'soft', 'EpicGames']
#         excluded_extensions = ['.tmp', '.log', '.exe']
#         all_disks_data = []
#         all_exe_data = []
#
#         disks_data, exe_data = self.scan_disks(directory, file_formats_to_scan, special_directories,
#                                                excluded_extensions)
#         all_disks_data.extend(disks_data)
#         all_exe_data.extend(exe_data)
#
#         output_csv_file = 'scanned_files.csv'
#         output_exe_file = 'exe_files.csv'
#
#         df = pd.DataFrame(all_disks_data)
#         df.to_csv(output_csv_file, index=False)
#         self.result_text.insert(tk.END, "Scanned and saved general files.\n")
#
#         df_exe = pd.DataFrame(all_exe_data)
#         df_exe.to_csv(output_exe_file, index=False)
#         self.result_text.insert(tk.END, "Scanned and saved .exe files separately.\n")
#
#     def scan_disks(self, directory, file_formats, special_directories, excluded_extensions):
#         disk_info = []
#         exe_files = []
#
#         for root, dirs, files in os.walk(directory):
#             current_dir_is_special = any(
#                 root.startswith(os.path.join(directory, special_dir)) for special_dir in special_directories)
#             # Сканирование файлов в текущей директории
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 file_extension = os.path.splitext(file)[1].lower()
#
#                 if current_dir_is_special:
#                     # Если текущая директория является специальной, сканируем только .exe файлы
#                     if file_extension == '.exe':
#                         file_size = os.path.getsize(file_path)
#                         formatted_size = self.bits_to_kilobytes_or_megabytes(file_size * 8)
#                         file_info = {'File': file, 'Path': file_path, 'Size': formatted_size,
#                                      'Format': file_extension}
#                         exe_files.append(file_info)
#                 else:
#                     # Во всех остальных директориях сканируем файлы согласно указанным форматам, исключая .exe и другие нежелательные расширения
#                     if file_extension in file_formats and file_extension not in excluded_extensions:
#                         file_size = os.path.getsize(file_path)
#                         formatted_size = self.bits_to_kilobytes_or_megabytes(file_size * 8)
#                         file_info = {'File': file, 'Path': file_path, 'Size': formatted_size,
#                                      'Format': file_extension}
#                         disk_info.append(file_info)
#
#         return disk_info, exe_files
#
#     def bits_to_kilobytes_or_megabytes(self, bits):
#         # Конвертация бит в байты
#         bytes = bits / 8
#         # Конвертация байтов в килобайты
#         kilobytes = bytes / 1024
#
#         # Если количество килобайтов меньше 1024, возвращаем килобайты
#         if kilobytes < 1024:
#             return f"{kilobytes:.2f} KB"
#         # Иначе конвертируем килобайты в мегабайты и возвращаем
#         else:
#             megabytes = kilobytes / 1024
#             return f"{megabytes:.2f} MB"
#
#     def show_system_info(self):
#         info = self.system_info()
#         self.result_text.delete(1.0, tk.END)
#         for key, value in info.items():
#             self.result_text.insert(tk.END, f"{key}: {value}\n")
#
#     def system_info(self):
#         # Сбор информации о системе
#
#         memory = psutil.virtual_memory()
#         memory_usage_percent = memory.percent
#
#         disk = psutil.disk_usage('/')
#         disk_usage_percent = disk.percent
#
#         network = psutil.net_io_counters()
#         download_speed = network.bytes_recv
#         upload_speed = network.bytes_sent
#
#         info = {}
#         info['cpu_usage_percent'] = psutil.cpu_percent(interval=1)
#         info['memory_usage'] = f"{memory_usage_percent}%", f"Total: {self.format_size(memory.total)}"
#         info['disk_usage'] = f"{disk_usage_percent}%", f"Total:{self.format_size(disk.total)}"
#         info[
#             'network_speed'] = f"Download: {self.format_size(download_speed)}", f"Upload: {self.format_size(upload_speed)}"
#         return info
#
#     def format_size(self, bytes):
#         # Функция для форматирования байт в более читаемые единицы
#         for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']:
#             if bytes < 1024:
#                 return f"{bytes:.2f} {unit}"
#             bytes /= 1024
#         return f"{bytes:.2f} PB"
#
#     def open_website(self):
#         website = tk.simpledialog.askstring("Введите URL", "Введите URL веб-сайта:")
#         if website:
#             webbrowser.open(f"https://{website}")
#
#     def open_file(self):
#         file_path = tk.filedialog.askopenfilename()
#         if file_path:
#             os.startfile(file_path)
#
#     def restart_server(self):
#         try:
#             with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#                 s.connect(('localhost', 12345))  # Адрес и порт вашего серверного приложения
#                 s.sendall(b'restart')  # Отправка команды перезагрузки серверу
#                 response = s.recv(1024).decode()
#                 self.result_text.insert(tk.END, f"Сервер: {response}\n")
#         except ConnectionRefusedError:
#             messagebox.showerror("Ошибка", "Не удалось подключиться к серверу.")
#         except Exception as e:
#             messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")
#
#
# class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
#     def handle(self):
#         self.data = self.request.recv(1024).strip()
#         print(f"{self.client_address[0]} wrote: {self.data.decode()}")
#         if self.data.decode() == 'restart':
#             self.server.restart_flag = True
#             self.request.sendall(b'Server is restarting...')
#         else:
#             self.request.sendall(b'Unknown command')
#
#
# class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
#     daemon_threads = True
#     allow_reuse_address = True
#     restart_flag = False
#
#
# def restart_server(server):
#     server.shutdown()
#     server.server_close()
#     time.sleep(1)  # wait for the server to shut down
#     server.restart_flag = False
#     start_server()
#
#
# def start_server():
#     HOST, PORT = "localhost", 12345
#     server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
#     server_thread = threading.Thread(target=server.serve_forever)
#     server_thread.daemon = True
#     server_thread.start()
#     print(f"Server loop running in thread: {server_thread.name}")
#
#     while True:
#         time.sleep(1)
#         if server.restart_flag:
#             print("Restarting server...")
#             restart_server(server)
#
#
# if __name__ == "__main__":
#     server_thread = threading.Thread(target=start_server)
#     server_thread.daemon = True
#     server_thread.start()
#
#     root = tk.Tk()
#     app = WidgetApp(root)
#     root.mainloop()


import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, Listbox, MULTIPLE
import pandas as pd


class ScanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ScanApp")
        self.root.geometry("500x400")

        self.selected_disks = []
        self.selected_folders = []
        self.file_formats = ['.pdf', '.doc', '.xml', '.ptx', '.jpg', '.png', '.mp3', '.gif', '.webm', '.mp4', '.txt']

        # Интерфейс выбора дисков
        self.disk_label = tk.Label(root, text="Выберите диски:")
        self.disk_label.pack(pady=5)

        self.disk_button = tk.Button(root, text="Выбрать диски", command=self.select_disks)
        self.disk_button.pack(pady=5)

        # Интерфейс выбора папок
        self.folder_label = tk.Label(root, text="Выберите папки для сканирования:")
        self.folder_label.pack(pady=5)

        self.folder_button = tk.Button(root, text="Выбрать папки", command=self.select_folders)
        self.folder_button.pack(pady=5)

        # Интерфейс выбора форматов файлов
        self.format_label = tk.Label(root, text="Форматы файлов для сканирования:")
        self.format_label.pack(pady=5)

        self.format_listbox = Listbox(root, selectmode=MULTIPLE)
        for fmt in self.file_formats:
            self.format_listbox.insert(tk.END, fmt)
        self.format_listbox.pack(pady=5)

        # Кнопка для начала сканирования
        self.scan_button = tk.Button(root, text="Начать сканирование", command=self.start_scan)
        self.scan_button.pack(pady=20)

        # Текстовое поле для вывода результатов
        self.result_text = tk.Text(root, height=10, width=60)
        self.result_text.pack(pady=10)

    def select_disks(self):
        disks = filedialog.askopenfilenames(title="Выберите диски", filetypes=[("Диск", "*")])
        if disks:
            self.selected_disks = list(disks)
            self.result_text.insert(tk.END, f"Выбранные диски: {', '.join(self.selected_disks)}\n")

    def select_folders(self):
        folders = filedialog.askdirectory(mustexist=True, title="Выберите папки")
        if folders:
            self.selected_folders.append(folders)
            self.result_text.insert(tk.END, f"Выбранные папки: {', '.join(self.selected_folders)}\n")

    def start_scan(self):
        self.result_text.delete(1.0, tk.END)
        selected_formats = [self.format_listbox.get(idx) for idx in self.format_listbox.curselection()]
        if not self.selected_disks or not self.selected_folders or not selected_formats:
            messagebox.showwarning("Ошибка", "Пожалуйста, выберите диски, папки и форматы файлов для сканирования.")
            return

        all_disks_data = []
        for disk in self.selected_disks:
            for folder in self.selected_folders:
                disks_data = self.scan_directory(folder, selected_formats)
                all_disks_data.extend(disks_data)

        output_csv_file = 'scanned_files.csv'
        df = pd.DataFrame(all_disks_data)
        df.to_csv(output_csv_file, index=False)
        self.result_text.insert(tk.END, "Сканирование завершено и результаты сохранены в 'scanned_files.csv'.\n")

    def scan_directory(self, directory, file_formats):
        disk_info = []

        for root, _, files in os.walk(directory):
            for file in files:
                file_extension = os.path.splitext(file)[1].lower()
                if file_extension in file_formats:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    file_info = {'File': file, 'Path': file_path, 'Size': f"{file_size / 1024:.2f} KB",
                                 'Format': file_extension}
                    disk_info.append(file_info)

        return disk_info


if __name__ == "__main__":
    root = tk.Tk()
    app = ScanApp(root)
    root.mainloop()
