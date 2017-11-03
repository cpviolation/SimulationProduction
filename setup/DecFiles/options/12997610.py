# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12997610.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 12997610
#
# ASCII decay Descriptor: {[B+ -> (D*- -> pi- (anti-D0 -> K+ pi-)) (D_s+ -> pi- pi+ pi+)... ]cc}
#
from Configurables import Generation
Generation().EventType = 12997610
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/B+_DstXc,Xc2hhhNneutrals_cocktail,upto5prongs=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
from Configurables import DaughtersInLHCb
Generation().SignalRepeatedHadronization.addTool( DaughtersInLHCb )
Generation().SignalRepeatedHadronization.DaughtersInLHCb.NeutralThetaMin = 0.
Generation().SignalRepeatedHadronization.DaughtersInLHCb.NeutralThetaMax = 10.
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "b2dst3piFilter" )
SignalFilter = Generation().b2dst3piFilter
SignalFilter.Code = "has( goodB  ) "
SignalFilter.Preambulo += [
"from GaudiKernel.SystemOfUnits import  MeV"
,"isB2cc = GDECTREE('[(Beauty & LongLived) --> (D*(2010)+ -> (D0 => K- pi+) pi+) pi- pi+  pi-  ...]CC')"
 ,"inAcc = (  0 < GPZ  )  &  ( 100 * MeV < GPT ) & in_range (  1.8    , GETA , 5.0 ) &  in_range (  0.005  , GTHETA  , 0.400  )"
,"nPi =  GCOUNT  ( ( 'pi+'  == GABSID  )  &  inAcc , HepMC.descendants   )"
,"nK  =  GCOUNT  ( ( 'K-'   == GABSID  )  &  inAcc , HepMC.descendants   )"
,"goodB  = isB2cc & ( 4.5 < nPi  ) & (  0.5 < nK  )"
   ]


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "DaughtersInLHCb"

pgun.addTool( Generation().SignalRepeatedHadronization.DaughtersInLHCb.clone() )

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 521,-521 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_521.root"
pgun.MomentumSpectrum.BinningVariables = "pteta"
pgun.MomentumSpectrum.HistogramPath = "h_pteta"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 12997610