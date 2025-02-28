import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/100000/420C5CCF-D235-D241-8185-12819ACB151C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/16A09334-E800-9F43-8660-53AC737FDBA0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/65E3A0AA-272B-FB4E-93BB-C6852BED0E53.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/7999F6FD-CFD7-BA48-85B6-80BA90319213.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/B925B6A2-45B4-0543-9DD0-23703A946FF6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/FBD71841-4F94-B94F-B2BC-A99B3695963D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/3CC1A90C-F5D0-084D-9C72-0AE3D658B09B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/005A59A7-F583-C04C-B958-601A3BC85997.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/0EAA5758-A89F-DC49-B48A-0B3551599BC6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/1082DC4E-9994-DE41-B259-6FC03CA0DE77.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/1B5AA399-3FB8-F340-B01E-CB4B7D947194.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/24B95EEA-6EE6-4441-AF4F-830B8C1B7F57.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/27C0DD21-48EC-E343-BDA5-5A89EA6224A9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/2F4D2D84-3DB9-174F-A211-7979D37F2FA3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/31287684-DE95-EB43-9C8D-B2FBBE73C5E6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/387F8DA0-CC45-7E4F-8CBB-C68924DD202E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/3BE08451-93BA-9F40-8BFB-7E2041BE8E0D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/3E4841EE-DC64-4E42-8FB3-806D5E9C256A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/3E49EF00-F931-8B41-AFD7-AC705EFED1D5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/412847F8-48AA-0A4F-A97D-1B18276E2FF0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/43420689-CC0E-7747-BBD4-30B38FEF5A5F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/43EA10CB-5273-1443-8EF9-536E6AFDE6A6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/45561A48-073C-344C-873A-83DCA44D79FF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/45579A1D-43CF-EF41-99C7-B2680E0C6F2F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/4A1E2C9A-80D3-E944-BCB8-CDD025D55D66.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/4CA473D3-54BF-2E40-A463-DB0907A07FC4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/58EEE557-A864-3542-AB86-B45F350C8C6B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/59AA9623-0A0A-BB47-85E1-3FAC275BF085.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/59AC6463-0CAD-474C-B508-9D2C07EBC01E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/5BED6BE4-943B-0B48-B82D-34F23A120407.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/5EDFF429-C052-044E-985E-049E8390BA87.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/648F4DE0-8D70-3C4B-9555-62CAFC7D31E1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/67E4AD35-EA5C-504A-86BC-A50095CF70FC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/68187E0E-116A-0642-B177-005CF7E1BAD1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/6F6F85DF-2597-C94E-962D-8597E523A878.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/72F5433F-3532-7040-90BD-770D6A79072E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/736D4EE6-3F07-524E-92FB-A894F29AF05B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/74ED1030-33C4-CA40-9C69-B8966314B981.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/77A2A386-A45F-FD43-B43C-1ABB54DCDE63.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/7854964C-3054-3746-90E6-1610A948F63B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/7D27DC74-F778-D142-9905-A5BEA1ABCE33.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/7E1BC932-EBE3-FF47-8C94-DA913B3EDA19.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/806AE990-2BDE-A04A-8BBF-09E70BCF6D85.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/83150D5B-494E-C844-B3B3-4CB1417DC120.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/914F461C-0872-7847-8965-E5A504DF30CA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/922EAC67-8705-8E49-ADC1-A90AA1137721.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/9283E293-0A88-BC4F-B1A8-165CD47C5822.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/949CED50-8FBC-5043-A87E-678EA839DBA3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/971484E0-49C9-C545-9342-1593F6F2EFB5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/991FFB3D-93CC-2042-ADD0-F29FD82C349D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/9E48368D-4530-4F49-802C-FBF868CFC07A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/A49F84EA-0439-884F-8D6A-81536DB4A6C2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/A73A25F2-1E7F-0848-A7DA-9687B169FBA4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/A7EC75B9-978E-C84B-9BE5-E96D8B2C1D96.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/B1C72631-A453-224B-BCA0-4DBC36FCAB59.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/B4BFCCB8-C776-584C-A2CC-1BD320F88424.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/BC334D51-B776-9D4C-B517-99FEEB9F467F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/C03C4F48-EAF9-104C-A83E-229CA8A610E5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/C2E50808-8424-F54A-B79D-1CED581B74E3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/C35FEC77-684B-3E41-A5C1-5F72F3755488.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/C8ED7E80-AD95-5A48-9281-921CD26E4715.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/CE3CB481-69BC-1740-AC4B-0A4F3008CB28.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/D39C1136-B681-1E4B-B5AE-17A8B00D2C91.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/D3D08D71-A4D9-1043-9CDA-D6D729FDF860.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/D7CF5D95-57CF-444F-AED8-0079BEC3811C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/D8287A13-D6B3-514B-B5D8-25C3AC76AEC7.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/E3C12C3A-F5FD-004C-A512-DE81E634DEDF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/E9E81FC4-795F-4945-8A7B-30423082C1C4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/EAE70A0C-A4EA-4348-B1B4-7B0E0EC4D65B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/EBADA444-C28E-7D4D-A1DF-7D7F770B2C50.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/EF878C6C-0F9A-5745-A5B2-BAD3BF8B7BAF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/F022434C-F3C5-B448-8B33-F9C1ED75511D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/F49A2857-7016-824E-A80B-91B5A2C85261.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/F5B917C1-45F3-3147-B782-83D4043A1480.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/FB08644B-CBDE-8D4A-A249-1BC6AAF10BC9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/A684EF0E-6B8B-6942-AF00-43B5CA61988E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/D74446FB-171A-4C41-9DAC-4662441C2188.root',
] )
