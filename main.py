from pytube import YouTube
from sys import argv
import os
from moviepy.editor import * 
import moviepy as mv
import flet as ft
from pathlib import Path
global dest
dest = str(Path.home() / "Downloads")


def main(page):
    def dwnload(e):
        '''link = new_task.value
        yt = YouTube(link)
        yd = yt.streams.get_highest_resolution()
        yd.download("C:/Users/admin/Downloads")
        page.add(ft.Text(value="Downloaded", color="green"))
        page.update()'''
        #dest="C:/Users/admin/Downloads"
        YouTube(new_task.value).streams.get_highest_resolution().download(dest)
        page.add(ft.Text(value="Downloaded", color="green"))
        page.update()


    def add_clicked(e):
        link = new_task.value
        yt = YouTube(link)
        yd = yt.streams.filter(only_audio=True).first()
        #dest="C:/Users/admin/Downloads"
        outfile = yd.download(output_path=dest)
        base = os.path.splitext(outfile)[0]
        new_file = base+ '.mp3'
        mp4_no_frame = AudioFileClip(outfile)
        mp4_no_frame.write_audiofile(new_file, logger=None)
        mp4_no_frame.close()
        os.remove(outfile)
        page.add(ft.Text(value="Downloaded", color="green"))
        page.update()

    
    new_task = ft.TextField(hint_text="What is to be downloaded?", width=300)
    #page.window_width=500
    #page.window_height=200
    page.add(ft.Row(
        [new_task,ft.ElevatedButton("Download mp3", on_click=add_clicked),ft.ElevatedButton("Download mp4", on_click=dwnload)],
        alignment=ft.MainAxisAlignment.CENTER
        )
        )
    page.update()



ft.app(target=main)