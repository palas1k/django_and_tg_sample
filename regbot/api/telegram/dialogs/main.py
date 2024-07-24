import logging

from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const

logger = logging.getLogger(__name__)


class MainStateGroup(StatesGroup):
    main = State()


main_window = Dialog(
    Window(
        Const(
            "*Создайте профиль и добавьте канал*\n"
            "Чтобы начать использовать бота, сделайте @SlonRobot администратором в "
            "канале, а затем пришлите сюда ссылку на канал или просто перешлите из него "
            "любое сообщение.\n"
            " Боту можно не выдавать никаких прав. Данная процедура нужна чтобы "
            "подтвердить, что вы являетесь владельцем канала.\n"
            " Другие полезные команды:\n"
            " \t/partners — сгенерировать уникальный промокод, чтобы вы могли приглашать "
            "других пользователей и получать бонусы\n"
            "\t/help — связь со службой поддержки и ответы на часто задаваемые вопросы"
        ),
        state=MainStateGroup.main,
        parse_mode="Markdown",
    ),
)
