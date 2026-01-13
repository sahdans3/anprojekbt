from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def feedback_keyboard(normal=True):
    suffix = "" if normal else "_next"
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("👍 ", callback_data=f"like{suffix}"),
            InlineKeyboardButton("👎 ", callback_data=f"dislike{suffix}")
        ],
        [
            InlineKeyboardButton("⚠️ Report", callback_data=f"report{suffix}")
        ]
    ])
