# ベースイメージ：Python 3.11 の軽量版（slim）を使用
FROM python:3.11-slim

# コンテナ内の作業ディレクトリを /app に設定
WORKDIR /app

# 必要な Python ライブラリをインストール
RUN pip install --no-cache-dir fastapi uvicorn[standard] python-multipart

# main.py をコンテナ内の /app にコピー
COPY main.py .

# コンテナ起動時に実行するコマンド
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
