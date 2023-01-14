#!/usr/bin/env python

from board_enum import BoardSpaceId, BoardSpaceTypeId
from card_enum import CardStackId

from card_stack import CardStack
from property_enum import PropertyGroupId


class BoardSpace:
    bsid_to_type_name = {
        BoardSpaceId.GO:
            (BoardSpaceTypeId.GO, 'Go'),
        BoardSpaceId.MEDITERRANEAN_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Mediterranean Avenue'),
        BoardSpaceId.COMMUNITY_CHEST_1:
            (BoardSpaceTypeId.CARDS_CC, 'Community Chest'),
        BoardSpaceId.BALTIC_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Baltic Avenue'),
        BoardSpaceId.TAX_INCOME:
            (BoardSpaceTypeId.TAX_INCOME, 'Income Tax'),
        # -----
        BoardSpaceId.READING_RAILROAD:
            (BoardSpaceTypeId.PROPERTY_RAILROAD, 'Reading Railroad'),
        BoardSpaceId.ORIENTAL_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Oriental Avenue'),
        BoardSpaceId.CHANCE_1:
            (BoardSpaceTypeId.CARDS_CHANCE, 'Chance'),
        BoardSpaceId.VERMONT_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Vermont Avenue'),
        BoardSpaceId.CONNECTICUT_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Connecticut Avenue'),
        # ==========
        BoardSpaceId.JAIL:
            (BoardSpaceTypeId.JAIL, 'Jail'),
        BoardSpaceId.ST_CHARLES_PLACE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'St. Charles Place'),
        BoardSpaceId.ELECTRIC_COMPANY:
            (BoardSpaceTypeId.PROPERTY_UTILITY, 'Electric Company'),
        BoardSpaceId.STATES_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'States Avenue'),
        BoardSpaceId.VIRGINIA_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Virginia Avenue'),
        # -----
        BoardSpaceId.PENNSYLVANIA_RAILROAD:
            (BoardSpaceTypeId.PROPERTY_RAILROAD, 'Pennsylvania Railroad'),
        BoardSpaceId.ST_JAMES_PLACE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'St. James Place'),
        BoardSpaceId.COMMUNITY_CHEST_2:
            (BoardSpaceTypeId.CARDS_CC, 'Community Chest'),
        BoardSpaceId.TENNESSEE_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Tennessee Avenue'),
        BoardSpaceId.NEW_YORK_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'New York Avenue'),
        # ==========
        BoardSpaceId.FREE_PARKING:
            (BoardSpaceTypeId.FREE_PARKING, 'Free Parking'),
        BoardSpaceId.KENTUCKY_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Kentucky Avenue'),
        BoardSpaceId.CHANCE_2:
            (BoardSpaceTypeId.CARDS_CHANCE, 'Chance'),
        BoardSpaceId.INDIANA_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Indiana Avenue'),
        BoardSpaceId.ILLINOIS_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Illinois Avenue'),
        # -----
        BoardSpaceId.B_AND_O_RAILROAD:
            (BoardSpaceTypeId.PROPERTY_RAILROAD, 'B&O Railroad'),
        BoardSpaceId.ATLANTIC_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Atlantic Avenue'),
        BoardSpaceId.VENTNOR_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Ventnor Avenue'),
        BoardSpaceId.WATER_WORKS:
            (BoardSpaceTypeId.PROPERTY_UTILITY, 'Water Works'),
        BoardSpaceId.MARVIN_GARDENS:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Marvin Gardens'),
        # ==========
        BoardSpaceId.GO_TO_JAIL:
            (BoardSpaceTypeId.JAIL_GO_TO, 'Go To Jail'),
        BoardSpaceId.PACIFIC_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Pacific Avenue'),
        BoardSpaceId.NORTH_CAROLINA_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'North Carolina Avenue'),
        BoardSpaceId.COMMUNITY_CHEST_3:
            (BoardSpaceTypeId.CARDS_CC, 'Community Chest'),
        BoardSpaceId.PENNSYLVANIA_AVENUE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Pennsylvania Avenue'),
        # -----
        BoardSpaceId.SHORT_LINE:
            (BoardSpaceTypeId.PROPERTY_RAILROAD, 'Short Line'),
        BoardSpaceId.CHANCE_3:
            (BoardSpaceTypeId.CARDS_CHANCE, 'Chance'),
        BoardSpaceId.PARK_PLACE:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Park Place'),
        BoardSpaceId.TAX_LUXURY:
            (BoardSpaceTypeId.TAX_LUXURY, 'Luxury Tax'),
        BoardSpaceId.BOARDWALK:
            (BoardSpaceTypeId.PROPERTY_RENTAL, 'Boardwalk')
        }

    property_group_to_bsids = {
        PropertyGroupId.BROWN:
            [ BoardSpaceId.MEDITERRANEAN_AVENUE, BoardSpaceId.BALTIC_AVENUE ],
        PropertyGroupId.LIGHT_BLUE:
            [ BoardSpaceId.ORIENTAL_AVENUE, BoardSpaceId.VERMONT_AVENUE,
              BoardSpaceId.CONNECTICUT_AVENUE ],
        PropertyGroupId.PINK:
            [ BoardSpaceId.ST_CHARLES_PLACE, BoardSpaceId.STATES_AVENUE,
              BoardSpaceId.VIRGINIA_AVENUE ],
        PropertyGroupId.ORANGE:
            [ BoardSpaceId.ST_JAMES_PLACE, BoardSpaceId.TENNESSEE_AVENUE,
              BoardSpaceId.NEW_YORK_AVENUE ],
        PropertyGroupId.RED:
            [ BoardSpaceId.KENTUCKY_AVENUE, BoardSpaceId.INDIANA_AVENUE,
              BoardSpaceId.ILLINOIS_AVENUE ],
        PropertyGroupId.YELLOW:
            [ BoardSpaceId.ATLANTIC_AVENUE, BoardSpaceId.VENTNOR_AVENUE,
              BoardSpaceId.MARVIN_GARDENS ],
        PropertyGroupId.GREEN:
            [ BoardSpaceId.PACIFIC_AVENUE, BoardSpaceId.NORTH_CAROLINA_AVENUE,
              BoardSpaceId.PENNSYLVANIA_AVENUE ],
        PropertyGroupId.DARK_BLUE:
            [ BoardSpaceId.PARK_PLACE, BoardSpaceId.BOARDWALK ],

        PropertyGroupId.RAILROAD:
            [ BoardSpaceId.READING_RAILROAD, BoardSpaceId.PENNSYLVANIA_RAILROAD,
              BoardSpaceId.B_AND_O_RAILROAD, BoardSpaceId.SHORT_LINE ],
        PropertyGroupId.UTILITY:
            [ BoardSpaceId.ELECTRIC_COMPANY, BoardSpaceId.WATER_WORKS ]
        }

    property_group_to_name = {
        PropertyGroupId.NONE: 'NO_GROUP',
        PropertyGroupId.BROWN: 'Brown',
        PropertyGroupId.LIGHT_BLUE: 'Light Blue',
        PropertyGroupId.PINK: 'Pink',
        PropertyGroupId.ORANGE: 'Orange',
        PropertyGroupId.RED: 'Red',
        PropertyGroupId.YELLOW: 'Yellow',
        PropertyGroupId.GREEN: 'Green',
        PropertyGroupId.DARK_BLUE: 'Dark Blue',

        PropertyGroupId.RAILROAD: 'Railroads',
        PropertyGroupId.UTILITY: 'Utilities'
        }

    def get_name(bsid):
        # print(f'\tBoardSpace.get_type(): bsid={bsid}')
        tmp = BoardSpace.bsid_to_type_name[BoardSpaceId(bsid)]
        # print(f'\t\tBoardSpace.get_type(): tmp={tmp}')
        return tmp[1]

    def get_type(bsid):
        # print(f'\tBoardSpace.get_type(): bsid={bsid}')
        tmp = BoardSpace.bsid_to_type_name[BoardSpaceId(bsid)]
        # print(f'\t\tBoardSpace.get_type(): tmp={tmp}')
        return tmp[0]

    # --------------------

    def __init__(self, bsid, pos, bst, name):
        self.bsid = bsid
        self.position = pos
        self.board_space_type = bst
        self.name = name

        # Using arrays for faster access
        self.board_space_types = [BoardSpace.get_type(BoardSpaceId(bsid)) for bsid in range(40)]
        self.board_space_name = [BoardSpace.get_type(BoardSpaceId(bsid)) for bsid in range(40)]

        self.houses = [0 for _ in range(40)]
        self.hotels = [0 for _ in range(40)]

        property_types = [ BoardSpaceTypeId.PROPERTY_RAILROAD
                         , BoardSpaceTypeId.PROPERTY_RENTAL
                         , BoardSpaceTypeId.PROPERTY_UTILITY
                         ]
        self.owner_ids = [0 if BoardSpace.get_type(BoardSpaceId(bsid)) in property_types else -1
                           for bsid in range(40)
                         ]

        bsid_to_rental_property_group = { bsid: prop_grp
                                          for prop_grp, bsids in BoardSpace.property_group_to_bsids.items()
                                          for bsid in bsids
                                        }
        # for bsid, prop_grp in bsid_to_rental_property_group.items():
        #     print(f'\tINFO: {bsid}: {prop_grp}')
        # print(f'INFO: Number of (bsid, rental_group) pairs: {len(bsid_to_rental_property_group)}')

        def bsid_to_property_group(bsid):
            type_name = BoardSpace.bsid_to_type_name[BoardSpaceId(bsid)]
            t = type_name[0]
            if t == BoardSpaceTypeId.PROPERTY_RAILROAD:
                return PropertyGroupId.RAILROAD
            elif t == BoardSpaceTypeId.PROPERTY_UTILITY:
                return PropertyGroupId.UTILITY
            elif t == BoardSpaceTypeId.PROPERTY_RENTAL:
                return bsid_to_rental_property_group[BoardSpaceId(bsid)]
            else:
                return PropertyGroupId.NONE
        self.property_groups = [bsid_to_property_group(bsid) for bsid in range(40)]

    def has_type(self, t):
        return self.board_space_type == t

    def is_property(self):
        return (  self.is_type(BoardSpaceTypeId.PropertyRailroad)
               or self.is_type(BoardSpaceTypeId.PropertyRental)
               or self.is_type(BoardSpaceTypeId.PropertyUtility)
               )

    def on_landing(self, game, pid):
        bst = self.board_space_type(self.bsid)
        if bst == BoardSpaceTypeId.CARDS_CC:
            game.draw_card_cc(pid)
        elif bst == BoardSpaceTypeId.CARDS_CHANCE:
            game.draw_card_chance(pid)
        elif bst == BoardSpaceTypeId.FREE_PARKING:
            game.on_landing_free_parking(pid)
        elif bst == BoardSpaceTypeId.GO:
            pass  # Rely instead on detetion of traversing
        elif bst == BoardSpaceTypeId.JAIL:
            pass  # Just visiting
        elif bst == BoardSpaceTypeId.JAIL_GO_TO:
            player.move_directly_to(BoardSpaceId.JAIL)
            player.set_jailed = True
        elif bst == BoardSpaceTypeId.PROPERTY_RAILROAD:
            game.on_landing_railroad(self, pid)
        elif bst == BoardSpaceTypeId.PROPERTY_RENTAL:
            game.on_landing_property_rental(self, pid)
        elif bst == BoardSpaceTypeId.PROPERTY_UTILITY:
            game.on_landing_property_utility(self, pid)
        elif bst == BoardSpaceTypeId.TAX_INCOME:
            game.on_landing_tax_income(self, pid)
        elif bst == BoardSpaceTypeId.TAX_LUXURY:
            game.on_landing_tax_luxury(self, pid)
        else:
            raise ValueError(f'Unrecognized BoardSpaceTypeId: {bst}')

    def on_traversing(self, game, player):  # Without landing on
        if self.board_space_type == BoardSpaceTypeId.GO:
            game.bank_plays_player(player, GameConfig.GO_PAYMENT_AMOUNT)


class BoardSpace_Cards_Chance(BoardSpace):
    def __init__():
        pass
    def on_landing():
        card = Game.cards_chance.draw_next_card()
        if not card.is_deployable():
            exec_card(card)


class BoardSpace_Cards_CommunityChest(BoardSpace):
    def __init__():
        pass
    def on_landing():
        card = Game.cards_chance.draw_next_card()
        if not card.is_deployable():
            exec_card(card)


class BoardSpace_FreeParking(BoardSpace):
    def __init__():
        pass
    def on_landing():
        pass
    # GameConfig if do_use_free_parking: exec_free_parking()


class BoardSpace_Go(BoardSpace):
    def __init__():
        pass
    def on_landing():
        pass  # Windfall handled by on_enterin()
    def on_entering():
        payment_from_bank_to_player(WINDFALL_GO)


class BoardSpace_GoToJail(BoardSpace):
    def __init__():
        pass
    def on_landing():
        go_to_jail()


class BoardSpace_Property(BoardSpace):
    def __init__():
        is_owned = False
        is_mortgaged = False
    def is_amount_due():
        return self.is_owned and not self.is_mortgaged


class BoardSpace_PropertyRailroad(BoardSpace_Property):
    def __init__():
        pass
    def amount_due():
        if not is_amount_due():
            return 0
        else:
            return PropertyRailroad.fee(owned_railroad_count)
    def on_landing():
        if self.is_amount_due():
            mover.owes_player(owner, self.amount_due)


class BoardSpace_PropertyRental(BoardSpace_Property):
    def __init__(name, color_group,
            price_property, price_house, price_hotel, rents):
        self.name = name
        self.color_group = color_group
        self.price_property = price_property
        self.price_house = price_house
        self.price_hotel = price_hotel
        self.rents = rents

    def is_monopoly():
        NNNN

    def is_undeveloped():
        return houses == 0 and hotels == 0

    def on_landing():
        if self.is_amount_due():
            rent_index = NNN
            rent_multipler = GameConfig.rent_multiplier
            if self.is_undeveloped():
                rent = (2 * self.rents[0] if self.is_monopoly()
                        else rents[0])
            else:
                rent = self.rents[rent_index]
            mover.owes_payment(owner, rent)


class BoardSpace_PropertyUtility(BoardSpace_Property):
    def __init__():
        pass
    def on_landing():
        pass


class BoardSpace_TaxIncome(BoardSpace):
    def __init__():
        pass
    def on_landing():
        pass


class BoardSpace_TaxUtility(BoardSpace):
    def __init__(amount):
        self.amount = amount
    def on_landing():
        mover.owe_bank(self.amount)


class Board:
    def __init__(self):
        board_space_data = [
              (bsid, bsid, BoardSpace.get_type(bsid), BoardSpace.get_name(bsid))
              for bsid in sorted([e.value for e in BoardSpaceId])
            ]
        self.board_spaces = [BoardSpace(*bsd) for bsd in board_space_data]
        self.cards_cc = CardStack(CardStackId.CARDS_CC)
        self.cards_chance = CardStack(CardStackId.CARDS_CHANCE)

    def move_forward_to(player, dest):
        pass

    def move_forward_spaces(player, n):
        while (space_count > 0):
            move_forward_one_space()
            player.position += 1
        # TODO: Complete

    def move_back_spaces(player, n):
        pass
