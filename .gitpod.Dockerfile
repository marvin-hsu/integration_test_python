FROM python:latest

# 安裝Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN echo 'export PATH="/home/gitpod/.local/bin:$PATH"' >> ~/.bashrc