#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.
import pyrogram
from typing import Optional

from ..object import Object
from .inline_keyboard_button import _parse_style, _write_style

from pyrogram import raw

class InlineKeyboardButtonBuy(Object):
    """One button of the inline keyboard.
    For simple invoice buttons.

    Parameters:
        text (``str``):
            Text of the button. If none of the optional fields are used, it will be sent as a message when
            the button is pressed.

        style (``str``, *optional*):
            Optional button style. Can be one of ``"primary"``, ``"danger"`` or ``"success"``.
            If omitted, Telegram uses an app-specific style.
    """

    def __init__(
        self,
        text: str,
        style: Optional[str] = None
    ):
        super().__init__()

        self.text = str(text)
        self.style = style

    @staticmethod
    def _parse_style(style):
        return _parse_style(style)

    def _write_style(self):
        return _write_style(self.style)

    @staticmethod
    def read(b):
        return InlineKeyboardButtonBuy(
            text=b.text,
            style=InlineKeyboardButtonBuy._parse_style(getattr(b, "style", None))
        )

    async def write(self, _: "pyrogram.Client"):
        return raw.types.KeyboardButtonBuy(
            text=self.text,
            style=self._write_style()
        )
