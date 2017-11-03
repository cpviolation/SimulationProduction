# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16103430.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 16103430
#
# ASCII decay Descriptor: [Xi_b-  -> (Delta+ -> p+ pi0) K- K-]cc
#
from Configurables import Generation
Generation().EventType = 16103430
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_Delta+K-K-,p+pi0=phsp,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]