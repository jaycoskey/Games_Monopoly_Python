#!/usr/bin/env python

from enum import Enum


# class CardActionType(Enum):
#     NoCardActionType = -1
#
#     BankPaysHolder = 0
#     EachPlayerPaysHolder = 1
#     GetOutOfJailFree = 2
#     HolderMoveBack = 3
#     HolderMoveDirectlyTo = 4
#     HolderMovesForwardTo = 5
#     HolderMovesForwardToPropertyGroupAndPayMultipleOfAmountDue = 6
#     HolderMovesForwardToPropertyGroupAndPayMultipleOfDiceRoll = 7
#     HolderPaysBank = 8  # Amount varies: e.g., assessment
#     HolderPaysEachPlayer = 9
#     HolderPaysPlayer = 10
#     PropertyAssessment = 11


class CardId(Enum):  # 16 CC, 16 Chance
    CC_ADVANCE_GO = 0
    CC_BANK_ERROR = 1
    CC_DOCTOR_FEE = 2
    CC_STOCK_SALE = 3
    CC_LEAVE_JAIL = 4
    CC_GO_TO_JAIL = 5
    CC_HOLIDAY_FUND = 6
    CC_INCOME_TAX_REFUND = 7
    CC_BIRTHDAY_GIFTS = 8
    CC_LIFE_INSURANCE = 9
    CC_HOSPITAL_FEE = 10
    CC_SCHOOL_FEE = 11
    CC_CONSULTANCY_FEE = 12
    CC_STREET_REPAIR = 13
    CC_SECOND_PRIZE = 14
    CC_INHERITANCE = 15

    CHANCE_ADVANCE_BOARDWALK = 16
    CHANCE_ADVANCE_GO = 17
    CHANCE_ADVANCE_ILLINOIS = 18
    CHANCE_ADVANCE_ST_CHARLES = 19
    CHANCE_ADVANCE_NEAREST_RAILROAD_1 = 20
    CHANCE_ADVANCE_NEAREST_RAILROAD_2 = 21
    CHANCE_ADVANCE_NEAREST_UTILITY = 22
    CHANCE_BANK_DIVIDEND = 23
    CHANCE_LEAVE_JAIL = 24
    CHANCE_GO_BACK_3 = 25
    CHANCE_GO_JAIL = 26
    CHANCE_PROPERTY_REPAIR = 27
    CHANCE_SPEEDING_FINE = 28
    CHANCE_GO_READING = 29
    CHANCE_CHAIRMAN_OF_BOARD = 30
    CHANCE_BUILDING_LOAN = 31


class CardStackId(Enum):
    CARDS_CC = 0
    CARDS_CHANCE = 1
