FROM python:latest
WORKDIR /app
COPY requirments.txt /app
RUN pip install -r requirments.txt
COPY app.py /app
EXPOSE 5000
CMD ["python", "app.py"]