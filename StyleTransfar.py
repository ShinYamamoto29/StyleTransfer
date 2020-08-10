$ git clone https://github.com/lengstrom/fast-style-transfer.git
$ cd fast-style-transfer 

#https://drive.google.com/drive/folders/0B9jhaT37ydSyRk9UX0wwX3BpMzQ
#上記のリンクからファイルを所得する。


# from moviepy.video.io.VideoFileClip import VideoFileClip
# import moviepy.video.io.ffmpeg_writer as ffmpeg_writer

#evaluate.pyのファイルの13.14行目を上記のように変更（エラー防止のため）

$ python evaluate.py --checkpoint ./変更したいスタイルのファイル名  --in-path 変更したい画像名 --out-path ./出力画像名

