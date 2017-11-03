# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164032.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 11164032
#
# ASCII decay Descriptor: {[[B0]nos -> (D~0 -> pi+ pi-)(rho(770)0 -> pi+ pi-)]cc, [[B0]os -> (D0 -> pi- pi+) (rho(770)0 -> pi+ pi-)]cc}
#
from Configurables import Generation
Generation().EventType = 11164032
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0rho0,pipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]