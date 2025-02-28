import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/295BC2BC-EDFA-384D-BB9D-392221C5196A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/4538AA5B-F605-FE44-BF79-EFD7E302D945.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/4E8296C6-0B74-5F44-9D37-7FB60B075BAA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/5A9D3195-BD5B-1B49-978D-2561D92E8057.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/7808865D-1581-B547-98E9-E2E63E51A2BB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/C2390145-5FF1-5E45-97B0-925095E9BAD9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/C7D7FC91-259F-DB4F-B4EC-00E8D34CF311.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/DA2A8B41-7B1D-1A46-BB18-FBF27F655707.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/FD817F37-A221-134A-83E9-10973C2BB817.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/011E9200-9399-BC4D-9D4D-2667A8337B1C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/03FDE737-4879-3C41-8240-0335B0EFCB34.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/05E80DB7-9949-D949-B4DF-2A0AF9314833.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/0B26AFAB-33A9-E849-99C6-79B165FB167D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/0C8C1B0B-2954-524C-ABF8-8CB2F70604F6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/10E36A5B-6DA8-C242-B17C-FE47A2791BA0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/14263269-12E1-F241-A6F5-F0479994B6F6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/1959CFA4-B25E-F146-A2FE-BC2BE2041D33.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/1AAA99F4-BDFF-3346-A594-EC9E97FA8E20.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/21B7E417-B96E-E246-8C99-B30795EC1064.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/2A9753DA-68AA-AB4B-A003-A0CE39367F5C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/31BA18A6-0EE1-A44C-AE7D-056E55D384B5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/387BA788-5EE0-6042-8606-35035E2AB550.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/3B2EB7B0-8978-994B-864F-B5510422444E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/3C702AD0-F337-834A-BC8C-C16FAB83D6C6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/3CD5D912-A488-604E-9E9E-2DA35BBC3753.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/40BFDE9C-F312-3D40-A319-AAFEF5223B56.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/449941AF-4017-8448-AEB5-76206A4B2A3C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/456355D3-102B-6F4E-B685-C926AD1AF3F0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/49139706-CF68-2244-994B-38AC527D4396.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/4DDB500D-D638-2D44-9505-A9440DD7F4F6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/5219D039-CF9C-F64D-829C-07983C95D202.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/57B41EF7-D0AE-2D4C-A59E-BBF3D1D7F699.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/5B5250A6-C458-7141-AADD-FB10D16987E1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/5BD74087-3B19-BF4C-B9EC-04587C807499.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/7242951F-57FA-0D4D-921C-2CB1DD55005C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/73C8FCE6-BA6E-184F-8273-41BDABE7D5AB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/773CB873-2683-2E40-8B48-157C3F015459.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/780B6EB1-E081-BC47-8199-F9CB5BA3A31E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/82308BD2-DA17-2540-9691-6FC9B6C7A531.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/940D7C36-C1A0-3345-AF29-D29AA8D0A717.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/9864976A-FCFF-8D42-B53B-D25129AA6E32.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/99218D67-5DC7-CF47-81C6-105C2A309645.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/9D41238D-9F30-334F-971B-CF294E0AB3A1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/A10961E7-0C59-7E47-B9AA-E6CD0758DA3A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/A41732A8-4360-E245-98EB-3C12E7CADF84.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/A75FC4F3-6BD6-F047-AD35-02ADBC8CD73A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/AC3B1C65-CADC-FA48-9CB4-F2E15F22F4FE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/BFB48783-9B5F-D849-A8D8-4A51B28E37CF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/C142C452-58B4-6043-8983-0779305C47FC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/D0A96546-6847-1A49-86B6-D9BA5C17B403.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/DD8F7884-F9B9-E243-BDBD-394F9906BF2C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/E32266AB-DD8C-8B47-927F-BEA750454E3C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/E61B1464-E398-FA43-B95F-2A2D10F95156.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/E676BA89-8342-154D-8506-5D6436CBAC98.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/EB33EBE7-827F-FB43-8780-64110C3DD1FB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/EC241E9A-4DBA-2945-A96A-E1ABEE0FB053.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/FD0A11E2-F016-2946-8F15-28731CB51A66.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/90128551-002C-1543-9090-6CD269E669D3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/9D3B5F9E-182F-204A-BD24-940DBEBA2AD5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/B5B3CFB2-D3C0-ED49-8C02-0347DBAC9983.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/80000/D754012D-1B56-444F-9662-1EC439E7359E.root',
] )
