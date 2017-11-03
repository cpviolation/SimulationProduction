# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164491.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 11164491
#
# ASCII decay Descriptor: {[[B0]nos => (D~0 => K+ pi- (pi0 -> gamma gamma)) p+ p~-]cc, [[B0]os => (D0 => K- pi+ (pi0 -> gamma gamma)) p~- p+]cc}
#
from Configurables import Generation
Generation().EventType = 11164491
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0ppbar,Kpipi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]