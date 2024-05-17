import flet as ft
from flet import Column, Text, AppBar, icons, AppView, Container, ListTile, ListView
import socket
import pandas as pd
import os
import pickle
def main(page: ft.Page):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = socket.gethostname()
    client.connect((socket.gethostbyname_ex(hostname)[-1][-1], 1234))
    page.title = "Comp-O-nion"
    page.theme_mode = 'dark'
 
    page.background_color = ft.colors.ORANGE_200
    #функции для страниц
    def open_website(e):
        send_message(e,'web')
        page.clean()
        page.add(app_bar_webs, website_page)
    def open_files(e):
        send_message(e,'file')
        page.clean()
        page.scroll = "auto"
        page.add(app_bar_files, file_page)

    def open_apps(e):
        send_message(e,'file')
        page.clean()
        page.scroll = "auto"
        page.add(app_bar_apps, app_page)
    # socket sender
    def send_message(e, message):
        # Отправка сообщения через сокет
        client.send(message.encode("utf-8"))
    # website name placeholder
    t = ft.TextField(label="Website Name", hint_text="example.com")

    #request sender
    def send_request(e):
        send_message(e, f"{t.value}")

    # back to main func
    def back_to_main(e):
        send_message(e, 'close')
        page.clean()
        page.add(app_bar, main_page)

    # show files
    if os.path.isfile("scanned_files.csv"):
        csvpd = pd.read_csv("scanned_files.csv")
        json_str = csvpd.to_json()
        df = pd.read_json(json_str)

        alldata = df.to_dict(orient = "records")

        datatable = ft.DataTable(
            columns=[
            ft.DataColumn(Text("Name")),
            ft.DataColumn(Text("Size")),
            ft.DataColumn(Text("Format")),
            ft.DataColumn(Text("Download"))
            ],
            rows=[]
        )
        for x in alldata:
            if x['Format'] != '.exe':
                datatable.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(Text(x['File'])),
                            ft.DataCell(Text(x['Size'])),
                            ft.DataCell(Text(x['Format'])),
                            ft.DataCell(ft.ElevatedButton(text="Скачать", on_click=lambda e: print("download")))
                        ], data=Text(f"{x['Path']}"),
                        on_select_changed=lambda e: open(e)
                    )
                )
    elif os.path.isdir("scanned_files.csv"):
        pass

    #show exe files
    if os.path.isfile("exe_files.csv"):
        csvpd = pd.read_csv("exe_files.csv")
        json_str = csvpd.to_json()
        df = pd.read_json(json_str)

        exe_alldata = df.to_dict(orient = "records")

        exe_datatable = ft.DataTable(
            columns=[
            ft.DataColumn(Text("Name")),
            ft.DataColumn(Text("Path"))
            ],
            rows=[]
        )
        for x in exe_alldata:
            if x['Format'] == '.exe':
                exe_datatable.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(Text(x['File'])),
                            ft.DataCell(Text(x['Path'])),
                        ], data=Text(f"{x['Path']}"),
                        on_select_changed=lambda e: open(e)
                    )
                )
    elif os.path.isdir("exe_files.csv"):
        pass

    def open(e):
        op = e.control.data.value
        send_message(e, f"{op}")

    # def handle_change(e):
    #
    #
    # anchor = ft.SearchBar(
    #     view_elevation=4,
    #     divider_color=ft.colors.AMBER_ACCENT_200,
    #     view_hint_text="Nazvanie",
    #     on_change=handle_change,
    # )

    #appbar text
    web_text = ft.Text("Открыть Вебсайт", style="headlineMedium", font_family='freesans-serif', size=25)
    file_text = ft.Text("Файлы", style="headlineMedium", font_family='freesans-serif', size=25)
    app_text = ft.Text("Приложения", style="headlineMedium", font_family='freesans-serif', size=25)

    # appbars
    app_bar_webs = AppBar(
                bgcolor=ft.colors.ORANGE_500,
                leading=ft.IconButton(icons.ARROW_LEFT, on_click=lambda e: back_to_main(e)),
                title=web_text,
                actions=[
                    ft.IconButton(icon=icons.SUNNY, on_click=lambda e: change_theme(e))
                ]

            )

    app_bar_files = AppBar(
        bgcolor=ft.colors.ORANGE_500,
        leading=ft.IconButton(icons.ARROW_LEFT, on_click=lambda e: back_to_main(e)),
        title=file_text,
        actions=[
            ft.IconButton(icon=icons.SUNNY, on_click=lambda e: change_theme(e))
        ]

    )

    app_bar_apps = AppBar(
        bgcolor=ft.colors.ORANGE_500,
        leading=ft.IconButton(icons.ARROW_LEFT, on_click=lambda e: back_to_main(e)),
        title=app_text,
        actions=[
            ft.IconButton(icon=icons.SUNNY, on_click=lambda e: change_theme(e))
        ]

    )
    #___________________________________________________
    app_bar = AppBar(
        bgcolor=ft.colors.ORANGE_500,
        title=Text("Comp-O-nion", style="headlineMedium", font_family='freesans-serif', size=25),
        actions=[
            ft.IconButton(icon=icons.RADAR, on_click=lambda e: send_message(e, 'scan')),
            ft.IconButton(icon=icons.SUNNY, on_click=lambda e: change_theme(e))
        ]

    )
    #___________________________________________


    # pages
    website_page = ft.Column([
        t,
        ft.ElevatedButton(text="Открыть", on_click=lambda e: send_request(e))
    ])
    #__________________________________________________-

    file_page = ft.Column([
        datatable,
    ])

    app_page = ft.Column([
        exe_datatable,
    ])
    data = client.recv(4096)
    if data:
        info = pickle.loads(data)
    #_____________________________________________________
    main_page = ft.Column([
        ft.ElevatedButton(text="Открыть вебсайт", on_click=lambda e: open_website(e)),
        ft.ElevatedButton(text="Открыть файлы", on_click=lambda e: open_files(e)),
        ft.ElevatedButton(text="Открыть приложение", on_click=lambda e: open_apps(e)),
        ft.Card(
            content=Container(
                content=Column(
                    [
                        ft.ListTile(
                        leading=ft.Icon(ft.icons.COMPUTER_ROUNDED),
                        title=ft.Text("Состояние компьютера"),
                        # subtitle=ft.Text(f"{socket.gethostbyname_ex(hostname)[-1][-1]}")

                    ),
                        ft.Text(f"Процессор:{info["cpu_usage_percent"]}%"),
                        ft.Text(f"Оперативная память:{info['memory_usage']}"),
                        ft.Text(f"Заполненность дисков:{info['disk_usage']}"),
                        ft.Text(f"Скорость интернета:{info['network_speed']}"),
                      ]), padding=15))


    ])
    #_______________________________________________________--
    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()
    page.add(app_bar,main_page)
ft.app(target=main, view=AppView.FLET_APP)


