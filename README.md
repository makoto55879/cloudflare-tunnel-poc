# cloudflare-tunnel-poc

Raspberry Pi 5 上で FastAPI + Cloudflare Named Tunnel を使って外部公開する PoC リポジトリです。

## 構成

```
.
├── app/
│   ├── Dockerfile        # FastAPI コンテナのビルド定義
│   ├── main.py           # FastAPI アプリ本体
│   └── data/             # アップロードファイルの保存先（git 管理外）
├── docs_site/            # ナレッジドキュメントサイト（HTML）
├── docker-compose.yml    # FastAPI + cloudflared の起動定義
├── .env.example          # 環境変数のサンプル（.env をコピーして使用）
└── .gitignore
```

## セットアップ

### 1. リポジトリをクローン

```bash
git clone https://github.com/makoto55879/cloudflare-tunnel-poc.git
cd cloudflare-tunnel-poc
```

### 2. 環境変数を設定

```bash
cp .env.example .env
nano .env  # CLOUDFLARE_TUNNEL_TOKEN を設定
```

Cloudflare ダッシュボード → Zero Trust → Networks → Tunnels → 対象トンネル → Configure からトークンを取得してください。

### 3. Cloudflare ダッシュボードで Public Hostname を設定

Tunnels → 対象トンネル → Public Hostname タブ：

| Subdomain | Domain | Service |
|---|---|---|
| `api` | `your-domain.com` | `http://api:8000` |

### 4. コンテナを起動

```bash
sudo docker compose up -d
```

### 5. 疎通確認

```bash
curl https://api.your-domain.com/ping
# → {"message":"pong"}
```

## エンドポイント

| メソッド | パス | 説明 |
|---|---|---|
| `GET` | `/ping` | 疎通確認 |
| `POST` | `/upload` | ファイルアップロード |

## ドキュメント

`docs_site/` ディレクトリの `index.html` をブラウザで開くと、ナレッジサイトを参照できます。

## Phase 履歴

| Phase | 内容 | 状態 |
|---|---|---|
| Phase 1-1 | Raspberry Pi 5 セットアップ + Docker 環境構築 | 完了 |
| Phase 1-2 | FastAPI コンテナ作成 + Quick Tunnel で外部公開確認 | 完了 |
| Phase 1-3 | Cloudflare Named Tunnel 設定 | 完了 |
| Phase 1-4 | DNS 移管（Squarespace → Cloudflare）+ Named Tunnel 本番稼働 | 完了 |
