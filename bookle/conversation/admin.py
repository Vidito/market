from django.contrib import admin
from .models import Conversation, ConversationMessage
# Register your models here.

admin.register(Conversation)

admin.register(ConversationMessage)