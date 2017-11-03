# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164522.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 11164522
#
# ASCII decay Descriptor: [B0 -> (K_S0 -> pi+ pi-) (eta_c -> K+ K- (pi0 -> gamma gamma))]cc
#
from Configurables import Generation
Generation().EventType = 11164522
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etacKS,KKpi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]