# JARVO: A Simple Voice Assistant

JARVO is a Python-based voice assistant that uses text-to-speech and speech recognition to interact with users. It can listen to voice commands, respond with pre-defined messages, and perform basic tasks like greeting users and exiting on command.

---

## Features

- **Speech Recognition:** Listens to user commands via microphone input.
- **Text-to-Speech:** Responds to user queries with synthesized voice output.
- **Interactive Commands:**
  - Responds to "hello" with a friendly greeting.
  - Exits the loop when "exit" is said.
  - Provides a polite default response for unrecognized commands.

---

## Requirements

Ensure you have the following Python libraries installed:

- `pyttsx3`: For text-to-speech synthesis.
- `speech_recognition`: For processing microphone input and converting it into text.

You can install these libraries using pip:
```bash
pip install pyttsx3 speechrecognition
