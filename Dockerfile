FROM python:3.9

WORKDIR /app

# Копіюємо файли залежностей та код
COPY requirements.txt ./
COPY telegram_chatgpt_bot.py ./

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Встановлюємо модель мови ChatGPT
RUN python -c "from transformers import pipeline; generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')"

CMD [ "python", "./telegram_chatgpt_bot.py" ]
