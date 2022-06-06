from dependences import dp, index
from aiogram import types
from handlers import commands
from DataBase.db_managing import update_source, update_target, get_source, get_target, get_word
from keyboards.inline_buttons import lang_guide


# Callback of key_ex inline keyboard
@dp.callback_query_handler(text='get_example')
async def get_sentence(call: types.callback_query):
    if call:
        await call.answer("🥳🥳🥳")
        data = get_word(call.from_user.id)
        answer = commands.get_translation_samples(data, call.from_user.id)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("☟ Sentences, where it can be used ☟")
        await call.message.answer(answer)


# Determine which button was pressed
def find_index(value, call_data):
    for i in value:
        if i == call_data:
            return call_data


# Callback of lang_guide inline keyboard
@dp.callback_query_handler()
async def get_lang(call: types.callback_query):
    if find_index(index, call.data) == call.data:

        # Choosing source language
        if get_source(call.from_user.id) == 'ns':
            update_source(call.from_user.id, call.data)
            await call.message.delete()
            await call.message.answer(f"# You chose ⤳ {call.data}")
            await call.message.answer("Choose the language we will translate into ⇩",
                                      reply_markup=lang_guide)

        # Choosing target language
        elif get_target(call.from_user.id) == 'nt':
            if get_source(call.from_user.id) != call.data:
                update_target(call.from_user.id, call.data)
                await call.message.delete()
                await call.message.answer(f"# You chose ⤳ {call.data}")
                await call.message.answer("❌ Click /set_language to change your answers"
                                          "\n❌ Enter word/phrase like 'believe in' ⤥")

            else:
                # Check that the language is not repeated
                await call.message.answer(f"You chose ⤳ {call.data} earlier"
                                          f"\nchoose something else, please 😎")
