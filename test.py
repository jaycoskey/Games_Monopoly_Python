#!/usr/bin/env python

import unittest

from board_enum import BoardSpaceId
from card_enum import CardId
from property_enum import PropertyGroupId

# from bank import Bank
from board import Board
from board import BoardSpace
from board import BoardSpace_Cards_Chance
from board import BoardSpace_Cards_CommunityChest
from board import BoardSpace_FreeParking
from board import BoardSpace_Go
from board import BoardSpace_GoToJail

from board import BoardSpace_Property
from board import BoardSpace_PropertyRailroad
from board import BoardSpace_PropertyRental
from board import BoardSpace_PropertyUtility

from board import BoardSpace_TaxIncome, BoardSpace_TaxUtility

from card import CardId

# from money import MoneyAmount
# from property import Property


class Test(unittest.TestCase):
    def test_foo(self):
        assert(True)


if __name__ == '__main__':
    unittest.main()
