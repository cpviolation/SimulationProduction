# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/30000044.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 30000044
#
# ASCII decay Descriptor: pp => [bbbar] ...
#
from Configurables import Generation
Generation().EventType = 30000044
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/minbias=HardScattering,pt60,pt120GeV,incl_b.dec"
Generation().MinimumBias.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/twobinAcc"

from Configurables import PythiaProduction
Generation().MinimumBias.addTool( PythiaProduction )
Generation().MinimumBias.PythiaProduction.Commands += ["pysubs ckin 3 60."]
Generation().MinimumBias.PythiaProduction.Commands += ["pysubs ckin 4 120."]
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "twobinAcc" )
tracksInAcc = Generation().twobinAcc
tracksInAcc.Code = "count ( isGoodB ) > 1"
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodB = ( ( 'b' == GABSID ) & ( GTHETA < 400.0*mrad ) & ( GPT > 5.0*GeV ) )" ]
