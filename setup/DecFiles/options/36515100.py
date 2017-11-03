# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/36515100.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 36515100
#
# ASCII decay Descriptor: [Omega- -> (Xi*0 -> (Xi-  -> (Lambda0 -> p+ pi-)  pi-) pi+) anti-nu_mu  mu-]cc
#
from Configurables import Generation
Generation().EventType = 36515100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omega_XiStarmunu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 3334,-3334 ]