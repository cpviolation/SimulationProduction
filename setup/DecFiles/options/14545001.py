# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14545001.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 14545001
#
# ASCII decay Descriptor: [B_c+ -> (JPsi -> mu+ mu-) (tau+ -> pi+ pi+ pi- anti-nu_tau) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 14545001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiTauNu=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"