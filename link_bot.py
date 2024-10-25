import asyncio
import telebot.async_telebot as telebot
from telebot import types
import os
from dotenv import (
    load_dotenv,
    find_dotenv
)

load_dotenv(
    find_dotenv()
)

ADMIN = os.getenv('ADMIN')
ADMIN_LINK = os.getenv('ADMIN_LINK')
REFERRAL_LINK = os.getenv('REFERRAL_LINK')

bot = telebot.AsyncTeleBot(
    token=os.getenv("BOT_TOKEN")
)

@bot.message_handler(commands=['start'])
async def start(message):
    keyboard = types.InlineKeyboardMarkup(
        row_width=1
    )
    permanent_access_button = types.InlineKeyboardButton(
        text="800$ Lifetime 🏆",
        callback_data="permanent"
    )
    monthly_access_button = types.InlineKeyboardButton(
        text="150$ Monthly ⏰",
        callback_data="monthly"
    )
    free_7_days_button = types.InlineKeyboardButton(
        text="14 DAYS FREE TRIAL✅",
        callback_data="trial"
    )
    keyboard.add(
        permanent_access_button,
        monthly_access_button,
        free_7_days_button
    )
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=open(f"resources/choose_plan.jpg", "rb"),
        caption="<b>🏷️Choose your tariff plan!</b>\n\n"
                "You have opportunity to join <b>Premium channel</b> and bet on my <b>personal and insiders signals.🤑</b>",
        parse_mode="HTML",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call:True)
async def callback_inline(call):
    if call.data == "trial":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        register_button = types.InlineKeyboardButton(
            text="REGISTRATION🧑‍💻",
            url=f"{REFERRAL_LINK}"
        )
        verify_button = types.InlineKeyboardButton(
            text="VERIFY REGISTRATION ✅",
            callback_data="verify_registration"
        )
        keyboard.add(
            register_button,
            verify_button
        )
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=open(f"resources/trial.jpg", "rb"),
            caption="<b>Well done, you have chosen the 14 days free trial✅</b>\n\n"
                 "To activate the <b>Free Trial</b>, you need to:\n\n"
                 '🧑‍💻Click on <b>"REGISTRATION"</b> and register on <b>22BET</b>\n\n'
                    'Use promo code <b>“KNIGHT”</b> to get your <b>WELCOME BONUS🎁</b>\n\n'
                 '🔍 Then click on <b>"Verify Registration"</b>.',
            parse_mode='HTML',
            reply_markup=keyboard
        )
    if call.data == "verify_registration":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        send_id_button = types.InlineKeyboardButton(
            text="SEND YOUR ID 🪪",
            url=f"{ADMIN}"
        )
        keyboard.add(
            send_id_button
        )
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=open(f"resources/send_id.jpg", "rb"),
            caption="<b>Great,We almost done ✅</b>\n\n"
                 "Now you need to send me your <b>ACCOUNT ID</b>\n\n"
                 "Then I'll forward you the link to the <b>Premium Channel</b> with my personal bets, and your <b>Welcome BONUSES 🎁</b>",
            parse_mode='HTML',
            reply_markup=keyboard
        )
    if call.data == "monthly":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        send_screenshot_button = types.InlineKeyboardButton(
            text="SEND SCREENSHOT 📲",
            url=f"{ADMIN_LINK}"
        )
        keyboard.add(
            send_screenshot_button
        )
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=open(f"resources/qr.jpg", "rb"),
            caption="<b>Great!👍🏻</b>\n"
                    "you choose monthly tariff plan access to <b>“Knight Premium”</b>✅\n\n"
                    "<b>Now you need to make a transfer🏦</b>\n\n"
                    "Amount - <b>150$</b>\n\n"
                    "Network: <b>TRC20</b>\n"
                    "💸 - \n<code>TBUM2bdza8NrepggwsfFHToHfqAAztYc2W</code>\n\n"
                    "Or just scan <b>QR CODE☝️</b>\n\n"
                    "<b>After payment send me screenshot</b>",
            parse_mode='HTML',
            reply_markup=keyboard
        )
    if call.data == "permanent":
        keyboard = types.InlineKeyboardMarkup(
            row_width=1
        )
        send_screenshot_button = types.InlineKeyboardButton(
            text="SEND SCREENSHOT 📲",
            url=f"{ADMIN_LINK}"
        )
        keyboard.add(
            send_screenshot_button
        )
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=open(f"resources/qr.jpg", "rb"),
            caption="<b>Great!👍🏻</b>\n"
                    "you choose lifetime tariff plan access to <b>“Knight Premium”</b>✅\n\n"
                    "<b>Now you need to make a transfer🏦</b>\n\n"
                    "Amount - <b>800$</b>\n\n"
                    "Network: <b>TRC20</b>\n"
                    "💸 - \n<code>TBUM2bdza8NrepggwsfFHToHfqAAztYc2W</code>\n\n"
                    "Or just scan <b>QR CODE☝️</b>\n\n"
                    "<b>After payment send me screenshot</b>",
            parse_mode='HTML',
            reply_markup=keyboard
        )

async def main():
    # await on_startup()
    await bot.polling(none_stop=True)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot Shut Down")