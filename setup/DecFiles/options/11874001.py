# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11874001.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11874001
#
# ASCII decay Descriptor: {[[B0]nos => nu_mu mu+ (D*(2010)- -> pi- (D~0 -> K+ pi-))]cc, [[B0]os => anti_nu_mu mu- (D*(2010)+ -> pi+ (D0 -> K- pi+))]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/D0muInAcc.py" )
from Configurables import Generation
Generation().EventType = 11874001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstmunu,Kpi=cocktail,D0muInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "ListOfDaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]