# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15364010.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 15364010
#
# ASCII decay Descriptor: [Lb_b0 -> (Lambda_c+ -> p+ K- pi+) pi-]cc
#
from Configurables import Generation
Generation().EventType = 15364010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lcpi,pKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]