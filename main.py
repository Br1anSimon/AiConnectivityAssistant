from elevenlabs import set_api_key
from elevenlabs import voices, generate, play
import openai
from whisper_mic.whisper_mic import WhisperMic
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings

openai.api_key = ("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")

set_api_key("98cfe093485bf42de7faecbd361eaaf2")

voices = voices()

mic = WhisperMic()
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)


messages =[{"role": "system", "content": "Your name is Master Chief, also known as John-117."}]
chat_completion = ""
talking = mic.listen()

while True:

    message = input("User: " + talking)
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    reply = chat_completion.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

    audio = generate(
        text=reply,
        voice="oaCr9QCE9XvkD117OnVy",
        model="eleven_multilingual_v1"
    )

    print(f'Master Chief: {reply}')
    play(audio)
