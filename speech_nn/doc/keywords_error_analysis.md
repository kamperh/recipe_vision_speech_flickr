Analysis: Errors in Keyword Spotting
====================================


### VisionSpeechCNN, MFCC, max pooling

Model directory: models/train_visionspeech_cnn/989f00f30a

    -------------------------------------------------------------------------------
    Keyword: beach
    Current P@10: 0.9000
    Current P@N: 0.7706
    Current EER: 0.0671
    Top 10 utterances:  ['003_3398746625_5199beea71_4', '051_2183227136_8bb657846b_3', '005_1322323208_c7ecb742c6_0', '005_2603792708_18a97bac97_4', '045_2183227136_8bb657846b_1', '007_1456393634_74022d9056_4', '007_1343426964_cde3fb54e8_2', '116_561940436_64d6fc125d_4', '023_1456393634_74022d9056_2', '112_2559921948_06af25d566_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/561940436_64d6fc125d_4.wav [variant] *(an overweight woman and man have upset faces as they sit on a bench)
    -------------------------------------------------------------------------------
    Keyword: behind
    Current P@10: 0.0000
    Current P@N: 0.0156
    Current EER: 0.4035
    Top 10 utterances:  ['007_3413571342_b9855795e2_3', '120_70995350_75d0698839_1', '005_2901880865_3fd7b66a45_0', '143_2901880865_3fd7b66a45_2', '014_3162045919_c2decbb69b_3', '007_2914206497_5e36ac6324_0', '046_3631986552_944ea208fc_1', '077_3624327440_bef4f33f32_3', '040_3085667767_66041b202e_0', '004_2533424347_cf2f84872b_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3413571342_b9855795e2_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/70995350_75d0698839_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2901880865_3fd7b66a45_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2901880865_3fd7b66a45_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3162045919_c2decbb69b_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2914206497_5e36ac6324_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3631986552_944ea208fc_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3624327440_bef4f33f32_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3085667767_66041b202e_0.wav *(a surfer does a flip on a wave)
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2533424347_cf2f84872b_0.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: bike
    Current P@10: 0.3000
    Current P@N: 0.3883
    Current EER: 0.0866
    Top 10 utterances:  ['046_3347798761_5c5260b000_1', '046_3635577874_48ebaac734_4', '069_3670907052_c827593564_1', '049_3299820401_c2589186c5_0', '046_2924259848_effb4dcb82_2', '014_3670907052_c827593564_2', '070_3576259024_9c05b163aa_1', '007_2893374123_087f98d58a_1', '019_3485425825_c2f3446e73_4', '117_3299820401_c2589186c5_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3347798761_5c5260b000_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3635577874_48ebaac734_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3670907052_c827593564_1.wav [variant] *(a dirt biker flies through the air)
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3299820401_c2589186c5_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2924259848_effb4dcb82_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2893374123_087f98d58a_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3299820401_c2589186c5_3.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: black
    Current P@10: 1.0000
    Current P@N: 0.5203
    Current EER: 0.2079
    Top 10 utterances:  ['051_2933912528_52b05f84a1_1', '060_3259002340_707ce96858_0', '046_254295381_d98fa049f4_0', '038_3070011270_390e597783_1', '055_2599444370_9e40103027_0', '007_326456451_effadbbe49_0', '009_670609997_5c7fdb3f0b_2', '083_2933912528_52b05f84a1_2', '107_343218198_1ca90e0734_0', '038_2595186208_9b16fa0ee3_0']
    -------------------------------------------------------------------------------
    Keyword: boys
    Current P@10: 0.3000
    Current P@N: 0.1647
    Current EER: 0.1786
    Top 10 utterances:  ['096_2370481277_a3085614c9_0', '017_3596131692_91b8a05606_3', '052_3375991133_87d7c40925_2', '061_3119875880_22f9129a1c_3', '030_197504190_fd1fc3d4b7_3', '046_3596131692_91b8a05606_0', '099_3545652636_0746537307_3', '064_154871781_ae77696b77_4', '006_1572532018_64c030c974_3', '041_2370481277_a3085614c9_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3596131692_91b8a05606_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3375991133_87d7c40925_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3119875880_22f9129a1c_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/197504190_fd1fc3d4b7_3.wav [semantic] *(two children play soccer in the park)
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3596131692_91b8a05606_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3545652636_0746537307_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/154871781_ae77696b77_4.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: dogs
    Current P@10: 0.8000
    Current P@N: 0.6178
    Current EER: 0.1138
    Top 10 utterances:  ['025_3128164023_ebe8da4c32_3', '006_3582742297_1daa29968e_2', '004_3582742297_1daa29968e_4', '046_293327462_20dee0de56_3', '049_2933912528_52b05f84a1_0', '132_2358561039_e215a8d6cd_1', '017_2892995070_39f3c9a56e_4', '037_2594902417_f65d8866a8_4', '007_1786425974_c7c5ad6aa1_3', '011_317383917_d8bfa350b6_2']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2358561039_e215a8d6cd_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1786425974_c7c5ad6aa1_3.wav [variant] *(the black dog is sniffing the brown dog's butt)
    -------------------------------------------------------------------------------
    Keyword: field
    Current P@10: 0.9000
    Current P@N: 0.4925
    Current EER: 0.1343
    Top 10 utterances:  ['006_3582742297_1daa29968e_2', '016_2600867924_cd502fc911_1', '007_2534502836_7a75305655_3', '061_2856080862_95d793fa9d_2', '017_3545652636_0746537307_0', '006_2763044275_aa498eb88b_1', '007_3232470286_903a61ea16_4', '087_2573625591_70291c894a_2', '072_2763044275_aa498eb88b_4', '004_3582742297_1daa29968e_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3232470286_903a61ea16_4.wav [semantic] *(goal attempt during a soccer game being played on green grass)
    -------------------------------------------------------------------------------
    Keyword: hat
    Current P@10: 0.3000
    Current P@N: 0.2410
    Current EER: 0.2289
    Top 10 utterances:  ['042_754852108_72f80d421f_1', '024_421322723_3470543368_1', '006_3047264346_e24601bfbf_2', '033_2309860995_c2e2a0feeb_1', '004_421730441_6b2267fd31_1', '025_2124040721_bffc0a091a_1', '038_3080056515_3013830309_3', '127_2309860995_c2e2a0feeb_2', '042_3393926562_66cc01b001_4', '019_3503623999_bbd5dcfb18_2']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/754852108_72f80d421f_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/421322723_3470543368_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3047264346_e24601bfbf_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2309860995_c2e2a0feeb_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/421730441_6b2267fd31_1.wav [semantic] *(a man in a knit cap stands next to a brick wall)
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2309860995_c2e2a0feeb_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3393926562_66cc01b001_4.wav
    -------------------------------------------------------------------------------
    Keyword: jacket
    Current P@10: 0.2000
    Current P@N: 0.1266
    Current EER: 0.3073
    Top 10 utterances:  ['006_3123351642_3794f2f601_2', '007_485245061_5a5de43e20_3', '066_416960865_048fd3f294_3', '007_3320032226_63390d74a6_0', '006_422763475_0bc814dac6_2', '032_2100816230_ff866fb352_3', '004_1714316707_8bbaa2a2ba_0', '052_3214237686_6566b8b52f_4', '005_3182121297_38c99b2769_2', '017_2285570521_05015cbf4b_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3123351642_3794f2f601_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/485245061_5a5de43e20_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3320032226_63390d74a6_0.wav [semantic] *(a child dressed for the cold sits in the snow)
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/422763475_0bc814dac6_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2100816230_ff866fb352_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3214237686_6566b8b52f_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3182121297_38c99b2769_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2285570521_05015cbf4b_3.wav
    -------------------------------------------------------------------------------
    Keyword: large
    Current P@10: 0.3000
    Current P@N: 0.1633
    Current EER: 0.3283
    Top 10 utterances:  ['005_3227148358_f152303584_0', '049_226607225_44d696db6b_2', '020_3191135894_2b4bdabb6d_1', '054_226607225_44d696db6b_1', '017_3375070563_3c290a7991_2', '004_3375070563_3c290a7991_4', '042_2748729903_3c7c920c4d_3', '046_801607443_f15956d1ce_1', '009_3227148358_f152303584_4', '006_396360611_941e5849a3_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3227148358_f152303584_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3191135894_2b4bdabb6d_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3375070563_3c290a7991_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2748729903_3c7c920c4d_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/801607443_f15956d1ce_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3227148358_f152303584_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/396360611_941e5849a3_1.wav [semantic] *(a man stands on a rocky cliff overlooking a body of water)
    -------------------------------------------------------------------------------
    Keyword: looking
    Current P@10: 0.1000
    Current P@N: 0.0460
    Current EER: 0.3583
    Top 10 utterances:  ['025_3045613316_4e88862836_1', '006_396360611_941e5849a3_1', '019_470373679_98dceb19e7_3', '011_3325497914_f9014d615b_0', '049_3364861247_d590fa170d_2', '007_3506560025_8d0f4f9ac4_4', '100_1343426964_cde3fb54e8_4', '033_3530843182_35af2c821c_2', '023_2435685480_a79d42e564_3', '062_3074842262_62b1b2168c_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_1.wav [variant] *(three men are standing on a cliff overlooking mountains and the ocean)
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/396360611_941e5849a3_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/470373679_98dceb19e7_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3325497914_f9014d615b_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3364861247_d590fa170d_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1343426964_cde3fb54e8_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3530843182_35af2c821c_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2435685480_a79d42e564_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3074842262_62b1b2168c_1.wav
    -------------------------------------------------------------------------------
    Keyword: people
    Current P@10: 1.0000
    Current P@N: 0.6183
    Current EER: 0.1316
    Top 10 utterances:  ['025_3245912109_fdeef6b456_0', '049_1174629344_a2e1a2bdbf_1', '046_3468694409_a51571d621_1', '025_1472230829_803818a383_1', '057_160792599_6a7ec52516_1', '100_2295216243_0712928988_1', '087_2877503811_4e311253ec_3', '020_416788726_5b4eb1466e_1', '049_3245912109_fdeef6b456_1', '032_2176980976_7054c99621_2']
    -------------------------------------------------------------------------------
    Keyword: play
    Current P@10: 0.1000
    Current P@N: 0.1512
    Current EER: 0.2562
    Top 10 utterances:  ['099_3545652636_0746537307_3', '007_2587818583_4aa8e7b174_3', '043_3498997518_c2b16f0a0e_0', '042_241347760_d44c8d3a01_1', '025_2526041608_a9775ab8d7_1', '007_909191414_1cf5d85821_4', '056_3498997518_c2b16f0a0e_2', '017_3596131692_91b8a05606_3', '074_1402640441_81978e32a9_2', '064_154871781_ae77696b77_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3545652636_0746537307_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2587818583_4aa8e7b174_3.wav [variant] *(children playing in a ball pit)
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3498997518_c2b16f0a0e_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/241347760_d44c8d3a01_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2526041608_a9775ab8d7_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/909191414_1cf5d85821_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3498997518_c2b16f0a0e_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3596131692_91b8a05606_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1402640441_81978e32a9_2.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: runs
    Current P@10: 0.3000
    Current P@N: 0.1392
    Current EER: 0.2633
    Top 10 utterances:  ['049_416106657_cab2a107a5_2', '147_3294209955_a1f1e2cc19_1', '007_3540416981_4e74f08cbb_4', '007_1267711451_e2a754b4f8_1', '004_512101751_05a6d93e19_1', '017_2301525531_edde12d673_1', '049_317488612_70ac35493b_3', '007_317488612_70ac35493b_2', '007_468310111_d9396abcbd_0', '005_352382023_7605223d1c_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3540416981_4e74f08cbb_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1267711451_e2a754b4f8_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/512101751_05a6d93e19_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2301525531_edde12d673_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/317488612_70ac35493b_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/468310111_d9396abcbd_0.wav [variant] *(a black and white dog is running through a cow field)
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/352382023_7605223d1c_3.wav
    -------------------------------------------------------------------------------
    Keyword: sitting
    Current P@10: 0.8000
    Current P@N: 0.3353
    Current EER: 0.2526
    Top 10 utterances:  ['006_3597326009_3678a98a43_4', '046_1082379191_ec1e53f996_2', '150_3099923914_fd450f6d51_3', '003_2842865689_e37256d9ce_4', '026_3449114979_6cdc3e8da8_2', '006_324208502_674488bcea_4', '004_561940436_64d6fc125d_2', '005_561940436_64d6fc125d_0', '033_370713359_7560808550_4', '112_1258913059_07c613f7ff_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3597326009_3678a98a43_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3099923914_fd450f6d51_3.wav [semantic] *(two people are seated at a table with drinks)
    -------------------------------------------------------------------------------
    Keyword: standing
    Current P@10: 0.4000
    Current P@N: 0.2585
    Current EER: 0.2680
    Top 10 utterances:  ['025_3045613316_4e88862836_1', '005_2096771662_984441d20d_4', '017_3045613316_4e88862836_4', '161_2102360862_264452db8e_1', '020_533979933_a95b03323b_2', '038_3398746625_5199beea71_1', '006_160792599_6a7ec52516_2', '005_115684808_cb01227802_0', '118_160792599_6a7ec52516_0', '033_3694093650_547259731e_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav [variant] *(three men stand on a mountain looking at another)
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2102360862_264452db8e_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/533979933_a95b03323b_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3398746625_5199beea71_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/115684808_cb01227802_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/160792599_6a7ec52516_0.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: street
    Current P@10: 1.0000
    Current P@N: 0.5882
    Current EER: 0.1134
    Top 10 utterances:  ['023_3655964639_21e76383d0_3', '052_463978865_c87c6ca84c_1', '042_1332722096_1e3de8ae70_1', '150_3655964639_21e76383d0_4', '025_2248487950_c62d0c81a9_0', '007_880220939_0ef1c37f1f_1', '049_2182488373_df73c7cc09_4', '042_435827376_4384c3005a_3', '004_3442242092_e579538d82_1', '052_2075321027_c8fcbaf581_0']
    -------------------------------------------------------------------------------
    Keyword: white
    Current P@10: 1.0000
    Current P@N: 0.4941
    Current EER: 0.2316
    Top 10 utterances:  ['049_416106657_cab2a107a5_2', '007_249394748_2e4acfbbb5_0', '049_317488612_70ac35493b_3', '051_1084040636_97d9633581_2', '019_249394748_2e4acfbbb5_4', '058_3128164023_ebe8da4c32_4', '007_468310111_d9396abcbd_0', '025_2120411340_104eb610b1_2', '046_1674612291_7154c5ab61_3', '007_3540416981_4e74f08cbb_4']
    -------------------------------------------------------------------------------
    Keyword: yellow
    Current P@10: 0.6000
    Current P@N: 0.1912
    Current EER: 0.3088
    Top 10 utterances:  ['125_2479162876_a5ce3306af_3', '052_3406930103_4db7b4dde0_2', '007_1808370027_2088394eb4_2', '022_2654514044_a70a6e2c21_4', '007_2103568100_5d018c495b_3', '019_429851331_b248ca01cd_2', '024_246055693_ccb69ac5c6_4', '025_2945036454_280fa5b29f_4', '083_2345984157_724823b1e4_2', '046_486712504_36be449055_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3406930103_4db7b4dde0_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2103568100_5d018c495b_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2345984157_724823b1e4_2.wav *(a brown dog shaking off water)
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/486712504_36be449055_4.wav *(a tan dog jumping over a red and blue toy)
    -------------------------------------------------------------------------------
    Keyword: young
    Current P@10: 0.6000
    Current P@N: 0.3003
    Current EER: 0.2260
    Top 10 utterances:  ['086_1561658940_a947f2446a_0', '117_2450299735_62c095f40e_4', '051_542317719_ed4dd95dc2_3', '046_1561658940_a947f2446a_3', '090_3030566410_393c36a6c5_4', '052_3627011534_485f667b10_2', '017_3388330419_85d72f7cda_4', '025_2963573792_dd51b5fbfb_2', '004_3741462565_cc35966b7a_3', '017_1682079482_9a72fa57fa_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1561658940_a947f2446a_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2450299735_62c095f40e_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3030566410_393c36a6c5_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1682079482_9a72fa57fa_0.wav [semantic] *(a little girl on a kid swing)
    -------------------------------------------------------------------------------

Results:

- No. errors: 36
- No. variants: 31
- No. semantic: 24
- No. correct: 109
- Semantic P@10: 0.825



### VissionSpeechPSyC, MFCC, logsumexp pooling

Model directory: models/train_visionsig_psyc/d5cb9be08b

    -------------------------------------------------------------------------------
    Keyword: beach
    Current P@10: 0.9000
    Current P@N: 0.7824
    Current EER: 0.0828
    Top 10 utterances:  ['046_1499581619_a5f65a882c_1', '006_2295216243_0712928988_2', '049_2729655904_1dd01922fb_1', '006_1572532018_64c030c974_3', '004_1499581619_a5f65a882c_4', '005_3316725440_9ccd9b5417_1', '085_1499581619_a5f65a882c_3', '037_1982852140_56425fa7a2_4', '011_799486353_f665d7b0f0_0', '006_3569979711_6507841268_2']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3316725440_9ccd9b5417_1.wav
    -------------------------------------------------------------------------------
    Keyword: behind
    Current P@10: 0.0000
    Current P@N: 0.0156
    Current EER: 0.4825
    Top 10 utterances:  ['004_3263497678_8bb688ca01_4', '007_3159995270_17334ccb5b_1', '007_3301859683_2d5e4b40a3_0', '004_2914206497_5e36ac6324_1', '007_2914206497_5e36ac6324_0', '017_3624327440_bef4f33f32_4', '085_3159995270_17334ccb5b_2', '005_3182121297_38c99b2769_2', '004_2676764246_c58205a365_1', '017_2518508760_68d8df7365_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3263497678_8bb688ca01_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3159995270_17334ccb5b_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3301859683_2d5e4b40a3_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2914206497_5e36ac6324_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2914206497_5e36ac6324_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3624327440_bef4f33f32_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3159995270_17334ccb5b_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3182121297_38c99b2769_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2676764246_c58205a365_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2518508760_68d8df7365_4.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: bike
    Current P@10: 0.4000
    Current P@N: 0.3883
    Current EER: 0.1386
    Top 10 utterances:  ['070_3576259024_9c05b163aa_1', '097_3601843201_4809e66909_4', '052_2902269566_419d9f1d8e_0', '041_2813992915_f732cf8539_4', '017_2084217208_7bd9bc85e5_2', '014_3549583146_3e8bb2f7e9_2', '046_3364151356_eecd07a23e_1', '089_3601843201_4809e66909_0', '007_2544182005_3aa1332bf9_1', '004_2581066814_179d28f306_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3601843201_4809e66909_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2902269566_419d9f1d8e_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2813992915_f732cf8539_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3364151356_eecd07a23e_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3601843201_4809e66909_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2581066814_179d28f306_0.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: black
    Current P@10: 1.0000
    Current P@N: 0.6403
    Current EER: 0.1573
    Top 10 utterances:  ['024_3223055565_68973f5d20_2', '077_2398605966_1d0c9e6a20_0', '046_359837950_9e22ffe6c2_3', '049_3602838407_bf13e49243_0', '055_2599444370_9e40103027_0', '038_3070011270_390e597783_1', '055_1392272228_cf104086e6_0', '006_2763044275_aa498eb88b_1', '083_2933912528_52b05f84a1_2', '024_3642220260_3aa8a52670_2']
    -------------------------------------------------------------------------------
    Keyword: boys
    Current P@10: 0.1000
    Current P@N: 0.1647
    Current EER: 0.2024
    Top 10 utterances:  ['003_820169182_f5e78d7d19_2', '041_2370481277_a3085614c9_3', '064_154871781_ae77696b77_4', '061_2856080862_95d793fa9d_2', '005_3596131692_91b8a05606_4', '016_2370481277_a3085614c9_4', '077_3222055946_45f7293bb2_2', '049_3605061440_1d08c80a57_3', '017_3596131692_91b8a05606_3', '025_2189995738_352607a63b_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/820169182_f5e78d7d19_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/154871781_ae77696b77_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2856080862_95d793fa9d_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3596131692_91b8a05606_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2370481277_a3085614c9_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3222055946_45f7293bb2_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3605061440_1d08c80a57_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3596131692_91b8a05606_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2189995738_352607a63b_3.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: dogs
    Current P@10: 0.8000
    Current P@N: 0.5714
    Current EER: 0.1136
    Top 10 utterances:  ['043_2869491449_1041485a6b_2', '049_3333921867_6cc7d7c73d_2', '046_2300168895_a9b83e16fc_3', '066_2340206885_58754a799a_2', '024_3333921867_6cc7d7c73d_4', '026_3630641436_8f9ac5b9b2_1', '046_3223055565_68973f5d20_3', '049_3655155990_b0e201dd3c_0', '041_3224227640_31865b3651_2', '016_447111935_5af98563e3_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2300168895_a9b83e16fc_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3224227640_31865b3651_2.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: field
    Current P@10: 0.8000
    Current P@N: 0.3731
    Current EER: 0.1718
    Top 10 utterances:  ['049_2731171552_4a808c7d5a_1', '006_3582742297_1daa29968e_2', '016_2600867924_cd502fc911_1', '049_3223224391_be50bf4f43_0', '017_3545652636_0746537307_0', '007_2890113532_ab2003d74e_4', '006_2763044275_aa498eb88b_1', '005_246055693_ccb69ac5c6_2', '007_249394748_2e4acfbbb5_0', '037_2594902417_f65d8866a8_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2731171552_4a808c7d5a_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/246055693_ccb69ac5c6_2.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: hat
    Current P@10: 0.0000
    Current P@N: 0.0602
    Current EER: 0.3098
    Top 10 utterances:  ['041_1836335410_de8313a64e_3', '017_3506560025_8d0f4f9ac4_2', '092_3425851292_de92a072ee_1', '018_2529116152_4331dabf50_1', '055_2549968784_39bfbe44f9_0', '025_3532205154_5674b628ea_0', '161_3450874870_c4dcf58fb3_2', '016_2991575785_bd4868e215_4', '057_2856080862_95d793fa9d_1', '049_2666179615_f05a9d8331_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1836335410_de8313a64e_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3506560025_8d0f4f9ac4_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3425851292_de92a072ee_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2529116152_4331dabf50_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2549968784_39bfbe44f9_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3532205154_5674b628ea_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3450874870_c4dcf58fb3_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2991575785_bd4868e215_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2856080862_95d793fa9d_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2666179615_f05a9d8331_3.wav
    -------------------------------------------------------------------------------
    Keyword: jacket
    Current P@10: 0.0000
    Current P@N: 0.0253
    Current EER: 0.3913
    Top 10 utterances:  ['085_3159995270_17334ccb5b_2', '017_3139876823_859c7d7c23_3', '006_3287549827_04dec6fb6e_0', '096_57422853_b5f6366081_4', '005_3182121297_38c99b2769_2', '007_3159995270_17334ccb5b_1', '016_1472882567_33dc14c8b6_4', '117_1472882567_33dc14c8b6_3', '049_3301859683_2d5e4b40a3_2', '007_3301859683_2d5e4b40a3_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3159995270_17334ccb5b_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3139876823_859c7d7c23_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3287549827_04dec6fb6e_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/57422853_b5f6366081_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3182121297_38c99b2769_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3159995270_17334ccb5b_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1472882567_33dc14c8b6_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1472882567_33dc14c8b6_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3301859683_2d5e4b40a3_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3301859683_2d5e4b40a3_0.wav
    -------------------------------------------------------------------------------
    Keyword: large
    Current P@10: 0.1000
    Current P@N: 0.0408
    Current EER: 0.3459
    Top 10 utterances:  ['086_308487515_7852928f90_0', '005_3227148358_f152303584_0', '002_308487515_7852928f90_2', '033_3227148358_f152303584_3', '048_3567061016_62768dcce1_2', '033_801607443_f15956d1ce_4', '033_3217187564_0ffd89dec1_1', '005_3119875880_22f9129a1c_0', '111_3567061016_62768dcce1_1', '095_544576742_283b65fa0d_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/308487515_7852928f90_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3227148358_f152303584_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/308487515_7852928f90_2.wav *
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3567061016_62768dcce1_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/801607443_f15956d1ce_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3217187564_0ffd89dec1_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3119875880_22f9129a1c_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3567061016_62768dcce1_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/544576742_283b65fa0d_0.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: looking
    Current P@10: 0.1000
    Current P@N: 0.0460
    Current EER: 0.3563
    Top 10 utterances:  ['095_544576742_283b65fa0d_0', '016_2991575785_bd4868e215_4', '117_143688283_a96ded20f1_4', '007_535830521_aa971319fc_1', '019_544576742_283b65fa0d_1', '017_3506560025_8d0f4f9ac4_2', '046_2759860913_f75b39d783_0', '006_396360611_941e5849a3_1', '046_1082379191_ec1e53f996_2', '007_3159995270_17334ccb5b_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/544576742_283b65fa0d_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2991575785_bd4868e215_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/535830521_aa971319fc_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/544576742_283b65fa0d_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3506560025_8d0f4f9ac4_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2759860913_f75b39d783_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/396360611_941e5849a3_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1082379191_ec1e53f996_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3159995270_17334ccb5b_1.wav
    -------------------------------------------------------------------------------
    Keyword: people
    Current P@10: 0.9000
    Current P@N: 0.6657
    Current EER: 0.1173
    Top 10 utterances:  ['017_2735558076_0d7bbc18fc_1', '017_3100251515_c68027cc22_1', '029_2843695880_eeea6c67db_2', '017_2877503811_4e311253ec_1', '046_3239021459_a6b71bb400_3', '003_1282392036_5a0328eb86_0', '017_3042380610_c5ea61eef8_0', '051_3042380610_c5ea61eef8_1', '085_2581066814_179d28f306_2', '046_3562050678_4196a7fff3_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3100251515_c68027cc22_1.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: play
    Current P@10: 0.3000
    Current P@N: 0.1395
    Current EER: 0.2136
    Top 10 utterances:  ['049_3605061440_1d08c80a57_3', '096_476233374_e1396998ef_2', '077_3222055946_45f7293bb2_2', '064_154871781_ae77696b77_4', '105_3125309108_1011486589_1', '120_2944952557_8484f0da8f_4', '006_2239938351_43c73c887c_4', '041_2370481277_a3085614c9_3', '017_3262075846_5695021d84_4', '007_2587818583_4aa8e7b174_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3605061440_1d08c80a57_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/476233374_e1396998ef_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3222055946_45f7293bb2_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3125309108_1011486589_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2944952557_8484f0da8f_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2239938351_43c73c887c_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2587818583_4aa8e7b174_3.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: runs
    Current P@10: 0.3000
    Current P@N: 0.1266
    Current EER: 0.2286
    Top 10 utterances:  ['004_1107246521_d16a476380_2', '027_3354883962_170d19bfe4_0', '007_317488612_70ac35493b_2', '007_1626754053_81126b67b6_0', '011_2922222717_12195af92d_1', '019_2654514044_a70a6e2c21_0', '070_512101751_05a6d93e19_4', '003_249394748_2e4acfbbb5_2', '041_3224227640_31865b3651_2', '077_2938747424_64e64784f0_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1107246521_d16a476380_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1626754053_81126b67b6_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2922222717_12195af92d_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2654514044_a70a6e2c21_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/512101751_05a6d93e19_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/249394748_2e4acfbbb5_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3224227640_31865b3651_2.wav
    -------------------------------------------------------------------------------
    Keyword: sitting
    Current P@10: 0.6000
    Current P@N: 0.3413
    Current EER: 0.2373
    Top 10 utterances:  ['001_2616643090_4f2d2d1a44_0', '117_2608289957_044849f73e_0', '019_2602258549_7401a3cdae_4', '123_3143155555_32b6d24f34_1', '019_3639967449_137f48b43d_2', '005_2238759450_6475641bdb_2', '066_3694064560_467683205b_4', '057_2176980976_7054c99621_4', '009_2876993733_cb26107d18_2', '069_3350786891_6d39b234e9_2']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2616643090_4f2d2d1a44_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2608289957_044849f73e_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2238759450_6475641bdb_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2876993733_cb26107d18_2.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: standing
    Current P@10: 0.5000
    Current P@N: 0.1780
    Current EER: 0.2895
    Top 10 utterances:  ['046_3562050678_4196a7fff3_0', '046_2317714088_bcd081f926_2', '046_53043785_c468d6f931_1', '029_2843695880_eeea6c67db_2', '015_2708686056_1b8f356264_2', '046_444481722_690d0cadcf_3', '071_2981702521_2459f2c1c4_1', '085_2581066814_179d28f306_2', '005_2096771662_984441d20d_4', '045_3058439373_9276a4702a_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3562050678_4196a7fff3_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2317714088_bcd081f926_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2843695880_eeea6c67db_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2708686056_1b8f356264_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2581066814_179d28f306_2.wav
    -------------------------------------------------------------------------------
    Keyword: street
    Current P@10: 1.0000
    Current P@N: 0.7143
    Current EER: 0.0917
    Top 10 utterances:  ['058_561417861_8e25d0c0e8_2', '049_2182488373_df73c7cc09_4', '007_3280052365_c4644bf0a5_0', '112_2608289957_044849f73e_4', '046_1389264266_8170bc1c54_2', '049_448658518_eec0b648a6_3', '112_436009777_440c7679a1_1', '030_2715035273_8fc8b1291c_3', '023_3655964639_21e76383d0_3', '027_3181701312_70a379ab6e_4']
    -------------------------------------------------------------------------------
    Keyword: white
    Current P@10: 1.0000
    Current P@N: 0.6094
    Current EER: 0.1378
    Top 10 utterances:  ['137_2103568100_5d018c495b_1', '024_3155390408_8e1a81efb2_4', '083_3197917064_e679a44b8e_4', '049_416106657_cab2a107a5_2', '009_3647750811_395fbd397e_0', '049_3224227640_31865b3651_0', '004_3197917064_e679a44b8e_1', '049_317488612_70ac35493b_3', '004_2112921744_92bf706805_4', '025_925491651_57df3a5b36_3']
    -------------------------------------------------------------------------------
    Keyword: yellow
    Current P@10: 0.7000
    Current P@N: 0.3235
    Current EER: 0.2308
    Top 10 utterances:  ['061_2866254827_9a8f592017_2', '046_2529116152_4331dabf50_0', '003_256085101_2c2617c5d0_3', '069_2909875716_25c8652614_0', '007_1808370027_2088394eb4_2', '046_2559921948_06af25d566_3', '019_2654514044_a70a6e2c21_0', '123_170100272_d820db2199_0', '058_540721368_12ac732c6c_2', '019_429851331_b248ca01cd_2']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/256085101_2c2617c5d0_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2654514044_a70a6e2c21_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/170100272_d820db2199_0.wav
    -------------------------------------------------------------------------------
    Keyword: young
    Current P@10: 0.2000
    Current P@N: 0.1641
    Current EER: 0.2891
    Top 10 utterances:  ['007_464251704_b0f0c4c87a_1', '074_3589895574_ee08207d26_0', '013_2510020918_b2ca0fb2aa_1', '057_583174725_6b522b621f_4', '005_2490768374_45d94fc658_2', '006_363617160_6cb0c723be_2', '017_2460797929_66446c13db_2', '090_1467533293_a2656cc000_1', '032_2431832075_00aa1a4457_3', '007_758921886_55a351dd67_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/464251704_b0f0c4c87a_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3589895574_ee08207d26_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2510020918_b2ca0fb2aa_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/583174725_6b522b621f_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/363617160_6cb0c723be_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2460797929_66446c13db_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1467533293_a2656cc000_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2431832075_00aa1a4457_3.wav [semantic]
    -------------------------------------------------------------------------------

Results:

- No. errors: 57
- No. variants: 20
- No. semantic: 26
- No. correct: 97
- Semantic P@10: 0.715



### OracleSpeechCNN, MFCC, max pooling

Model directory: models/train_bow_cnn/4f8af91591

    -------------------------------------------------------------------------------
    Keyword: beach
    Current P@10: 1.0000
    Current P@N: 0.8765
    Current EER: 0.0386
    Top 10 utterances:  ['017_3070031806_3d587c2a66_0', '005_1322323208_c7ecb742c6_0', '049_339350939_6643bfb270_4', '017_533483374_86c5d4c13e_2', '004_1982852140_56425fa7a2_3', '011_3149919755_f9272b10b3_1', '095_1408958345_68eea9a4e4_3', '046_1402640441_81978e32a9_4', '091_1322323208_c7ecb742c6_1', '025_3482974845_db4f16befa_3']
    -------------------------------------------------------------------------------
    Keyword: behind
    Current P@10: 0.6000
    Current P@N: 0.2500
    Current EER: 0.2098
    Top 10 utterances:  ['040_2419221084_01a14176b4_0', '006_2309860995_c2e2a0feeb_0', '007_2064790732_219e52e19c_0', '011_3259666643_ae49524c81_1', '010_2182488373_df73c7cc09_0', '066_3688858505_e8afd1475d_0', '014_2822290399_97c809d43b_4', '017_2646116932_232573f030_4', '014_2860872588_f2c7b30e1a_4', '072_3328646934_5cca4cebce_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2419221084_01a14176b4_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3259666643_ae49524c81_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3688858505_e8afd1475d_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2860872588_f2c7b30e1a_4.wav
    -------------------------------------------------------------------------------
    Keyword: bike
    Current P@10: 0.7000
    Current P@N: 0.5437
    Current EER: 0.0928
    Top 10 utterances:  ['007_2866254827_9a8f592017_1', '017_2084217208_7bd9bc85e5_2', '005_2891617125_f939f604c7_3', '046_2924259848_effb4dcb82_2', '127_3316725440_9ccd9b5417_2', '041_3299820401_c2589186c5_1', '050_150387174_24825cf871_0', '007_2893374123_087f98d58a_1', '004_3609032038_005c789f64_0', '061_3635577874_48ebaac734_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2924259848_effb4dcb82_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/150387174_24825cf871_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2893374123_087f98d58a_1.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: black
    Current P@10: 1.0000
    Current P@N: 0.8908
    Current EER: 0.0278
    Top 10 utterances:  ['005_401079494_562454c4d6_0', '040_2607462776_78e639d891_0', '058_2844641033_dab3715a99_1', '027_3004823335_9b82cbd8a7_4', '011_3259002340_707ce96858_2', '038_2595186208_9b16fa0ee3_0', '007_326456451_effadbbe49_0', '058_1679617928_a73c1769be_4', '086_2922222717_12195af92d_3', '004_2301525531_edde12d673_3']
    -------------------------------------------------------------------------------
    Keyword: boys
    Current P@10: 1.0000
    Current P@N: 0.7294
    Current EER: 0.0595
    Top 10 utterances:  ['023_2470486377_c3a39ccb7b_4', '020_3217266166_4e0091860b_3', '052_3694064560_467683205b_2', '017_3737539561_d1dc161040_2', '046_3630332976_fdba22c50b_4', '049_3584561689_b6eb24dd70_0', '005_3251648670_9339943ba2_4', '006_522063319_33827f1627_3', '057_2373234213_4ebe9c4ee5_4', '043_1572532018_64c030c974_4']
    -------------------------------------------------------------------------------
    Keyword: dogs
    Current P@10: 1.0000
    Current P@N: 0.8610
    Current EER: 0.0497
    Top 10 utterances:  ['005_3578914491_36019ba703_3', '016_2600867924_cd502fc911_1', '007_2890113532_ab2003d74e_4', '016_447111935_5af98563e3_4', '006_3582742297_1daa29968e_2', '043_2869491449_1041485a6b_2', '004_3578914491_36019ba703_0', '004_2723477522_d89f5ac62b_4', '005_3630641436_8f9ac5b9b2_0', '006_447111935_5af98563e3_1']
    -------------------------------------------------------------------------------
    Keyword: field
    Current P@10: 1.0000
    Current P@N: 0.8507
    Current EER: 0.0448
    Top 10 utterances:  ['063_2890113532_ab2003d74e_3', '007_2534502836_7a75305655_3', '006_2854959952_3991a385ab_3', '147_3294209955_a1f1e2cc19_1', '006_3582742297_1daa29968e_2', '100_3294209955_a1f1e2cc19_3', '033_3613800013_5a54968ab0_0', '007_3582742297_1daa29968e_3', '010_3613955682_3860e116cf_3', '017_3545652636_0746537307_0']
    -------------------------------------------------------------------------------
    Keyword: hat
    Current P@10: 1.0000
    Current P@N: 0.5783
    Current EER: 0.0835
    Top 10 utterances:  ['025_2124040721_bffc0a091a_1', '156_3150742439_b8a352e1e0_2', '007_3503623999_bbd5dcfb18_0', '133_1461667284_041c8a2475_2', '019_2167644298_100ca79f54_2', '033_3530843182_35af2c821c_2', '007_2124040721_bffc0a091a_2', '014_3503623999_bbd5dcfb18_3', '031_486917990_72bd4069af_2', '033_373394550_1b2296b8c4_1']
    -------------------------------------------------------------------------------
    Keyword: jacket
    Current P@10: 0.9000
    Current P@N: 0.7975
    Current EER: 0.0385
    Top 10 utterances:  ['083_2641770481_c98465ff35_0', '084_3213992947_3f3f967a9f_4', '033_172097782_f0844ec317_2', '003_3429956016_3c7e3096c2_3', '066_416960865_048fd3f294_3', '005_3494394662_3edfd4a34c_3', '168_2518508760_68d8df7365_2', '077_1499581619_a5f65a882c_2', '007_2089426086_7acc98a3a8_1', '038_3080056515_3013830309_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/172097782_f0844ec317_2.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: large
    Current P@10: 1.0000
    Current P@N: 0.7619
    Current EER: 0.0546
    Top 10 utterances:  ['034_3070011270_390e597783_3', '017_2723477522_d89f5ac62b_2', '017_3364151356_eecd07a23e_4', '011_2283966256_70317e1759_3', '058_387830531_e89c192b92_1', '017_3472364264_dbde5a8d0a_2', '082_2308978137_bfe776d541_1', '045_2938120171_970564e3d8_0', '006_1786425974_c7c5ad6aa1_0', '017_2374652725_32f90fa15c_2']
    -------------------------------------------------------------------------------
    Keyword: looking
    Current P@10: 0.9000
    Current P@N: 0.5402
    Current EER: 0.0789
    Top 10 utterances:  ['025_3523471597_87e0bf3b21_0', '025_3070011270_390e597783_4', '086_488590040_35a3e96c89_1', '004_2985679744_75a7102aab_3', '089_3045613316_4e88862836_0', '004_2435685480_a79d42e564_2', '004_1131800850_89c7ffd477_1', '042_3149919755_f9272b10b3_0', '051_3523471597_87e0bf3b21_1', '016_2602258549_7401a3cdae_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2602258549_7401a3cdae_1.wav
    -------------------------------------------------------------------------------
    Keyword: people
    Current P@10: 1.0000
    Current P@N: 0.9260
    Current EER: 0.0298
    Top 10 utterances:  ['051_3042380610_c5ea61eef8_1', '007_260520547_944f9f4c91_1', '046_444481722_690d0cadcf_3', '085_2581066814_179d28f306_2', '046_3562050678_4196a7fff3_0', '086_2575647360_f5de38c751_3', '025_3245912109_fdeef6b456_0', '090_3500136982_bf7a85531e_3', '046_1536774449_e16b1b6382_2', '007_1536774449_e16b1b6382_4']
    -------------------------------------------------------------------------------
    Keyword: play
    Current P@10: 0.4000
    Current P@N: 0.3023
    Current EER: 0.1143
    Top 10 utterances:  ['006_2854959952_3991a385ab_3', '037_3630641436_8f9ac5b9b2_4', '046_3301811927_a2797339e5_0', '003_180094434_b0f244832d_2', '007_3605676864_0fb491267e_2', '004_2723477522_d89f5ac62b_4', '026_2189995738_352607a63b_2', '101_3585487286_ef9a8d4c56_2', '005_3262075846_5695021d84_1', '017_1917265421_aeccf1ca38_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3630641436_8f9ac5b9b2_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3301811927_a2797339e5_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2189995738_352607a63b_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3585487286_ef9a8d4c56_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3262075846_5695021d84_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1917265421_aeccf1ca38_1.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: runs
    Current P@10: 0.9000
    Current P@N: 0.5443
    Current EER: 0.0723
    Top 10 utterances:  ['027_3354883962_170d19bfe4_0', '007_2280525192_81911f2b00_1', '007_3251976937_20625dc2b8_3', '019_3294209955_a1f1e2cc19_0', '005_3354883962_170d19bfe4_3', '147_3294209955_a1f1e2cc19_1', '010_566397227_a469e9e415_3', '002_3363750526_efcedc47a9_1', '096_2891617125_f939f604c7_0', '017_2534502836_7a75305655_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2891617125_f939f604c7_0.wav
    -------------------------------------------------------------------------------
    Keyword: sitting
    Current P@10: 1.0000
    Current P@N: 0.7305
    Current EER: 0.0748
    Top 10 utterances:  ['033_3729525173_7f984ed776_2', '007_3516825206_5750824874_0', '007_1082379191_ec1e53f996_3', '039_439037721_cdf1fc7358_0', '005_561940436_64d6fc125d_0', '019_1082379191_ec1e53f996_1', '017_533713007_bf9f3e25b4_2', '038_3471841031_a949645ba8_2', '057_2901074943_041aba4607_2', '004_561940436_64d6fc125d_2']
    -------------------------------------------------------------------------------
    Keyword: standing
    Current P@10: 1.0000
    Current P@N: 0.8136
    Current EER: 0.0468
    Top 10 utterances:  ['017_3572267708_9d8a81d4a4_1', '046_3673165148_67f217064f_4', '049_3051384385_c5c850c1f8_1', '046_3421789737_f625dd17ed_4', '025_2938120171_970564e3d8_3', '137_2103568100_5d018c495b_1', '031_444481722_690d0cadcf_4', '006_410453140_5401bf659a_1', '046_53043785_c468d6f931_1', '088_2120411340_104eb610b1_1']
    -------------------------------------------------------------------------------
    Keyword: street
    Current P@10: 1.0000
    Current P@N: 0.8151
    Current EER: 0.0396
    Top 10 utterances:  ['023_3655964639_21e76383d0_3', '042_1332722096_1e3de8ae70_1', '007_300577375_26cc2773a1_2', '017_1332722096_1e3de8ae70_0', '025_2248487950_c62d0c81a9_0', '058_561417861_8e25d0c0e8_2', '052_463978865_c87c6ca84c_1', '049_2182488373_df73c7cc09_4', '042_435827376_4384c3005a_3', '127_2078311270_f01c9eaf4c_3']
    -------------------------------------------------------------------------------
    Keyword: white
    Current P@10: 1.0000
    Current P@N: 0.8613
    Current EER: 0.0468
    Top 10 utterances:  ['031_3128164023_ebe8da4c32_1', '089_3363750526_efcedc47a9_2', '070_1772859261_236c09b861_1', '145_509778093_21236bb64d_1', '027_3004823335_9b82cbd8a7_4', '070_3363750526_efcedc47a9_0', '034_3004823335_9b82cbd8a7_0', '017_2301525531_edde12d673_1', '049_416106657_cab2a107a5_2', '049_317488612_70ac35493b_3']
    -------------------------------------------------------------------------------
    Keyword: yellow
    Current P@10: 1.0000
    Current P@N: 0.8897
    Current EER: 0.0212
    Top 10 utterances:  ['046_2759860913_f75b39d783_0', '017_1167669558_87a8a467d6_0', '150_1523984678_edd68464da_0', '061_375392855_54d46ed5c8_0', '005_1167669558_87a8a467d6_3', '083_2641770481_c98465ff35_0', '046_1674612291_7154c5ab61_4', '130_2518508760_68d8df7365_0', '058_1679617928_a73c1769be_4', '061_2866254827_9a8f592017_2']
    -------------------------------------------------------------------------------
    Keyword: young
    Current P@10: 1.0000
    Current P@N: 0.9133
    Current EER: 0.0307
    Top 10 utterances:  ['046_1561658940_a947f2446a_3', '052_2207244634_1db1a1890b_4', '033_3079787482_0757e9d167_4', '017_2921094201_2ed70a7963_4', '007_2378149488_648e5deeac_1', '085_3270691950_88583c3524_3', '028_1389264266_8170bc1c54_4', '014_3549583146_3e8bb2f7e9_2', '017_3388330419_85d72f7cda_4', '096_2370481277_a3085614c9_0']
    -------------------------------------------------------------------------------

Results:

- No. errors: 4
- No. variants: 10
- No. semantic: 2
- No. correct: 184
- Semantic P@10: 0.98



### OracleSpeechPSyC, MFCC, logsumexp pooling

Model directory: models/train_psyc/246f3f7f69

    -------------------------------------------------------------------------------
    Keyword: beach
    Current P@10: 1.0000
    Current P@N: 0.8353
    Current EER: 0.0333
    Top 10 utterances:  ['007_106490881_5a2dd9b7bd_2', '025_3482974845_db4f16befa_3', '016_300922408_05a4f9938c_3', '049_1572532018_64c030c974_1', '019_1408958345_68eea9a4e4_1', '016_476233374_e1396998ef_0', '011_3149919755_f9272b10b3_1', '006_1572532018_64c030c974_3', '046_2603792708_18a97bac97_2', '049_2729655904_1dd01922fb_1']
    -------------------------------------------------------------------------------
    Keyword: behind
    Current P@10: 0.9000
    Current P@N: 0.7656
    Current EER: 0.0625
    Top 10 utterances:  ['016_3016606751_0e8be20abd_0', '041_2929506802_5432054d77_3', '049_3119875880_22f9129a1c_1', '046_3157847991_463e006a28_3', '123_2759860913_f75b39d783_2', '002_324208502_674488bcea_1', '017_2646116932_232573f030_4', '123_3585487286_ef9a8d4c56_3', '045_138718600_f430ebca17_4', '071_189721896_1ffe76d89e_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2759860913_f75b39d783_2.wav
    -------------------------------------------------------------------------------
    Keyword: bike
    Current P@10: 0.6000
    Current P@N: 0.6311
    Current EER: 0.0767
    Top 10 utterances:  ['007_2544182005_3aa1332bf9_1', '007_1262583859_653f1469a9_4', '007_2289068031_fe26990183_1', '085_2581066814_179d28f306_2', '007_2544182005_3aa1332bf9_2', '007_3584534971_b44f82c4b9_3', '007_3295680663_af21ea648b_1', '019_3485425825_c2f3446e73_4', '077_3458559770_12cf9f134e_1', '050_150387174_24825cf871_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2289068031_fe26990183_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2581066814_179d28f306_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3584534971_b44f82c4b9_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/150387174_24825cf871_0.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: black
    Current P@10: 1.0000
    Current P@N: 0.9143
    Current EER: 0.0265
    Top 10 utterances:  ['046_254295381_d98fa049f4_0', '024_3642220260_3aa8a52670_2', '007_2101457132_69c950bc45_2', '055_2813033949_e19fa08805_0', '051_3145967309_b33abe4d84_4', '024_2844641033_dab3715a99_0', '005_401079494_562454c4d6_0', '024_3275704430_a75828048f_3', '058_2844641033_dab3715a99_1', '024_3214237686_6566b8b52f_1']
    -------------------------------------------------------------------------------
    Keyword: boys
    Current P@10: 1.0000
    Current P@N: 0.8000
    Current EER: 0.0357
    Top 10 utterances:  ['049_2729655904_1dd01922fb_1', '006_3217910740_d1d61c08ab_4', '091_3072172967_630e9c69d0_3', '006_3251648670_9339943ba2_1', '095_820169182_f5e78d7d19_1', '019_3251648670_9339943ba2_3', '005_2844018783_524b08e5aa_3', '003_180094434_b0f244832d_2', '045_3639967449_137f48b43d_0', '005_3251648670_9339943ba2_4']
    -------------------------------------------------------------------------------
    Keyword: dogs
    Current P@10: 1.0000
    Current P@N: 0.8378
    Current EER: 0.0541
    Top 10 utterances:  ['019_245252561_4f20f1c89e_4', '049_2308271254_27fb466eb4_3', '046_468608014_09fd20eb9b_4', '073_524282699_71e678a6bd_4', '043_2869491449_1041485a6b_2', '019_3224227640_31865b3651_4', '024_3333921867_6cc7d7c73d_4', '004_2723477522_d89f5ac62b_4', '052_3593392955_a4125087f6_3', '025_3482974845_db4f16befa_3']
    -------------------------------------------------------------------------------
    Keyword: field
    Current P@10: 1.0000
    Current P@N: 0.8209
    Current EER: 0.0896
    Top 10 utterances:  ['049_241345905_5826a72da1_2', '002_241346971_c100650320_1', '017_3545652636_0746537307_0', '017_430173345_86388d8822_0', '089_2295750198_6d152d7ceb_0', '016_2594902417_f65d8866a8_0', '006_1119015538_e8e796281e_4', '127_3523559027_a65619a34b_1', '006_2854959952_3991a385ab_3', '010_447111935_5af98563e3_3']
    -------------------------------------------------------------------------------
    Keyword: hat
    Current P@10: 1.0000
    Current P@N: 0.7108
    Current EER: 0.0602
    Top 10 utterances:  ['044_2652522323_9218afd8c2_1', '114_2162564553_96de62c7e6_3', '074_700884207_d3ec546494_4', '004_2167644298_100ca79f54_4', '003_2553550034_5901aa9d6c_4', '007_2346401538_f5e8da66fc_1', '063_1547883892_e29b3db42e_3', '025_2124040721_bffc0a091a_1', '007_3532205154_5674b628ea_3', '052_2553550034_5901aa9d6c_3']
    -------------------------------------------------------------------------------
    Keyword: jacket
    Current P@10: 1.0000
    Current P@N: 0.8481
    Current EER: 0.0117
    Top 10 utterances:  ['066_416960865_048fd3f294_3', '016_1714316707_8bbaa2a2ba_3', '171_2435685480_a79d42e564_1', '005_2641770481_c98465ff35_3', '044_375392855_54d46ed5c8_3', '084_3213992947_3f3f967a9f_4', '104_3258874419_23fec1bdc1_2', '005_422763475_0bc814dac6_1', '046_2086513494_dbbcb583e7_1', '077_1499581619_a5f65a882c_2']
    -------------------------------------------------------------------------------
    Keyword: large
    Current P@10: 1.0000
    Current P@N: 0.8844
    Current EER: 0.0211
    Top 10 utterances:  ['049_470373679_98dceb19e7_1', '007_1107246521_d16a476380_4', '045_2170222061_e8bce4a32d_3', '046_968081289_cdba83ce2e_3', '024_3507076266_8b17993fbb_1', '046_2228022180_9597b2a458_1', '007_3217266166_4e0091860b_0', '007_2374652725_32f90fa15c_1', '005_2511019188_ca71775f2d_1', '087_3363750526_efcedc47a9_4']
    -------------------------------------------------------------------------------
    Keyword: looking
    Current P@10: 1.0000
    Current P@N: 0.8391
    Current EER: 0.0264
    Top 10 utterances:  ['025_3523471597_87e0bf3b21_0', '007_127488876_f2d2a89588_4', '005_3079787482_0757e9d167_1', '005_3004823335_9b82cbd8a7_2', '017_2839038702_e168128665_3', '051_3042380610_c5ea61eef8_1', '005_434792818_56375e203f_1', '017_247637795_fdf26a03cf_2', '007_3250695024_93e8ab7305_4', '007_3502343542_f9b46688e5_0']
    -------------------------------------------------------------------------------
    Keyword: people
    Current P@10: 1.0000
    Current P@N: 0.9083
    Current EER: 0.0387
    Top 10 utterances:  ['085_2581066814_179d28f306_2', '097_3220650628_4ed964e5b4_4', '005_1174629344_a2e1a2bdbf_0', '085_2657484284_daa07a3a1b_4', '017_444481722_690d0cadcf_2', '005_3365783912_e12c3510d8_4', '005_2096771662_984441d20d_4', '007_1536774449_e16b1b6382_4', '011_260520547_944f9f4c91_2', '007_3365783912_e12c3510d8_0']
    -------------------------------------------------------------------------------
    Keyword: play
    Current P@10: 0.9000
    Current P@N: 0.5698
    Current EER: 0.0680
    Top 10 utterances:  ['016_2419221084_01a14176b4_3', '061_3385593926_d3e9c21170_1', '007_3217266166_4e0091860b_0', '016_2878190821_6e4e03dc5f_4', '007_476233374_e1396998ef_3', '066_2216695423_1362cb25f3_1', '007_1446053356_a924b4893f_3', '007_2999730677_0cfa1c146e_1', '046_244571201_0339d8e8d1_1', '007_2216695423_1362cb25f3_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2878190821_6e4e03dc5f_4.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: runs
    Current P@10: 1.0000
    Current P@N: 0.8228
    Current EER: 0.0679
    Top 10 utterances:  ['066_3514179514_cbc3371b92_3', '147_3294209955_a1f1e2cc19_1', '001_1119015538_e8e796281e_2', '018_3613800013_5a54968ab0_4', '060_3259002340_707ce96858_0', '016_566397227_a469e9e415_2', '007_3185409663_95f6b958d8_1', '026_2757803246_8aa3499d26_3', '038_2938747424_64e64784f0_0', '049_416106657_cab2a107a5_2']
    -------------------------------------------------------------------------------
    Keyword: sitting
    Current P@10: 1.0000
    Current P@N: 0.8982
    Current EER: 0.0299
    Top 10 utterances:  ['033_3729525173_7f984ed776_2', '019_2985679744_75a7102aab_2', '032_1082379191_ec1e53f996_4', '034_3697359692_8a5cdbe4fe_1', '033_370713359_7560808550_4', '004_561940436_64d6fc125d_2', '017_2966552760_e65b22cd26_4', '020_113678030_87a6a6e42e_3', '019_3639967449_137f48b43d_2', '017_3436063693_15c8d377a2_1']
    -------------------------------------------------------------------------------
    Keyword: standing
    Current P@10: 1.0000
    Current P@N: 0.9110
    Current EER: 0.0251
    Top 10 utterances:  ['049_494792770_2c5f767ac0_3', '017_3044500219_778f9f2b71_3', '049_2182488373_df73c7cc09_4', '009_224369028_b1ac40d1fa_2', '049_224369028_b1ac40d1fa_4', '004_3080056515_3013830309_4', '006_3411393875_a9ff73c67a_4', '049_3051384385_c5c850c1f8_1', '154_3397220683_4aca010f86_0', '077_2878190821_6e4e03dc5f_2']
    -------------------------------------------------------------------------------
    Keyword: street
    Current P@10: 1.0000
    Current P@N: 0.8655
    Current EER: 0.0211
    Top 10 utterances:  ['007_2083434441_a93bc6306b_3', '005_3110649716_c17e14670e_2', '049_448658518_eec0b648a6_2', '112_436009777_440c7679a1_1', '058_561417861_8e25d0c0e8_2', '005_448658518_eec0b648a6_0', '005_3234401637_84e0d14414_1', '058_2868575889_2c030aa8ae_2', '033_245252561_4f20f1c89e_1', '049_2182488373_df73c7cc09_4']
    -------------------------------------------------------------------------------
    Keyword: white
    Current P@10: 1.0000
    Current P@N: 0.8848
    Current EER: 0.0346
    Top 10 utterances:  ['137_2103568100_5d018c495b_1', '003_3482974845_db4f16befa_1', '049_416106657_cab2a107a5_2', '025_2239938351_43c73c887c_1', '025_3009644534_992e9ea2a7_1', '025_2086513494_dbbcb583e7_0', '089_3363750526_efcedc47a9_2', '025_3497224764_6e17544e0d_1', '007_2374652725_32f90fa15c_1', '031_3128164023_ebe8da4c32_1']
    -------------------------------------------------------------------------------
    Keyword: yellow
    Current P@10: 0.9000
    Current P@N: 0.9265
    Current EER: 0.0212
    Top 10 utterances:  ['028_2083434441_a93bc6306b_4', '027_2443380641_7b38d18f5b_3', '046_2083434441_a93bc6306b_0', '027_2554081584_233bdf289a_2', '086_2909955251_4b326a46a7_0', '016_263854883_0f320c1562_4', '046_1679617928_a73c1769be_0', '058_1679617928_a73c1769be_4', '046_3554634863_5f6f616639_4', '040_3554634863_5f6f616639_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3554634863_5f6f616639_0.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: young
    Current P@10: 1.0000
    Current P@N: 0.9319
    Current EER: 0.0219
    Top 10 utterances:  ['085_3270691950_88583c3524_3', '052_2207244634_1db1a1890b_4', '017_2921094201_2ed70a7963_4', '071_2706766641_a9df81969d_3', '043_1572532018_64c030c974_4', '038_2921094201_2ed70a7963_0', '099_3627011534_485f667b10_3', '038_1415591512_a84644750c_2', '070_2652522323_9218afd8c2_3', '015_444057017_f1e0fcaef7_4']
    -------------------------------------------------------------------------------

Results:

- No. errors: 1
- No. variants: 6
- No. semantic: 0
- No. correct: 193
- Semantic P@10: 0.995



### Unigram baseline results

    -------------------------------------------------------------------------------
    Keyword: beach
    Current P@10: 0.0000
    Current P@N: 0.0176
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: behind
    Current P@10: 0.0000
    Current P@N: 0.0312
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: bike
    Current P@10: 0.0000
    Current P@N: 0.0000
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: black
    Current P@10: 0.0000
    Current P@N: 0.0964
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: boys
    Current P@10: 0.0000
    Current P@N: 0.0118
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: dogs
    Current P@10: 0.0000
    Current P@N: 0.0541
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: field
    Current P@10: 0.0000
    Current P@N: 0.0299
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: hat
    Current P@10: 0.0000
    Current P@N: 0.0000
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: jacket
    Current P@10: 0.0000
    Current P@N: 0.0000
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: large
    Current P@10: 0.2000
    Current P@N: 0.0476
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: looking
    Current P@10: 0.1000
    Current P@N: 0.0115
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    -------------------------------------------------------------------------------
    Keyword: people
    Current P@10: 0.1000
    Current P@N: 0.0621
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: play
    Current P@10: 0.0000
    Current P@N: 0.0116
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: runs
    Current P@10: 0.0000
    Current P@N: 0.0000
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: sitting
    Current P@10: 0.1000
    Current P@N: 0.0659
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: standing
    Current P@10: 0.2000
    Current P@N: 0.0466
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: street
    Current P@10: 0.0000
    Current P@N: 0.0084
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: white
    Current P@10: 0.1000
    Current P@N: 0.1094
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: yellow
    Current P@10: 0.0000
    Current P@N: 0.0147
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3016606751_0e8be20abd_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3025549604_38b86198f5_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------
    Keyword: young
    Current P@10: 0.2000
    Current P@N: 0.0774
    Current EER: 0.5000
    Top 10 utterances:  ['183_2495931537_9b8d4474b6_1', '017_3044500219_778f9f2b71_3', '017_2994179598_a45c2732b5_3', '017_3003691049_f4363c2d5c_3', '017_3009644534_992e9ea2a7_4', '017_3016606751_0e8be20abd_4', '017_3024172109_a10198e1dd_2', '017_3025549604_38b86198f5_4', '017_3042380610_c5ea61eef8_0', '017_3045613316_4e88862836_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2495931537_9b8d4474b6_1.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3044500219_778f9f2b71_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_3.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3003691049_f4363c2d5c_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3009644534_992e9ea2a7_4.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3024172109_a10198e1dd_2.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3042380610_c5ea61eef8_0.wav
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3045613316_4e88862836_4.wav
    -------------------------------------------------------------------------------

Results:

- No. errors: 180
- No. variants: 2
- No. semantic: 8
- No. correct: 10
- Semantic P@10: 0.10
