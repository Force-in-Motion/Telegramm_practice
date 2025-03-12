from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


class KeyBoards:

    grade = ('1', '2', '3', '4', '5')

    @staticmethod
    def create_reply_keyboard():
        """
        Создает клавиатуру обычных кнопок, возвращающих текст
        """
        builder = ReplyKeyboardBuilder()

        builder.button(text='Оставить отзыв')
        builder.button(text='Показать отзывы')
        builder.button(text='Сохранить в csv')

        return builder.as_markup(resize_keyboard=True)


    @staticmethod
    def create_inline_kb():
        """
        Создает клавиатуру инлайн кнопок, возвращающих колбэк
        """
        builder = InlineKeyboardBuilder()

        for btn in KeyBoards.grade:

            builder.button(text=btn, callback_data=btn)

        return builder.as_markup(resize_keyboard=True)

