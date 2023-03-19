# LineStickerToolkit

This project is an assistant tool to help you quickly generate Line stickers.

## Requirements

This project requires Python 3.8 or later to run. You can download the latest version of Python from the [official website](https://www.python.org/downloads/).

## Installation

python

```shell
pip install -r requirements.txt
```

## Run Project

```shell
python main.py
```

## User Guide

1. 從網路上找一張適合的圖片，複製連結並取代 assets/inputs/command/prefix.txt 中的圖檔連結。（以下「貓」做例子）
2. 於 assets/inputs/command/chatGPT.txt，將第一句改為「做一款主題是貓的 LINE 貼圖」
3. 於 assets/inputs/command/suffix.txt，「... is a dog, with dog ears ...」改為貓
4. 複製 assets/inputs/command/chatGPT.txt 全部內容，請 `chatGPT` 生成新的 cases
5. 將新生成的 cases 複製並取代 assets/inputs/command/body.txt 所有內容
6. 執行 `python main.py` 輸入「1」合併成完整的 command
7. 到 `Midjourney` (discord) 用生成好的 command 生成圖片，並依序下載
8. 將所有圖片放到 assets/inputs/images/ 目錄底下
9. 執行 `python main.py` 輸入「2」執行切分腳本
10. 可以選擇手動挑選圖片，或執行 `python main.py` 輸入「p1」~「p3」自動隨機選取官方指定數量
11. 手動編輯圖片
    1. 去背：https://express.adobe.com/zh-Hant-TW/tools/remove-background
    2. 用無痕視窗開啟 https://pixlr.com/tw/e/ 上文字

## Directory Structure

```
├── README.md
├── assets
│   ├── inputs
│   │   ├── command
│   │   │   ├── body.txt
│   │   │   ├── chatGPT.txt
│   │   │   ├── prefix.txt
│   │   │   └── suffix.txt
│   │   └── images
│   │       ├── README.md
│   │       ├── **.png
│   └── outputs
│       └── images
├── main.py
├── modules
│   ├── __init__.py
│   ├── config.py
│   ├── init.py
│   ├── scripts
│   │   ├── __init__.py
│   │   ├── cleaner.py
│   │   ├── merge.py
│   │   ├── png_auto_pack.py
│   │   └── png_separator.py
│   ├── theme.py
│   └── utils.py
└── requirements.txt
```
