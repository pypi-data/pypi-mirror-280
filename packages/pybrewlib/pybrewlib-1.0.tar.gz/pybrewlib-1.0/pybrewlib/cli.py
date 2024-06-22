#!/usr/bin/env python3

"""
    cli exposed by the library
"""
from .lang_pack import *
from .calculations import *

# "Reality is an illusion that occurs due to lack of alcohol." ~ Anonymous


def interactive_menu():
    final_str = ""
    try:
        print(OPT_STR)
        choice = int(input())
        if choice == 1:
            alc_str, wtr_qnt = intput(ALK_STR), intput(WTR_QNT)
            alc_qnt = intput(ALC_QNT)
            str = dilution_calc(alc_str, wtr_qnt, alc_qnt)
            final_str = f"{ALK_STR[lang]}:{str}%"
        elif choice == 2:
            final_str = f"{OG_STR[lang]}: {build_sg_interactive()}"
        elif choice == 3:
            og, fg = fluput(OG_STR), fluput(FG_STR)
            final_str = f"{ALK_STR[lang]}:{sg_strength_calc(og, fg)}%"
        elif choice == 4:
            alk_str, total = intput(ALK_STR), intput(TOT_QNT)
            wanted =  intput(WNT_STR)
            spirit, water = dilution_proportions(alk_str, total, wanted)
            final_str = f"{ALC_QNT[lang]}:{spirit} {WTR_QNT[lang]}:{water}"
        elif choice == 5:
            alk_str, wnt_str = intput(ALK_STR), intput(WNT_STR)
            alc_qnt = intput(ALC_QNT)
            total, water = dillution_outcome(alk_str, wnt_str, alc_qnt)
            final_str = f"{TOT_QNT[lang]}:{total} {WTR_QNT[lang]}:{water}"
        elif choice == 6:
            abv = estimate_mixed_abv_interactive()
            final_str = f"{ALK_STR[lang]}: {abv}%"
    except Exception as e:
        print(e)
    else:
        print(f"{final_str}")

if __name__ == "__main__":
    while input() != "Q":
        interactive_menu()