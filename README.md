# Vector Chat

## Installation concerns

The Anki Vector SDK is only compatible with Python 3.8. Higher than this will cause an arror with a loop parameter in AsyncIO. It's also not compatible with newer versions of Protobuff. Do not attempt to upgrade

```
pip3 install openai
pip3 install protobuf==3.20.1
pip3 install anki_vector
```

For audio capture (OSX)

```
brew install portaudio 
pip3 install --no-binary :all: pyaudio
```