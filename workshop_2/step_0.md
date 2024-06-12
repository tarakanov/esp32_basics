1. Установить удобный редактор кода - VS Code или Sublime

2. Установить python3 и менеджер пакетов pip3:
   - python3 - https://www.python.org/downloads/
   - pip3  - скорее всего уже установился с python3. Проверить можно через `pip3 --version` (набирать в консоли). Если команда выдала версию pip3, то все ОК. Иначе - гуглим как поставить pip3 (например, тут - https://www.activestate.com/resources/quick-reads/how-to-install-and-use-pip3/)

3. Установить пакет esptool и mpremote через `pip3 install esptool, mpremote` (два пакета через запятую)

4. Подключить плату esp32 devkit к ноуту и проверить, что поднялся порт:
  - Для Windows - COM1
  - Для macOS - /dev/tty.usbserial-0001
  - Для Debian/Ubuntu - /dev/ttyUSB0

Если порт не поднялся, то возможно проблемы с драйверами USB-UART конвертера на плате. Скорее всего конвертор - CP2102. Драйвера можно установить по инструкциям:
  - Для Windows - https://myrobot.ru/downloads/driver-cp2102-esp32.php
  - Для macOS - https://randomnerdtutorials.com/install-esp32-esp8266-usb-drivers-cp210x-mac-os/
  - Для Debian/Linus - драйвера уже включены в операционную систему.

5. Залить на esp32 прошивку с micropython:
  - Скачать прошивку из репозитория - https://micropython.org/download/ESP32_GENERIC/
  - Подсоединить esp32 devkit к компьютеру через microUSB
  - Стереть внутреннюю флеш - `esptool.py -p /dev/tty.usbserial-0001 erase_flash`
  - Залить свежую прошивку - `esptool.py -p /dev/tty.usbserial-0001 -b 460800 write_flash -z 0x1000  ./ESP32_GENERIC-20240105-v1.22.1.bin`
  - Перезагрузить esp32 (по питанию или нажать кнопку `EN`)
  
6. Подключиться к оболочке micropython:
  - Подсоединить esp32 devkit к компьютеру через microUSB
  - Открыть порт через программу mpremote - `mpremote`
  - Нажать `Enter` до появления строки приглашения оболочки - `>>>`
  - Выполнить простейшие команды на python. Полезная функция - `help()`
  - Выйти из оболочки можно через - `control-A` + `contorl-X` на macOS и Debian или `ctrl-C` на Windows
  - Другие команды для `mpremote` - https://docs.micropython.org/en/latest/reference/mpremote.html

7. Другие команды, которые понадобятся на мастерклассе
  - Закачать файл внутрь esp32 - `mpremote cp mqtt_example_ssl.py :main.py` - копирует файл `mqtt_example_ssl.py` на esp32 и переименовывает в `main.py`