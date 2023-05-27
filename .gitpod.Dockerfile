FROM python:latest

# 安裝Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# 將項目代碼複製到工作目錄
WORKDIR /workspace
COPY . .

# 安裝項目依賴項
RUN poetry install