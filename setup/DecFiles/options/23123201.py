# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23123201.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 23123201
#
# ASCII decay Descriptor: [D_s- -> K- (pi0 -> e+ e- gamma)]cc
#
from Configurables import Generation
Generation().EventType = 23123201
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_K+pi0,eeg=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D_s+ -> ^K+ ( pi0 -> ^e+ ^e- gamma )]CC'
tightCut.Cuts      =    {
    '[e+]cc'  : ' inAcc & eCuts',
    '[K+]cc'  : ' inAcc & piCuts',
    '[D_s+]cc': ' Dcuts ' }
tightCut.Preambulo += [
    'inAcc = in_range ( 0.005, GTHETA, 0.400 ) ' , 
    'eCuts = ( (GPT > 50 * MeV) & ( GP > 600 * MeV))',
    'piCuts = ( (GPT > 200 * MeV) & ( GP > 600 * MeV))',
    'Dcuts = (GPT > 1000 * MeV)' ]
