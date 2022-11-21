# Retrieve latest ubuntu base image
FROM python:latest

# Create a directory inside the container
RUN mkdir -p /home/app

# Copy current folder files to /home/app
COPY . /home/app

# Set /home/app as working directory
WORKDIR /home/app

# Install the required libraries
RUN pip install -r requirements.txt

# Instruction to run the code
CMD ["python", "code.py"]