# csvstat

![test](https://github.com/uruchi884/robosys2026/actions/workflows/test.yml/badge.svg)

[日本語](#日本語) | [English](#english)

## 日本語

### 概要

`csvstat` は、標準入力から受け取った CSV の指定列について、数値の基本統計量を計算するコマンドです。ロボットのセンサーログなど、CSV 形式の数値データを簡単に確認できます。

### 動作環境

- Python 3.8 以上
- Linux などの Unix 系環境
- GitHub Actions でのテスト環境: Ubuntu 26.04、Python 3.10〜3.14

### 使い方

列番号は **1 から始まる番号**で指定します。

```sh
$ chmod +x csvstat
$ printf 'time,value\n0,10\n1,20\n2,30\n' | ./csvstat 2 --header
{"count": 3, "min": 10.0, "max": 30.0, "mean": 20.0, "rms": 21.602468994692867}
```

### 引数

- `column`: 集計する列番号（1 始まり）
- `--header`: CSV の先頭行をヘッダーとして読み飛ばす

### 出力

成功時は、標準出力に JSON 形式で次の値を出力します。

- `count`: 数値データの件数
- `min`: 最小値
- `max`: 最大値
- `mean`: 算術平均
- `rms`: 二乗平均平方根

入力に数値以外の値がある場合、指定列が存在しない場合、または数値データが 1 件もない場合は、エラーメッセージを標準エラー出力に出して終了コード 2 で終了します。空行は読み飛ばします。

### テスト

```sh
$ bash ./test.bash
```

## English

### Overview

`csvstat` calculates summary statistics for one numeric column in CSV data read from standard input. It is useful for quickly checking numeric logs, such as robot sensor measurements.

### Requirements

- Python 3.8 or later
- A Unix-like environment such as Linux
- GitHub Actions test environment: Ubuntu 26.04, Python 3.10–3.14

### Usage

The column number is **1-based**.

```sh
$ chmod +x csvstat
$ printf 'time,value\n0,10\n1,20\n2,30\n' | ./csvstat 2 --header
{"count": 3, "min": 10.0, "max": 30.0, "mean": 20.0, "rms": 21.602468994692867}
```

### Arguments

- `column`: 1-based column number to analyze
- `--header`: Skip the first CSV row

### Output

On success, the command writes a JSON object to standard output containing:

- `count`: Number of numeric values
- `min`: Minimum value
- `max`: Maximum value
- `mean`: Arithmetic mean
- `rms`: Root mean square

Invalid or missing numeric data is reported to standard error, and the command exits with status 2. Empty rows are ignored.

### Tests

```sh
$ bash ./test.bash
```

## 著作権・ライセンス・謝辞

- Copyright (c) 2026 Hayashi Masayuki
- このソフトウェアは BSD 3-Clause License の下で公開します。詳細は [LICENSE](LICENSE) を参照してください。
- 実装には Python の標準ライブラリ `argparse`、`csv`、`json`、`math`、`sys` を使用しています。
- 参考資料: [ロボットシステム学 第3回](https://tarolab-cit.github.io/lectures/robosys2026/lecture03.html)（標準入出力）、[第5回](https://tarolab-cit.github.io/lectures/robosys2026/lecture05.html)（著作権・ライセンス）、[第6回](https://tarolab-cit.github.io/lectures/robosys2026/lecture06.html)（テスト）、[第7回](https://tarolab-cit.github.io/lectures/robosys2026/lecture07.html)（GitHub Actions・README）。
- `csvstat` は独自に作成したコマンドであり、講義資料のコードを転用していません。

## License and Acknowledgements

- Copyright (c) 2026 Hayashi Masayuki
- Licensed under the BSD 3-Clause License. See [LICENSE](LICENSE).
- The implementation uses Python standard-library modules: `argparse`, `csv`, `json`, `math`, and `sys`.
- Reference materials: [Robotics Systems Lecture 3](https://tarolab-cit.github.io/lectures/robosys2026/lecture03.html) (standard input/output), [Lecture 5](https://tarolab-cit.github.io/lectures/robosys2026/lecture05.html) (copyright and licenses), [Lecture 6](https://tarolab-cit.github.io/lectures/robosys2026/lecture06.html) (testing), and [Lecture 7](https://tarolab-cit.github.io/lectures/robosys2026/lecture07.html) (GitHub Actions and README).
- `csvstat` is an original command and does not copy code from the lecture slides.
