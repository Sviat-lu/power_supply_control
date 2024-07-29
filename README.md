# Проект "Power supply control"
Сервис позволяет управлять источником питания через API. В качестве интерфейса используется FastAPI Swagger. <br>
[Ссылка на документацию ИП](https://www.gwinstek.com/en-global/products/downloadSeriesDownNew/18109/2090)

## Запуск:
> *Предполагается, что перед запуском проекта у пользователя уже установлены Docker и Git*
1. Скопировать репозиторий на локальный компьютер, выполнив команду:

```
git clone https://github.com/lisSobaka/power_supply_control
```

2. Перейти в директорию проекта, выполнив команду:
```
cd power_supply_control
```
3. Запустить сервис, выполнив команду:
```
source start.sh
```
4. Для остановки сервиса нажать в терминале сочитание клавиш Ctrl+C или выполнить команду:
```
source stop.sh
```

#### Проект будет развёрнут по адресу http://localhost:8000/docs/ <br><br>