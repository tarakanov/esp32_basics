1. Клиенты MQTT для мастеркласса:
	- MQTTX приложение для Win/mac/Linux - https://mqttx.app
	- MQTTX веб-приложение (не требует установки) - http://mqtt-client.emqx.com
	- MQTT Cool веб-приложение (работает через VPN) - https://testclient-cloud.mqtt.cool
	- Мобильное приложение. Например, MQTTAnalyzer (iOS) и MyMQTT (Android)

2. Создаем подключение (см. скриншоты `step_1_1.png`, `step_1_2.png`). Параметры подключения:
	- Адрес брокера - `broker.emqx.io`
	- Порт - `1883`
	- Без логина/пароля
	- Без SSL

3. Отправляем сообщение (Publish, см. скриншоты `step_1_3.png`):
	- В поле Topic (Destination) указываем наш чат - `esp32_basics`
	- В поле сообщения - набираем сообщение
	- Отправляем
	- Если вы не подписаны на этот чат, то никакой реакции не заметите

4. Подписываемся на наш чат (Subscribe, см. скриншот `step_1_4.png`, `step_1_5.png`):
	- Нажимаем New Subscription
	- В качестве Topic указываем `esp32_basics`
	- В качестве QoS указываем либо 0, либо 1
	- После подписки к вам будут приходить все сообщения отправленные в этот чат