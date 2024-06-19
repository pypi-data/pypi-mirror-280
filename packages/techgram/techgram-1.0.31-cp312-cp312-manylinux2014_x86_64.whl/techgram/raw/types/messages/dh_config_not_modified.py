#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from techgram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from techgram.raw.core import TLObject
from techgram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class DhConfigNotModified(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~techgram.raw.base.messages.DhConfig`.

    Details:
        - Layer: ``158``
        - ID: ``C0E24635``

    Parameters:
        random (``bytes``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: techgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDhConfig
    """

    __slots__: List[str] = ["random"]

    ID = 0xc0e24635
    QUALNAME = "types.messages.DhConfigNotModified"

    def __init__(self, *, random: bytes) -> None:
        self.random = random  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DhConfigNotModified":
        # No flags
        
        random = Bytes.read(b)
        
        return DhConfigNotModified(random=random)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.random))
        
        return b.getvalue()
