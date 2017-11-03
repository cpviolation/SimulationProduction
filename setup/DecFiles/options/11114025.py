# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11114025.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 11114025
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ mu- (rho0 -> pi+ pi-)]cc, [[B0]os -> mu- mu+ (rho0 -> pi- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11114025
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_rhomumu=PHSP,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]