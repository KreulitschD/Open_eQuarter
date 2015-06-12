# OeQ autogenerated correlation for 'Flat Heating Type Distribution in Correlation to the population density'

import math
import numpy as np
import oeqCorrelation as oeq
def get(*xin):

    # OeQ autogenerated correlation for 'Flats heated by a district heating systems in buildings with housing'
    FLT_HEAT_DISTR= oeq.correlation(
    const= -0.0376356597249,
    a=     0.055630888123,
    b=     -0.0187745475567,
    c=     0.00244209863747,
    d=     -7.48369103227e-05,
    mode= "log")
    # OeQ autogenerated correlation for 'Flats heated by self-contained central heating systems in buildings with housing'
    FLT_HEAT_SCDWELL= oeq.correlation(
    const= -0.0684937601574,
    a=     0.10128084038,
    b=     -0.036646484587,
    c=     0.00535661489889,
    d=     -0.000246366195974,
    mode= "log")
    # OeQ autogenerated correlation for 'Flats heated by a block-type combined heat and power plants in buildings with housing'
    FLT_HEAT_BLOCKTYPE= oeq.correlation(
    const= 0.00459916148686,
    a=     1.74044525842e-05,
    b=     -5.43453734006e-09,
    c=     7.06799781477e-13,
    mode= "lin")
    # OeQ autogenerated correlation for 'Flats in buildings with housing heated by a centralheating systems'
    FLT_HEAT_CENTRAL= oeq.correlation(
    const= 1.33518852477,
    a=     -0.596050491595,
    b=     0.211481787232,
    c=     -0.0290821005703,
    d=     0.00132808255549,
    mode= "log")
    # OeQ autogenerated correlation for 'Flats in buildings with housing heated by single room heating systems including stoves and night storage heaters'
    FLT_HEAT_SNGLROOM= oeq.correlation(
    const= 0.0606245152717,
    a=     0.114497071102,
    b=     -0.0432913974939,
    c=     0.00553116417972,
    d=     -0.000243749816477,
    mode= "log")
    # OeQ autogenerated correlation for 'Flats in buildings w/ housing without heating systems'
    FLT_HEAT_NONE= oeq.correlation(
    const= -0.0289954397875,
    a=     0.0447342324728,
    b=     -0.0152803821221,
    c=     0.00201423156615,
    d=     -9.27184773373e-05,
    mode= "log")

    return dict(FLT_HEAT_DISTR=FLT_HEAT_DISTR.lookup(*xin),
    FLT_HEAT_SCDWELL=FLT_HEAT_SCDWELL.lookup(*xin),
    FLT_HEAT_BLOCKTYPE=FLT_HEAT_BLOCKTYPE.lookup(*xin),
    FLT_HEAT_CENTRAL=FLT_HEAT_CENTRAL.lookup(*xin),
    FLT_HEAT_SNGLROOM=FLT_HEAT_SNGLROOM.lookup(*xin),
    FLT_HEAT_NONE=FLT_HEAT_NONE.lookup(*xin))

