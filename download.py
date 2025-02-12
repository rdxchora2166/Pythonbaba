import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import pytubefix as pytube


class YouTubeDownloader(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.label = Label(text="Enter YouTube URL:")
        self.add_widget(self.label)

        self.url_input = TextInput(hint_text="Paste video URL here", multiline=False)
        self.add_widget(self.url_input)

        self.download_button = Button(text="Download Video", on_press=self.download_video)
        self.add_widget(self.download_button)

        self.status_label = Label(text="")
        self.add_widget(self.status_label)

    def download_video(self, instance):
        url = self.url_input.text
        if not url:
            self.status_label.text = "Please enter a valid URL"
            return

        try:
            yt = pytube.YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            self.status_label.text = f"Downloaded: {yt.title}"
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"


class YouTubeDownloaderApp(App):
    def build(self):
        return YouTubeDownloader()


if __name__ == "__main__":
    YouTubeDownloaderApp().run()
