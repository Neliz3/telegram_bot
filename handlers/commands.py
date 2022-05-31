from aiogram import types
from keyboards.menu_buttons import key_trouble
from keyboards.inline_buttons import key_ex, lang_guide
from DataBase.db_managing import delete_user, exist_user, add_user, get_source, get_target, update_word
from reverso_context_api import Client
from dependences import git_hub


# Starting a bot
async def welcome_command(message: types.Message):
    user_name = message.from_user.first_name
    user_id = int(message.from_user.id)
    if exist_user(user_id):
        delete_user(user_id)
        add_user(user_name, user_id)
    else:
        add_user(user_name, user_id)
    await message.answer(f"› Hi, {message.from_user.first_name}❗️"
                         "\n› I'm a Bot 😎"
                         "\n› I'll translate words for you ❤️"
                         "\n› Let's go❗️")
    await message.answer("Choose the language from which we will translate ⇩",
                         reply_markup=lang_guide)


# Getting information to user
async def help_command(message: types.Message):
    await message.answer(f"What happen, {message.from_user.first_name}❓")
    await message.answer("\n❓ How to change a language ☟"
                         "\n⤐⤐⤐Click /set_language"
                         "\n❓ Which commands I have ☟"
                         "\n⤐⤐⤐Click 'menu' button ⤦"
                         "\n❓ What resources were used for translation ☟"
                         "\n⤐Reverso Context ⤑ context.reverso.net"
                         "\n⤐Google Translate ⤑ translate.google.co.uk"
                         "\n❓ How to see a code ☟"
                         "\n⤐⤐⤐Click /git_hub"
                         #"\n❓ How to say 'thanks'\nor give any ideas ☟"
                         #"\n⤐Click /response"
                         "\n❓ How to be happy ☟"
                         "\n⤐⤐⤐smile :)")
                         #"\n❓ other problem... ☟"
                         #"\n⤐⤐⤐Click /complain"


# Translating giving words
def get_translations(data: str, self, source_lang, target_lang):

    r = self._request_translations(data, source_lang, target_lang, target_text=None)
    contents = r.json()

    block = ''
    for entry in contents["dictionary_entry_list"]:
        block += entry["term"] + " | "
    return block


# Translating giving sentences
def get_translation_samples(data: str, user_id):

    # Initialize client and language
    source_lang = get_source(user_id)
    target_lang = get_target(user_id)
    self = Client(source_lang, target_lang)

    iterate = next(self._translations_pager(data))
    count = 0
    output = ''
    for entry in iterate["list"]:
        source_text, translation = entry["s_text"], entry["t_text"]
        source_text = self._cleanup_html_tags(source_text)
        translation = self._cleanup_html_tags(translation)

        output += ''.join(source_text) + '\n' + ''.join(translation) +\
                  '\n    ⇜⇜⇜😎⇝⇝⇝    \n'
        count += 1
        if count == 3:
            break
    return output


# Launching translation
async def choice_func(message: types.Message):

    # Initialize client and language
    source_lang = get_source(message.from_user.id)
    target_lang = get_target(message.from_user.id)
    self = Client(source_lang, target_lang)

    data = str(message.text)
    try:
        await message.answer(get_translations(data, self, source_lang, target_lang), reply_markup=key_trouble)
        await message.answer(f'☞    <{data}> ⤸', reply_markup=key_ex)
        update_word(message.from_user.id, data)

    # If no data is found
    except Exception as _ex:
        a = get_source(message.from_user.id)
        b = get_target(message.from_user.id)

        # Generating a link to google translator
        if ' ' in data:
            link = f'https://translate.google.co.uk/?sl={a}&tl={b}&op=translate'
        else:
            link = f'https://translate.google.co.uk/?sl={a}&tl={b}&text={data}&op=translate'
        await message.answer("Sorry, I can't find the translation 😝"
                             "\nAnyway, you can find it here ☟"
                             f"\n{link}")
        print("[INFO] Error with finding translation", _ex)


# Instruction of using a bot
async def get_instruction(message: types.Message):
    await message.answer("❌ Send me word/phrase like 'believe in'"
                         "\n❌ Then click <How to use it 🧐>"
                         "\nto see examples of using that"
                         "\n❌ Click /help if you have any questions")


# Link to a source code on GitHub
async def git_hub_account(message: types.Message):
    await message.answer(f"Here you can see a source code of a project ☟"
                         f"#\n {git_hub}")


def list_handlers(dp):
    dp.register_message_handler(welcome_command, commands=['start', 'set_language'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(get_instruction, commands=['instruction', 'I_have_a_little_problem_😝'])
    dp.register_message_handler(git_hub_account, commands=['git_hub'])
    dp.register_message_handler(choice_func)
