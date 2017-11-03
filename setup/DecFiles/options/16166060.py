# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16166060.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 16166060
#
# ASCII decay Descriptor: [ Xi_bc0 -> (Lambda_b -> (Lambda_c+ -> p K- pi+) pi-)  K- pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 16166060
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "GenXiccProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import GenXiccProduction
Generation().Special.addTool( GenXiccProduction )
Generation().Special.GenXiccProduction.BaryonState = "Xi_bc0"
Generation().Special.GenXiccProduction.Commands = ["mixevnt imix 1", "loggrade ivegasopen 0", "loggrade igrade 1", "vegasbin nvbin 300", "counter xmaxwgt 5000000", "confine pscutmin 0.0", "confine pscutmax 7.0"]
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xibc_LambdabKpi,Lambdacpi=DecProdCut.dec"
Generation().Special.CutTool = "XiccDaughtersInLHCb"
from Configurables import XiccDaughtersInLHCb
Generation().Special.addTool( XiccDaughtersInLHCb )
Generation().Special.XiccDaughtersInLHCb.BaryonState = Generation().Special.GenXiccProduction.BaryonState