FROM python:latest

USER root

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN echo 'export PATH="/home/gitpod/.local/bin:$PATH"' >> ~/.bashrc
RUN source ~/.bashrc

# 安裝 Docker 的相依套件
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# 添加 Docker 的官方 GPG 金鑰
RUN curl -fsSL https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]')/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 設定 Docker 的 apt 庫
RUN echo \
    "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]') \
    $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# 安裝 Docker
RUN apt-get update && apt-get install -y docker-ce-cli

# 將 Gitpod 的默認使用者添加到 Docker 群組中
RUN usermod -aG docker gitpod

# 切換回 Gitpod 的默認使用者
USER gitpod