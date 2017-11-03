# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11196011.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11196011
#
# ASCII decay Descriptor: [B0 -> D*(2010)- D0 K+]cc
#
from Configurables import Generation
Generation().EventType = 11196011
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstD0K,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]