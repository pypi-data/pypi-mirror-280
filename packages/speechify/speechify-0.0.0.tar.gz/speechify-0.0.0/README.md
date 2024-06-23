# Unofficial module of the TTS Speechify tool.

## Install

```bash
pip install speechify
```

# List of voices

| DisplayName | Name | Gender | Engine | Language |
| --- | --- | --- | --- | --- |
| John | john | male | speechify | en-US |
| MrBeast | mrbeast | male | speechify | en-US |
| Snoop Dogg | snoop | male | resemble | en-US |
| Gwyneth Paltrow | gwyneth | female | speechify | en-US |
| Nate | nate | male | speechify | en-US |
| Stephanie | stephanie | female | speechify | en-GB |
| Jael | iselin | female | azure | nb-NO |
| Oskar | finn | male | azure | nb-NO |
| Caterina | pernille | female | azure | nb-NO |
| Olena | polina | female | azure | uk-UA |
| Dmytro | ostap | male | azure | uk-UA |

# Example usage

```py
# Import the Speechify API class
from speechify import SpeechifyAPI

# Create an instance of the Speechify API
speechify_api = SpeechifyAPI()

# Get a list of available client voices
client_voices = speechify_api.get_client_voices()
print("Available client voices:", client_voices)

# Define a paragraph of text to convert to speech
paragraph = "Hello, how are you?"

# Generate an audio file for the paragraph using the "mrbeast" voice, "speechify" engine, and "en-US" language
audio_file = speechify_api.generate_audio_files(paragraph, "mrbeast", "speechify", "en-US")
print("Generated audio file:", audio_file)
```