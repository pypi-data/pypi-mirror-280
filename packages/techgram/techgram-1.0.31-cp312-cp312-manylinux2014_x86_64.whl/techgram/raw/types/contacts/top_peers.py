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


class TopPeers(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~techgram.raw.base.contacts.TopPeers`.

    Details:
        - Layer: ``158``
        - ID: ``70B772A8``

    Parameters:
        categories (List of :obj:`TopPeerCategoryPeers <techgram.raw.base.TopPeerCategoryPeers>`):
            N/A

        chats (List of :obj:`Chat <techgram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <techgram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: techgram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetTopPeers
    """

    __slots__: List[str] = ["categories", "chats", "users"]

    ID = 0x70b772a8
    QUALNAME = "types.contacts.TopPeers"

    def __init__(self, *, categories: List["raw.base.TopPeerCategoryPeers"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.categories = categories  # Vector<TopPeerCategoryPeers>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TopPeers":
        # No flags
        
        categories = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return TopPeers(categories=categories, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.categories))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
