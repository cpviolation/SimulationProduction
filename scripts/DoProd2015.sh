#!/bin/bash

#from https://its.cern.ch/jira/browse/LHCBGAUSS-964
#Stripping 24

# 1 = EvtType
# 2 = nbr of evts
# 3 = Polarity
# 4 = muDST

Optfile=$1
Nevents=$2
Polarity=$3
RunNumber=$4

if [ "$Polarity" == "MagUp" ]; then
	SimCond=Gauss/Beam6500GeV-mu100-2015-nu1.6.py
	DBtag="sim-20160606-vc-md100"
elif [ "$Polarity" == "MagDown" ]; then
	SimCond=Gauss/Beam6500GeV-md100-2015-nu1.6.py
	DBtag="sim-20160606-vc-mu100"
else
	echo "Error, Polarity '$3' is not valid!" 
	exit 1
fi

# Prepare conditions
echo "from Configurables import LHCbApp" >> Conditions.py
echo 'LHCbApp().DDDBtag   = "dddb-20150724"' >> Conditions.py
echo "LHCbApp().CondDBtag = '$DBtag'" >> Conditions.py

#-------------# 
#   GAUSS     #
#-------------#


export CMTCONFIG=x86_64-slc6-gcc48-opt
source LbLogin.sh -c x86_64-slc6-gcc48-opt
source SetupProject.sh Gauss v49r3

# Prepare files
echo "from Gauss.Configuration import *" >> Gauss-Job.py
echo "GaussGen = GenInit('GaussGen')"    >> Gauss-Job.py
echo "GaussGen.FirstEventNumber = 1"     >> Gauss-Job.py
echo "GaussGen.RunNumber = $RunNumber"   >> Gauss-Job.py
echo "LHCbApp().EvtMax = $Nevents"       >> Gauss-Job.py

# Run
gaudirun.py $APPCONFIGOPTS/$SimCond $APPCONFIGOPTS/Gauss/DataType-2015.py $APPCONFIGOPTS/Gauss/RICHRandomHits.py $LBPYTHIA8ROOT/options/Pythia8.py $APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py $APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py $Optfile Conditions.py Gauss-Job.py

# Prepare output
mv `ls *.sim` Gauss.sim
rm Gauss-Job.py

#-------------#
#   BOOLE     #
#-------------#

export CMTCONFIG=x86_64-slc6-gcc48-opt
source LbLogin.sh -c x86_64-slc6-gcc48-opt
source SetupProject.sh Boole v30r1 --use "AppConfig v3r266"

# Prepare files
echo "from Gaudi.Configuration import *" >> Boole-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Gauss.sim' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> Boole-Files.py

# Run
gaudirun.py $APPCONFIGOPTS/Boole/Default.py $APPCONFIGOPTS/Boole/DataType-2015.py $APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py $APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py Conditions.py Boole-Files.py

rm Gauss.sim
rm Boole-Files.py


#------------#
#     L0     #
#------------#

#Prepare special conditions
echo "from Gaudi.Configuration import *" > L0Configuration.py
echo "from Configurables import L0App" >> L0Configuration.py
echo 'L0App().outputFile="L0.digi"' >> L0Configuration.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Boole.digi' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> L0Configuration.py
# Run
lb-run Moore/v24r2 gaudirun.py $APPCONFIGOPTS/L0App/L0AppSimProduction.py $APPCONFIGOPTS/L0App/L0AppTCK-0x00a2.py $APPCONFIGOPTS/L0App/ForceLUTVersionV8.py $APPCONFIGOPTS/L0App/DataType-2015.py $APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py L0Configuration.py

rm Boole.digi
rm L0Configuration.py

#------------#
#   MOORE    #
#------------#

# Prepare special conditions
echo "from Gaudi.Configuration import *" > MooreConfiguration.py
echo "from Configurables import Moore" >> MooreConfiguration.py
echo "Moore().DDDBtag   = 'dddb-20150724'" >> MooreConfiguration.py
echo "Moore().CondDBtag = '$DBtag'" >> MooreConfiguration.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./L0.digi' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> MooreConfiguration.py
echo "Moore().outputFile = 'Moore.digi'" >> MooreConfiguration.py
# Run

lb-run Moore/v24r2 gaudirun.py \$APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep2015.py \$APPCONFIGOPTS/Conditions/TCK-0x411400a2.py \$APPCONFIGOPTS/Moore/DataType-2015.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py MooreConfiguration.py

rm L0.digi
rm MooreConfiguration.py

#-------------#
#   BRUNEL    #
#-------------#

# Prepare files
echo "from Gaudi.Configuration import *" >> Brunel-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Moore.digi' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> Brunel-Files.py

# Run
lb-run Brunel/v48r2 gaudirun.py \$APPCONFIGOPTS/Brunel/DataType-2015.py \$APPCONFIGOPTS/Brunel/MC-WithTruth.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py Brunel-Files.py Conditions.py

rm Moore.digi
rm Brunel-Files.py

#------------------------#
#   DAVINCI/STRIPPING    #
#------------------------#

# Prepare files
echo "from Gaudi.Configuration import *" >> DaVinci-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Brunel.dst' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> DaVinci-Files.py

# Run
lb-run DaVinci/v38r1p1 gaudirun.py \$APPCONFIGOPTS/DaVinci/DV-Stripping24-Stripping-MC-NoPrescaling.py \$APPCONFIGOPTS/DaVinci/DataType-2015.py \$APPCONFIGOPTS/DaVinci/InputType-DST.py Conditions.py DaVinci-Files.py

rm Brunel.dst
rm DaVinci-Files.py

rm *.root
rm *.py

rm test_catalog.xml
rm NewCatalog.xml

mv *AllStreams.dst ${Nevents}_events.dst

# Finish

# EOF