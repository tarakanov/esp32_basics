1. Установить python3 и менеджер пакетов pip3:
   python - https://www.python.org/downloads/
   pip3  - python -m pip3 install

2. Установить пакет esptool и mpremote - pip3 install esptool, mpremote

3. Залить на esp32 прошивку с micropython:
  - Скачать прошивку из репозитория - https://micropython.org/download/ESP32_GENERIC/
  - Подсоединить esp32 devkit к компьютеру через microUSB
  - Стереть внутреннюю флеш - esptool.py -p /dev/tty.usbserial-0001 erase_flash
  - Залить свежую прошивку - esptool.py -p /dev/tty.usbserial-0001 -b 460800 write_flash -z 0x1000  ./ESP32_GENERIC-20240105-v1.22.1.bin
  - Перезагрузить esp32
  
4. Подключиться к оболочке micropython:
  - Подсоединить esp32 devkit к компьютеру через microUSB
  - Открыть порт через программу mpremote - mpremote
  - Выполнить простейшие команды на python. Полезная функция - help()