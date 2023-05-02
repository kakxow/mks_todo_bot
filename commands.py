import telegram
from telegram.ext import MessageHandler, Filters
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.helpers import escape_markdown


inline_keyboard_markup_mark_complete = {
    "inline_keyboard": [
        [
            {
                "text": "✅ Выполнить",
                "callback_data": "complete",
            }
        ]
    ]
}
inline_keyboard_markup_unmark_complete = {
    "inline_keyboard": [
        [
            {
                "text": "Выполнено",
                "callback_data": "not_complete",
            }
        ]
    ]
}


def _mark_complete(update, context):
    text = update.effective_message.text
    if text:
        new_text = escape_markdown(f"~{text}~", version=2)
        context.bot.editMessageText(
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id,
            text=new_text,
            parse_mode=telegram.constants.PARSEMODE_MARKDOWN_V2,
            reply_markup=inline_keyboard_markup_unmark_complete,
        )
    else:
        context.bot.editMessageReplyMarkup(
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id,
            reply_markup=inline_keyboard_markup_unmark_complete,
        )


def _unmark_complete(update, context):
    text = update.effective_message.text
    if text:
        new_text = escape_markdown(text.strip("~"), version=2)
        context.bot.editMessageText(
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id,
            text=new_text,
            parse_mode=telegram.constants.PARSEMODE_MARKDOWN_V2,
            reply_markup=inline_keyboard_markup_mark_complete,
        )
    else:
        context.bot.editMessageReplyMarkup(
            chat_id=update.effective_chat.id,
            message_id=update.effective_message.message_id,
            reply_markup=inline_keyboard_markup_mark_complete,
        )


start = MessageHandler(
    Filters.chat_type.channel & (~Filters.update.edited_channel_post), _unmark_complete
)
mark_complete = CallbackQueryHandler(_mark_complete, pattern="complete")
unmark_complete = CallbackQueryHandler(_unmark_complete, pattern="not_complete")
