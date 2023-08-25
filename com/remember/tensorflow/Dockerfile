FROM tensorflow/tensorflow:2.13.0 AS base
RUN python -V && \
    pip list && \
        pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

FROM base AS run
WORKDIR /app
COPY . .
CMD ["sh", "-c", "python app.py"]
