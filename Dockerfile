FROM python:3.8-slim

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY app.py /app/app.py

CMD streamlit run app.py

