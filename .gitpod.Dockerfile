FROM gitpod/workspace-python-3.11

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN echo 'export PATH="/root/.local/bin:$PATH"' >> ~/.bashrc