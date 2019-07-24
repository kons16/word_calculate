# word_calculate
茨城大学工学部オープンキャンパスで使うためのデモプログラムです.  
単語同士の足し算引き算, 類似単語の表示をブラウザ上で試すことができます.  


## 使い方
Python用WebフレームワークであるFlaskが導入されている環境で,  
`main.py`を実行し, ブラウザ上でURLを開いてください.  
URLはssh先サーバーで実行している場合, `http://{ssh先のip address}:{ポート番号}`になります.
ローカルの場合は, `http://0.0.0.0:{ポート番号}`です.  

単語の分散表現を得るために`main.py`の`model_path`をword2vecのモデルが置いてある  
適切なパスに置き換える必要があります.  


## 注意事項
cssが読み込まれない場合はブラウザのキャッシュを削除してから再度実行してください.  