import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2520000/1A3DAE34-2B00-B14A-ACED-6C4F111ACE4E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2520000/2A7614CA-94CB-8F40-9D80-A007290B4BC3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2520000/6208ED3B-35DD-2847-A0E6-F5F681C7DD55.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2520000/68D7F556-2856-3642-BBEF-7B9EFF402FE6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2520000/95E8D068-7887-F648-855D-BAC09D73F593.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2520000/D5B63F2E-072A-754B-90B2-7D67BC88C7F5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2520000/EACA5674-1119-114E-B75B-C14A134EF09F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2520000/FB680289-DBC6-3B4D-B2C5-396572142424.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/20B40B4B-D514-BD4F-9822-EC4BB3E50C31.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/2530000/B29F43F4-609E-5F4B-B03C-266A9782EFD6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/049BC5A0-B2D3-F147-A3EB-EC589E22718D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/051CE5C6-16CB-2545-A6B3-E735EF9B19C8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/05B51CE3-D7EC-AD4F-ACC1-21BECC727464.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/0676868A-7984-E44D-BC9D-D143F9EE3150.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/06FC43B6-2725-1941-ACFD-EA666BFD5B2C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/073754B0-712D-7548-A5A3-FD26D32C9F20.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/0B0967D7-CC41-2441-A969-E3E9573DE319.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/0B5FF194-E876-8C4E-8929-C74C882F802C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/0B605142-C7FD-4744-B77E-A3A93AC94BC7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/1A010B6D-61D4-FC48-8BBA-C7F563A21A4B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/1BE82898-FA4E-D742-94F8-CD45F1740B7D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/24D95DAE-23F5-914B-8323-5C43A355F5A9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/27260866-7566-B54A-BF47-155E55271434.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/2769523C-0C4D-7D49-859D-577AA32A296B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/2BAF8C4D-1CB7-FA44-9306-BDC7F15DFA66.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/2E402060-8F13-5146-AE7C-BDB287427FD1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/2F800902-D0D6-EE47-B651-81AF80071F99.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/35ED553D-0B4F-1143-9752-5F6A89EF181A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/3C6EE007-BBA3-844C-B184-E3F0B022870B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/42BF4B0E-2C8A-9448-92A9-4C7599036473.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/53F5C51A-DA3A-E84C-8D72-093CE01B3D91.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/547A6086-378E-E34C-A9E3-A14FBE886030.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/604D5F2F-67E3-BD46-85AA-AA58FBCB48B1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/61D7323B-95DD-5C47-9944-1B263F4A2EB0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/63B4A37A-88D6-D649-BB79-36A2D5573B58.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/6C25C27D-F4D5-0945-B3EF-DF1433C4B12A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/70F41058-A26B-AE4C-A264-1F7057DC0B94.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/7452CA45-0ED8-0D4B-A12A-2EB4BE258258.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/7631E547-F1C7-6E4A-A849-94A416874C64.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/778548B9-B3CE-ED48-A049-98EB2A1F87B3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/79542887-5171-CB42-B026-BF9AABCA8189.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/8317D90F-1802-D64D-9C06-53B07C251794.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/85534AE7-ADA8-F74A-B502-B5963BAB3BFF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/86251C42-9658-854A-8834-63430E40B636.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/886DEE03-B300-E542-852B-5D0D163362F1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/91181094-6A4D-3645-9A8D-EF82EA4CD7C2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/9A0D36CF-389C-7C47-B09B-5396E0180469.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/9EBD6B96-5AFC-5648-ABBC-630472BEBEBC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/9F3FD87D-3AED-7E4B-8BD5-39A1635637D0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/9F897CF5-1D05-7542-B058-68E6DDAE3955.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/A0C92D50-CF31-064E-960A-BE41DAB7E30A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/A1E31CD2-579B-2C4A-9A16-B366EBBD0C2E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/A4CD58E7-3183-B444-8702-0521FA162193.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/AE7B571A-0B1D-2842-89CF-4F36F6A69DC5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/AE823C6F-2FBE-3F43-87E1-A434300BE525.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B1104DD1-2D9D-9041-A7A9-AF37EA99DA49.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B57333E6-0B14-D340-88C4-B6CA8FF11476.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B5B817B2-42D9-6443-9856-CD79EE8BE598.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B63D7243-1EA4-1C4A-9F1C-770B21A24FDD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B77108B3-9E16-6142-A98F-E4EC7E3C426C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/B7C2859A-8BDA-8648-9968-7991FC841679.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/BACA137C-A4C0-BA4A-A8A2-A478B6F0D12E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/BAD3BE94-D543-3848-BD58-A9AC515D4C74.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/C01EB883-4913-7F45-9AB0-D62D0B5294F9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/C442F9D7-39DD-004F-B1B5-68C81DAD82DE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/C803229A-F236-354C-A6BB-E85C527CD40A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/CBD622A2-49C2-4345-AB4F-65A28CEB93CB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/CF452D4D-A193-774A-99F6-CF1CBC7FE428.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/D5EE9680-A788-0C45-8A59-A423AA9C96C8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/D9958A69-C892-1845-AD13-6DCBBC436A1B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/DD672FD3-6A3E-CE43-9491-A43C32AC6C36.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/DD77F4B6-1772-2746-BB68-58EC3505DBC1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/E1F24263-3323-134F-87EB-A28BC6050C6E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/E6BD4DB2-09D4-6742-B5A0-79B739504C3A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/E9A7E491-E324-0D4E-A5B6-5AB22602D662.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/EBA71974-9051-154A-B4A3-9D071A3127BC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/F599B13B-C81C-B448-88B9-11A7612BE819.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/F9505593-2ECC-2B46-8503-F6A7FDCD244B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/260000/FDE56275-79F7-C349-862C-ABBB907FB62E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/0641C435-7DB8-9C47-8F55-6B326CD55606.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/0CE682DB-662A-D24E-82D3-F9825E189A4B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/0FFB8BC7-4B08-8C40-A417-84385DA7E948.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/10D0CA8F-42C6-674B-B02A-EB01003240A5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/154A8C14-DA30-904B-96A8-3B0FF56B5F19.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/17DD2B0E-CBC8-1140-9151-25D742546DE5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/254CC7F7-6058-9247-B39B-33EDAAADF95A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/35402514-8DA0-2C44-BCF4-33EC8F8449B6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/367660FA-7B65-3946-8C22-F8A1F3E7C84E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/3CC522F0-2FBD-C846-8F33-C9497BD336BB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/3E453790-8896-634C-A985-8507FA67AF16.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/3F19B1E5-3024-004F-8337-1C63A410C969.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/483BB832-6B79-8C49-A0D3-5CA5C9EA3F35.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/54636DF7-C939-D849-8240-3A5BCFCAD618.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/56A589CC-3B8F-294B-97D3-58B80EFA8DC7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/67DF66C2-5886-D343-8CC9-14B7216E5FE9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/6BAD0041-721F-5145-99BB-99B94BD7C0AA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/6CF310DF-AEB6-FA4A-885D-4AFE06CAD736.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/722CB37A-D53D-7744-AAFE-1D4963648592.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/76837629-0653-2B4C-AD04-51E882CBC00F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/791991BC-EDD3-974C-AF52-A3892A6FD675.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/7D4F6DB9-02DE-C748-A99C-717F92351176.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/82627736-C601-E64D-BF15-CC10760CF73F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/88ECADE7-789E-9843-BA50-1DB029951E4C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/9277B2AF-4E26-5349-B044-D95D3890B2A3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/A6BFC44A-9FBE-A74F-BE8C-01E3CC2C696F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/AADAAA0E-10EE-6F42-9AAB-C5C43FF6730C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/B7D20F1F-94E7-F147-9A9F-38191A1F6A8B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/BFF4B14B-A8F6-2E4A-A270-BDB714367835.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/C0440EAC-D171-CF4D-B7F7-4162834F7050.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/C1996F95-5DF0-DD4C-85A3-ECAB55A8C26E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/C4A95991-B8E5-454A-8BE6-D4E9D1B1A995.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/D65F2A1D-5FCF-9A41-95B2-430A200A3B5A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/E6648CE8-57F1-2742-B5A0-65222111A9CA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/EA2FF1EE-ED85-9148-8D31-BF4F05F33A98.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/F04201C7-FE0B-F844-A246-4093B3BC017C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/F0447C10-647D-6943-A653-428CB0722DB4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/F7516E03-92D9-3C4C-AF42-90B3A0942F67.root',
] )
