# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15296501.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 15296501
#
# ASCII decay Descriptor: [Lambda_b0 -> (X_1(3872) ->  (D0 -> K- pi+) (anti-D*0 -> (anti-D0 -> K+ pi-) pi0) ) (Lambda0 -> p+ pi-)]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 15296501
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_X38721++Lambda,D0barDst0,D0D0barPi0,Kpi=DecProdCut,pCut1600MeV.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]