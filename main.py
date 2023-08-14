from elevenlabs import set_api_key
from elevenlabs import voices, generate, play
import os
import openai
openai.api_key = ("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")

set_api_key("98cfe093485bf42de7faecbd361eaaf2")

voices = voices()

messages =[{"role": "system", "content": "Your name is Master Chief, also known as John-117."}]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    #print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

    audio = generate(
        text=reply,
        voice="oaCr9QCE9XvkD117OnVy",
        model="eleven_multilingual_v1"
    )

    print(f'Master Chief: {reply}')
    play(audio)
