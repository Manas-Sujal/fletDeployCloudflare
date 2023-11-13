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
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    label=ft.Text(value=f"", color="green")
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    def dwnloadmp4(e):
        label.value=""
        page.update()
        #dest="C:/Users/admin/Downloads"
        YouTube(new_task.value).streams.get_highest_resolution().download(dest)
        label.value=f"Downloaded on {dest}"
        page.update()


    def dwnloadmp3(e):
        label.value=""
        page.update()
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
        label.value=f"Downloaded on {dest}"
        page.update()

    
    new_task = ft.TextField(hint_text="What is to be downloaded?", width=300)
    #page.window_width=500
    #page.window_height=200
    page.add(#ft.Column(
        #[
         new_task,
         ft.Row([ft.ElevatedButton("Download mp3", on_click=dwnloadmp3),
         ft.ElevatedButton("Download mp4", on_click=dwnloadmp4)],alignment=ft.MainAxisAlignment.CENTER),
         label#],
        
       # )
        )
    page.update()



ft.app(target=main)
