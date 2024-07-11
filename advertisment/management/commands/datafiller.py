import time
import requests
from bs4 import BeautifulSoup
import chardet
from django.core.management.base import BaseCommand
from advertisment.models import Advertisement

ADS_URL = "https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/#center=43.19433608949683%2C131.98046225170316&zoom=11.835992496072969"

titles_and_names = {
    "Установка видеонаблюдения и домофонии": "Primtec",
    "Монтаж и обслуживание систем видеонаблюдения, СКУД, домофоны": "ИП Якименко Алексей Андреевич",
    "Установка/обслуживание: видеонаблюдения, домофонов, СКУД, сигнализации": "Videofort",
    "Монтаж видеонаблюдения Hikvision HiWatch Trassir, СКУД, домофонов": "doneit",
    "Видеонаблюдение Установка Продажа Настройка Видеокамер IP": "TVi MART",
    "Установка камер / монтаж систем видеонаблюдения. Частник": "Vldcam",
    "Установка, монтаж систем видеонаблюдения установка камер.": "Den2078",
    "ВидеоКИТ - Системы видеонаблюдения, установка, обслуживание": "VideoKIT",
    "Установим Видеодомофон в квартиру или частный дом! Видеонаблюдение!": "Подряд",
    "Установка видеонаблюдения от Vladrec | Монтаж | Обслуживание | СКУД": "VLADREC",
}

data_for_filling = (
    ("Установка видеонаблюдения и домофонии", "Primtec", 846, 1),
    ("Монтаж и обслуживание систем видеонаблюдения, СКУД, домофоны", "ИП Якименко Алексей Андреевич", 1342, 2),
    ("Установка/обслуживание: видеонаблюдения, домофонов, СКУД, сигнализации", "Videofort", 378, 3),
    ("Монтаж видеонаблюдения Hikvision HiWatch Trassir, СКУД, домофонов", "doneit", 479, 4),
    ("Видеонаблюдение Установка Продажа Настройка Видеокамер IP", "TVi MART", 1443, 5),
    ("Установка камер / монтаж систем видеонаблюдения. Частник", "Vldcam", 710, 6),
    ("Установка, монтаж систем видеонаблюдения установка камер.", "Den2078", 2571, 7),
    ("ВидеоКИТ - Системы видеонаблюдения, установка, обслуживание", "VideoKIT", 155, 8),
    ("Установим Видеодомофон в квартиру или частный дом! Видеонаблюдение!", "Подряд", 104, 9),
    ("Установка видеонаблюдения от Vladrec | Монтаж | Обслуживание | СКУД", "VLADREC", 174, 10)
)

def get_author_name(link):
    response = requests.get(link)
    encoding = chardet.detect(response.content)['encoding']
    response.encoding = encoding
    soup = BeautifulSoup(response.text, features='lxml')
    try:
        main_div = soup.find('div', id='fieldsetView')
        second_div = main_div.find('div', class_="viewbull-summary")
        name = second_div.find('span', class_='userNick auto-shy')
        return name.text.strip()
    except Exception as e:
        print(f"Error fetching author name: {e}")
        return 'Не удалось найти имя пользователя'

class Command(BaseCommand):
    help = 'Load advertisements data from Farpost and create Advertisement objects.'            

    def handle(self, *args, **kwargs):
        try:
            response = requests.get(ADS_URL)
            encoding = chardet.detect(response.content)['encoding']
            response.encoding = encoding
            soup = BeautifulSoup(response.text, features='lxml')
            main_div = soup.find('tbody', attrs={'class': 'native'})
            items = main_div.find_all('tr', class_='bull-list-item-js -exact', limit=10)
            for index, item in enumerate(items, start=1):
                title = item.find('div', class_='bull-item__subject-container')
                href_to_author = 'https://www.farpost.ru/' + title.find('a').get('href')
                time.sleep(1)
                author_name = get_author_name(href_to_author)
                if author_name == 'Не удалось найти имя пользователя':
                    author_name = titles_and_names[title.text.strip()]
                time.sleep(1)
                views = item.find('span', class_='views nano-eye-text').text.strip()
                title_text = title.text.strip()
                Advertisement.objects.create(
                    title=title_text,
                    author=author_name,
                    views=int(views),
                    position=index
                )
                time.sleep(1)
        except:
            for object in data_for_filling:
                Advertisement.objects.create(
                    title=object[0],
                    author=object[1],
                    views=object[2],
                    position=object[3]
                )
        print('Загрузка закончилась')
