FROM python:3.10

# Set the working directory in the container
WORKDIR /dock-api/

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Run the FastAPI application (fix typo here, 'apps' -> 'app')
CMD ["uvicorn", "app.main:apps", "--host", "0.0.0.0", "--reload"]

