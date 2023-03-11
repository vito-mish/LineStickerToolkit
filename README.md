# LineStickerToolkit

A command-line tool for converting Line stickers into various image formats.

## Install

```shell
pip install -r requirements.txt
```

## Run project

```shell
python main.py
```

## Project tree

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
│   │       └── input.png
│   └── outputs
│       ├── full-command.txt
│       └── images
│           ├── cropped_1.png
│           ├── cropped_2.png
│           ├── cropped_3.png
│           └── cropped_4.png
├── main.py
├── merge.py
├── modules
├── png_separator.py
└── requirements.txt
```

## Dev note

TODO: 自動亂選 8 (01 ~ 08) + 2 (main + tab)
TODO: 自動亂選 16、24、32、40
TODO: 使用說明

https://pixlr.com/tw/e/
