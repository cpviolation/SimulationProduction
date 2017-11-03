# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14165006.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 14165006
#
# ASCII decay Descriptor: [B_c+ -> ([B0]nos -> (D- -> K+ pi- pi-) pi+, [B0]os -> (D+ -> K- pi+ pi+) pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14165006
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bdpi+_Dpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"