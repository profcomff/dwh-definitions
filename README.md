# dwh-definitions

Библиотека, описывающая структуру всех баз данных профкома ФФ. Реализована с помощью разделения всех баз данных в 4 категории - [STG](https://github.com/profcomff/dwh-definitions/blob/main/profcomff_definitions/STG/README.md), [DWH](https://github.com/profcomff/dwh-definitions/blob/main/profcomff_definitions/DWH/README.md), [ODS](https://github.com/profcomff/dwh-definitions/blob/main/profcomff_definitions/ODS/README.md) и [DM](https://github.com/profcomff/dwh-definitions/blob/main/profcomff_definitions/DM/README.md).

[<img src="https://cdn.profcomff.com/easycode/easycode.svg" width="200"></img>](https://easycode.profcomff.com/templates/docker-airflow/workspace?mode=manual)

## Функционал
- Удобное и структурированное хранение данных
- Разграничение и удобное управление правами доступа

## Разработка
- Backend разработка – https://github.com/profcomff/.github/wiki/%5Bdev%5D-Backend-разработка
- Работа с данными -https://github.com/profcomff/.github/wiki/%5Bdev%5D-Работа-с-данными

## Quick start
1. Перейдите в папку проекта
2. Создайте виртуальное окружение командой:
```commandline
python3 -m venv ./venv/
```
3. Установите библиотеки
```commandline
pip install -r requirements.txt
```

## Использование
В своих базах данных мы используем postgres базы данных. Для того чтобы использовать данный репозиторий необходимо сделать несколько предварительных шагов
1. Проделай пункты из "Как начать работу локально" отсюда: https://github.com/profcomff/dwh-airflow
2. Склонируй этот репозиторий на свой компьютер командой `git clone https://github.com/profcomff/dwh-definitions`
3. Создай виртуальное окружение Python. Для этого нужно:
    - Установить python3.11 (если еще не установлен): https://www.python.org/downloads/
    - Установить pip (если еще не установлен, команда в консоли `python -m ensurepip --upgrade`)
    - Создать в папке `dwh-definitions` новое виртуальное окружение python3.11 (команда в консоли `python3.11 -m venv venv` или `python -m venv venv`)
    - Подключиться к этому виртуальному окружению (команда консоли на windows: `venv\Scripts\activate.bat`, на мак/линукс: `source venv/bin/activate`)
    - Установить библиотеки командой `pip install -U -r requirements.dev.txt -r requirements.txt`

    Теперь у тебя на компьютере есть база данных, Airflow, описание базы данных в виде питона

4. Обнови схему базы данных командой `alembic upgrade head`. Это создаст в базе данных все те же таблицы, что есть в production базе данных.

5. После этого в папках из /ddl можно создавать свои схемы таблиц. Пример таблицы можно посмотреть в /ddl/STG/union_member.py


### Дальнейшие шаги:

Рассмотрим дальнейшие действия на примере тестовой таблицы Test. Допустим, что она лежит в /ddl/STG/test_table.py

1. Импортировать созданную таблицу в \_\_init__.py файл соответствующей папки. В нашем случае в /ddl/STG/\_\_init__.py необходимо дописать строчку:
```python
from .test_table import Test
```
2. В строчку c \_\_all__ = [] необходимо добавить название импортированной таблицы в кавычках. В нашем случае файл \_\_init__.py будет выглядеть так:
```python
from .test_table import Test

__all__ = ["Test"]
```
3. Если у вас несколько таблиц, то в \_\_all__ их надо перечислять через запятую. К примеру:
```python
from .test_file_first import TestFirst, TestTrird
from .test_file_second import TestSecond

__all__ = ["TestFirst", "TestSecond", "TestTrird"]
```
При этом порядок перечисления таблиц в \_\_all__ не важен

4. После импортирования всех таблиц проведите миграцию, чтобы создались новые таблицы. Миграцию можно провести командами:
```commandline
alembic revision --autogenerate -m "название_вашей_миграции"
alembic upgrade head
```
Перва команда создает ревизию - скрипт для перехода на новую версию базы данных.
Вторая команда обновляет базу данных (в данном случае создает новую таблицу Test)

## Параметризация и плагины
Никаких настроек кроме стандартных нет

## Ссылки
- Backend разработка – https://github.com/profcomff/.github/wiki/%5Bdev%5D-Backend-разработка
- Работа с данными -https://github.com/profcomff/.github/wiki/%5Bdev%5D-Работа-с-данными
