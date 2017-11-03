# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102221.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 11102221
#
# ASCII decay Descriptor: [B0 -> (rho0 -> pi+ pi-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 11102221
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_rhogamma,pipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]