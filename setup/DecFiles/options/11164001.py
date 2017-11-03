# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164001.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 11164001
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => K+ pi- pi-) pi+]cc, [[B0]os -> (D+ => K- pi+ pi+) pi-]cc}
#
from Configurables import Generation
Generation().EventType = 11164001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-pi+.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]