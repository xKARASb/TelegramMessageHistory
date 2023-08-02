from routers.commands import *
from routers.on_message import *
from routers.on_delete import on_delete
from routers.on_edit import on_edit

class Commands:
    add_chat = add_chat
    remove_chat = remove_chat

class OnMessage:
    text_message = on_text_message
    sticker = on_sticker
    animation = on_animation
    audio = on_audio
    doc = on_doc
    photo = on_photo
    video = on_video
    voice = on_voice

class OnDelete:
    delete = on_delete

class OnEdit:
    edit = on_edit