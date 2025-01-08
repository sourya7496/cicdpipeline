import streamlit as st
import time

def text_generator():
    sentence="Please keep the song playing!"
    for i in range(len(sentence)):
        yield sentence[i]
        time.sleep(0.1)


def text_1():
    sentence="I know you will never talk to me. I have done mistakes, I know. I have some clarification points but\
        nothing matters at all. I know you are gone, and you will never come back. I could not do much for you\
            and I know this last gift would not be anything to you."
    for i in range(len(sentence)):
        yield sentence[i]
        time.sleep(0.08)

def text_2():
    sentence="I always had trust issues and I was never able to trust you. Within me, I really do want you, \
        but I do not know, I am weird. Deep in my mind, I always thought you are too pretty and many men\
             would look at you, where as I cannot. What if you go away one day to all these men? \
                What if you are with one of them when I am not around? Thoughts killed me all the time.\
                    But we had some amazing memories"
    for i in range(len(sentence)):
        yield sentence[i]
        time.sleep(0.08)

def text_3():
    sentence="It is true, I will never find someone like you. I was sick, tired and lonely here. I had no friends\
         like you, no one to travel around like you did, and I am still struggling with career. I have nothing\
            with me. Also, trying to validate myself was wrong, I know. It is all my fault, I am the bad person.\
            I hope someday, I will come out of the loneliness, if I stay alive. You will never know this side \
                of the pain. I really miss us, and I know you wont believe, I crave for you now. Well, these\
                    pictures serve as my memory."
    for i in range(len(sentence)):
        yield sentence[i]
        time.sleep(0.08)

def text_4():
    sentence="Finally, a good bye to you. Bhalo thakis! Jani na tui ar kotha bolbi kina, but you have always\
        asked tor jonne kichu korte pari kina. Dekh, ajke ekta website o baniye fellam. Bye! And take care!"
    for i in range(len(sentence)):
        yield sentence[i]
        time.sleep(0.08)

st.set_page_config(page_title="Suryani", page_icon="❤️")
st.title("Suryani, I am sorry!")
st.write_stream(text_generator())
st.audio("song.mp4", format="audio/mp4")

st.write_stream(text_1())
st.image('Zoom_in\Zoom_in\IMG-20220422-WA0015.jpg',caption='You and your next! :D', use_container_width=True)
time.sleep(5)

st.write_stream(text_2())
st.image('Zoom_in\Zoom_in\IMG_20220421_204830.jpg',caption='Just me and you <3', use_container_width=True)
time.sleep(2)
st.image('Zoom_in\Zoom_in\IMG_20220223_193034.jpg',caption='Wish we could be together like this', use_container_width=True)
time.sleep(2)
st.image('Zoom_in\Zoom_in\IMG_20220731_192414.jpg',caption=':)', use_container_width=True)
time.sleep(2)

st.write_stream(text_3())
st.image('Zoom_in\Zoom_in/IMG_20220710_131929.jpg',caption='Newtown memory', use_container_width=True)
time.sleep(2)
st.image('Zoom_in\Zoom_in/IMG_20220716_185432.jpg',caption='Howrah Bridge memory', use_container_width=True)
time.sleep(2)
st.image('Zoom_in\Zoom_in/IMG_20220815_201835.jpg',caption='Independence Day memory', use_container_width=True)
time.sleep(2)

st.write_stream(text_4())
st.image('Zoom_in\Zoom_in/Screenshot_2021-11-28-22-19-29-268_com.whatsapp.jpg',caption='Initial Vcalls', use_container_width=True)
time.sleep(3)

st.write("Good Bye! You can close the page.")
