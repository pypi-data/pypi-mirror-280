# -*- coding: utf-8 -*-

from wow_wtf.tests.exp03_wotlk.acc_dataset import ds


# fmt: off
class AccountEnum:
    acc01 = ds.accounts["acc01"]
    acc02 = ds.accounts["acc02"]
    acc03 = ds.accounts["acc03"]
    acc04 = ds.accounts["acc04"]
    acc05 = ds.accounts["acc05"]
    acc06 = ds.accounts["acc06"]
    acc07 = ds.accounts["acc07"]
    acc08 = ds.accounts["acc08"]
    acc09 = ds.accounts["acc09"]
    acc10 = ds.accounts["acc10"]


class RealmEnum:
    acc01_realm1 = ds.accounts["acc01"].realms_mapper["realm1"]
    acc02_realm1 = ds.accounts["acc02"].realms_mapper["realm1"]
    acc03_realm1 = ds.accounts["acc03"].realms_mapper["realm1"]
    acc04_realm1 = ds.accounts["acc04"].realms_mapper["realm1"]
    acc05_realm1 = ds.accounts["acc05"].realms_mapper["realm1"]
    acc06_realm1 = ds.accounts["acc06"].realms_mapper["realm1"]
    acc07_realm1 = ds.accounts["acc07"].realms_mapper["realm1"]
    acc08_realm1 = ds.accounts["acc08"].realms_mapper["realm1"]
    acc09_realm1 = ds.accounts["acc09"].realms_mapper["realm1"]
    acc10_realm1 = ds.accounts["acc10"].realms_mapper["realm1"]


class CharacterEnum:
    acc01_realm1_mywarrior = ds.accounts["acc01"].realms_mapper["realm1"].characters_mapper["mywarrior"]
    acc02_realm1_mypaladin = ds.accounts["acc02"].realms_mapper["realm1"].characters_mapper["mypaladin"]
    acc03_realm1_mydk = ds.accounts["acc03"].realms_mapper["realm1"].characters_mapper["mydk"]
    acc04_realm1_myhunter = ds.accounts["acc04"].realms_mapper["realm1"].characters_mapper["myhunter"]
    acc05_realm1_myshaman = ds.accounts["acc05"].realms_mapper["realm1"].characters_mapper["myshaman"]
    acc06_realm1_myrogue = ds.accounts["acc06"].realms_mapper["realm1"].characters_mapper["myrogue"]
    acc07_realm1_mydruid = ds.accounts["acc07"].realms_mapper["realm1"].characters_mapper["mydruid"]
    acc08_realm1_mywarlock = ds.accounts["acc08"].realms_mapper["realm1"].characters_mapper["mywarlock"]
    acc09_realm1_mymage = ds.accounts["acc09"].realms_mapper["realm1"].characters_mapper["mymage"]
    acc10_realm1_mypriest = ds.accounts["acc10"].realms_mapper["realm1"].characters_mapper["mypriest"]
# fmt: on