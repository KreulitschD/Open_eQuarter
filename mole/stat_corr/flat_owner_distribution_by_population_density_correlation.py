# OeQ autogenerated correlation for 'Flat Owner Distribution in Correlation to the population density'

import math
import numpy as np
import oeqCorrelation as oeq
def get(*xin):

    # OeQ autogenerated correlation for 'Flats owned by assiciations in buildings with housing'
    FLT_OWNER_ASSOC= oeq.correlation(
    const= 0.0382406726621,
    a=     0.0536153782634,
    b=     -0.035134718078,
    c=     0.00829837639639,
    d=     -0.00052334363694,
    mode= "log")
    # OeQ autogenerated correlation for 'Flats owned by private persons in buildings with housing'
    FLT_OWNER_PRIV= oeq.correlation(
    const= 0.769540217551,
    a=     0.10771774888,
    b=     -0.0226050631117,
    c=     0.000482584575234,
    mode= "log")
    # OeQ autogenerated correlation for 'Flats owned by societies in buildings with housing'
    FLT_OWNER_BUILDSOC= oeq.correlation(
    const= 0.000497056078439,
    a=     7.15504094488e-05,
    b=     -3.51267523097e-08,
    c=     7.08970536512e-12,
    d=     -4.91258164829e-16,
    mode= "lin")
    # OeQ autogenerated correlation for 'Flats owned by muicipalities and municipal housing companies in buildings with housing '
    FLT_OWNER_MUNDWELLCOMP= oeq.correlation(
    const= 0.0208587742518,
    a=     2.36237985744e-05,
    b=     -1.14776836815e-08,
    c=     2.09228384381e-12,
    mode= "lin")
    # OeQ autogenerated correlation for 'Flats owned by private housing companies in buildings with housing'
    FLT_OWNER_PRIVDWELLCOMP= oeq.correlation(
    const= -0.0176152576183,
    a=     0.0247258035773,
    b=     -0.00839915003845,
    c=     0.000874716026183,
    mode= "log")
    # OeQ autogenerated correlation for 'Flats owned by other private companies in buildings with housing'
    FLT_OWNER_OTHERPRIVCOMP= oeq.correlation(
    const= -0.00793934343275,
    a=     0.014652185582,
    b=     -0.00414270576932,
    c=     0.000350180363826,
    mode= "log")
    # OeQ autogenerated correlation for 'Flats owned by government in buildings with housing'
    FLT_OWNER_GOV= oeq.correlation(
    const= -0.00228690737983,
    a=     1.79619828145e-05,
    b=     -9.77923788907e-09,
    c=     1.65709885572e-12,
    mode= "lin")
    # OeQ autogenerated correlation for 'Flats owned by nongovernment organisations in buildings with housing'
    FLT_OWNER_ORG= oeq.correlation(
    const= 0.0125586007218,
    a=     -0.0182576725727,
    b=     0.00813016941144,
    c=     -0.00134384709698,
    d=     7.64337974804e-05,
    mode= "log")

    return dict(FLT_OWNER_ASSOC=FLT_OWNER_ASSOC.lookup(*xin),
    FLT_OWNER_PRIV=FLT_OWNER_PRIV.lookup(*xin),
    FLT_OWNER_BUILDSOC=FLT_OWNER_BUILDSOC.lookup(*xin),
    FLT_OWNER_MUNDWELLCOMP=FLT_OWNER_MUNDWELLCOMP.lookup(*xin),
    FLT_OWNER_PRIVDWELLCOMP=FLT_OWNER_PRIVDWELLCOMP.lookup(*xin),
    FLT_OWNER_OTHERPRIVCOMP=FLT_OWNER_OTHERPRIVCOMP.lookup(*xin),
    FLT_OWNER_GOV=FLT_OWNER_GOV.lookup(*xin),
    FLT_OWNER_ORG=FLT_OWNER_ORG.lookup(*xin))

