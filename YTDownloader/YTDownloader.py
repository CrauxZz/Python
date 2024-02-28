from tkinter import Label
from pytube import YouTube
import flet as ft
import os

def main(page):

    page.title = ("YouTube downloader")
    url = ft.TextField(label = "URL", autofocus = True)
    submit = ft.ElevatedButton("Download")

    page.add(ft.Text("Input the link to the video you want to download",
            size=20, color=ft.colors.WHITE,
            weight=ft.FontWeight.NORMAL,))
            
    def btn_click(e):
        current_folder = os.getcwd()
        yt = YouTube(url.value)
        video = yt.streams.get_highest_resolution()
        video.download(output_path = current_folder)


    submit.on_click = btn_click
    page.add(url, submit)

ft.app(target = main)

