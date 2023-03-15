from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont #dynamic import
import os

# 처리할 파일이 있는 폴더 경로
folder_path = 'venv/mov/w1'

# 폴더 내 모든 파일 경로 가져오기
files = os.listdir(folder_path)

# 폴더 내 AniGIF 파일을 프레임 별로 추출하여 각 파일로 저장
for file in files:
    if file.endswith('.gif'):
        # GIF 파일 로드
        clip = VideoFileClip(os.path.join(folder_path, file))

        # GIF 파일의 각 프레임을 개별 GIF 파일로 추출하여 저장
        frame_folder_path = os.path.join(folder_path, os.path.splitext(file)[0])
        os.makedirs(frame_folder_path, exist_ok=True)
        duration = 1 / clip.fps  # 한 프레임당 표시되는 시간
        for i, frame in enumerate(clip.iter_frames()):
            frame_clip = ImageClip(frame, duration=duration)
            frame_clip.write_gif(os.path.join(frame_folder_path, f"{i:04}.gif"), fps=clip.fps)

# GIF 파일을 PNG로 변환하기.

for n in range(1, 26):
    folder_path = 'venv/mov/w1/'+str(n)
    files = os.listdir(folder_path)
    for file in files:
        if file.endswith('.gif'):

            path = 'venv/mov/w1'+'/'+str(n)+'/'+f"{os.path.splitext(file)[0]:04}.gif"
            pngimg = Image.open(path)
            pngimg.save('venv/mov/w1'+'/'+str(n)+'/'+f"{os.path.splitext(file)[0]:04}.png")

# GIF파일만 지우기

for n in range(1, 26):
    folder_path = 'venv/mov/w1/' + str(n)
    files = os.listdir(folder_path)
    for file in files:
        if file.endswith('.gif'):
            os.remove(folder_path+'/'+file)

