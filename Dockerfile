FROM python:latest AS builder

# 安裝 Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# 設定工作目錄
WORKDIR /app

# 複製程式碼到容器中
COPY . /app

# 安裝專案依賴項
RUN poetry install --no-dev

# 執行測試指令
CMD ["poetry", "run", "pytest", "--continue-on-collection-errors", "--html=pytest-report.html", "--self-contained-html"]