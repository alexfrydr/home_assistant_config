# Конфигурация Home Assistant 

![Home Assistant](https://github.com/alexfrydr/home_assistant_config/blob/master/screen1.JPG)

Содержит конфигурацию для моего проекта домашней автоматизации. Значительное количество конфигураций на самом деле хранятся
в базе данных homeassistant и, следовательно, здесь не показаны.

## Что интересного:
- Голосовое управление через Яндекс станции.
- Автоматическое управление подсветкой.
- Автоматическое управление освещением в ванной, прихожей и складом.
- Автоматическое управление вентиляцией.
- Автоматическое управление домофоном.
- Автоматическое управление увлажнителем.
- Автоматическая уборка.
- Автоматическая установка темы.
- Управление будильником.
- Управление умными колонками и телевизором.
- Упрвление умным домом через telegramm.
- Оповещение о протечках воды ванная и кухня.
- Отключение оповещения о протечках не отключая автоматизацию 
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

- [Advanced SSH & Web Terminal](https://github.com/hassio-addons/addon-ssh) version 17.2.0 by @hassio-addons
- [ESPHome](https://github.com/esphome/) version 2024.3.1 by @esphome
- [File editor](https://github.com/home-assistant/addons/tree/master/configurator) version 5.8.0 by @home-assistant
- [Home Assistant Google Drive Backup](https://github.com/sabeechen/hassio-google-drive-backup) version 0.112.1 by @sabeechen
- [Let's Encrypt](https://github.com/home-assistant/addons/tree/master/letsencrypt) version 5.0.18 by @home-assistant
- [MariaDB](https://github.com/home-assistant/addons/tree/master/mariadb) version 2.7.1 by @home-assistant
- [Mopidy](https://github.com/bestlibre/hassio-addons/tree/master/mopidy) version 0.2.7 by @bestlibre
- [Mosquitto broker](https://github.com/home-assistant/addons/tree/master/mosquitto) version 6.4.0 by @home-assistant
- [NGINX Home Assistant SSL proxy](https://github.com/home-assistant/addons/tree/master/nginx_proxy) version 3.9.0 by @home-assistant
- [Studio Code Server](https://github.com/hassio-addons/addon-vscode) version 5.15.0 by @hassio-addons
- [Vaultwarden (Bitwarden)](https://github.com/hassio-addons/addon-bitwarden) version 0.21.1 by @hassio-addons
- [Zigbee2MQTT](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt/tree/master/zigbee2mqtt) version 1.37.1-1 by @zigbee2mqtt
- [Zigbee2MQTT Edge](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt/tree/master/zigbee2mqtt-edge) version edge by @zigbee2mqtt

🏡🔧📱💡🚪🚿🛋️🔌
