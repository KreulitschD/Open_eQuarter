# OeQ autogenerated correlation for 'Owner Distribution in Correlation to the population density'

import math
import numpy as np
import oeqCorrelation as oeq
def get(*xin):

    # OeQ autogenerated correlation for 'Buildings with housing owned by assiciations'
    BLD_OWNER_ASSOC= oeq.correlation(
    const= 0.0312402617763,
    a=     0.0118744160584,
    b=     -0.00729746079842,
    c=     0.00173208156049,
    d=     -9.53526866706e-05,
    mode= "log")
    # OeQ autogenerated correlation for 'Buildings with housing owned by private persons'
    BLD_OWNER_PRIV= oeq.correlation(
    const= 0.870142013652,
    a=     0.0125902143919,
    b=     0.00423575284842,
    c=     -0.00101572305978,
    mode= "log")
    # OeQ autogenerated correlation for ''
    BLD_OWNER_BUILDSOC= oeq.correlation(
    const= 7.05505520927e-05,
    a=     2.41405868896e-05,
    b=     -8.36861380787e-09,
    c=     1.19731589642e-12,
    d=     -3.91117785944e-17,
    mode= "lin")
    # OeQ autogenerated correlation for 'Buildings with housing owned by muicipalities and municipal housing companies'
    BLD_OWNER_MUNDWELLCOMP= oeq.correlation(
    const= 0.0119495453475,
    a=     0.00711820124277,
    b=     -0.00303579094598,
    c=     0.000296825110286,
    mode= "log")
    # OeQ autogenerated correlation for 'Buildings with housing owned by private housing companies'
    BLD_OWNER_PRIVDWELLCOMP= oeq.correlation(
    const= -0.00352036390092,
    a=     0.00501006910544,
    b=     -0.000436116039481,
    c=     -0.000303172760381,
    d=     4.66056854617e-05,
    mode= "log")
    # OeQ autogenerated correlation for 'Buildings with housing owned by other private companies'
    BLD_OWNER_OTHERPRIVCOMP= oeq.correlation(
    const= 5.2083798971e-05,
    a=     0.00594480102356,
    b=     -0.00189094906311,
    c=     0.000167059857312,
    mode= "log")
    # OeQ autogenerated correlation for 'Buildings with housing owned by government'
    BLD_OWNER_GOV= oeq.correlation(
    const= 0.00125717232549,
    a=     3.53179848584e-06,
    b=     -2.32282383087e-09,
    c=     4.87405593612e-13,
    mode= "lin")
    # OeQ autogenerated correlation for 'Buildings with housing owned by nongovernment organisations'
    BLD_OWNER_ORG= oeq.correlation(
    const= -0.00178904938759,
    a=     0.00356828920262,
    b=     -0.000892835212844,
    c=     7.13734965882e-05,
    mode= "log")

    return dict(BLD_OWNER_ASSOC=BLD_OWNER_ASSOC.lookup(*xin),
    BLD_OWNER_PRIV=BLD_OWNER_PRIV.lookup(*xin),
    BLD_OWNER_BUILDSOC=BLD_OWNER_BUILDSOC.lookup(*xin),
    BLD_OWNER_MUNDWELLCOMP=BLD_OWNER_MUNDWELLCOMP.lookup(*xin),
    BLD_OWNER_PRIVDWELLCOMP=BLD_OWNER_PRIVDWELLCOMP.lookup(*xin),
    BLD_OWNER_OTHERPRIVCOMP=BLD_OWNER_OTHERPRIVCOMP.lookup(*xin),
    BLD_OWNER_GOV=BLD_OWNER_GOV.lookup(*xin),
    BLD_OWNER_ORG=BLD_OWNER_ORG.lookup(*xin)
