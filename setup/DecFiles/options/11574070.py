# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11574070.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 11574070
#
# ASCII decay Descriptor: {[[B0]nos => nu_mu mu+ (D- -> K+ pi- pi-)]cc, [[B0]os => anti_nu_mu mu- (D+ -> K- pi+ pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11574070
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dststmunu,D+=CocktailHigher,RDplusCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D*(2640)+           759      100413  1.0        2.6492   4.70e-24                  D*(2S)+           0   0.5","D*(2640)-           760     -100413 -1.0        2.6492   4.70e-24                  D*(2S)-           0   0.5","D(2S)+              757      100411  1.0        2.579   3.69e-24                   D(2S)+           0   0.5","D(2S)-              758     -100411 -1.0        2.579   3.69e-24                   D(2S)-           0   0.5","D_1(2420)+          157       10413  1.0        2.978   3.50e-24                     D_1+       10413        0.5","D_1(2420)-          161      -10413 -1.0        2.978   3.50e-24                     D_1-      -10413        0.5","D*_2(2460)+         162         415  1.0        2.737   9.01660175e-24                    D_2*+         415        0.5","D*_2(2460)-         158        -415 -1.0        2.737   9.01660175e-24                   D_2*-        -415        0.5" ]

from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[ (Beauty) ==> ^(D- -> ^K+ ^pi- ^pi- {gamma} {gamma} {gamma}) ^mu+ nu_mu {X} {X} {X} {X} {X} {X} {X} {X} ]CC"
tightCut.Preambulo += [
 "from LoKiCore.functions import in_range"  ,
 "from GaudiKernel.SystemOfUnits import GeV, MeV"  ,
 "pipiKP     = GCHILD(GP,1) + GCHILD(GP,2) + GCHILD(GP,3)" ,
 "pipiKPT     = GCHILD(GPT,1) + GCHILD(GPT,2) + GCHILD(GPT,3)" ,
]
tightCut.Cuts      =    {
'[pi+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 150 * MeV )" ,
'[K-]cc'   : " in_range( 0.010 , GTHETA , 0.400 ) & ( GPT > 150 * MeV )" ,
'[mu+]cc'  : " in_range( 0.010 , GTHETA , 0.400 ) & (GP > 2500* MeV) ",
'[D+]cc'   : "( pipiKP > 15000 * MeV ) & (pipiKPT > 2300 * MeV)"
   }
