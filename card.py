#!/usr/bin/env python

from enum import Enum

from board_enum import BoardSpaceId
from card_enum import CardId
from property_enum import PropertyGroupId


class Card:
    def bank_pays_holder(holder, amount):
        bank_pays_player(holder, amount)

    def every_player_pays_holder(holder, amount):
        for other in game.other_players(holder):
            other.owes(holder, amount)

    def holder_gets_out_of_jail(holder):
        holder.is_jailed = False

    def holder_moves_back(holder, spaces):
        new_bsid = BoardSpaceId((player.position - spaces) % BOARD_SIZE)
        holder.bsid = new_bsid

    def holder_moves_directly_to_jail(holder, dest):
        new_bsid = BoardSpaceId.JAIL
        holder.bsid = new_bsid
        holder.is_jailed = True

    def holder_pays_bank(holder, amount):
        holder.owe_bank(amount)

    def holder_pays_every_player(holder, amount):
        for other in game.other_players(holder):
            holder.owes_player(other, amount)

    def player_pays_holder(holder, other, amount):
        other.owes_player(holder, amount)

    def holder_pays_player(holder, other, amount):
        holder.owe_player(other, amount)

    # --------------------

    def __init__(self):
        # self.card_action_type
        self.is_use_voluntary = False

    def action(self):
        raise NotImplementedError('Card.action()')


class Card_BankPaysHolder(Card):
    def __init__(self, cid, desc, amount):
        self.cid = cid
        self.description = desc
        self.amount = amount

    def action(self, holder):
        holder.owe_bank(self.amount)


class Card_EachPlayerPaysHolder(Card):
    def __init__(self, cid, desc, amount):
        self.cid = cid
        self.description = desc
        self.amount = amount

    def action(self, holder):
        action_every_player_pays_holder(holder, self.amount)


class Card_GetOutOfJailFree(Card):
    def __init__(self, cid, desc):
        self.cid = cid
        self.description = desc
        self.is_use_voluntary = True

    def action(self, holder):
        assert(player.position == BoardSpaceId.JAJail)
        holder.is_jailed = False


class Card_HolderGetsOutOfJailFree(Card):
    def __init__(self, cid, desc):
        self.cid = cid
        self.description = desc
        self.is_use_voluntary = True

    def action(self, holder):
        assert(player.position == Jail)
        Card.holder_get_out_of_jail_free(holder)


class Card_HolderMovesBack(Card):
    def __init__(self, cid, desc, spaces):
        self.cid = cid
        self.description = desc
        self.spaces = spaces

    def action(self, holder):
        Card.holder_move_back(holder, spaces)


class Card_HolderMovesDirectlyTo(Card):
    def __init__(self, cid, desc, dest):
        self.cid = cid
        self.description = desc
        self.dest = dest

    def action(self, holder):
        Card.holder_move_directly(holder, dest)
        if dest == BoardSpaceId.JAIL:
            holder.is_jailed = True


class Card_HolderMovesForwardTo(Card):
    def __init__(self, cid, desc, dest):
        self.cid = cid
        self.description = desc
        self.dest = dest

    def action(self, holder):
        Card.holder_move_forward_to(holder, dest)


class Card_HolderMovesForwardToPropertyGroupIdAndPaysMultipleOfAmountDue(Card):
    def __init__(self, cid, desc, dest_prop_grp, mult):
        self.cid = cid
        self.description = desc
        self.dest_prop_grp = dest_prop_grp
        self.mult = mult

    def action(self, holder):
        Card.holder_move_forward_and_pay_multiple_of_amount_due(holder, self.dest_prop_grp, mult)


class Card_HolderMovesForwardToPropertyGroupIdAndPaysMultipleOfDiceRoll(Card):
    def __init__(self, cid, desc, dest_prop_grp, mult):
        self.cid = cid
        self.description = desc
        self.dest_prop_grp = dest_prop_grp
        self.mult = mult

    def action(self, holder):
        Card.holder_move_forward_and_pay_multiple_of_amount_due(holder, self.dest_prop_grp, mult)


class Card_HolderPaysBank(Card):
    def __init__(self, cid, desc, amount):
        self.cid = cid
        self.description = desc
        self.amount = amount

    def action(self, holder):
        holder.owe_bank(self.amount)


class Card_HolderPaysEachPlayer(Card):
    def __init__(self, cid, desc, amount):
        self.cid = cid
        self.description = desc
        self.amount = amount

    def action(self, holder):
        for other in game.get_other_players(holder):
            holder.owe_player(other, amount)


class Card_HolderPaysPlayer(Card):
    def __init__(self, cid, desc, amount):
        self.cid = cid
        self.description = desc
        self.amount = amount

    def action(self, holder):
        holder.owe_player(other, amount)


class Card_PropertyAssessment(Card):
    def __init__(self, cid, desc, per_house, per_hotel):
        self.cid = cid
        self.description = desc
        self.per_house = per_house
        self.per_hotel = per_hotel

    def action(self, holder):
        holder.owe_bank( holder.house_count() * self.per_house
                       + holder.hotel_count() * self.per_hotel)

# ========================================

initial_cards_cc = [
    Card_HolderMovesForwardTo(CardId.CC_ADVANCE_GO,
        'Advance to Go (Collect $200)',
        BoardSpaceId.GO),
    Card_BankPaysHolder(CardId.CC_BANK_ERROR,
        'Bank error in your favor. Collect $200',
        200),
    Card_HolderPaysBank(CardId.CC_DOCTOR_FEE,
        "Doctor's fee. Pay $50",
        50),
    Card_BankPaysHolder(CardId.CC_STOCK_SALE,
        'From sale of stock you get $50',
        50),
    Card_HolderGetsOutOfJailFree(CardId.CC_LEAVE_JAIL,
        'Get Out of Jail Free',
        ),
    Card_HolderMovesDirectlyTo(CardId.CC_GO_TO_JAIL,
        'Go to Jail. Go directly to jail, do not pass Go, do not collect $200',
        BoardSpaceId.JAIL),
    Card_BankPaysHolder(CardId.CC_HOLIDAY_FUND,
        'Holiday fund matures. Receive $100',
        100),
    Card_BankPaysHolder(CardId.CC_INCOME_TAX_REFUND,
        'Income tax refund. Collect $20',
        20),
    Card_EachPlayerPaysHolder(CardId.CC_BIRTHDAY_GIFTS,
        'It is your birthday. Collect $10 from every player',
        10),
    Card_BankPaysHolder(CardId.CC_LIFE_INSURANCE,
        'Life insurance matures. Collect $100',
        100),
    Card_HolderPaysBank(CardId.CC_HOSPITAL_FEE,
        'Pay hospital fees of $100',
        100),
    Card_HolderPaysBank(CardId.CC_SCHOOL_FEE,
        'Pay school fees of $50',
        50),
    Card_BankPaysHolder(CardId.CC_CONSULTANCY_FEE,
        'Receive $25 consultancy fee',
        25),
    Card_PropertyAssessment(CardId.CC_STREET_REPAIR,
        'You are assessed for street repair. $40 per house. $115 per hotel',
        40, 115),
    Card_BankPaysHolder(CardId.CC_SECOND_PRIZE,
        'You have won second prize in a beauty contest. Collect $10',
        10),
    Card_BankPaysHolder(CardId.CC_INHERITANCE,
        'You inherit $100',
        100)
    ]


initial_cards_chance = [
    Card_HolderMovesForwardTo(CardId.CHANCE_ADVANCE_BOARDWALK,
        'Advance to Boardwalk',
        BoardSpaceId.BOARDWALK),
    Card_HolderMovesForwardTo(CardId.CHANCE_ADVANCE_GO,
        'Advance to Go (Collect $200)',
        BoardSpaceId.GO),
    Card_HolderMovesForwardTo(CardId.CHANCE_ADVANCE_ILLINOIS,
        'Advance to Illinois Avenue. If you pass Go, collect $200',
        BoardSpaceId.ILLINOIS_AVENUE),
    Card_HolderMovesForwardTo(CardId.CHANCE_ADVANCE_ST_CHARLES,
        'Advance to St. Charles Place. If you pass Go, collect $200',
        BoardSpaceId.ST_CHARLES_PLACE),
    Card_HolderMovesForwardToPropertyGroupIdAndPaysMultipleOfAmountDue(CardId.CHANCE_ADVANCE_NEAREST_RAILROAD_1,
        'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled',
        PropertyGroupId.RAILROAD, 2),
    Card_HolderMovesForwardToPropertyGroupIdAndPaysMultipleOfAmountDue(CardId.CHANCE_ADVANCE_NEAREST_RAILROAD_2,
        'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled',
        PropertyGroupId.RAILROAD, 2),
    Card_HolderMovesForwardToPropertyGroupIdAndPaysMultipleOfDiceRoll(CardId.CHANCE_ADVANCE_NEAREST_UTILITY,
        'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.',
        PropertyGroupId.UTILITY, 10),
    Card_BankPaysHolder(CardId.CHANCE_BANK_DIVIDEND,
        'Bank pays you dividend of $50',
        50),
    Card_GetOutOfJailFree(CardId.CHANCE_LEAVE_JAIL,
        'Get Out of Jail Free'
        ),
    Card_HolderMovesBack(CardId.CHANCE_GO_BACK_3,
        'Go Back 3 Spaces',
        3),
    Card_HolderMovesDirectlyTo(CardId.CHANCE_GO_JAIL,
        'Go to Jail. Go directly to Jail, do not pass Go, do not collect $200',
        BoardSpaceId.JAIL
        ),
    Card_PropertyAssessment(CardId.CHANCE_PROPERTY_REPAIR,
        'Make general repairs on all your property. For each house pay $25. For each hotel pay $100',
        25, 100),
    Card_HolderPaysBank(CardId.CHANCE_SPEEDING_FINE,
        'Speeding fine $15',
        15),
    Card_HolderMovesForwardTo(CardId.CHANCE_GO_READING,
        'Take a trip to Reading Railroad. If you pass Go, collect $200',
        BoardSpaceId.READING_RAILROAD),
    Card_HolderPaysEachPlayer(CardId.CHANCE_CHAIRMAN_OF_BOARD,
        'You have been elected Chairman of the Board. Pay each player $50',
        50),
    Card_BankPaysHolder(CardId.CHANCE_BUILDING_LOAN,
        'Your building loan matures. Collect $150',
        150)
    ]
