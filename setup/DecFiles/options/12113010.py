# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12113010.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 12113010
#
# ASCII decay Descriptor: { B+ ->  (Higgs0 -> mu+ pi-) mu+, B- ->  (Higgs0 -> mu- pi+) mu- }
#
from Configurables import Generation
Generation().EventType = 12113010
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_MuMajoranaNeutrino2MuPi,m=3000MeV,t=10ps,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

from Gauss.Configuration import *
from Configurables import LHCb__ParticlePropertySvc as ParticlePropertySvc
from Configurables import Gauss, PrintMCTree, PrintMCDecayTreeTool, HistogramPersistencySvc, NTupleSvc, DumpHepMCDecay, DumpHepMCTree, GaussMonitor__CheckLifeTimeHepMC, GaussMonitor__CheckLifeTimeMC, GiGa, GiGaPhysListModular, GiGaHiggsParticles, GenerationToSimulation, PythiaProduction

ParticlePropertySvc().Particles = [ "H_10 87 25 0.0000 3.0000 1.0000e-11 Higgs0 25 0.0000" ]
ApplicationMgr().ExtSvc += [ ParticlePropertySvc() ]

gigaHiggsPart = GiGaHiggsParticles()
gigaHiggsPart.Higgses = ["H_10"] # H_10, H_20, H_30
GiGaPhysListModular("ModularPL").PhysicsConstructors += [ gigaHiggsPart ]


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "DaughtersInLHCb"

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
pgun.EventType = 12113010