
import openai
import anki_vector
import tkinter as tk

from action_list import ActionList
from action import Action
from action_list_watcher import ActionListWatcher
from recorder_window import RecorderWindow
from whisper_asr import WhisperASR 
from chat_completion import chat_completion
from text_conversation import TextConversation

def create_app():
    whisper_asr = WhisperASR()
    conversation = TextConversation()
    controller = VectorController()
    controller.connect()

    def on_transcription_ready(transcript):
        print(transcript['text'])
        conversation.add_message('USER: ' + transcript['text'])
        print(conversation.get_convo())
        completion = chat_completion(conversation.get_convo())
        answer = completion.choices[0].message.content
        print(answer)
        # action = Action(answer)
        # action_list.add_action(action)

    def on_recording_ready(file_path):
        # Send the recorded file to the OpenAI Whisper API to convert it to text
        # This is a placeholder for the actual API call
        # Replace it with the appropriate API call to obtain the transcript
        
        transcription = whisper_asr.transcribe(file_path)
        print(f"Transcription: {transcription}")
        on_transcription_ready(transcription)

    action_list = ActionList()
    action_list_watcher = ActionListWatcher(action_list, callback=lambda action: print(f"Executing action: {action.description}"))
    recorder_window = RecorderWindow(callback=on_recording_ready)

    recorder_window.run()
    action_list_watcher.stop()


if __name__ == "__main__":
    create_app()





# import openai
# import anki_vector
# import tkinter as tk

# from action_list import ActionList
# from action import Action
# from action_list_watcher import ActionListWatcher
# from recorder_window import RecorderWindow

# openai.api_key = "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"

# def main():
#     args = anki_vector.util.parse_command_args()

#     conversation = ''



#     with anki_vector.Robot(args.serial) as robot:
#         def handle_action(action):
#             print(f"Handling action: {action.description}")

#         def handle_human_input(text):
#             print(f"Human said: {text}")
#         action_list =  ActionList()
#         action_list_watcher = ActionListWatcher(action_list, callback=handle_action)
#         action_list.add_action(Action("Turn on the light"))
#         action_list.add_action(Action("Close the door"))
#         action_list.add_action(Action("Pick up the book"))

#         root = tk.Tk()
#         recorder_window = RecorderWindow(root, action_list, callback=create_action)
#         root.mainloop()

#     print('doe')
    

# if __name__ == "__main__":
#     main()
