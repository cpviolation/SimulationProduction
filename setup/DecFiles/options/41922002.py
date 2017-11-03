# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/41922002.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 41922002
#
# ASCII decay Descriptor: pp -> ([W+ -> l nu_l]) ([W- -> l nu_l]) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/WWlnullnul=1l15GeV.py" )
from Configurables import Generation
Generation().EventType = 41922002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/WW_lnul,lnul=1l15GeV.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 15*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1