# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166190.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 11166190
#
# ASCII decay Descriptor: {[[B0]nos -> (D_s- => pi+ pi- pi-) (K*(892)+-> (K_S0->pi+ pi-) pi+)]cc, [[B0]os -> (D_s+ => pi- pi+ pi+)  (K*(892)- -> (K_S0->pi+ pi-) pi-)]cc}
#
from Configurables import Generation
Generation().EventType = 11166190
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DsKst,pipipi,KSpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]