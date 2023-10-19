FROM python:3.9-slim
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install fastapi uvicorn supabase google-auth PyDrive python-dotenv
COPY ./ /code/
EXPOSE 8000
# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]