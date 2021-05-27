# 計算格子の可視化プログラム
2021.5.27 last updated
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
### 商用の可視化ソフトのフォーマットを使用の場合(microAVSでの可視化用ファイルなど)
* 「節点座標のデータ」と「要素と節点の依存関係のデータ」を取り出すための，シェルスクリプト(convert_inp_csv.sh)
    + 一例として，microAVSのフォーマット(inpファイル)から「節点座標のデータ」と「要素と節点の依存関係のデータ」を取り出す．
        + 「節点座標のデータ」が書かれている行を複数行まとめて`# mesh_start`と`# mesh_end`で囲む．
        + 同様に，「要素と節点の依存関係のデータ」が書かれている行を複数行まとめて`# nbool_start`と`# nbool_end`で囲む．
        + `sh convert_inp_csv.sh`で実行をして，inpファイルからデータのトリミングが行える．
## 実行方法
動作保証環境
* macOS 10.15.7
* Python 3.8.5
* Cython version 0.29.23
* matplotlib 3.3.1
cythonをインストール
* `pip3 install cython`
可視化プログラムを実行
* `cythonize -i visualization_culculation.pyx`
    + カレントディレクトリに.soファイルが生成される
* `python3 run.py`
    + "Input node file name >>>>"に続けて，節点座標のデータが記述されたファイルのパスを入力
    + "Input nbool file name >>>>"に続けて，要素と節点の依存関係を示すデータが記述されたファイルのパスを入力
### 実行例
![実行例](https://gyazo.com/5c5a0c1a2f222659b5228cc1afa3c9aa/raw)
