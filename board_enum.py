#!/usr/bin/env python

from enum import Enum


class BoardSpaceTypeId(Enum):
    CARDS_CC = 0
    CARDS_CHANCE = 1
    FREE_PARKING = 2
    GO = 3
    JAIL = 4  # Includes "Just Visiting"
    JAIL_GO_TO = 5
    PROPERTY_RAILROAD = 6
    PROPERTY_RENTAL = 7
    PROPERTY_UTILITY = 8
    TAX_INCOME = 9
    TAX_LUXURY = 10

# ========================================

class BoardSpaceId(Enum):
    @classmethod
    def get_index(cls, type):
        return list(cls).index(type)

    GO = 0
    MEDITERRANEAN_AVENUE = 1
    COMMUNITY_CHEST_1 = 2
    BALTIC_AVENUE = 3
    TAX_INCOME = 4
    # -----
    READING_RAILROAD = 5
    ORIENTAL_AVENUE =  6
    CHANCE_1 = 7
    VERMONT_AVENUE = 8
    CONNECTICUT_AVENUE = 9
    # ==========
    JAIL = 10
    ST_CHARLES_PLACE = 11
    ELECTRIC_COMPANY = 12
    STATES_AVENUE = 13
    VIRGINIA_AVENUE = 14
    # -----
    PENNSYLVANIA_RAILROAD =15
    ST_JAMES_PLACE = 16
    COMMUNITY_CHEST_2 = 17
    TENNESSEE_AVENUE = 18
    NEW_YORK_AVENUE = 19
    # ==========
    FREE_PARKING = 20
    KENTUCKY_AVENUE = 21
    CHANCE_2 = 22
    INDIANA_AVENUE = 23
    ILLINOIS_AVENUE = 24
    # -----
    B_AND_O_RAILROAD = 25
    ATLANTIC_AVENUE = 26
    VENTNOR_AVENUE = 27
    WATER_WORKS = 28
    MARVIN_GARDENS = 29
    # ==========
    GO_TO_JAIL = 30
    PACIFIC_AVENUE = 31
    NORTH_CAROLINA_AVENUE = 32
    COMMUNITY_CHEST_3 = 33
    PENNSYLVANIA_AVENUE = 34
    # -----
    SHORT_LINE = 35
    CHANCE_3 = 36
    PARK_PLACE = 37
    TAX_LUXURY = 38
    BOARDWALK = 39
