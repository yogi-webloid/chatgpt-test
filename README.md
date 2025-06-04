# chatgpt-test

これはゲーミフィケーション要素を取り入れたタスク管理ツールのサンプルです。

## 使い方

Python 3 が必要です。以下のコマンドでタスクを管理できます。

### タスクの追加
```
python tasks.py add "タスク名" --points 5
```

### タスクの一覧表示
```
python tasks.py list
```

### タスクの完了
```
python tasks.py done <タスクID>
```

### 現在のポイント表示
```
python tasks.py status
```

## Web サーバーとして利用する

`webapp.py` を実行すると Flask ベースの簡易 API サーバーが起動します。

```
python webapp.py
```

デフォルトではポート `8000` で起動し、以下のエンドポイントが利用できます。

- `GET /tasks` タスク一覧を取得
- `POST /tasks` `{"name": "タスク名", "points": 5}` でタスクを追加
- `POST /tasks/<id>/done` 指定 ID のタスクを完了
- `GET /points` 現在のポイントを取得

## Docker を用いたデプロイ

Docker が利用可能な環境であれば、次のようにビルドして実行できます。

```bash
docker build -t gamified-tasks .
docker run -p 8000:8000 gamified-tasks
```

これによりコンテナ内でウェブサーバーが起動し、外部からアクセス可能になります。
