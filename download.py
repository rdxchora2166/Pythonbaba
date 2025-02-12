from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from pytubefix import YouTube

class MyApp(App):
    def build(self):
        # Create a BoxLayout to hold the widgets
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create a label
        self.label = Label(text="Enter YouTube URL:")

        # Create a text input for the YouTube URL
        self.url_input = TextInput(hint_text="Paste YouTube URL here", multiline=False)

        # Create a button to start the download
        download_button = Button(text="Download Video")
        download_button.bind(on_press=self.download_video)

        # Add widgets to the layout
        layout.add_widget(self.label)
        layout.add_widget(self.url_input)
        layout.add_widget(download_button)

        return layout

    def download_video(self, instance):
        # Get the URL from the text input
        url = self.url_input.text.strip()

        if not url:
            self.label.text = "Please enter a valid YouTube URL."
            return

        try:
            # Initialize YouTube object
            yt = YouTube(url)
            # Get the highest resolution stream
            ys = yt.streams.get_highest_resolution()
            # Download the video
            ys.download()
            self.label.text = f"Downloaded: {yt.title}"
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

if __name__ == "__main__":
    MyApp().run()
