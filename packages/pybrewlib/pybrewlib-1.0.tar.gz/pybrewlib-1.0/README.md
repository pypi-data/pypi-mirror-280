# Library description
Library contains functions for calculations that can be used in alcohol making.
Most of the functions are related to wine or beer making, but there might be
a small part of code related to stronger alcohols.

## Command-Line interface
Library exposes command line interface, which can be run by runing cli script inside pybrewlib folder.
This has been done for manual testing at the start, but then I have started using it as interface hence,
its left and documented, however not all API functions have been documented.

## Current API

|Name|Type|Description|
|--|--|--|
|alcohol_mass|function| return alcohol mass (volume in liters) |
|alcohol_units|function| return alcohol units in drink (irish) |
|blood_alcohol_content|function| return estimated bac|
|build_sg|function| builds starting gravity from a list of sugar additions expects a list of tuples/list in format: [(gravity before addition, gravity after addition)] |
|build_sg_interactive|function|build starting gravity for wine (if there was extra sugar added) (interactively)|
|calculations|module|calculations exposed by library and used by the cli|
|cli|function|command-line interface for the library|
|dillution_approx_outcome|function| return total quantity of alcohol at given strenght and water required|
|dilution_approx_calc|function|calculate abv of diluted drink|
|dilution_approx_proportions|function|return proportions to get requested strength and quantity of alcohol|
|e_bac|function| estimate blood alcohol content |
|estimate_mixed_abv|function| Estimate abv of a drink mixed from other drinks expects a list in format [(abv of 1st drink, volume)]|
|estimate_mixed_abv_interactive|function| Estimate abv of a drink mixed from other drinks (interractive)|
|sg_for_abv|function|calculate sg for wanted abv|
|sg_strength_calc|function|calculate abv content|
|spirit_dilution_spirit|function|acurate formula for diluting spirit with other spirit returns amount of other spirit required|
|spirit_dilution_water|function|acurate formula for diluting spirit with water returns required amount of water|
