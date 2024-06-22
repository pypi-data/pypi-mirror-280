#!/usr/bin/env python3

"""
    calculations exposed by library and used by the cli
"""
from .lang_pack import OG_STR, IN_ADD, GRV_AF, GRV_B4
from .lang_pack import NO_DRNK, TOT_QNT, ALK_STR, lang

# “Here’s to alcohol, the cause of, and solution to, all life’s problems.”
#  —Homer Simpson, The Simpsons

intput = lambda x: int(input(f"{x[lang]}: "))
fluput = lambda x: float(input(f"{x[lang]}: "))


def dilution_approx_calc(alc_str, water_quantity, alc_quantity): 
    """
        calculate abv of diluted drink
    """      
    return (alc_quantity/(alc_quantity + water_quantity)*100) / 100 * alc_str


def dillution_approx_outcome(alc_str, alc_wanted, alc_qu):
    """ return total quantity of alcohol at given strenght and water required"""
    total_qu = alc_qu * alc_str / alc_wanted
    # alcohol, water
    return alc_qu, total_qu - alc_qu 


def dilution_approx_proportions(alc_str, total_qu, alc_wanted):
    "return proportions to get requested strength and quantity of alcohol"
    spir_req = total_qu / (alc_str / alc_wanted)
    # return spirit, water
    return spir_req, total_qu - spir_req


def build_sg(sg, additions, addition_list):
    """ builds starting gravity from a list of sugar additions
        expects a list of tuples/list in format:
        [(gravity before addition, gravity after addition)]
    """
    sg_afloat = 0
    for b4, after in additions:
        sg += after - b4
        sg += ( (sg_afloat - b4) if sg_afloat > 0 else 0)
        sg_afloat = after


def build_sg_interactive():
    """build starting gravity for wine (if there was extra sugar added)
     (interactively)"""
    sg = fluput(OG_STR)
    additions = intput(IN_ADD)
    sg_afloat = 0
    for _ in range(additions):
        gravity_b4 = fluput(GRV_B4)
        gravity_after = fluput(GRV_AF)
        sg += (gravity_after - gravity_b4)
        sg += ( (sg_afloat - gravity_b4) if sg_afloat > 0 else 0)
        sg_afloat = gravity_after 
    return sg


def estimate_mixed_abv(abvs):
    """ Estimate abv of a drink mixed from other drinks
        expects a list in format [(abv of 1st drink, volume)]
    """
    volume = 0
    alc_cont = 0
    for alc, vol in abvs:
        volume += vol
        alc_cont += (alc/100) * vol
    return alc_cont/volume*100


def estimate_mixed_abv_interactive():
    """ Estimate abv of a drink mixed from other drinks
        (interractive)
    """
    volume = 0
    alc_cont = 0
    drinks = intput(NO_DRNK)
    for _ in range(drinks):
        vol = fluput(TOT_QNT)
        alc = fluput(ALK_STR)
        volume += vol
        alc_cont += (alc/100) * vol
    return alc_cont/volume*100


def sg_strength_calc(og, fg):
    "calculate abv content"
    return (og - fg) * 131.25


def sg_for_abv(abv, fg):
    """
    calculate sg for wanted abv
    """
    return (abv / 131.25) + fg


def alcohol_units(volume, abv):
    """ retrun alkohol units in drink (irish) """
    return volume * abv * 0.000789


def alcohol_mass(volume, abv):
    """ return alcohol mass (volume in liters) """
    return volume * (abv/100) * 789


def e_bac(mass, body_water_ratio, weight, metabolism, time):
    """ estimate blood alcohol content """
    return (mass/(body_water_ratio*weight)) * 100 - metabolism * time


def blood_alcohol_content(volume, abv, weight, time, man=True):
    """ return estimated bac"""
    alc_mass = alcohol_mass(volume, abv)
    if man:
        return e_bac(alc_mass, 0.68, weight, 0.017, time)
    return e_bac(alc_mass, 0.55, weight, 0.017, time)


def spirit_dilution_water(spirit_abv, spirit_vol, wanted_abv):
    """
         acurate formula for diluting spirit with water
         returns required amount of water
    """
    return spirit_abv * spirit_vol / wanted_abv - spirit_vol


def spirit_dilution_spirit(spirit_abv, spirit_vol, spirit2_abv, wanted_abv):
    """ 
        acurate formula for diluting spirit with other spirit
        returns amount of other spirit required
    """
    return (spirit_abv * spirit_vol - wanted_abv * spirit_vol) / (wanted_abv - spirit2_abv)

