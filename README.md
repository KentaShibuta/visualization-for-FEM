# 計算格子の可視化プログラム
## できること
* 計算格子の形状の可視化ができる．
    + 現在は2次元での可視化のみ．
    + (3次元での可視化機能は開発中)
## 入力ファイル
* 節点座標のデータ
    + csv形式
    + 節点番号と節点座標のx成分,y成分
![計算格子_節点](https://gyazo.com/4077f5a32d5c1aa4fdb67086cfa07158/raw)
* 要素と節点の依存関係のデータ
    + csv形式
    + 要素番号, 節点0の節点番号, 節点1の節点番号, 節点2の節点番号, 節点3の節点番号
![計算格子_要素と節点の関係](https://gyazo.com/8162c13fea78554b4e8e366d5a5f6298/raw)
## 実行方法
* 可視化プログラムを実行
    + `python visualization_culculation.py`
* "Input node file name >>>>"に続けて，節点座標のデータが記述されたファイルのパスを入力．
* "Input nbool file name >>>>"に続けて，要素と節点の依存関係を示すデータが記述されたファイルのパスを入力．
* 実行例
![実行例](https://gyazo.com/5c5a0c1a2f222659b5228cc1afa3c9aa/raw)
