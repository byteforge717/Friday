from modules.speech_input import listen
from modules.speech_output import speak
from modules.intent_handler import parse_intent
from modules.task_executor import execute_task

def friday_main():
    speak("Hello, I am Friday. How can I help?")
    while True:
        command = listen()
        intent = parse_intent(command)
        execute_task(intent)

if __name__ == "__main__":
    friday_main()