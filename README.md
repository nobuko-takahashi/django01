### ポートフォリオ（django01）

#### 機能

- ログイン＆ログアウト（ログイン後遷移前のパスのリダイレクト）

- 新規会員登録（確認画面あり）

- パスワードとメルアドの変更

- 川柳参照

- 川柳投稿（会員のみ、確認画面あり）

#### 設置方法

Anacondaをセットアップし、環境を作ってcloneしたフォルダ「django01」をコピペしてください。

以下は例としてAnacondaのWindows版のインストールサイトです。

https://www.python.jp/install/anaconda/windows/install.html


開発した環境は以下のようなちょっと高めのバージョンですが、これより多少低くても動くと思います。

    Python:3.9.12

    Django:4.0.4        
  
#### 【重要】SECRET_KEYの設置について
clone直後のdjango01/config/settings.pyにある「SECRET_KEY」は空白となっています。

(設置環境により違いがあります)/django01/config/generate_secretkey_setting.pyを実行して、実行結果として表示されたキーをsettings.pyに設定します。

```python (設置環境により違いがあります)/django01/config/generate_secretkey_setting.py```

※上記を実行すると、実行結果として「SECRET_KEY = 'ランダムなキー'」が返ってきます。
