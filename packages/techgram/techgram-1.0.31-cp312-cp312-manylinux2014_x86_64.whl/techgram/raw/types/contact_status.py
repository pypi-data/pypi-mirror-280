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


class ContactStatus(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~techgram.raw.base.ContactStatus`.

    Details:
        - Layer: ``158``
        - ID: ``16D9703B``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        status (:obj:`UserStatus <techgram.raw.base.UserStatus>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: techgram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetStatuses
    """

    __slots__: List[str] = ["user_id", "status"]

    ID = 0x16d9703b
    QUALNAME = "types.ContactStatus"

    def __init__(self, *, user_id: int, status: "raw.base.UserStatus") -> None:
        self.user_id = user_id  # long
        self.status = status  # UserStatus

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ContactStatus":
        # No flags
        
        user_id = Long.read(b)
        
        status = TLObject.read(b)
        
        return ContactStatus(user_id=user_id, status=status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(self.status.write())
        
        return b.getvalue()
