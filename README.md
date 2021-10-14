## 使い方
- pic内にinputに圧縮したい画像を配置する(JPGのみ)
- 下に沿ってコマンドを実行する
- pic内のoutputに圧縮した画像が配置される(完了)



### コマンド
1. `docker-compose up -d --build`
2. `docker-compose exec python3 bash`
3. `cd src`
4. `python3 compress.py`


### streamlitを動かす場合
1. `pip install streamlit Pillow`
3. `streamlit run src/app.py`

### Todo
* [ ] streamlitでダウンロード追加
* [ ] 複数ファイルへの対応
* [ ] pipenvで動かした際にアップロードができるように変更