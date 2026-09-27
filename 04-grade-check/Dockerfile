FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY grade_check.py .
# run as a normal user, not root
RUN useradd appuser
USER appuser
CMD ["python", "grade_check.py"]
