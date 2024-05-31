import socket
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hostname = socket.gethostname()
        self.client.connect((socket.gethostbyname_ex(hostname)[-1][-1], 1234))

        # Кнопка "Open" для открытия программ на компьютере
        self.open_button = Button(text='Open', size_hint=(0.2, 0.1),  background_color= (0.96, 0.87, 0.7) )
        self.open_button.bind(on_press=self.open_programs)

        # Кнопка "Web" для открытия веб-сайта
        self.web_button = Button(text='Web', size_hint=(0.2, 0.1),  background_color= (0.898, 0.71, 0.463, 1) )
        self.web_button.bind(on_press=self.show_text_input)
        # Добавляем кнопки на экран
        # Создаем виджет AsyncImage с заданным источником изображения
        image = AsyncImage(source='radar_icon.png')
        # Создаем кнопку и устанавливаем изображение как ее фон
        self.scan_button = Button(background_normal=image.source, background_down=image.source)
        self.scan_button.bind(on_press=self.scan)
        self.add_widget(self.open_button)
        self.add_widget(self.web_button)
        self.add_widget(self.scan_button)

    def show_main_screen(self, instance):
        # Очищаем экран и добавляем кнопки основного экрана
        self.clear_widgets()
        self.add_widget(self.open_button)
        self.add_widget(self.web_button)
        self.add_widget(self.scan_button)

        # Скрываем кнопку "Back"
        self.back_button.visible = False


    def scan(self, instance):
        self.send_message('scan')
    def send_web_request(self, instance):
        # Отправляем запрос на открытие веб-сайта
        data = self.text_input.text
        self.send_message(data)
        print('Opening website:', data)
        # Здесь можно добавить код для открытия веб-сайта
    def open_programs(self, instance):
        # Отправляем запрос на сервер для открытия программы
        self.send_message('open')
        # Отображаем всплывающее окно с кнопками для отправки запросов
        popup = Popup(title='Select Action', size_hint=(None, None), size=(400, 200))
        box = BoxLayout(orientation='vertical')

        # Кнопка для отправки запроса "Steam"
        button1 = Button(text='Steam', size_hint=(1, 0.5),   background_color= (0, 0.02, 0.1, 0.03) )
        button1.bind(on_press=lambda instance: self.send_message('Steam'))
        box.add_widget(button1)

        # Кнопка для отправки запроса "Microsoft Edge"
        button2 = Button(text='Microsoft Edge', size_hint=(1, 0.5),   background_color= (0.898, 0.71, 0.463, 1) )
        button2.bind(on_press=lambda instance: self.send_message('Edge'))
        box.add_widget(button2)

        # Кнопка для возвращения на главный экран
        back_button = Button(text='Back', size_hint=(1, 0.5),  background_color=(0.898, 0.71, 0.463, 1))
        back_button.bind(on_press=self.return_to_main_screen)
        box.add_widget(back_button)

        popup.content = box
        popup.open()

    def show_text_input(self, instance):
        self.send_message('web')
        # Отображаем поле для ввода текста (название сайта)
        self.clear_widgets()

        # Поле для ввода текста
        self.text_input = TextInput(text='', size_hint=(1, 0.1),  background_color=(0.898, 0.71, 0.463, 1))
        self.add_widget(self.text_input)

        # Кнопка для отправки запроса
        send_button = Button(text='Send Request', size_hint=(1, 0.2),  background_color=(0.898, 0.71, 0.463, 1))
        send_button.bind(on_press=self.send_web_request)
        self.add_widget(send_button)

        # Кнопка для возвращения на главный экран
        back_button = Button(text='Back', size_hint=(1, 0.2), background_color=(0.898, 0.71, 0.463, 1))
        back_button.bind(on_press=self.return_to_main_screen)
        self.add_widget(back_button)

    def return_to_main_screen(self, instance):
        self.send_message("close")
        # Очищаем текущий экран и добавляем кнопки "Open" и "Web"
        self.clear_widgets()
        self.add_widget(self.open_button)
        self.add_widget(self.web_button)
        self.add_widget(self.scan_button)

    def send_message(self, message):
        # Отправка сообщения через сокет
        self.client.send(message.encode("utf-8"))

    def send_web_request(self, instance):
        # Отправляем запрос на открытие веб-сайта
        data = self.text_input.text
        self.send_message(data)
        print('Opening website:', data)
        # Здесь можно добавить код для открытия веб-сайта

class MyApp(App):
    def build(self):
        self.title = 'Doppel'
        Window.clearcolor = (0.96, 0.87, 0.7) #red green blue contr
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()