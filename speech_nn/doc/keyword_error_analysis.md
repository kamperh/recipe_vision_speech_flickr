Analysis: Errors in Keyword Spotting
====================================


### VisionSpeechCNN, MFCC, max pooling

Model directory: models/train_visionsig_cnn/5bb5c4b4bd

    -------------------------------------------------------------------------------
    Keyword: beach
    Current P@10: 1.0000
    Current P@N: 0.7412
    Current EER: 0.0652
    Top 10 utterances:  ['016_3642220260_3aa8a52670_4', '005_1322323208_c7ecb742c6_0', '003_3398746625_5199beea71_4', '085_1499581619_a5f65a882c_3', '004_1982852140_56425fa7a2_3', '046_1402640441_81978e32a9_4', '005_1456393634_74022d9056_0', '091_1322323208_c7ecb742c6_1', '049_339350939_6643bfb270_4', '007_3602838407_bf13e49243_1']
    -------------------------------------------------------------------------------
    Keyword: behind
    Current P@10: 0.0000
    Current P@N: 0.0000
    Current EER: 0.4130
    Top 10 utterances:  ['086_3263497678_8bb688ca01_0', '046_2533424347_cf2f84872b_4', '019_2621415349_ef1a7e73be_0', '004_2914206497_5e36ac6324_1', '075_3578841731_f775cab089_2', '009_2984174290_a915748d77_1', '017_2358561039_e215a8d6cd_4', '053_791338571_7f38510bf7_2', '148_3047264346_e24601bfbf_1', '020_3217187564_0ffd89dec1_2']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3263497678_8bb688ca01_0.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2533424347_cf2f84872b_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2621415349_ef1a7e73be_0.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2914206497_5e36ac6324_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3578841731_f775cab089_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2984174290_a915748d77_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2358561039_e215a8d6cd_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/791338571_7f38510bf7_2.wav [semantic]*
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3047264346_e24601bfbf_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3217187564_0ffd89dec1_2.wav [error]
    -------------------------------------------------------------------------------
    Keyword: bike
    Current P@10: 0.3000
    Current P@N: 0.3689
    Current EER: 0.0991
    Top 10 utterances:  ['046_3347798761_5c5260b000_1', '070_3576259024_9c05b163aa_1', '090_3179336562_c3d0c0a3bd_0', '004_2073964624_52da3a0fc4_0', '041_2764178773_d63b502812_2', '046_2764178773_d63b502812_3', '046_3635577874_48ebaac734_4', '033_2084217208_7bd9bc85e5_4', '017_3549583146_3e8bb2f7e9_4', '005_3316725440_9ccd9b5417_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3347798761_5c5260b000_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3179336562_c3d0c0a3bd_0.wav [variant]*
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2073964624_52da3a0fc4_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2764178773_d63b502812_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2764178773_d63b502812_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3635577874_48ebaac734_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3549583146_3e8bb2f7e9_4.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: black
    Current P@10: 1.0000
    Current P@N: 0.4818
    Current EER: 0.2434
    Top 10 utterances:  ['038_2595186208_9b16fa0ee3_0', '007_326456451_effadbbe49_0', '107_343218198_1ca90e0734_0', '047_424416723_19c56cb365_0', '009_670609997_5c7fdb3f0b_2', '011_245252561_4f20f1c89e_2', '038_3070011270_390e597783_1', '011_3259002340_707ce96858_2', '040_2607462776_78e639d891_0', '007_1392272228_cf104086e6_1']
    -------------------------------------------------------------------------------
    Keyword: boys
    Current P@10: 0.3000
    Current P@N: 0.1647
    Current EER: 0.1859
    Top 10 utterances:  ['030_197504190_fd1fc3d4b7_3', '004_197504190_fd1fc3d4b7_1', '052_3375991133_87d7c40925_2', '007_2587818583_4aa8e7b174_3', '096_2370481277_a3085614c9_0', '049_3584561689_b6eb24dd70_0', '046_3596131692_91b8a05606_0', '017_820169182_f5e78d7d19_4', '041_2370481277_a3085614c9_3', '007_3217266166_4e0091860b_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/197504190_fd1fc3d4b7_3.wav [semantic]*
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/197504190_fd1fc3d4b7_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3375991133_87d7c40925_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2587818583_4aa8e7b174_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3596131692_91b8a05606_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/820169182_f5e78d7d19_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3217266166_4e0091860b_0.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: dogs
    Current P@10: 1.0000
    Current P@N: 0.7722
    Current EER: 0.0734
    Top 10 utterances:  ['004_2676764246_c58205a365_1', '049_2676764246_c58205a365_2', '004_2573625591_70291c894a_0', '006_3582742297_1daa29968e_2', '031_3128164023_ebe8da4c32_1', '120_2968182121_b3b491df85_3', '004_3582742297_1daa29968e_4', '002_2968182121_b3b491df85_4', '017_387830531_e89c192b92_3', '017_2892995070_39f3c9a56e_4']
    -------------------------------------------------------------------------------
    Keyword: field
    Current P@10: 0.8000
    Current P@N: 0.4403
    Current EER: 0.1583
    Top 10 utterances:  ['147_3294209955_a1f1e2cc19_1', '061_2856080862_95d793fa9d_2', '016_2600867924_cd502fc911_1', '033_2511019188_ca71775f2d_2', '006_2763044275_aa498eb88b_1', '100_3294209955_a1f1e2cc19_3', '030_1446053356_a924b4893f_2', '001_1119015538_e8e796281e_2', '005_3004823335_9b82cbd8a7_3', '007_2890113532_ab2003d74e_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2511019188_ca71775f2d_2.wav [semantic]*
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1119015538_e8e796281e_2.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: hat
    Current P@10: 0.4000
    Current P@N: 0.2048
    Current EER: 0.2163
    Top 10 utterances:  ['005_3494394662_3edfd4a34c_3', '045_2343525685_3eba3b6686_0', '007_3532205154_5674b628ea_3', '005_2218609886_892dcd6915_2', '002_421730441_6b2267fd31_2', '066_416960865_048fd3f294_3', '156_3150742439_b8a352e1e0_2', '090_2621415349_ef1a7e73be_2', '007_2307118114_c258e3a47e_2', '010_3397220683_4aca010f86_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3494394662_3edfd4a34c_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2343525685_3eba3b6686_0.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/421730441_6b2267fd31_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2621415349_ef1a7e73be_2.wav [semantic]*
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2307118114_c258e3a47e_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3397220683_4aca010f86_1.wav [error]
    -------------------------------------------------------------------------------
    Keyword: jacket
    Current P@10: 0.3000
    Current P@N: 0.0506
    Current EER: 0.3198
    Top 10 utterances:  ['007_485245061_5a5de43e20_3', '004_1714316707_8bbaa2a2ba_0', '014_3301859683_2d5e4b40a3_1', '066_416960865_048fd3f294_3', '005_3494394662_3edfd4a34c_3', '005_2218609886_892dcd6915_2', '005_3182121297_38c99b2769_2', '119_485245061_5a5de43e20_2', '007_3320032226_63390d74a6_0', '017_2100816230_ff866fb352_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/485245061_5a5de43e20_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3301859683_2d5e4b40a3_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2218609886_892dcd6915_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3182121297_38c99b2769_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/485245061_5a5de43e20_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3320032226_63390d74a6_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2100816230_ff866fb352_4.wav [error]
    -------------------------------------------------------------------------------
    Keyword: large
    Current P@10: 0.3000
    Current P@N: 0.1088
    Current EER: 0.3491
    Top 10 utterances:  ['061_309687244_4bdf3b591f_2', '006_396360611_941e5849a3_1', '004_3413571342_b9855795e2_0', '127_3320356356_1497e53f80_4', '006_3320356356_1497e53f80_3', '006_3413571342_b9855795e2_2', '058_309687244_4bdf3b591f_3', '015_3375070563_3c290a7991_1', '005_3071676551_a65741e372_3', '086_396360611_941e5849a3_2']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/309687244_4bdf3b591f_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/396360611_941e5849a3_1.wav [semantic]*
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3413571342_b9855795e2_0.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3320356356_1497e53f80_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3413571342_b9855795e2_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/309687244_4bdf3b591f_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/396360611_941e5849a3_2.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: looking
    Current P@10: 0.1000
    Current P@N: 0.0805
    Current EER: 0.3342
    Top 10 utterances:  ['016_3222041930_f642f49d28_3', '141_2176980976_7054c99621_0', '066_3694064560_467683205b_4', '136_3613424631_3ae537624f_4', '011_3325497914_f9014d615b_0', '007_2049051050_20359a434a_3', '011_480505313_2dc686e5db_2', '019_1082379191_ec1e53f996_1', '033_3729525173_7f984ed776_2', '059_1282392036_5a0328eb86_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3222041930_f642f49d28_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2176980976_7054c99621_0.wav [semantic]*
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3613424631_3ae537624f_4.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3325497914_f9014d615b_0.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2049051050_20359a434a_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/480505313_2dc686e5db_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1082379191_ec1e53f996_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3729525173_7f984ed776_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1282392036_5a0328eb86_3.wav [error]
    -------------------------------------------------------------------------------
    Keyword: people
    Current P@10: 1.0000
    Current P@N: 0.6154
    Current EER: 0.1321
    Top 10 utterances:  ['005_1962729184_6996e128e7_3', '086_2575647360_f5de38c751_3', '025_3245912109_fdeef6b456_0', '025_1472230829_803818a383_1', '007_880220939_0ef1c37f1f_4', '007_260520547_944f9f4c91_1', '046_3468694409_a51571d621_1', '057_160792599_6a7ec52516_1', '011_260520547_944f9f4c91_2', '123_3359530430_249f51972c_2']
    -------------------------------------------------------------------------------
    Keyword: play
    Current P@10: 0.0000
    Current P@N: 0.2674
    Current EER: 0.1744
    Top 10 utterances:  ['006_3582742297_1daa29968e_2', '004_197504190_fd1fc3d4b7_1', '007_2587818583_4aa8e7b174_3', '060_387830531_e89c192b92_4', '007_3385593926_d3e9c21170_4', '037_3630641436_8f9ac5b9b2_4', '111_315880837_90db309bab_0', '017_2892995070_39f3c9a56e_4', '046_3596131692_91b8a05606_0', '017_387830531_e89c192b92_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3582742297_1daa29968e_2.wav [variant]*
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/197504190_fd1fc3d4b7_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2587818583_4aa8e7b174_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/387830531_e89c192b92_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3385593926_d3e9c21170_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3630641436_8f9ac5b9b2_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/315880837_90db309bab_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2892995070_39f3c9a56e_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3596131692_91b8a05606_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/387830531_e89c192b92_3.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: runs
    Current P@10: 0.4000
    Current P@N: 0.1899
    Current EER: 0.2405
    Top 10 utterances:  ['147_3294209955_a1f1e2cc19_1', '007_317488612_70ac35493b_2', '049_3223224391_be50bf4f43_0', '033_270724499_107481c88f_1', '001_1119015538_e8e796281e_2', '046_1523984678_edd68464da_1', '100_3294209955_a1f1e2cc19_3', '027_3354883962_170d19bfe4_0', '150_1523984678_edd68464da_0', '003_263854883_0f320c1562_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3223224391_be50bf4f43_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/270724499_107481c88f_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1523984678_edd68464da_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3294209955_a1f1e2cc19_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1523984678_edd68464da_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/263854883_0f320c1562_0.wav [variant]*
    -------------------------------------------------------------------------------
    Keyword: sitting
    Current P@10: 0.8000
    Current P@N: 0.4012
    Current EER: 0.2096
    Top 10 utterances:  ['006_324208502_674488bcea_4', '006_3597326009_3678a98a43_4', '046_1082379191_ec1e53f996_2', '089_436009777_440c7679a1_3', '074_2905942129_2b4bf59bc0_1', '032_1082379191_ec1e53f996_4', '004_561940436_64d6fc125d_2', '112_1258913059_07c613f7ff_1', '004_3737539561_d1dc161040_3', '145_2498897831_0bbb5d5b51_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3597326009_3678a98a43_4.wav [variant]*
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2905942129_2b4bf59bc0_1.wav [error]
    -------------------------------------------------------------------------------
    Keyword: standing
    Current P@10: 0.4000
    Current P@N: 0.1949
    Current EER: 0.3111
    Top 10 utterances:  ['042_435827376_4384c3005a_3', '150_3655964639_21e76383d0_4', '025_2248487950_c62d0c81a9_0', '025_3245912109_fdeef6b456_0', '007_880220939_0ef1c37f1f_1', '033_3694093650_547259731e_0', '017_2735558076_0d7bbc18fc_1', '046_444481722_690d0cadcf_3', '025_3045613316_4e88862836_1', '007_86412576_c53392ef80_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/435827376_4384c3005a_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3655964639_21e76383d0_4.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2248487950_c62d0c81a9_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/880220939_0ef1c37f1f_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2735558076_0d7bbc18fc_1.wav [variant]*
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/86412576_c53392ef80_4.wav [error]
    -------------------------------------------------------------------------------
    Keyword: street
    Current P@10: 0.9000
    Current P@N: 0.4958
    Current EER: 0.1512
    Top 10 utterances:  ['023_3655964639_21e76383d0_3', '127_3286822339_5535af6b93_0', '042_435827376_4384c3005a_3', '112_435827376_4384c3005a_2', '003_3442242092_e579538d82_0', '150_3655964639_21e76383d0_4', '030_2715035273_8fc8b1291c_3', '005_3365783912_e12c3510d8_4', '025_2248487950_c62d0c81a9_0', '127_2078311270_f01c9eaf4c_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3442242092_e579538d82_0.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: white
    Current P@10: 1.0000
    Current P@N: 0.4707
    Current EER: 0.2403
    Top 10 utterances:  ['005_3222055946_45f7293bb2_0', '046_1523984678_edd68464da_1', '046_3294209955_a1f1e2cc19_2', '049_3363750526_efcedc47a9_3', '046_1674612291_7154c5ab61_3', '049_3155987659_b9ea318dd3_1', '005_2813033949_e19fa08805_1', '055_2813033949_e19fa08805_0', '027_3004823335_9b82cbd8a7_4', '007_249394748_2e4acfbbb5_0']
    -------------------------------------------------------------------------------
    Keyword: yellow
    Current P@10: 0.4000
    Current P@N: 0.1176
    Current EER: 0.3927
    Top 10 utterances:  ['030_2358898017_24496b80e8_1', '034_430173345_86388d8822_2', '022_2654514044_a70a6e2c21_4', '168_2518508760_68d8df7365_2', '052_261490838_2f3ac98b12_2', '134_3123463486_f5b36a3624_2', '025_2945036454_280fa5b29f_4', '075_3578841731_f775cab089_2', '007_430173345_86388d8822_1', '039_2676764246_c58205a365_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2358898017_24496b80e8_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/430173345_86388d8822_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3123463486_f5b36a3624_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3578841731_f775cab089_2.wav [error] *
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/430173345_86388d8822_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2676764246_c58205a365_3.wav [error]
    -------------------------------------------------------------------------------
    Keyword: young
    Current P@10: 0.3000
    Current P@N: 0.2755
    Current EER: 0.2397
    Top 10 utterances:  ['025_2436081047_bca044c1d3_4', '086_1561658940_a947f2446a_0', '123_170100272_d820db2199_0', '085_2693425189_47740c22ed_4', '051_542317719_ed4dd95dc2_3', '007_3677318686_b018862bb7_2', '016_476233374_e1396998ef_0', '024_2436081047_bca044c1d3_2', '004_3484649669_7bfe62080b_1', '005_1509786421_f03158adfc_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1561658940_a947f2446a_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/170100272_d820db2199_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2693425189_47740c22ed_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3677318686_b018862bb7_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/476233374_e1396998ef_0.wav [semantic] *
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2436081047_bca044c1d3_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1509786421_f03158adfc_3.wav [semantic]
    -------------------------------------------------------------------------------

No. errors: 36
No. variants: 25
No. semantic: 32
No. correct: 107
Semantic P@10: 0.825



### VissionSpeechPSyC, MFCC, logsumexp pooling

    -------------------------------------------------------------------------------
    Keyword: beach
    Current P@10: 1.0000
    Current P@N: 0.7647
    Current EER: 0.0776
    Top 10 utterances:  ['091_1322323208_c7ecb742c6_1', '016_300922408_05a4f9938c_3', '004_1499581619_a5f65a882c_4', '095_1408958345_68eea9a4e4_3', '049_3673165148_67f217064f_2', '016_3642220260_3aa8a52670_4', '016_476233374_e1396998ef_0', '019_300922408_05a4f9938c_2', '017_533483374_86c5d4c13e_2', '049_2729655904_1dd01922fb_1']
    -------------------------------------------------------------------------------
    Keyword: behind
    Current P@10: 0.0000
    Current P@N: 0.0000
    Current EER: 0.4657
    Top 10 utterances:  ['006_3413571342_b9855795e2_2', '077_3624327440_bef4f33f32_3', '007_3071676551_a65741e372_1', '103_3085667767_66041b202e_4', '009_2984174290_a915748d77_1', '043_3071676551_a65741e372_0', '046_3631986552_944ea208fc_1', '019_3168123064_d1983b8f92_3', '017_3624327440_bef4f33f32_4', '007_3413571342_b9855795e2_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3413571342_b9855795e2_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3624327440_bef4f33f32_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3071676551_a65741e372_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3085667767_66041b202e_4.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2984174290_a915748d77_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3071676551_a65741e372_0.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3631986552_944ea208fc_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3168123064_d1983b8f92_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3624327440_bef4f33f32_4.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3413571342_b9855795e2_3.wav [error]
    -------------------------------------------------------------------------------
    Keyword: bike
    Current P@10: 0.7000
    Current P@N: 0.3883
    Current EER: 0.1421
    Top 10 utterances:  ['046_2891617125_f939f604c7_2', '028_3263395801_5e4cee2b9e_2', '008_3558370311_5734a15890_0', '181_2764178773_d63b502812_0', '007_2544182005_3aa1332bf9_1', '005_3316725440_9ccd9b5417_4', '005_219070971_ae43410b9e_1', '016_3640422448_a0f42e4559_1', '028_2083434441_a93bc6306b_4', '017_2924259848_effb4dcb82_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3640422448_a0f42e4559_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2083434441_a93bc6306b_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2924259848_effb4dcb82_0.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: black
    Current P@10: 1.0000
    Current P@N: 0.5867
    Current EER: 0.1615
    Top 10 utterances:  ['107_343218198_1ca90e0734_0', '007_326456451_effadbbe49_0', '024_3642220260_3aa8a52670_2', '083_2933912528_52b05f84a1_2', '024_3223055565_68973f5d20_2', '049_3602838407_bf13e49243_0', '006_2763044275_aa498eb88b_1', '003_2421446839_fe7d46c177_4', '025_1897025969_0c41688fa6_1', '083_2723477522_d89f5ac62b_1']
    -------------------------------------------------------------------------------
    Keyword: boys
    Current P@10: 0.1000
    Current P@N: 0.0941
    Current EER: 0.2040
    Top 10 utterances:  ['016_2370481277_a3085614c9_4', '061_2856080862_95d793fa9d_2', '064_154871781_ae77696b77_4', '003_820169182_f5e78d7d19_2', '025_2189995738_352607a63b_3', '030_197504190_fd1fc3d4b7_3', '049_2905942129_2b4bf59bc0_2', '052_3375991133_87d7c40925_2', '036_3347666612_659e6e2207_2', '041_2370481277_a3085614c9_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2370481277_a3085614c9_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2856080862_95d793fa9d_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/154871781_ae77696b77_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/820169182_f5e78d7d19_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2189995738_352607a63b_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/197504190_fd1fc3d4b7_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2905942129_2b4bf59bc0_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3375991133_87d7c40925_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3347666612_659e6e2207_2.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: dogs
    Current P@10: 1.0000
    Current P@N: 0.7259
    Current EER: 0.0935
    Top 10 utterances:  ['005_3630641436_8f9ac5b9b2_0', '046_2938120171_970564e3d8_4', '049_2676764246_c58205a365_2', '060_387830531_e89c192b92_4', '049_3655155990_b0e201dd3c_0', '025_2938120171_970564e3d8_3', '043_2869491449_1041485a6b_2', '006_447111935_5af98563e3_1', '134_3593392955_a4125087f6_1', '003_263854883_0f320c1562_0']
    -------------------------------------------------------------------------------
    Keyword: field
    Current P@10: 0.7000
    Current P@N: 0.3284
    Current EER: 0.1567
    Top 10 utterances:  ['064_154871781_ae77696b77_4', '016_2370481277_a3085614c9_4', '061_2856080862_95d793fa9d_2', '017_241345905_5826a72da1_3', '077_2496370758_a3fbc49837_2', '007_2890113532_ab2003d74e_4', '004_2723477522_d89f5ac62b_4', '017_2358898017_24496b80e8_0', '042_2854959952_3991a385ab_2', '016_566397227_a469e9e415_2']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/241345905_5826a72da1_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2496370758_a3fbc49837_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2723477522_d89f5ac62b_4.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: hat
    Current P@10: 0.0000
    Current P@N: 0.0602
    Current EER: 0.2919
    Top 10 utterances:  ['152_2292406847_f366350600_2', '025_3523474077_16e14bc54c_3', '007_2994179598_a45c2732b5_1', '092_3425851292_de92a072ee_1', '006_3320356356_1497e53f80_3', '049_3641022607_e7a5455d6c_2', '071_2861932486_52befd8592_2', '003_872622575_ba1d3632cc_0', '018_2529116152_4331dabf50_1', '019_2443380641_7b38d18f5b_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2292406847_f366350600_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3523474077_16e14bc54c_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2994179598_a45c2732b5_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3425851292_de92a072ee_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3320356356_1497e53f80_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3641022607_e7a5455d6c_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2861932486_52befd8592_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/872622575_ba1d3632cc_0.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2529116152_4331dabf50_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2443380641_7b38d18f5b_1.wav [error]
    -------------------------------------------------------------------------------
    Keyword: jacket
    Current P@10: 0.0000
    Current P@N: 0.0380
    Current EER: 0.3891
    Top 10 utterances:  ['005_3182121297_38c99b2769_2', '061_375392855_54d46ed5c8_0', '007_3159995270_17334ccb5b_1', '014_3301859683_2d5e4b40a3_1', '033_3139876823_859c7d7c23_1', '007_3301859683_2d5e4b40a3_0', '030_2100816230_ff866fb352_0', '049_3301859683_2d5e4b40a3_2', '152_2292406847_f366350600_2', '032_3123351642_3794f2f601_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3182121297_38c99b2769_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/375392855_54d46ed5c8_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3159995270_17334ccb5b_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3301859683_2d5e4b40a3_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3139876823_859c7d7c23_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3301859683_2d5e4b40a3_0.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2100816230_ff866fb352_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3301859683_2d5e4b40a3_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2292406847_f366350600_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3123351642_3794f2f601_0.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: large
    Current P@10: 0.0000
    Current P@N: 0.0408
    Current EER: 0.3207
    Top 10 utterances:  ['086_308487515_7852928f90_0', '019_3168123064_d1983b8f92_3', '092_2901880865_3fd7b66a45_3', '077_3624327440_bef4f33f32_3', '058_309687244_4bdf3b591f_3', '006_3320356356_1497e53f80_3', '019_544576742_283b65fa0d_1', '037_544576742_283b65fa0d_4', '033_801607443_f15956d1ce_4', '017_3624327440_bef4f33f32_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/308487515_7852928f90_0.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3168123064_d1983b8f92_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2901880865_3fd7b66a45_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3624327440_bef4f33f32_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/309687244_4bdf3b591f_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3320356356_1497e53f80_3.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/544576742_283b65fa0d_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/544576742_283b65fa0d_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/801607443_f15956d1ce_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3624327440_bef4f33f32_4.wav [error]
    -------------------------------------------------------------------------------
    Keyword: looking
    Current P@10: 0.0000
    Current P@N: 0.0460
    Current EER: 0.3693
    Top 10 utterances:  ['112_436009777_440c7679a1_1', '023_3186412658_2ab2ebd397_4', '046_2300168895_a9b83e16fc_3', '042_2922973230_5a769ef92a_4', '039_1056338697_4f7d7ce270_1', '017_3506560025_8d0f4f9ac4_2', '049_3716244806_97d5a1fb61_0', '112_435827376_4384c3005a_2', '152_2292406847_f366350600_2', '007_535830521_aa971319fc_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/436009777_440c7679a1_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3186412658_2ab2ebd397_4.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2300168895_a9b83e16fc_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2922973230_5a769ef92a_4.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1056338697_4f7d7ce270_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3506560025_8d0f4f9ac4_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3716244806_97d5a1fb61_0.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/435827376_4384c3005a_2.wav  [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2292406847_f366350600_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/535830521_aa971319fc_1.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: people
    Current P@10: 0.9000
    Current P@N: 0.6361
    Current EER: 0.1220
    Top 10 utterances:  ['003_3502343542_f9b46688e5_2', '137_3200120942_59cfbb3437_3', '011_3344233740_c010378da7_3', '045_2086513494_dbbcb583e7_2', '007_3061481868_d1e00b1f2e_2', '022_2991994607_06f24ec7a6_2', '049_3062173277_bfb5ef4c45_4', '126_3052196390_c59dd24ca8_2', '051_2991994607_06f24ec7a6_3', '003_2981702521_2459f2c1c4_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3052196390_c59dd24ca8_2.wav
    -------------------------------------------------------------------------------
    Keyword: play
    Current P@10: 0.3000
    Current P@N: 0.2442
    Current EER: 0.1977
    Top 10 utterances:  ['046_3109704348_c6416244ce_1', '016_2370481277_a3085614c9_4', '049_2308271254_27fb466eb4_3', '024_2999730677_0cfa1c146e_2', '061_2856080862_95d793fa9d_2', '030_197504190_fd1fc3d4b7_3', '064_154871781_ae77696b77_4', '049_3655155990_b0e201dd3c_0', '025_2189995738_352607a63b_3', '049_2729655904_1dd01922fb_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2370481277_a3085614c9_4.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2308271254_27fb466eb4_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2999730677_0cfa1c146e_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2856080862_95d793fa9d_2.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3655155990_b0e201dd3c_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2189995738_352607a63b_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2729655904_1dd01922fb_1.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: runs
    Current P@10: 0.3000
    Current P@N: 0.1772
    Current EER: 0.2308
    Top 10 utterances:  ['027_3354883962_170d19bfe4_0', '027_3004823335_9b82cbd8a7_4', '019_2654514044_a70a6e2c21_0', '007_429851331_b248ca01cd_3', '049_3223224391_be50bf4f43_0', '086_2206960564_325ed0c7ae_3', '049_317488612_70ac35493b_3', '049_416106657_cab2a107a5_2', '007_3123463486_f5b36a3624_1', '026_317488612_70ac35493b_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3004823335_9b82cbd8a7_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2654514044_a70a6e2c21_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/429851331_b248ca01cd_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3223224391_be50bf4f43_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2206960564_325ed0c7ae_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/317488612_70ac35493b_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/317488612_70ac35493b_4.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: sitting
    Current P@10: 0.8000
    Current P@N: 0.5030
    Current EER: 0.1737
    Top 10 utterances:  ['007_324208502_674488bcea_3', '046_2300168895_a9b83e16fc_3', '017_3106026005_473a7b1c8c_4', '096_3393343330_b13df4d8ec_0', '019_2602258549_7401a3cdae_4', '032_2985679744_75a7102aab_4', '049_3716244806_97d5a1fb61_0', '086_2575647360_f5de38c751_3', '017_533713007_bf9f3e25b4_2', '032_1082379191_ec1e53f996_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/324208502_674488bcea_3.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3393343330_b13df4d8ec_0.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: standing
    Current P@10: 0.5000
    Current P@N: 0.3136
    Current EER: 0.2380
    Top 10 utterances:  ['077_3571147934_d1c8af1d6e_3', '137_3200120942_59cfbb3437_3', '125_2196846255_2c1635359a_1', '025_3070011270_390e597783_4', '004_3220126881_b0a4f7cccb_3', '049_3245912109_fdeef6b456_1', '067_3058439373_9276a4702a_1', '046_444481722_690d0cadcf_3', '071_2981702521_2459f2c1c4_1', '038_3398746625_5199beea71_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3571147934_d1c8af1d6e_3.wav  [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3200120942_59cfbb3437_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3245912109_fdeef6b456_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3058439373_9276a4702a_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3398746625_5199beea71_1.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: street
    Current P@10: 0.9000
    Current P@N: 0.5882
    Current EER: 0.1271
    Top 10 utterances:  ['066_436009777_440c7679a1_0', '003_3359551687_68f2f0212a_4', '041_3569406219_f37ebf7b92_4', '033_245252561_4f20f1c89e_1', '054_2878272032_fda05ffac7_2', '112_2608289957_044849f73e_4', '007_3565598162_56044bc2f7_0', '017_1332722096_1e3de8ae70_0', '007_561417861_8e25d0c0e8_0', '045_3499720588_c32590108e_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2878272032_fda05ffac7_2.wav [error]
    -------------------------------------------------------------------------------
    Keyword: white
    Current P@10: 0.5000
    Current P@N: 0.4805
    Current EER: 0.2016
    Top 10 utterances:  ['125_2271755053_e1b1ec8442_3', '046_1764955991_5e53a28c87_0', '033_429851331_b248ca01cd_1', '062_2739331794_4ae78f69a0_1', '003_249394748_2e4acfbbb5_2', '004_2021613437_d99731f986_3', '011_3217620013_8b17873273_1', '034_3004823335_9b82cbd8a7_0', '074_3222055946_45f7293bb2_4', '046_3109704348_c6416244ce_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2271755053_e1b1ec8442_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/429851331_b248ca01cd_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2021613437_d99731f986_3.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3217620013_8b17873273_1.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3109704348_c6416244ce_1.wav [error]
    -------------------------------------------------------------------------------
    Keyword: yellow
    Current P@10: 0.5000
    Current P@N: 0.2353
    Current EER: 0.3510
    Top 10 utterances:  ['058_540721368_12ac732c6c_2', '049_241345905_5826a72da1_2', '061_2968182121_b3b491df85_2', '046_2759860913_f75b39d783_0', '005_3004823335_9b82cbd8a7_2', '014_732468337_a37075225e_4', '017_1167669558_87a8a467d6_0', '024_246055693_ccb69ac5c6_4', '025_2945036454_280fa5b29f_4', '007_1220401002_3f44b1f3f7_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/241345905_5826a72da1_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2968182121_b3b491df85_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3004823335_9b82cbd8a7_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/732468337_a37075225e_4.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1220401002_3f44b1f3f7_4.wav [error]
    -------------------------------------------------------------------------------
    Keyword: young
    Current P@10: 0.4000
    Current P@N: 0.1981
    Current EER: 0.2708
    Top 10 utterances:  ['049_2192131110_8a40e7c028_0', '046_1561658940_a947f2446a_3', '043_2660008870_b672a4c76a_2', '086_1561658940_a947f2446a_0', '007_1220401002_3f44b1f3f7_4', '013_2510020918_b2ca0fb2aa_1', '123_170100272_d820db2199_0', '037_2431832075_00aa1a4457_1', '019_2354540393_a149722680_1', '096_2370481277_a3085614c9_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2192131110_8a40e7c028_0.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2660008870_b672a4c76a_2.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1561658940_a947f2446a_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2510020918_b2ca0fb2aa_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/170100272_d820db2199_0.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2431832075_00aa1a4457_1.wav [semantic]
    -------------------------------------------------------------------------------

No. errors: 53
No. variants: 21
No. semantic: 29
No. correct: 96
Semantic P@10: 0.73



### OracleSpeechCNN, MFCC, max pooling

    -------------------------------------------------------------------------------
    Keyword: beach
    Current P@10: 0.9000
    Current P@N: 0.8588
    Current EER: 0.0462
    Top 10 utterances:  ['005_1322323208_c7ecb742c6_0', '049_339350939_6643bfb270_4', '101_524282699_71e678a6bd_3', '116_561940436_64d6fc125d_4', '007_1456393634_74022d9056_4', '005_1456393634_74022d9056_0', '046_1402640441_81978e32a9_4', '025_3482974845_db4f16befa_3', '003_3398746625_5199beea71_4', '007_3472364264_dbde5a8d0a_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/561940436_64d6fc125d_4.wav [error]
    -------------------------------------------------------------------------------
    Keyword: behind
    Current P@10: 0.6000
    Current P@N: 0.2969
    Current EER: 0.2812
    Top 10 utterances:  ['006_2309860995_c2e2a0feeb_0', '058_2041867793_552819a40b_1', '004_3673165148_67f217064f_3', '049_3119875880_22f9129a1c_1', '033_3585487286_ef9a8d4c56_4', '074_3589895574_ee08207d26_0', '010_2182488373_df73c7cc09_0', '016_3016606751_0e8be20abd_0', '040_2473689180_e9d8fd656a_2', '139_3259666643_ae49524c81_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2041867793_552819a40b_1.wav [semantic]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3589895574_ee08207d26_0.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2473689180_e9d8fd656a_2.wav [error]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3259666643_ae49524c81_3.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: bike
    Current P@10: 1.0000
    Current P@N: 0.6019
    Current EER: 0.0891
    Top 10 utterances:  ['070_3576259024_9c05b163aa_1', '007_2544182005_3aa1332bf9_2', '004_3609032038_005c789f64_0', '061_3635577874_48ebaac734_0', '020_2544182005_3aa1332bf9_0', '049_3549583146_3e8bb2f7e9_0', '007_2866254827_9a8f592017_1', '019_2075321027_c8fcbaf581_2', '005_2891617125_f939f604c7_3', '005_3316725440_9ccd9b5417_1']
    -------------------------------------------------------------------------------
    Keyword: black
    Current P@10: 1.0000
    Current P@N: 0.8672
    Current EER: 0.0410
    Top 10 utterances:  ['004_421730441_6b2267fd31_4', '038_3070011270_390e597783_1', '005_401079494_562454c4d6_0', '046_3540416981_4e74f08cbb_1', '018_2307118114_c258e3a47e_0', '044_3642220260_3aa8a52670_0', '003_2421446839_fe7d46c177_4', '107_343218198_1ca90e0734_0', '058_1679617928_a73c1769be_4', '005_317383917_d8bfa350b6_3']
    -------------------------------------------------------------------------------
    Keyword: boys
    Current P@10: 1.0000
    Current P@N: 0.7647
    Current EER: 0.0604
    Top 10 utterances:  ['043_1572532018_64c030c974_4', '017_2288099178_41091aa00c_2', '006_522063319_33827f1627_3', '006_3217910740_d1d61c08ab_4', '005_2844018783_524b08e5aa_3', '004_2208310655_a3d83080c5_4', '052_3694064560_467683205b_2', '058_154871781_ae77696b77_2', '019_3639967449_137f48b43d_2', '045_3639967449_137f48b43d_0']
    -------------------------------------------------------------------------------
    Keyword: dogs
    Current P@10: 1.0000
    Current P@N: 0.8301
    Current EER: 0.0641
    Top 10 utterances:  ['016_447111935_5af98563e3_4', '016_2600867924_cd502fc911_1', '016_3593392955_a4125087f6_2', '049_3333921867_6cc7d7c73d_2', '043_2869491449_1041485a6b_2', '049_2676764246_c58205a365_2', '004_2723477522_d89f5ac62b_4', '007_1897025969_0c41688fa6_3', '017_2890113532_ab2003d74e_2', '075_3482974845_db4f16befa_2']
    -------------------------------------------------------------------------------
    Keyword: field
    Current P@10: 1.0000
    Current P@N: 0.8284
    Current EER: 0.0746
    Top 10 utterances:  ['100_3294209955_a1f1e2cc19_3', '049_3223224391_be50bf4f43_0', '006_3582742297_1daa29968e_2', '147_3294209955_a1f1e2cc19_1', '006_2763044275_aa498eb88b_1', '006_2854959952_3991a385ab_3', '010_3358682439_be4b83544c_1', '007_2534502836_7a75305655_3', '063_2295750198_6d152d7ceb_4', '063_2890113532_ab2003d74e_3']
    -------------------------------------------------------------------------------
    Keyword: hat
    Current P@10: 0.9000
    Current P@N: 0.5422
    Current EER: 0.1042
    Top 10 utterances:  ['025_2124040721_bffc0a091a_1', '004_2196107384_361d73a170_0', '120_2167644298_100ca79f54_1', '057_1547883892_e29b3db42e_1', '005_2124040721_bffc0a091a_4', '156_3150742439_b8a352e1e0_2', '003_2218609886_892dcd6915_4', '009_2484190118_e89363c465_0', '005_2218609886_892dcd6915_2', '005_2078311270_f01c9eaf4c_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2484190118_e89363c465_0.wav [error]
    -------------------------------------------------------------------------------
    Keyword: jacket
    Current P@10: 0.9000
    Current P@N: 0.7595
    Current EER: 0.0728
    Top 10 utterances:  ['084_3213992947_3f3f967a9f_4', '067_485245061_5a5de43e20_1', '077_1499581619_a5f65a882c_2', '072_535830521_aa971319fc_0', '044_375392855_54d46ed5c8_3', '033_172097782_f0844ec317_2', '168_2518508760_68d8df7365_2', '038_3287549827_04dec6fb6e_2', '072_488408004_a1e26d4886_2', '083_2641770481_c98465ff35_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/172097782_f0844ec317_2.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: large
    Current P@10: 1.0000
    Current P@N: 0.6939
    Current EER: 0.0550
    Top 10 utterances:  ['017_3364151356_eecd07a23e_4', '088_2196846255_2c1635359a_3', '017_2723477522_d89f5ac62b_2', '034_3070011270_390e597783_3', '017_2374652725_32f90fa15c_2', '030_2410320522_d967f0b75c_1', '086_1773928579_5664a810dc_3', '011_3624327440_bef4f33f32_0', '045_2938120171_970564e3d8_0', '030_3099923914_fd450f6d51_0']
    -------------------------------------------------------------------------------
    Keyword: looking
    Current P@10: 0.9000
    Current P@N: 0.5287
    Current EER: 0.0805
    Top 10 utterances:  ['025_3523471597_87e0bf3b21_0', '004_2657484284_daa07a3a1b_3', '017_247637795_fdf26a03cf_2', '090_2054869561_ff723e9eab_2', '007_127488876_f2d2a89588_4', '005_3718964174_cb2dc1615e_1', '089_3045613316_4e88862836_0', '004_2985679744_75a7102aab_3', '007_3506560025_8d0f4f9ac4_4', '051_3523471597_87e0bf3b21_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2657484284_daa07a3a1b_3.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: people
    Current P@10: 1.0000
    Current P@N: 0.9231
    Current EER: 0.0238
    Top 10 utterances:  ['086_2575647360_f5de38c751_3', '006_324208502_674488bcea_4', '052_1417031097_ab656bc4bd_3', '050_215214751_e913b6ff09_4', '049_3701291852_373ea46bb6_3', '004_2581066814_179d28f306_0', '049_3245912109_fdeef6b456_1', '141_2176980976_7054c99621_0', '017_138718600_f430ebca17_3', '123_3359530430_249f51972c_2']
    -------------------------------------------------------------------------------
    Keyword: play
    Current P@10: 0.7000
    Current P@N: 0.3837
    Current EER: 0.1628
    Top 10 utterances:  ['006_2854959952_3991a385ab_3', '030_197504190_fd1fc3d4b7_3', '041_2370481277_a3085614c9_3', '046_3301811927_a2797339e5_0', '145_2354540393_a149722680_3', '005_3655155990_b0e201dd3c_4', '052_3375991133_87d7c40925_2', '046_244571201_0339d8e8d1_1', '011_3052196390_c59dd24ca8_1', '061_3385593926_d3e9c21170_1']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3301811927_a2797339e5_0.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3655155990_b0e201dd3c_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3052196390_c59dd24ca8_1.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: runs
    Current P@10: 0.8000
    Current P@N: 0.5443
    Current EER: 0.1261
    Top 10 utterances:  ['141_3435035138_af32890a4c_0', '007_317488612_70ac35493b_2', '027_3354883962_170d19bfe4_0', '049_1523984678_edd68464da_4', '002_3363750526_efcedc47a9_1', '147_3294209955_a1f1e2cc19_1', '033_542179694_e170e9e465_2', '007_3123463486_f5b36a3624_1', '017_3472364264_dbde5a8d0a_2', '010_566397227_a469e9e415_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1523984678_edd68464da_4.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/542179694_e170e9e465_2.wav [semantic]
    -------------------------------------------------------------------------------
    Keyword: sitting
    Current P@10: 1.0000
    Current P@N: 0.7365
    Current EER: 0.0599
    Top 10 utterances:  ['049_3471841031_a949645ba8_0', '125_532457586_bddfc5251d_3', '033_3729525173_7f984ed776_2', '019_1082379191_ec1e53f996_1', '005_2608289957_044849f73e_1', '046_1082379191_ec1e53f996_2', '039_439037721_cdf1fc7358_0', '032_1082379191_ec1e53f996_4', '019_2602258549_7401a3cdae_4', '017_533713007_bf9f3e25b4_2']
    -------------------------------------------------------------------------------
    Keyword: standing
    Current P@10: 1.0000
    Current P@N: 0.7754
    Current EER: 0.0638
    Top 10 utterances:  ['006_410453140_5401bf659a_1', '074_1317292658_ba29330a0b_1', '025_3222041930_f642f49d28_4', '025_2938120171_970564e3d8_3', '057_3720366614_dfa8fe1088_0', '038_2884420269_225d27f242_0', '088_2120411340_104eb610b1_1', '003_410453140_5401bf659a_4', '086_396360611_941e5849a3_2', '137_2103568100_5d018c495b_1']
    -------------------------------------------------------------------------------
    Keyword: street
    Current P@10: 1.0000
    Current P@N: 0.7899
    Current EER: 0.0518
    Top 10 utterances:  ['023_3655964639_21e76383d0_3', '127_2078311270_f01c9eaf4c_3', '041_3569406219_f37ebf7b92_4', '042_1332722096_1e3de8ae70_1', '007_2083434441_a93bc6306b_3', '052_3072114570_e1c0127529_1', '112_436009777_440c7679a1_1', '112_435827376_4384c3005a_2', '164_3181701312_70a379ab6e_0', '027_3259991972_fce3ab18b2_3']
    -------------------------------------------------------------------------------
    Keyword: white
    Current P@10: 1.0000
    Current P@N: 0.8398
    Current EER: 0.0625
    Top 10 utterances:  ['016_3613800013_5a54968ab0_1', '025_3497224764_6e17544e0d_1', '045_1764955991_5e53a28c87_4', '031_3128164023_ebe8da4c32_1', '145_509778093_21236bb64d_1', '070_1772859261_236c09b861_1', '017_2301525531_edde12d673_1', '004_3123463486_f5b36a3624_0', '049_416106657_cab2a107a5_2', '046_3256043809_47258e0b3e_0']
    -------------------------------------------------------------------------------
    Keyword: yellow
    Current P@10: 1.0000
    Current P@N: 0.8456
    Current EER: 0.0391
    Top 10 utterances:  ['046_2759860913_f75b39d783_0', '112_2559921948_06af25d566_0', '049_2608289957_044849f73e_2', '027_2443380641_7b38d18f5b_3', '017_1167669558_87a8a467d6_1', '010_2470486377_c3a39ccb7b_0', '083_2641770481_c98465ff35_0', '086_2909955251_4b326a46a7_0', '036_2522297487_57edf117f7_2', '044_375392855_54d46ed5c8_4']
    -------------------------------------------------------------------------------
    Keyword: young
    Current P@10: 1.0000
    Current P@N: 0.8916
    Current EER: 0.0379
    Top 10 utterances:  ['017_136644343_0e2b423829_4', '059_2774430374_fee1d793e7_4', '063_583174725_6b522b621f_3', '017_488408004_a1e26d4886_3', '007_3217266166_4e0091860b_4', '066_3220161734_77f42734b9_4', '017_422763475_0bc814dac6_4', '014_2928152792_b16c73434a_3', '007_2667015110_1670324a33_2', '071_2706766641_a9df81969d_3']
    -------------------------------------------------------------------------------

No. errors: 4
No. variants: 7
No. semantic: 3
No. correct: 187
Semantic P@10: 0.995



### OracleSpeechPSyC, MFCC, logsumexp pooling

    -------------------------------------------------------------------------------
    Keyword: beach
    Current P@10: 1.0000
    Current P@N: 0.8706
    Current EER: 0.0414
    Top 10 utterances:  ['044_3642220260_3aa8a52670_0', '016_300922408_05a4f9938c_3', '011_3149919755_f9272b10b3_1', '007_106490881_5a2dd9b7bd_2', '011_3070031806_3d587c2a66_4', '025_3482974845_db4f16befa_3', '004_1499581619_a5f65a882c_4', '007_3602838407_bf13e49243_1', '007_3472364264_dbde5a8d0a_1', '007_3185409663_95f6b958d8_1']
    -------------------------------------------------------------------------------
    Keyword: behind
    Current P@10: 1.0000
    Current P@N: 0.7656
    Current EER: 0.0621
    Top 10 utterances:  ['016_3016606751_0e8be20abd_0', '060_3530843182_35af2c821c_1', '049_3119875880_22f9129a1c_1', '005_138718600_f430ebca17_0', '011_2170222061_e8bce4a32d_2', '052_3072114570_e1c0127529_1', '034_56489627_e1de43de34_2', '046_3677318686_b018862bb7_4', '046_3157847991_463e006a28_3', '002_324208502_674488bcea_1']
    -------------------------------------------------------------------------------
    Keyword: bike
    Current P@10: 0.9000
    Current P@N: 0.5922
    Current EER: 0.1188
    Top 10 utterances:  ['017_3576259024_9c05b163aa_4', '007_2544182005_3aa1332bf9_1', '007_2544182005_3aa1332bf9_4', '007_2544182005_3aa1332bf9_2', '007_1262583859_653f1469a9_4', '019_2075321027_c8fcbaf581_2', '095_136552115_6dc3e7231c_0', '017_2084217208_7bd9bc85e5_2', '038_3655074079_7df3812bc5_3', '114_3061481868_d1e00b1f2e_0']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3061481868_d1e00b1f2e_0.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: black
    Current P@10: 1.0000
    Current P@N: 0.8951
    Current EER: 0.0323
    Top 10 utterances:  ['007_1392272228_cf104086e6_1', '017_3143982558_9e2d44c155_4', '051_3145967309_b33abe4d84_4', '046_3540416981_4e74f08cbb_1', '058_2844641033_dab3715a99_1', '024_3642220260_3aa8a52670_2', '011_3259002340_707ce96858_2', '150_3655964639_21e76383d0_4', '017_2049051050_20359a434a_0', '046_359837950_9e22ffe6c2_3']
    -------------------------------------------------------------------------------
    Keyword: boys
    Current P@10: 0.9000
    Current P@N: 0.7529
    Current EER: 0.0357
    Top 10 utterances:  ['006_3217910740_d1d61c08ab_4', '006_3251648670_9339943ba2_1', '046_3072114570_e1c0127529_2', '091_3072172967_630e9c69d0_3', '005_2844018783_524b08e5aa_3', '005_3217910740_d1d61c08ab_1', '046_968081289_cdba83ce2e_3', '049_2729655904_1dd01922fb_1', '045_3639967449_137f48b43d_0', '034_2501595799_6316001e89_2']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/2501595799_6316001e89_2.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: dogs
    Current P@10: 1.0000
    Current P@N: 0.7838
    Current EER: 0.0548
    Top 10 utterances:  ['043_2869491449_1041485a6b_2', '006_447111935_5af98563e3_1', '004_3578914491_36019ba703_0', '046_468608014_09fd20eb9b_4', '049_3655155990_b0e201dd3c_0', '006_2854959952_3991a385ab_3', '123_3578914491_36019ba703_4', '041_387830531_e89c192b92_2', '049_2729655904_1dd01922fb_1', '095_2308271254_27fb466eb4_2']
    -------------------------------------------------------------------------------
    Keyword: field
    Current P@10: 1.0000
    Current P@N: 0.8209
    Current EER: 0.0826
    Top 10 utterances:  ['049_241345905_5826a72da1_2', '083_791338571_7f38510bf7_4', '100_3294209955_a1f1e2cc19_3', '161_430173345_86388d8822_4', '043_241345905_5826a72da1_4', '016_3613800013_5a54968ab0_1', '026_3192266178_f9bf5d3dba_4', '010_3358682439_be4b83544c_1', '033_3613800013_5a54968ab0_0', '003_241345811_46b5f157d4_4']
    -------------------------------------------------------------------------------
    Keyword: hat
    Current P@10: 1.0000
    Current P@N: 0.6627
    Current EER: 0.0677
    Top 10 utterances:  ['003_3185371756_ff4e9fa8a6_1', '042_2167644298_100ca79f54_0', '003_2553550034_5901aa9d6c_4', '057_1547883892_e29b3db42e_1', '025_2124040721_bffc0a091a_1', '017_2621415349_ef1a7e73be_1', '114_2162564553_96de62c7e6_3', '156_3150742439_b8a352e1e0_2', '007_2124040721_bffc0a091a_2', '052_2553550034_5901aa9d6c_3']
    -------------------------------------------------------------------------------
    Keyword: jacket
    Current P@10: 0.9000
    Current P@N: 0.8228
    Current EER: 0.0128
    Top 10 utterances:  ['046_3220650628_4ed964e5b4_2', '104_3258874419_23fec1bdc1_2', '005_3494394662_3edfd4a34c_3', '033_2084217208_7bd9bc85e5_3', '168_2518508760_68d8df7365_2', '026_416960865_048fd3f294_1', '084_3213992947_3f3f967a9f_4', '044_375392855_54d46ed5c8_3', '033_3507076266_8b17993fbb_2', '003_3429956016_3c7e3096c2_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/3220650628_4ed964e5b4_2.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: large
    Current P@10: 1.0000
    Current P@N: 0.8163
    Current EER: 0.0465
    Top 10 utterances:  ['017_211295363_49010ca38d_2', '011_3624327440_bef4f33f32_0', '017_2723477522_d89f5ac62b_2', '033_745880539_cd3f948837_0', '017_3364151356_eecd07a23e_4', '045_2170222061_e8bce4a32d_3', '009_211295363_49010ca38d_1', '004_3673165148_67f217064f_3', '007_2595186208_9b16fa0ee3_4', '046_2228022180_9597b2a458_1']
    -------------------------------------------------------------------------------
    Keyword: looking
    Current P@10: 0.9000
    Current P@N: 0.8161
    Current EER: 0.0345
    Top 10 utterances:  ['049_524105255_b346f288be_4', '049_3532205154_5674b628ea_4', '025_3523471597_87e0bf3b21_0', '045_2086513494_dbbcb583e7_2', '007_3502343542_f9b46688e5_0', '042_3149919755_f9272b10b3_0', '011_476233374_e1396998ef_1', '150_2577972703_a22c5f2a87_4', '051_3042380610_c5ea61eef8_1', '005_3004823335_9b82cbd8a7_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/524105255_b346f288be_4.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: people
    Current P@10: 1.0000
    Current P@N: 0.9112
    Current EER: 0.0358
    Top 10 utterances:  ['086_3480051754_18e5802558_1', '017_436009777_440c7679a1_2', '046_244571201_0339d8e8d1_1', '007_1536774449_e16b1b6382_4', '049_3562050678_4196a7fff3_3', '046_3468694409_a51571d621_1', '123_3359530430_249f51972c_2', '046_1536774449_e16b1b6382_2', '049_3245912109_fdeef6b456_1', '017_3609645320_815c294b65_2']
    -------------------------------------------------------------------------------
    Keyword: play
    Current P@10: 0.8000
    Current P@N: 0.5465
    Current EER: 0.0930
    Top 10 utterances:  ['090_1467533293_a2656cc000_1', '049_3584561689_b6eb24dd70_0', '043_1248940539_46d33ed487_2', '042_2913965136_2d00136697_4', '061_3385593926_d3e9c21170_1', '061_1461667284_041c8a2475_1', '052_2913965136_2d00136697_1', '004_3223055565_68973f5d20_4', '007_3375991133_87d7c40925_0', '047_444057017_f1e0fcaef7_3']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/1461667284_041c8a2475_1.wav [variant]
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/444057017_f1e0fcaef7_3.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: runs
    Current P@10: 1.0000
    Current P@N: 0.8101
    Current EER: 0.0506
    Top 10 utterances:  ['147_3294209955_a1f1e2cc19_1', '017_3470951932_27ed74eb0b_0', '017_3472364264_dbde5a8d0a_2', '027_3354883962_170d19bfe4_0', '018_3613800013_5a54968ab0_4', '046_3470951932_27ed74eb0b_2', '019_505929313_7668f021ab_1', '019_1408958345_68eea9a4e4_1', '016_566397227_a469e9e415_2', '141_3435035138_af32890a4c_0']
    -------------------------------------------------------------------------------
    Keyword: sitting
    Current P@10: 1.0000
    Current P@N: 0.8922
    Current EER: 0.0243
    Top 10 utterances:  ['039_439037721_cdf1fc7358_0', '125_532457586_bddfc5251d_3', '057_3359551687_68f2f0212a_2', '019_2985679744_75a7102aab_2', '046_1082379191_ec1e53f996_2', '045_138718600_f430ebca17_4', '019_2602258549_7401a3cdae_4', '025_3143982558_9e2d44c155_1', '046_801607443_f15956d1ce_0', '057_2901074943_041aba4607_2']
    -------------------------------------------------------------------------------
    Keyword: standing
    Current P@10: 1.0000
    Current P@N: 0.8814
    Current EER: 0.0340
    Top 10 utterances:  ['017_245895500_a4eb97af02_4', '005_2788945468_74a9618cfa_2', '049_3673165148_67f217064f_2', '049_3051384385_c5c850c1f8_1', '074_3767841911_6678052eb6_1', '038_2884420269_225d27f242_0', '004_3080056515_3013830309_4', '016_300922408_05a4f9938c_4', '066_3364861247_d590fa170d_4', '086_1317292658_ba29330a0b_4']
    -------------------------------------------------------------------------------
    Keyword: street
    Current P@10: 0.9000
    Current P@N: 0.8067
    Current EER: 0.0339
    Top 10 utterances:  ['005_3259991972_fce3ab18b2_4', '049_448658518_eec0b648a6_2', '005_3310067561_b92017acab_4', '005_463978865_c87c6ca84c_0', '083_3359551687_68f2f0212a_0', '023_3655964639_21e76383d0_3', '045_311146855_0b65fdb169_3', '007_2083434441_a93bc6306b_3', '097_2083434441_a93bc6306b_2', '112_2608289957_044849f73e_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/311146855_0b65fdb169_3.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: white
    Current P@10: 1.0000
    Current P@N: 0.8691
    Current EER: 0.0376
    Top 10 utterances:  ['005_510531976_90bbee22a2_4', '089_3363750526_efcedc47a9_2', '137_2103568100_5d018c495b_1', '031_3128164023_ebe8da4c32_1', '111_2612488996_9450de0e54_0', '043_363617160_6cb0c723be_4', '009_256085101_2c2617c5d0_1', '023_500446858_125702b296_2', '025_925491651_57df3a5b36_3', '046_2533424347_cf2f84872b_4']
    -------------------------------------------------------------------------------
    Keyword: yellow
    Current P@10: 0.9000
    Current P@N: 0.9412
    Current EER: 0.0294
    Top 10 utterances:  ['017_1167669558_87a8a467d6_0', '117_2218609886_892dcd6915_1', '058_540721368_12ac732c6c_2', '049_2608289957_044849f73e_2', '117_439037721_cdf1fc7358_4', '046_2083434441_a93bc6306b_0', '024_246055693_ccb69ac5c6_4', '017_2926595608_69b22be8d4_0', '046_1679617928_a73c1769be_0', '058_1679617928_a73c1769be_4']
    Incorrect in top 10:
    /share/data/lang/users/kamperh/flickr_multimod/flickr_audio/wavs/439037721_cdf1fc7358_4.wav [variant]
    -------------------------------------------------------------------------------
    Keyword: young
    Current P@10: 1.0000
    Current P@N: 0.9040
    Current EER: 0.0410
    Top 10 utterances:  ['085_3270691950_88583c3524_3', '052_2207244634_1db1a1890b_4', '071_2706766641_a9df81969d_3', '003_3692892751_f6574e2700_2', '007_3328646934_5cca4cebce_4', '100_1490670858_e122df2560_4', '087_1224851143_33bcdd299c_4', '042_2480327661_fb69829f57_3', '059_2646116932_232573f030_3', '004_2706766641_a9df81969d_4']
    -------------------------------------------------------------------------------

No. errors: 0
No. variants: 8
No. semantic: 2
No. correct: 192
Semantic P@10: 1.0



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

No. errors: 180
No. variants: 2
No. semantic: 8
No. correct: 10
Semantic P@10: 0.10
