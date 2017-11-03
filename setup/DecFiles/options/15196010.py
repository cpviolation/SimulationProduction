# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15196010.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 15196010
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> p+ K- pi+) (D*(2010)- -> pi- (D~0 -> K+ pi-))]cc
#
from Configurables import Generation
Generation().EventType = 15196010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcDst,pKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]