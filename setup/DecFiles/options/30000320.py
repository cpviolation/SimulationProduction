# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/30000320.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 30000320
#
# ASCII decay Descriptor: pp => ?
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Perugia0.py" )
from Configurables import Generation
Generation().EventType = 30000320
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/minbias_Perugia0.dec"
Generation().MinimumBias.CutTool = ""