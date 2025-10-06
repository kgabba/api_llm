# LLM Agent API Prototype

Микросервис на FastAPI с LLM-агентом (LangChain + GPT), который взаимодействует с внутренней базой данных через инструменты.

## Стэк
- **API**: FastAPI
- **LLM**: LangChain, OpenAI GPT-4o-mini
- **Агент**: ReAct Agent с кастомными инструментами
- **Инфраструктура**: Docker, Python 3.11

## Эндпоинты
- **GET** / - проверка работы сервиса
- **GET** /db_list - просмотр содержимого БД
- **POST** /w_mess - добавление сообщения через агента
