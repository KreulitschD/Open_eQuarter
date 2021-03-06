# OeQ autogenerated correlation for 'Window/Wall Ratio in Correlation to the Building Age'

import math
import numpy as np
import oeqCorrelation as oeq
def get(*xin):

    # OeQ autogenerated correlation for 'Window to Wall Ratio in all Directions'
    A_WIN_BY_AW= oeq.correlation(
    const= 23214.7776635,
    a=     -47.3526648501,
    b=     0.0361917067716,
    c=     -1.22840089011e-05,
    d=     1.56225770296e-09,
    mode= "lin")

    return dict(A_WIN_BY_AW=A_WIN_BY_AW.lookup(*xin))

