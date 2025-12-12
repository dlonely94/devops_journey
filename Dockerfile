FROM python:3.9-slim
WORKDIR /app
COPY system_monitor.py .
RUN pip install flask psutil jsonify
CMD ["python", "system_monitor.py"]
