# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/22264000.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 22264000
#
# ASCII decay Descriptor: [D0 -> K- pi- pi+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 22264000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_Kpipipi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]