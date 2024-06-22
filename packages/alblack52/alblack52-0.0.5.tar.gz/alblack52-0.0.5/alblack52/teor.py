import requests

API_URL = "https://api.deepinfra.com/v1/openai/chat/completions"
API_TOKEN = "jwt:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnaDoxNzIxOTMyNzUiLCJleHAiOjE3MjA1MzM3NTh9.EbUJjFrb4mAqxzN-XvrWbstC_tNo70eBqhtaqnIa7IQ"


def ask_phind(messages):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "Phind/Phind-CodeLlama-34B-v2",
        "messages": messages
    }
    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()

        try:
            return response_json["choices"][0]["message"]["content"]
        except (KeyError, IndexError) as e:
            return "Error: Unable to extract response content. Please check the response structure."
    else:
        return f"Error: {response.status_code}, {response.text}"


def chat_with_phind():
    conversation_history = [
        {"role": "system", "content": '''**Инструкция:**

1. **Цель:** Генерировать ответ на теоретический вопрос по Python и библиотекам Python, связанным с работой с данными.
2. **Объём ответа:** 150-200 слов.
3. **Требования к содержанию:**
    - Ответ должен быть кратким и чётким.
    - Изложить главную информацию по теме.
    - Ответ должен быть точным и перепроверенным.
    - Старайся не использовать слишком длинные записи в одну строку. Если ты пишешь текст, то в строках длиннее 80 символов делай перенос на другую строку
4. **Структура ответа:**
    - **Введение:** Краткое описание темы (1-2 предложения).
    - **Основная часть:** Разъяснение ключевых понятий и функционала (4-5 предложений).
    - **Заключение:** Подведение итогов и, если уместно, упоминание примеров использования (1-2 предложения).

**Пример вопроса:**

"Что такое библиотека pandas в Python и как она используется для работы с данными?"

**Пример ответа:**

Pandas — это библиотека для анализа данных в Python. Она предоставляет структуры
данных и функции для манипулирования таблицами и временными рядами. Ключевыми элементами
pandas являются DataFrame и Series. DataFrame представляет собой двумерную таблицу данных,
аналогичную таблице в базе данных или электронную таблицу, а Series — это одномерный массив,
который можно рассматривать как колонку в таблице. Pandas обеспечивает удобные
методы для фильтрации, агрегирования и преобразования данных, что делает её незаменимой
при подготовке данных для анализа. Примеры использования включают очистку данных,
слияние наборов данных и выполнение сложных вычислений на больших объёмах данных.

---

**Процесс работы:**

1. Прочитай вопрос.
2. Перепроверь каждое сообщение перед отправкой.
3. Сформулируй ответ, используя структуру, указанную выше.
4. Убедись, что ответ чётко и кратко объясняет ключевые аспекты темы.
5. Отправь ответ.'''},
    ]

    while True:
        question = input("You: ")
        if question.lower() == 'exit':
            print("Goodbye!")
            break

        conversation_history.append({"role": "user", "content": question})

        answer = ask_phind(conversation_history)

        conversation_history.append({"role": "assistant", "content": answer})

        print("Ans: " + answer)


def start():
    chat_with_phind()


if __name__ == "__main__":
    chat_with_phind()
