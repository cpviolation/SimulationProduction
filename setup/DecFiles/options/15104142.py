# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15104142.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 15104142
#
# ASCII decay Descriptor: [Lambda_b0  -> p+ p~- (Lambda0 -> p+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15104142
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambdapp=sqDalitz,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]