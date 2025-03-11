# Конфигурация Home Assistant 

![Home Assistant](https://github.com/alexfrydr/home_assistant_config/blob/master/screen1.JPG)

Содержит конфигурацию для моего проекта домашней автоматизации. Значительное количество конфигураций на самом деле хранятся
в базе данных homeassistant и, следовательно, здесь не показаны.

## Что интересного:
- [Голосовое управление через Яндекс станции.](https://github.com/dext0r/yandex_smart_home)
- Автоматическое управление подсветкой.
- Автоматическое управление освещением в [ванной](https://github.com/alexfrydr/home_assistant_config/blob/master/includes/automation/005_bathroom.yaml), [прихожей](https://github.com/alexfrydr/home_assistant_config/blob/master/includes/automation/007_Light_hallway.yaml) и [складом](https://github.com/alexfrydr/home_assistant_config/blob/master/includes/automation/034_stock_light.yaml). 
- Автоматическое управление [вентиляцией](https://github.com/alexfrydr/home_assistant_config/blob/master/includes/automation/005_bathroom.yaml).
- Автоматическое управление [домофоном](https://github.com/alexfrydr/home_assistant_config/blob/master/includes/automation/025_intercom.yaml).
- Автоматическое управление увлажнителем.
- Автоматическая уборка.
- Автоматическая установка темы.
- Управление будильником.
- Управление умными колонками и телевизором.
- Упрвление умным домом через [telegramm](https://github.com/alexfrydr/home_assistant_config/blob/master/includes/packages/001_telegramm.yaml).
- Оповещение о протечках воды [ванная и кухня](https://github.com/alexfrydr/home_assistant_config/blob/master/includes/automation/006_Water_sensor.yaml) с временным отключением.
- Оповещение о наличии дыма на кухне.
- Оповещение о открытой входной двери больше 5 минут.
- Оповещения что я в домашней зоне.
- Отправка видео с входной двери в случае нарушения периметра.
- Отправка уведомлений telegramm.
- Список покупок.

## Что еще нужно доделать:
- Управление зонами уборки.
- Мягкий свет и аварийное освещение.
- Автоматическое закрытие вентилей воды в случаии аварии.
- Управление климатом.
- Передача геоданных устройств.
- Автоматизация охраны.
- Панель управления для детей.

## Аппаратное обеспечение:
- Выключатель TuYa TS0011
- Выключатель Aqara E1
- Датчик протечки Aqara water leak sensor
- Датчик открытия Mi door and window sensor
- Датчик движения Aqara motion sensor
- Датчик температуры и влажности Aqara temperature and humidity sensor
- Датчик температуры esp8216 + DS18B20
- Беспроводная кнопка Aqara wireless mini switch
- Беспроводной кубик Aqara Cube 
- Контроллер открытия  домофона Matrix intercom auto opener
- Контроллер управления адресной лентой WLED ESP8266
- Беспроводная розетка Xiaomi Mi Smart Power Plug
- Робот пылесос Xiaomi Mi 1C
- Увлажнитель воздуха Mijia Smart Sterilization Humidifier S

## Supervisor add-ons

Я использую [Supervised install](https://www.home-assistant.io/getting-started/) со следующими дополнениями:

- [Advanced SSH & Web Terminal](https://github.com/hassio-addons/addon-ssh) by @hassio-addons
- [ESPHome](https://github.com/esphome/) version 2024.3.1 by @esphome
- [File editor](https://github.com/home-assistant/addons/tree/master/configurator) by @home-assistant
- [Home Assistant Google Drive Backup](https://github.com/sabeechen/hassio-google-drive-backup) by @sabeechen
- [Let's Encrypt](https://github.com/home-assistant/addons/tree/master/letsencrypt) by @home-assistant
- [MariaDB](https://github.com/home-assistant/addons/tree/master/mariadb) by @home-assistant
- [Mopidy](https://github.com/bestlibre/hassio-addons/tree/master/mopidy) by @bestlibre
- [Mosquitto broker](https://github.com/home-assistant/addons/tree/master/mosquitto) by @home-assistant
- [NGINX Home Assistant SSL proxy](https://github.com/home-assistant/addons/tree/master/nginx_proxy) by @home-assistant
- [Studio Code Server](https://github.com/hassio-addons/addon-vscode) by @hassio-addons
- [Vaultwarden (Bitwarden)](https://github.com/hassio-addons/addon-bitwarden) by @hassio-addons
- [Zigbee2MQTT](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt/tree/master/zigbee2mqtt) by @zigbee2mqtt
- [Zigbee2MQTT Edge](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt/tree/master/zigbee2mqtt-edge) by @zigbee2mqtt

## Некоторые скриншоты

Уведомление в телеграмм о протечке.

![Home Assistant](https://github.com/alexfrydr/home_assistant_config/blob/master/img/Screenshot_50.png)

Статус системы после перезагрузки и вызов меню.

![Home Assistant](https://github.com/alexfrydr/home_assistant_config/blob/master/img/Screenshot_51.png)

Оповещение о звонке в дверь.

![Home Assistant](https://github.com/alexfrydr/home_assistant_config/blob/master/img/Screenshot_52.png)

Оповещение о том что я домашней зоне.

![Home Assistant](https://github.com/alexfrydr/home_assistant_config/blob/master/img/Screenshot_54.png)

Автоматическая постановка в режим охраны если дома никого нет.

![Home Assistant](https://github.com/alexfrydr/home_assistant_config/blob/master/img/Screenshot_55.png)

Оповещение о звонке в домофон и возможности открытия или сброса звонка.

![Home Assistant](https://github.com/alexfrydr/home_assistant_config/blob/master/img/Screenshot_56.png)

🏡🔧📱💡🚪🚿🛋️🔌
