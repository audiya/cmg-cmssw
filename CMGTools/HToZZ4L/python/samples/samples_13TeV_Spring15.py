import os

################## 
## Triggers for HLT_MC_SPRING15 and Run II
## Based on HLT_MC_SPRING15 and /frozen/2015/25ns14e33/v2.1/HLT/V1 and /frozen/2015/50ns_5e33/v2.1/HLT/V5
## Names with _50ns are unprescaled at 50ns but prescaled at 25ns
## Names with _run1 are for comparing Spring15 MC to 8 TeV data: they're the closest thing I could find to run1 triggers, they're prescaled or even excluded in data but should appear in MC.

triggers_mumu_run1   = ["HLT_Mu17_Mu8_v*","HLT_Mu17_TkMu8_DZ_v*"]
triggers_mumu = [ "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*", "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*" ]
triggers_mumu_sync = triggers_mumu[:]

triggers_ee_run1   = ["HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL*" ]
triggers_ee = [ "HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*" ]
triggers_ee_sync = [ "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*" ]

triggers_mue_run1 = [ "HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*", 
                      "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v*" ]
triggers_mue = [ "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v*",
                 "HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*" ]
triggers_mue_sync = [ "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*", 
                 "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*" ]

triggers_3e = [ "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v*" ]
triggers_3mu = [ "HLT_TripleMu_12_10_5_v*" ]
triggers_2mu1e = [ "HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v*" ]
triggers_2e1mu = [ "HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v*" ]

triggers_trilep = triggers_3e + triggers_3mu + triggers_2mu1e + triggers_2e1mu

triggers_1e      = [ 'HLT_Ele27_WP85_Gsf_v*', 'HLT_Ele27_WPLoose_Gsf_v*'  ]
triggers_1e_sync = [ "HLT_Ele32_eta2p1_WP75_Gsf_v*", "HLT_Ele32_eta2p1_WPLoose_Gsf_v*" ]

triggers_1mu     = [ 'HLT_IsoMu24_eta2p1_v*', 'HLT_IsoTkMu24_eta2p1_v*'  ]

triggers_signal_real = triggers_mumu + triggers_ee + triggers_mue + triggers_trilep + triggers_1e
triggers_signal_sync = triggers_mumu_sync + triggers_ee_sync + triggers_mue_sync + triggers_trilep + triggers_1e_sync
triggers_any = list(set(triggers_signal_real+triggers_signal_sync+triggers_1mu))

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

# GGH cross section from LHC Higgs XS WG: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt1314TeV?rev=15
GGHZZ4L = kreator.makeMCComponent("GGHZZ4L", "/GluGluHToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 0.01212) #43.92*2.76E-04)
QQHZZ4L = kreator.makeMCComponent("QQHZZ4L", "/VBF_HToZZTo4L_M125_13TeV_powheg_JHUgen_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 0.001034)# 3.748*2.76E-04)
# split in assing W+/(W+ + W-) = 0.6385 as at 8 TeV, to be updated
WpHZZ4L = kreator.makeMCComponent("WpHZZ4L", "/WplusH_HToZZTo4L_M125_13TeV_powheg-minlo-HWJ_JHUgen_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 0.0002339) # 1.38*0.6385*2.76E-04)
WmHZZ4L = kreator.makeMCComponent("WmHZZ4L", "/WminusH_HToZZTo4L_M125_13TeV_powheg-minlo-HWJ_JHUgen_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 0.0001471) # 1.38*(1-0.6385)*2.76E-04)
ZHZZ4LF = kreator.makeMCComponent("ZHZZ4LF", "/ZH_HToZZ_4LFilter_M125_13TeV_powheg-minlo-HZJ_JHUgen_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 0.000652) #0.8696*(3.70E-03+2.34E-02+2.76E-04)*0.15038)

H4L = [ GGHZZ4L, QQHZZ4L, WpHZZ4L, WmHZZ4L, ZHZZ4LF ]

# cross section from McM (powheg) 
ZZTo4L = kreator.makeMCComponent("ZZTo4L","/ZZTo4L_13TeV_powheg_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 1.256)
ZZTo4L_amc_v2 = kreator.makeMCComponent("ZZTo4L_amc_v2","/ZZTo4L_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 1.256)

# cross section from McM (MCFM)
GGZZTo2e2mu = kreator.makeMCComponent("GGZZTo2e2mu", "/GluGluToZZTo2e2mu_BackgroundOnly_13TeV_MCFM/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 0.00319364)
GGZZTo2e2tau = kreator.makeMCComponent("GGZZTo2e2tau", "/GluGluToZZTo2e2tau_BackgroundOnly_13TeV_MCFM/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 0.00319364)
GGZZTo2mu2tau = kreator.makeMCComponent("GGZZTo2mu2tau", "/GluGluToZZTo2mu2tau_BackgroundOnly_13TeV_MCFM/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 0.00319364)
GGZZTo4e = kreator.makeMCComponent("GGZZTo4e", "/GluGluToZZTo4e_BackgroundOnly_13TeV_MCFM/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 0.00158582)
GGZZTo4mu = kreator.makeMCComponent("GGZZTo4mu", "/GluGluToZZTo4mu_BackgroundOnly_13TeV_MCFM/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 0.00158582)
GGZZTo4tau = kreator.makeMCComponent("GGZZTo4tau", "/GluGluToZZTo4tau_BackgroundOnly_13TeV_MCFM/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 0.00158582)

GGZZTo2e2mu_v2 = kreator.makeMCComponent("GGZZTo2e2mu_v2", "/GluGluToZZTo2e2mu_BackgroundOnly_13TeV_MCFM/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 0.00319364)
GGZZTo2e2tau_v2 = kreator.makeMCComponent("GGZZTo2e2tau_v2", "/GluGluToZZTo2e2tau_BackgroundOnly_13TeV_MCFM/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 0.00319364)
GGZZTo2mu2tau_v2 = kreator.makeMCComponent("GGZZTo2mu2tau_v2", "/GluGluToZZTo2mu2tau_BackgroundOnly_13TeV_MCFM/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 0.00319364)
GGZZTo4e_v2 = kreator.makeMCComponent("GGZZTo4e_v2", "/GluGluToZZTo4e_BackgroundOnly_13TeV_MCFM/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 0.00158582)
#GGZZTo4mu_v2 = kreator.makeMCComponent("GGZZTo4mu_v2", "/GluGluToZZTo4mu_BackgroundOnly_13TeV_MCFM/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 0.00158582)
GGZZTo4tau_v2 = kreator.makeMCComponent("GGZZTo4tau_v2", "/GluGluToZZTo4tau_BackgroundOnly_13TeV_MCFM/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 0.00158582)


GGZZTo4L = [ GGZZTo4mu, #GGZZTo2e2mu, GGZZTo2e2tau, GGZZTo2mu2tau, GGZZTo4e, GGZZTo4tau,
             GGZZTo2e2mu_v2, GGZZTo2e2tau_v2, GGZZTo2mu2tau_v2, GGZZTo4e_v2, GGZZTo4tau_v2 ] # GGZZTo4mu_v2


### Z+jets inclusive (from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV)
DYJetsToLL_M50 = kreator.makeMCComponent("DYJetsToLL_M50", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/MINIAODSIM", "CMS", ".*root", 2008.*3)
DYJetsToLL_M50_v2 = kreator.makeMCComponent("DYJetsToLL_M50_v2", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 2008.*3)
DYJetsToLL_LO_M50 = kreator.makeMCComponent("DYJetsToLL_LO_M50", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 2008.*3)
DYJetsToLL_LO_M50_50ns = kreator.makeMCComponent("DYJetsToLL_LO_M50_50ns", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM", "CMS", ".*root", 2008.*3)

## Cross section from McM (aMC@NLO)
DYJetsToLL_M10to50 = kreator.makeMCComponent("DYJetsToLL_M10to50", "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 18610)
DYJets = [ DYJetsToLL_M50, DYJetsToLL_M10to50 ]

# cross section from McM (powheg)
WZTo3LNu = kreator.makeMCComponent("WZTo3LNu", "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 4.42965)

# cross section from StandardModelCrossSectionsat13TeV NNLO times BR=(3*0.108)**2
WWTo2L2Nu = kreator.makeMCComponent("WWTo2L2Nu", "/WWTo2L2Nu_13TeV-powheg/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 118.7*((3*0.108)**2) )

# TTbar cross section: MCFM with dynamic scale, StandardModelCrossSectionsat13TeV
TTLep = kreator.makeMCComponent("TTLep", "/TTTo2L2Nu_13TeV-powheg/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2))
TTLep_v2 = kreator.makeMCComponent("TTLep_v2", "/TTTo2L2Nu_13TeV-powheg/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2))

# Single top cross sections: https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
TToLeptons_tch = kreator.makeMCComponent("TToLeptons_tch", "/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", (136.05+80.97)*0.108*3) 
TToLeptons_sch = kreator.makeMCComponent("TToLeptons_sch", "/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", (7.20+4.16)*0.108*3)
TBar_tWch = kreator.makeMCComponent("TBar_tWch", "/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root",35.6)
T_tWch = kreator.makeMCComponent("T_tWch", "/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root",35.6)
SingleTop = [ TToLeptons_tch, TToLeptons_sch, TBar_tWch, T_tWch ]

### W+jets inclusive (from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV)
WJetsToLNu = kreator.makeMCComponent("WJetsToLNu","/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 20508.9*3)

mcSamples_25ns =  H4L + [ ZZTo4L ] + GGZZTo4L + DYJets + [ WZTo3LNu, WWTo2L2Nu, TTLep ] + SingleTop + [ WJetsToLNu ]

### ===== 50ns samples ====
DYJetsToLL_M50_50ns = kreator.makeMCComponent("DYJetsToLL_M50_50ns","/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v2/MINIAODSIM", "CMS", ".*root", 2008.*3)
DYJetsToLL_M10to50_50ns = kreator.makeMCComponent("DYJetsToLL_M10to50_50ns", "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM", "CMS", ".*root", 18610)
TTJets_50ns = kreator.makeMCComponent("TTJets_50ns", "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM", "CMS", ".*root", 831.76)
TTLep_50ns = kreator.makeMCComponent("TTLep_50ns", "/TTTo2L2Nu_13TeV-powheg/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v2/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2))
WJetsToLNu_50ns = kreator.makeMCComponent("WJetsToLNu_50ns","/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM", "CMS", ".*root", 20508.9*3)

mcSamples_50ns = [ DYJetsToLL_M50_50ns, DYJetsToLL_M10to50_50ns, TTJets_50ns, TTLep_50ns, WJetsToLNu_50ns ]

mcSamples = mcSamples_25ns + mcSamples_50ns

#-----------DATA---------------
dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"
#lumi: 12.21+7.27+0.134 = 19.62 /fb @ 8TeV
json=dataDir+'/json/Cert_Run2012ABCD_22Jan2013ReReco.json'
from CMGTools.TTHAnalysis.setup.Efficiencies import eff2012

json_25ns = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-258714_13TeV_PromptReco_Collisions15_25ns_JSON.txt'
json_50ns = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-255031_13TeV_PromptReco_Collisions15_50ns_JSON_v2.txt'

DoubleMuon_Run2015B_05Oct2015_50ns = kreator.makeDataComponent("DoubleMuon_Run2015B_05Oct2015_50ns", "/DoubleMuon/Run2015B-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
DoubleEG_Run2015B_05Oct2015_50ns = kreator.makeDataComponent("DoubleEG_Run2015B_05Oct2015_50ns", "/DoubleEG/Run2015B-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
MuonEG_Run2015B_05Oct2015_50ns = kreator.makeDataComponent("MuonEG_Run2015B_05Oct2015_50ns", "/MuonEG/Run2015B-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
SingleMuon_Run2015B_05Oct2015_50ns = kreator.makeDataComponent("SingleMuon_Run2015B_05Oct2015_50ns", "/SingleMuon/Run2015B-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
SingleElectron_Run2015B_05Oct2015_50ns = kreator.makeDataComponent("SingleElectron_Run2015B_05Oct2015_50ns", "/SingleElectron/Run2015B-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_50ns)

DoubleEG_Run2015B_Prompt_50ns = kreator.makeDataComponent("DoubleEG_Run2015B_Prompt_50ns", "/DoubleEG/Run2015B-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
DoubleMuon_Run2015B_Prompt_50ns = kreator.makeDataComponent("DoubleMuon_Run2015B_Prompt_50ns", "/DoubleMuon/Run2015B-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
MuonEG_Run2015B_Prompt_50ns = kreator.makeDataComponent("MuonEG_Run2015B_Prompt_50ns", "/MuonEG/Run2015B-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
SingleMuon_Run2015B_Prompt_50ns = kreator.makeDataComponent("SingleMuon_Run2015B_Prompt_50ns", "/SingleMuon/Run2015B-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
SingleElectron_Run2015B_Prompt_50ns = kreator.makeDataComponent("SingleElectron_Run2015B_Prompt_50ns", "/SingleElectron/Run2015B-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_50ns)

DoubleMuon_Run2015C_05Oct2015_50ns = kreator.makeDataComponent("DoubleMuon_Run2015C_05Oct2015_50ns", "/DoubleMuon/Run2015C_50ns-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
DoubleEG_Run2015C_05Oct2015_50ns = kreator.makeDataComponent("DoubleEG_Run2015C_05Oct2015_50ns", "/DoubleEG/Run2015C_50ns-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
MuonEG_Run2015C_05Oct2015_50ns = kreator.makeDataComponent("MuonEG_Run2015C_05Oct2015_50ns", "/MuonEG/Run2015C_50ns-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
SingleMuon_Run2015C_05Oct2015_50ns = kreator.makeDataComponent("SingleMuon_Run2015C_05Oct2015_50ns", "/SingleMuon/Run2015C_50ns-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
SingleElectron_Run2015C_05Oct2015_50ns = kreator.makeDataComponent("SingleElectron_Run2015C_05Oct2015_50ns", "/SingleElectron/Run2015C_50ns-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_50ns)

DoubleEG_Run2015C_Prompt_50ns = kreator.makeDataComponent("DoubleEG_Run2015C_Prompt_50ns", "/DoubleEG/Run2015C-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
DoubleMuon_Run2015C_Prompt_50ns = kreator.makeDataComponent("DoubleMuon_Run2015C_Prompt_50ns", "/DoubleMuon/Run2015C-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
MuonEG_Run2015C_Prompt_50ns = kreator.makeDataComponent("MuonEG_Run2015C_Prompt_50ns", "/MuonEG/Run2015C-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
SingleMuon_Run2015C_Prompt_50ns = kreator.makeDataComponent("SingleMuon_Run2015C_Prompt_50ns", "/SingleMuon/Run2015C-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_50ns)
SingleElectron_Run2015C_Prompt_50ns = kreator.makeDataComponent("SingleElectron_Run2015C_Prompt_50ns", "/SingleElectron/Run2015C-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_50ns)

data_50ns_05Oct2015 = [ 
    DoubleMuon_Run2015B_05Oct2015_50ns, DoubleEG_Run2015B_05Oct2015_50ns, MuonEG_Run2015B_05Oct2015_50ns, SingleMuon_Run2015B_05Oct2015_50ns, SingleElectron_Run2015B_05Oct2015_50ns,
    DoubleMuon_Run2015C_05Oct2015_50ns, DoubleEG_Run2015C_05Oct2015_50ns, MuonEG_Run2015C_05Oct2015_50ns, SingleMuon_Run2015C_05Oct2015_50ns, SingleElectron_Run2015C_05Oct2015_50ns
]
data_50ns_prompt = [
    DoubleMuon_Run2015B_Prompt_50ns, DoubleEG_Run2015B_Prompt_50ns, MuonEG_Run2015B_Prompt_50ns, SingleMuon_Run2015B_Prompt_50ns, SingleElectron_Run2015B_Prompt_50ns,
    DoubleMuon_Run2015C_Prompt_50ns, DoubleEG_Run2015C_Prompt_50ns, MuonEG_Run2015C_Prompt_50ns, SingleMuon_Run2015C_Prompt_50ns, SingleElectron_Run2015C_Prompt_50ns
]
data_50ns = data_50ns_05Oct2015
data_50ns_all = data_50ns + data_50ns_prompt

DoubleEG_Run2015C_Prompt_25ns = kreator.makeDataComponent("DoubleEG_Run2015C_Prompt_25ns", "/DoubleEG/Run2015C-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_25ns)
DoubleMuon_Run2015C_Prompt_25ns = kreator.makeDataComponent("DoubleMuon_Run2015C_Prompt_25ns", "/DoubleMuon/Run2015C-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_25ns)
MuonEG_Run2015C_Prompt_25ns = kreator.makeDataComponent("MuonEG_Run2015C_Prompt_25ns", "/MuonEG/Run2015C-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_25ns)
SingleMuon_Run2015C_Prompt_25ns = kreator.makeDataComponent("SingleMuon_Run2015C_Prompt_25ns", "/SingleMuon/Run2015C-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_25ns)
SingleElectron_Run2015C_Prompt_25ns = kreator.makeDataComponent("SingleElectron_Run2015C_Prompt_25ns", "/SingleElectron/Run2015C-PromptReco-v1/MINIAOD", "CMS", ".*root", json=json_25ns)

DoubleMuon_Run2015D_05Oct2015_25ns = kreator.makeDataComponent("DoubleMuon_Run2015D_05Oct2015_25ns", "/DoubleMuon/Run2015D-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_25ns)
DoubleEG_Run2015D_05Oct2015_25ns = kreator.makeDataComponent("DoubleEG_Run2015D_05Oct2015_25ns", "/DoubleEG/Run2015D-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_25ns)
MuonEG_Run2015D_05Oct2015_25ns = kreator.makeDataComponent("MuonEG_Run2015D_05Oct2015_25ns", "/MuonEG/Run2015D-05Oct2015-v2/MINIAOD", "CMS", ".*root", json=json_25ns)
SingleMuon_Run2015D_05Oct2015_25ns = kreator.makeDataComponent("SingleMuon_Run2015D_05Oct2015_25ns", "/SingleMuon/Run2015D-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_25ns)
SingleElectron_Run2015D_05Oct2015_25ns = kreator.makeDataComponent("SingleElectron_Run2015D_05Oct2015_25ns", "/SingleElectron/Run2015D-05Oct2015-v1/MINIAOD", "CMS", ".*root", json=json_25ns)

MuonEG_Run2015D_PromptV3_25ns = kreator.makeDataComponent("MuonEG_Run2015D_PromptV3_25ns", "/MuonEG/Run2015D-PromptReco-v3/MINIAOD", "CMS", ".*root", json=json_25ns)
DoubleEG_Run2015D_PromptV3_25ns = kreator.makeDataComponent("DoubleEG_Run2015D_PromptV3_25ns", "/DoubleEG/Run2015D-PromptReco-v3/MINIAOD", "CMS", ".*root", json=json_25ns)
DoubleMuon_Run2015D_PromptV3_25ns = kreator.makeDataComponent("DoubleMuon_Run2015D_PromptV3_25ns", "/DoubleMuon/Run2015D-PromptReco-v3/MINIAOD", "CMS", ".*root", json=json_25ns)
SingleMuon_Run2015D_PromptV3_25ns = kreator.makeDataComponent("SingleMuon_Run2015D_PromptV3_25ns", "/SingleMuon/Run2015D-PromptReco-v3/MINIAOD", "CMS", ".*root", json=json_25ns)
SingleElectron_Run2015D_PromptV3_25ns = kreator.makeDataComponent("SingleElectron_Run2015D_PromptV3_25ns", "/SingleElectron/Run2015D-PromptReco-v3/MINIAOD", "CMS", ".*root", json=json_25ns)

run_range = [ 258159, 258714 ]
DoubleMuon_Run2015D_PromptV4_25ns = kreator.makeDataComponent("DoubleMuon_Run2015D_PromptV4_25ns", "/DoubleMuon/Run2015D-PromptReco-v4/MINIAOD", "CMS", ".*root", json=json_25ns, run_range=run_range)
DoubleEG_Run2015D_PromptV4_25ns = kreator.makeDataComponent("DoubleEG_Run2015D_PromptV4_25ns", "/DoubleEG/Run2015D-PromptReco-v4/MINIAOD", "CMS", ".*root", json=json_25ns, run_range=run_range)
MuonEG_Run2015D_PromptV4_25ns = kreator.makeDataComponent("MuonEG_Run2015D_PromptV4_25ns", "/MuonEG/Run2015D-PromptReco-v4/MINIAOD", "CMS", ".*root", json=json_25ns, run_range=run_range)
SingleMuon_Run2015D_PromptV4_25ns = kreator.makeDataComponent("SingleMuon_Run2015D_PromptV4_25ns", "/SingleMuon/Run2015D-PromptReco-v4/MINIAOD", "CMS", ".*root", json=json_25ns, run_range=run_range)
SingleElectron_Run2015D_PromptV4_25ns = kreator.makeDataComponent("SingleElectron_Run2015D_PromptV4_25ns", "/SingleElectron/Run2015D-PromptReco-v4/MINIAOD", "CMS", ".*root", json=json_25ns, run_range=run_range)

data_25ns = [
    DoubleMuon_Run2015D_05Oct2015_25ns, DoubleEG_Run2015D_05Oct2015_25ns, SingleMuon_Run2015D_05Oct2015_25ns, SingleElectron_Run2015D_05Oct2015_25ns, MuonEG_Run2015D_05Oct2015_25ns,
    DoubleMuon_Run2015D_PromptV4_25ns, DoubleEG_Run2015D_PromptV4_25ns, MuonEG_Run2015D_PromptV4_25ns, SingleMuon_Run2015D_PromptV4_25ns, SingleElectron_Run2015D_PromptV4_25ns,
]
data_25ns_all = data_25ns + [
    MuonEG_Run2015D_PromptV3_25ns,
    DoubleMuon_Run2015D_PromptV3_25ns, DoubleEG_Run2015D_PromptV3_25ns, SingleElectron_Run2015D_PromptV3_25ns, SingleMuon_Run2015D_PromptV3_25ns,
]

dataSamples = data_50ns + data_25ns
dataSamples_all = data_50ns_all + data_25ns_all

#Define splitting
for comp in mcSamples:
    comp.splitFactor = 250 
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012

for comp in dataSamples_all:
    comp.splitFactor = 2000

DatasetsAndTriggers = []
DatasetsAndTriggers.append( ("DoubleMuon", triggers_mumu + triggers_3mu) )
DatasetsAndTriggers.append( ("DoubleEG",   triggers_ee + triggers_3e) )
DatasetsAndTriggers.append( ("MuonEG",     triggers_mue + triggers_2mu1e + triggers_2e1mu) )
DatasetsAndTriggers.append( ("SingleElectron", triggers_1e) )
DatasetsAndTriggers.append( ("SingleMuon", triggers_1mu) )
vetos = []
for pd,triggers in DatasetsAndTriggers:
    for comp in dataSamples_all:
        if pd in comp.dataset:
            comp.triggers = triggers[:]
            comp.vetoTriggers = vetos[:]
    vetos += triggers
    
if __name__ == '__main__':
    if False:
        from CMGTools.Production.cacheChecker import CacheChecker
        checker = CacheChecker()
        for d in dataSamples_all:
            if "Prompt" in d.dataset:
                checker.checkComp(d, verbose=True)
