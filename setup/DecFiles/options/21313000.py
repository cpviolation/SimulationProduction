# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21313000.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 21313000
#
# ASCII decay Descriptor: [[D+ ==> (phi(1020) ==> e- mu+) pi+]CC, [D+ ==> (phi(1020) ==> e+ mu-) pi+]CC]
#
from Configurables import Generation
Generation().EventType = 21313000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_phipi,emu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]