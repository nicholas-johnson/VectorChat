# Vector Chat

## Installation

the Vector SDK is quite old and has some very specific requirements. Suggested installation is via conda and the env file:

    conda env create -f environment.yml
    conda activate vector_chat

## Manual installation

Manual Installation is possible via pip, but you will run into the following issues:

The Anki Vector SDK is only compatible with Python 3.8 (possibly 3.75). Higher than this will cause an error with a loop parameter in AsyncIO. It's also not compatible with newer versions of Protobuff. Do not attempt to upgrade past 3.20.1.

```
pip3 install openai
pip3 install protobuf==3.20.1
pip3 install anki_vector
pip3 install sounddevice
```

## Open AI Key

Go to Open AI https://platform.openai.com/account/api-keys and generate an API key. Rename the file config_example.py to config.py. Paste your API key into the correct place in the file.

## Robot certs

You need SSH keys to connect with your robot. If you have previously set up a Wirepod, you should find a folder called .anki_vector in your home directory. Ensure this folder is available on the machine you want to run vector chat.

For example, I have Wirepod running on a Raspberry Pi 4. I have Vector Chat running on a MacBook. I copy ~/.anki_vector from my pi to the ~/.anki_vector on my Macbook.

Inside this folder, you will find two files:

- sdy_config.yml - you may need to edit this to set the correct path to the cert in your usernames are different between devices
- [vectorname].cert - this is the actual cert that gives you access to Vector. This file is precious, don't lose it or share it.

## Running

    python src/main.py

The app will attempt to connect to your vector five times. If you get a timeout exception on your Vector, try again. Note you must be running a Wirepod hacked vector to connect the SDK to the machine. If your vector works with Wirepod, it should also work with Vector Chat.
