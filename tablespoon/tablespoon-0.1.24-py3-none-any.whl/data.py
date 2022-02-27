from pandas import read_csv
from io import StringIO

APPL = read_csv(
      StringIO(
"""
ds,y
2021-08-01,4.986069344321214
2021-08-02,4.986069344321214
2021-08-03,4.982304387584444
2021-08-04,4.992267665749145
2021-08-05,4.9902964940324095
2021-08-06,4.986001054842818
2021-08-07,4.986001054842818
2021-08-08,4.986001054842818
2021-08-09,4.984975526441821
2021-08-10,4.986615804923752
2021-08-11,4.983949049729045
2021-08-12,4.9849071622237515
2021-08-13,5.00374495158579
2021-08-14,5.00374495158579
2021-08-15,5.00374495158579
2021-08-16,5.000854237042097
2021-08-17,5.012167424634866
2021-08-18,5.009301091455334
2021-08-19,4.976940609155258
2021-08-20,4.99342132992021
2021-08-21,4.99342132992021
2021-08-22,4.99342132992021
2021-08-23,4.999304661292363
2021-08-24,5.006961868310022
2021-08-25,5.009367808232606
2021-08-26,4.999574387879504
2021-08-27,4.993692544396178
2021-08-28,4.993692544396178
2021-08-29,4.993692544396178
2021-08-30,5.003946305945459
2021-08-31,5.028213250358988
2021-09-01,5.029326204520735
2021-09-02,5.036108058335924
2021-09-03,5.035392909496409
2021-09-04,5.035392909496409
2021-09-05,5.035392909496409
2021-09-06,5.035392909496409
2021-09-07,5.043231557676272
2021-09-08,5.056118381482073
2021-09-09,5.04658145619781
2021-09-10,5.043425116919247
2021-09-11,5.043425116919247
2021-09-12,5.043425116919247
2021-09-13,5.01482653113066
2021-09-14,5.012965950029919
2021-09-15,5.000988900610644
2021-09-16,5.000180852639488
2021-09-17,5.002737571184399
2021-09-18,5.002737571184399
2021-09-19,5.002737571184399
2021-09-20,4.968423466509184
2021-09-21,4.969327019387211
2021-09-22,4.972933405785502
2021-09-23,4.9880487538038505
2021-09-24,4.981275163931258
2021-09-25,4.981275163931258
2021-09-26,4.981275163931258
2021-09-27,4.979969888176813
2021-09-28,4.964591355594849
2021-09-29,4.959131459797281
2021-09-30,4.967449422138158
2021-10-01,4.955122541153201
2021-10-02,4.955122541153201
2021-10-03,4.955122541153201
2021-10-04,4.954135448107023
2021-10-05,4.937992953484486
2021-10-06,4.937849533123045
2021-10-07,4.963264105614627
2021-10-08,4.97002160273562
2021-10-09,4.97002160273562
2021-10-10,4.97002160273562
2021-10-11,4.957726690693728
2021-10-12,4.964451699962401
2021-10-13,4.950460609952596
2021-10-14,4.956601409898694
2021-10-15,4.968214830151833
2021-10-16,4.968214830151833
2021-10-17,4.968214830151833
2021-10-18,4.965986521153356
2021-10-19,4.990500574309953
2021-10-20,5.0019308329431915
2021-10-21,5.0026703080357615
2021-10-22,5.008566505236892
2021-10-23,5.008566505236892
2021-10-24,5.008566505236892
2021-10-25,5.001796296167423
2021-10-26,5.006158634330978
2021-10-27,5.0063595033199135
2021-10-28,5.009434622406525
2021-10-29,4.991928074922253
2021-10-30,4.991928074922253
2021-10-31,4.991928074922253
2021-11-01,5.0038792264685945
2021-11-02,5.0016618439312746
2021-11-03,5.013231915885063
2021-11-04,5.0211135504636735
2021-11-05,5.023156570631548
2021-11-06,5.023156570631548
2021-11-07,5.023156570631548
2021-11-08,5.019991413206988
2021-11-09,5.011967719012072
2021-11-10,5.0107686470207655
2021-11-11,5.003677858600367
2021-11-12,5.000113417292074
2021-11-13,5.000113417292074
2021-11-14,5.000113417292074
2021-11-15,5.013098891062242
2021-11-16,5.010235230357471
2021-11-17,5.017279836814924
2021-11-18,5.035067753915632
2021-11-19,5.060377347275461
2021-11-20,5.060377347275461
2021-11-21,5.060377347275461
2021-11-22,5.085619027794655
2021-11-23,5.082149398664812
2021-11-24,5.079850363117729
2021-11-25,5.079850363117729
2021-11-26,5.072482743322057
2021-11-27,5.072482743322057
2021-11-28,5.072482743322057
2021-11-29,5.071228512233326
2021-11-30,5.075111347615041
2021-12-01,5.120863915640666
2021-12-02,5.067267678267517
2021-12-03,5.099988397656679
2021-12-04,5.099988397656679
2021-12-05,5.099988397656679
2021-12-06,5.101633118052293
2021-12-07,5.130371986528106
2021-12-08,5.1482500336504184
2021-12-09,5.164271576856079
2021-12-10,5.165985292817968
2021-12-11,5.165985292817968
2021-12-12,5.165985292817968
2021-12-13,5.199159768055827
2021-12-14,5.166213525914699
2021-12-15,5.165414351369342
2021-12-16,5.188948822683752
2021-12-17,5.135386544444626
2021-12-18,5.135386544444626
2021-12-19,5.135386544444626
2021-12-20,5.12562925146832
2021-12-21,5.144933045418053
2021-12-22,5.1535227428452925
2021-12-23,5.169631393628638
2021-12-24,5.169631393628638
2021-12-25,5.169631393628638
2021-12-26,5.169631393628638
2021-12-27,5.1766580572413385
2021-12-28,5.193845365278309
2021-12-29,5.189227694170865
2021-12-30,5.1900080698428965
2021-12-31,5.182289019924663
2022-01-01,5.182289019924663
""")
)

WALMART = read_csv(
      StringIO(
"""ds,state_id,y
2015-01-02,CA,9.691469384005337
2015-01-03,CA,9.764800032762235
2015-01-04,CA,9.823632327286663
2015-01-05,CA,9.604609707323613
2015-01-06,CA,9.45688790106941
2015-01-07,CA,9.417435838868785
2015-01-08,CA,9.479451058842528
2015-01-09,CA,9.537122958049878
2015-01-10,CA,9.864954602819344
2015-01-11,CA,9.899529730681785
2015-01-12,CA,9.551373619924957
2015-01-13,CA,9.450616322030694
2015-01-14,CA,9.395158808968725
2015-01-15,CA,9.428833125074965
2015-01-16,CA,9.546598299920646
2015-01-17,CA,9.834887461043872
2015-01-18,CA,9.80890211004626
2015-01-19,CA,9.650850821827147
2015-01-20,CA,9.44057869576626
2015-01-21,CA,9.417435838868785
2015-01-22,CA,9.362889770436468
2015-01-23,CA,9.526974266377731
2015-01-24,CA,9.81569405158546
2015-01-25,CA,9.882161765821376
2015-01-26,CA,9.482654967296842
2015-01-27,CA,9.380842351964795
2015-01-28,CA,9.377971213360134
2015-01-29,CA,9.394493583599107
2015-01-30,CA,9.58465875108751
2015-01-31,CA,9.89469904650305
2015-02-01,CA,9.879143629146611
2015-02-02,CA,9.588982266040471
2015-02-03,CA,9.579279798734897
2015-02-04,CA,9.523470868881551
2015-02-05,CA,9.565213693968287
2015-02-06,CA,9.471550124096849
2015-02-07,CA,9.987093136390925
2015-02-08,CA,9.920492151351953
2015-02-09,CA,9.71571114505921
2015-02-10,CA,9.643355794171352
2015-02-11,CA,9.536617962187327
2015-02-12,CA,9.603125426926972
2015-02-13,CA,9.543521484499182
2015-02-14,CA,9.681842877345654
2015-02-15,CA,9.719204072428633
2015-02-16,CA,9.694924684536947
2015-02-17,CA,9.453757028129948
2015-02-18,CA,9.392995206560258
2015-02-19,CA,9.34975442775886
2015-02-20,CA,9.517383797906584
2015-02-21,CA,9.678028823264478
2015-02-22,CA,9.817330356084954
2015-02-23,CA,9.52427481557203
2015-02-24,CA,9.412546252075513
2015-02-25,CA,9.422058905620926
2015-02-26,CA,9.406564833939129
2015-02-27,CA,9.531988993991236
2015-02-28,CA,9.809616336926057
2015-03-01,CA,9.877964595305043
2015-03-02,CA,9.57289797907307
2015-03-03,CA,9.559587800086119
2015-03-04,CA,9.472858470764415
2015-03-05,CA,9.53285855926342
2015-03-06,CA,9.590077331511615
2015-03-07,CA,9.822277497110585
2015-03-08,CA,9.958922259424229
2015-03-09,CA,9.633710883953182
2015-03-10,CA,9.536473630802217
2015-03-11,CA,9.494014423030425
2015-03-12,CA,9.49461665129313
2015-03-13,CA,9.606091787896707
2015-03-14,CA,9.825742203911275
2015-03-15,CA,9.943285022410194
2015-03-16,CA,9.595534743241988
2015-03-17,CA,9.48440514846878
2015-03-18,CA,9.429957713513835
2015-03-19,CA,9.413852481341165
2015-03-20,CA,9.546026585476431
2015-03-21,CA,9.83729432980133
2015-03-22,CA,9.90218670680308
2015-03-23,CA,9.57073837671504
2015-03-24,CA,9.433803872101313
2015-03-25,CA,9.452737380212278
2015-03-26,CA,9.477003077203888
2015-03-27,CA,9.545168400484906
2015-03-28,CA,9.784422445377189
2015-03-29,CA,9.864122829013851
2015-03-30,CA,9.581972891547895
2015-03-31,CA,9.5302475917227
2015-04-01,CA,9.613202094214232
2015-04-02,CA,9.588091641516831
2015-04-03,CA,9.772011189747742
2015-04-04,CA,9.975854724662028
2015-04-05,CA,9.821517989668877
2015-04-06,CA,9.61573881119536
2015-04-07,CA,9.562615651570228
2015-04-08,CA,9.556550752867032
2015-04-09,CA,9.51355124604559
2015-04-10,CA,9.653293924495339
2015-04-11,CA,9.818800744368934
2015-04-12,CA,9.885119895177944
2015-04-13,CA,9.499121839871265
2015-04-14,CA,9.505320746909074
2015-04-15,CA,9.47883962501119
2015-04-16,CA,9.511185430954244
2015-04-17,CA,9.565844630930576
2015-04-18,CA,9.754871528207344
2015-04-19,CA,9.879041159631202
2015-04-20,CA,9.561138078742038
2015-04-21,CA,9.485468978356344
2015-04-22,CA,9.48029117039765
2015-04-23,CA,9.522885774152654
2015-04-24,CA,9.604609707323613
2015-04-25,CA,9.855924135604518
2015-04-26,CA,9.874367653962276
2015-04-27,CA,9.600556469321608
2015-04-28,CA,9.47608353690921
2015-04-29,CA,9.434203664214742
2015-04-30,CA,9.471550124096849
2015-05-01,CA,9.75080246487048
2015-05-02,CA,9.878015886562459
2015-05-03,CA,9.92299601892417
2015-05-04,CA,9.742790491838836
2015-05-05,CA,9.589393056132515
2015-05-06,CA,9.574427775630369
2015-05-07,CA,9.524420918282495
2015-05-08,CA,9.653358136136932
2015-05-09,CA,9.858803944909488
2015-05-10,CA,9.71250862865099
2015-05-11,CA,9.65033572298117
2015-05-12,CA,9.536690120068803
2015-05-13,CA,9.542445945729886
2015-05-14,CA,9.419466131522189
2015-05-15,CA,9.63266259715077
2015-05-16,CA,9.826390502151161
2015-05-17,CA,9.84659969032908
2015-05-18,CA,9.58486505717771
2015-05-19,CA,9.473857817428666
2015-05-20,CA,9.46815584482167
2015-05-21,CA,9.498597279178806
2015-05-22,CA,9.674325928896355
2015-05-23,CA,9.752490228984199
2015-05-24,CA,9.726153537253213
2015-05-25,CA,9.778037701818713
2015-05-26,CA,9.544166252942194
2015-05-27,CA,9.470702633773001
2015-05-28,CA,9.470856776355195
2015-05-29,CA,9.546241016698438
2015-05-30,CA,9.82135516299751
2015-05-31,CA,9.890098315417111
2015-06-01,CA,9.722804652410682
2015-06-02,CA,9.729669736233394
2015-06-03,CA,9.616005460087013
2015-06-04,CA,9.612198984490236
2015-06-05,CA,9.707411839509511
2015-06-06,CA,9.942804414913079
2015-06-07,CA,9.967353972864542
2015-06-08,CA,9.784985508455128
2015-06-09,CA,9.703511060503452
2015-06-10,CA,9.654897979890443
2015-06-11,CA,9.589940513889292
2015-06-12,CA,9.689922976002242
2015-06-13,CA,9.895908907012577
2015-06-14,CA,9.980263391338177
2015-06-15,CA,9.731512287796317
2015-06-16,CA,9.567595147779924
2015-06-17,CA,9.598116617213263
2015-06-18,CA,9.63351441386512
2015-06-19,CA,9.70418259070176
2015-06-20,CA,9.905834795604477
2015-06-21,CA,9.827416115584832
2015-06-22,CA,9.675080171546819
2015-06-23,CA,9.61547209118311
2015-06-24,CA,9.550092936718967
2015-06-25,CA,9.600150240473774
2015-06-26,CA,9.718181546701214
2015-06-27,CA,9.899027621814035
2015-06-28,CA,9.942034962148368
2015-06-29,CA,9.655218482441182
2015-06-30,CA,9.629576884168266
2015-07-01,CA,9.7553934942914
2015-07-02,CA,9.785435730759993
2015-07-03,CA,10.060833123259906
2015-07-04,CA,9.713234625415893
2015-07-05,CA,9.872358017339208
2015-07-06,CA,9.78318258949248
2015-07-07,CA,9.69319852665812
2015-07-08,CA,9.639782389465795
2015-07-09,CA,9.682840881420505
2015-07-10,CA,9.796625910752034
2015-07-11,CA,9.947504437952903
2015-07-12,CA,9.973433303222794
2015-07-13,CA,9.728955578017002
2015-07-14,CA,9.637632201310455
2015-07-15,CA,9.664151101014628
2015-07-16,CA,9.700820421076743
2015-07-17,CA,9.775995032020852
2015-07-18,CA,9.923633258229085
2015-07-19,CA,9.98072633287693
2015-07-20,CA,9.728479189036397
2015-07-21,CA,9.653293924495339
2015-07-22,CA,9.594377532670727
2015-07-23,CA,9.624038165010823
2015-07-24,CA,9.740733301234702
2015-07-25,CA,9.854769885738698
2015-07-26,CA,9.913883328718248
2015-07-27,CA,9.726511682066926
2015-07-28,CA,9.61326893243235
2015-07-29,CA,9.57373270366244
2015-07-30,CA,9.633383412358416
2015-07-31,CA,9.759963542450086
2015-08-01,CA,9.997979215628845
2015-08-02,CA,10.063606103428887
2015-08-03,CA,9.82822506803558
2015-08-04,CA,9.73477299914839
2015-08-05,CA,9.702227794721923
2015-08-06,CA,9.678655075789957
2015-08-07,CA,9.791438048727505
2015-08-08,CA,10.001339952703633
2015-08-09,CA,10.062284564283125
2015-08-10,CA,9.795790977080754
2015-08-11,CA,9.68638819820623
2015-08-12,CA,9.687133400997965
2015-08-13,CA,9.65033572298117
2015-08-14,CA,9.742320649814571
2015-08-15,CA,9.972360416822504
2015-08-16,CA,10.094025264101424
2015-08-17,CA,9.808627271512169
2015-08-18,CA,9.677590213025297
2015-08-19,CA,9.675896626294639
2015-08-20,CA,9.639652206558628
2015-08-21,CA,9.701248961901815
2015-08-22,CA,9.955225747940542
2015-08-23,CA,10.018912253951546
2015-08-24,CA,9.657778811561771
2015-08-25,CA,9.560081331311986
2015-08-26,CA,9.551800150108434
2015-08-27,CA,9.574080300037034
2015-08-28,CA,9.701554950093058
2015-08-29,CA,9.965193941972107
2015-08-30,CA,10.05702375789833
2015-08-31,CA,9.694185267410399
2015-09-01,CA,9.69922708822342
2015-09-02,CA,9.669346247012378
2015-09-03,CA,9.69412362463029
2015-09-04,CA,9.801399454452342
2015-09-05,CA,9.951991961595743
2015-09-06,CA,9.898374503149306
2015-09-07,CA,9.961331842220567
2015-09-08,CA,9.711600390872473
2015-09-09,CA,9.701860844684168
2015-09-10,CA,9.704121561132915
2015-09-11,CA,9.752839066197039
2015-09-12,CA,9.979568576941464
2015-09-13,CA,10.066966021528604
2015-09-14,CA,9.675205823365795
2015-09-15,CA,9.668081624649718
2015-09-16,CA,9.561630845638076
2015-09-17,CA,9.598116617213263
2015-09-18,CA,9.752199438322346
2015-09-19,CA,10.01332801821566
2015-09-20,CA,10.050181931686932
2015-09-21,CA,9.75475549873573
2015-09-22,CA,9.66478610230597
2015-09-23,CA,9.62231756369957
2015-09-24,CA,9.589461504744746
2015-09-25,CA,9.766062876624456
2015-09-26,CA,9.98220630724752
2015-09-27,CA,10.019580271522981
2015-09-28,CA,9.696401880595555
2015-09-29,CA,9.523470868881551
2015-09-30,CA,9.543378146148761
2015-10-01,CA,9.663070672551461
2015-10-02,CA,9.84065424336456
2015-10-03,CA,10.097655331613764
2015-10-04,CA,10.115731922981338
2015-10-05,CA,9.826120428959685
2015-10-06,CA,9.690479958409808
2015-10-07,CA,9.667575327569097
2015-10-08,CA,9.671681590643265
2015-10-09,CA,9.824768967824722
2015-10-10,CA,10.002608643403935
2015-10-11,CA,9.967822928041022
2015-10-12,CA,9.824065485558638
2015-10-13,CA,9.63795828472548
2015-10-14,CA,9.601436066117046
2015-10-15,CA,9.585071320714485
2015-10-16,CA,9.695786647402777
2015-10-17,CA,9.988012507605816
2015-10-18,CA,10.047024967532325
2015-10-19,CA,9.680656452403964
2015-10-20,CA,9.615005159913578
2015-10-21,CA,9.57094757444252
2015-10-22,CA,9.55470991405776
2015-10-23,CA,9.687629894522718
2015-10-24,CA,9.90593455617918
2015-10-25,CA,10.027120112981404
2015-10-26,CA,9.6542566664586
2015-10-27,CA,9.606293719711752
2015-10-28,CA,9.564722689855031
2015-10-29,CA,9.588639812011577
2015-10-30,CA,9.747535250762242
2015-10-31,CA,9.922113016659292
2015-11-01,CA,9.996294602122335
2015-11-02,CA,9.65059330557001
2015-11-03,CA,9.683588731386807
2015-11-04,CA,9.565634362837983
2015-11-05,CA,9.57644075656207
2015-11-06,CA,9.695417325719395
2015-11-07,CA,9.93672888631593
2015-11-08,CA,9.996157887377436
2015-11-09,CA,9.617137925318126
2015-11-10,CA,9.615272004478204
2015-11-11,CA,9.575677688993569
2015-11-12,CA,9.483187955469509
2015-11-13,CA,9.588228712314113
2015-11-14,CA,9.893740201081249
2015-11-15,CA,9.98216009118743
2015-11-16,CA,9.6242365055622
2015-11-17,CA,9.530538036104643
2015-11-18,CA,9.496721598694915
2015-11-19,CA,9.4925826756776
2015-11-20,CA,9.627799924932715
2015-11-21,CA,9.900081759401296
2015-11-22,CA,9.94453352197213
2015-11-23,CA,9.683837890476173
2015-11-24,CA,9.611596635310292
2015-11-25,CA,9.746541302073402
2015-11-26,CA,9.166388484447
2015-11-27,CA,9.35331454092729
2015-11-28,CA,9.621655004873238
2015-11-29,CA,9.75359446296151
2015-11-30,CA,9.57838048699361
2015-12-01,CA,9.60393530751386
2015-12-02,CA,9.5591645793702
2015-12-03,CA,9.617137925318126
2015-12-04,CA,9.721125994942152
2015-12-05,CA,9.91353688838913
2015-12-06,CA,9.957075711706057
2015-12-07,CA,9.632990304838447
2015-12-08,CA,9.536473630802217
2015-12-09,CA,9.530029703062944
2015-12-10,CA,9.532568788180548
2015-12-11,CA,9.589598387915172
2015-12-12,CA,9.871170951059584
2015-12-13,CA,9.889033595565978
2015-12-14,CA,9.647239545573877
2015-12-15,CA,9.560151815893512
2015-12-16,CA,9.56843430866833
2015-12-17,CA,9.599201730917567
2015-12-18,CA,9.588365764325566
2015-12-19,CA,9.900483043515829
2015-12-20,CA,9.851983709669012
2015-12-21,CA,9.643226075660339
2015-12-22,CA,9.681967682338016
2015-12-23,CA,9.712448105122451
2015-12-24,CA,9.535390480896702
2015-12-25,CA,1.791759469228055
2015-12-26,CA,9.702900186935281
2015-12-27,CA,9.68190528178887
2015-12-28,CA,9.618668045697824
2015-12-29,CA,9.593491702487762
2015-12-30,CA,9.600962533214572
2015-12-31,CA,9.695725103260221
2016-01-01,CA,9.500319803476646
2016-01-02,CA,9.855032332266724
2016-01-03,CA,9.884508585938326
2016-01-04,CA,9.70838466137744
2016-01-05,CA,9.57644075656207
2016-01-06,CA,9.51576412590412
2016-01-07,CA,9.643290937019207
2016-01-08,CA,9.695355758842355
2016-01-09,CA,10.039852427056644
2016-01-10,CA,10.008568028986636
2016-01-11,CA,9.693136823020671
2016-01-12,CA,9.55094690773585
2016-01-13,CA,9.472781556562168
2016-01-14,CA,9.500843461614666
2016-01-15,CA,9.667765219015058
2016-01-16,CA,9.970211184579036
2016-01-17,CA,9.945205145887996
2016-01-18,CA,9.798349234412823
2016-01-19,CA,9.501740523796375
2016-01-20,CA,9.563880407219427
2016-01-21,CA,9.54230245311951
2016-01-22,CA,9.62258246436337
2016-01-23,CA,10.036400003655869
2016-01-24,CA,9.991727341385536
2016-01-25,CA,9.670230532062421
2016-01-26,CA,9.537627699020323
2016-01-27,CA,9.530102337891375
2016-01-28,CA,9.532278933106054
2016-01-29,CA,9.674325928896355
2016-01-30,CA,9.970865787866076
2016-01-31,CA,10.0650109866928
2016-02-01,CA,9.718241724224926
2016-02-02,CA,9.625491749673769
2016-02-03,CA,9.640302951684735
2016-02-04,CA,9.6457525564523
2016-02-05,CA,9.735364715141987
2016-02-06,CA,10.052338499268483
2016-02-07,CA,9.834137474401334
2016-02-08,CA,9.652844327519334
2016-02-09,CA,9.653358136136932
2016-02-10,CA,9.700452954144632
2016-02-11,CA,9.738789780495722
2016-02-12,CA,9.732461955484025
2016-02-13,CA,9.99186466315354
2016-02-14,CA,9.86464276871256
2016-02-15,CA,9.864278839310847
2016-02-16,CA,9.632269206115012
2016-02-17,CA,9.585689856179723
2016-02-18,CA,9.636000187369866
2016-02-19,CA,9.747652120978
2016-02-20,CA,9.968713337453835
2016-02-21,CA,10.022958052512294
2016-02-22,CA,9.69701673550917
2016-02-23,CA,9.589872098057842
2016-02-24,CA,9.54273286919502
2016-02-25,CA,9.583075655461428
2016-02-26,CA,9.701738498076075
2016-02-27,CA,9.977945463454137
2016-02-28,CA,10.050052389617964
2016-02-29,CA,9.694739881505651
2016-03-01,CA,9.69873632077599
2016-03-02,CA,9.64309634032025
2016-03-03,CA,9.65637144183101
2016-03-04,CA,9.686263943732909
2016-03-05,CA,9.999797232673536
2016-03-06,CA,10.135551201224898
2016-03-07,CA,9.749636827717868
2016-03-08,CA,9.685518092495647
2016-03-09,CA,9.651429991057276
2016-03-10,CA,9.66997795897274
2016-03-11,CA,9.69738546707677
2016-03-12,CA,10.021937032735671
2016-03-13,CA,9.995929987925688
2016-03-14,CA,9.732580600557428
2016-03-15,CA,9.619199713152362
2016-03-16,CA,9.602855320908718
2016-03-17,CA,9.560715513766388
2016-03-18,CA,9.721005982940808
2016-03-19,CA,9.846917201047734
2016-03-20,CA,9.874110233825451
2016-03-21,CA,9.713597426242222
2016-03-22,CA,9.653807502217354
2016-03-23,CA,9.625161575008372
2016-03-24,CA,9.630891117502388
2016-03-25,CA,9.83595789574253
2016-03-26,CA,10.076894491940509
2016-03-27,CA,9.966274540634894
2016-03-28,CA,9.647433337764658
2016-03-29,CA,9.636849167012697
2016-03-30,CA,9.571644584298577
2016-03-31,CA,9.65509029374725
2016-04-01,CA,9.84808054526439
2016-04-02,CA,10.00654040759221
2016-04-03,CA,10.109566325223746
2016-04-04,CA,9.808792183696804
2016-04-05,CA,9.704792681624228
2016-04-06,CA,9.668208158877395
2016-04-07,CA,9.645946636996333
2016-04-08,CA,9.782110566369528
2016-04-09,CA,10.056680631152522
2016-04-10,CA,10.088430670035034
2016-04-11,CA,9.769384568012647
2016-04-12,CA,9.628524252492122
2016-04-13,CA,9.589735252351163
2016-04-14,CA,9.620394932418154
2016-04-15,CA,9.696155832738006
2016-04-16,CA,9.931297253175396
2016-04-17,CA,10.044639832292011
2016-04-18,CA,9.744022777885101
2016-04-19,CA,9.66675204770245
2016-04-20,CA,9.625623789021686
2016-04-21,CA,9.58107599956325
2016-04-22,CA,9.746541302073402
2016-04-23,CA,9.991223666840215
2016-04-24,CA,10.05134705577498
2016-04-25,CA,9.771326648933789
2016-04-26,CA,9.616605160254911
2016-04-27,CA,9.604811938609481
2016-04-28,CA,9.593150789519541
2016-04-29,CA,9.751501195538246
2016-04-30,CA,10.013551987398436
2016-05-01,CA,10.072766084358127
2016-05-02,CA,9.858333270529018
2016-05-03,CA,9.788637710857186
2016-05-04,CA,9.756494528795468
2016-05-05,CA,9.692581318886397
2016-05-06,CA,9.777810944448126
2016-05-07,CA,10.048410069255738
2016-05-08,CA,9.901485549865455
2016-05-09,CA,9.847763403763766
2016-05-10,CA,9.739261284011265
2016-05-11,CA,9.692210811286753
2016-05-12,CA,9.648466262323895
2016-05-13,CA,9.82395721357932
2016-05-14,CA,10.044856897998653
2016-05-15,CA,10.114720452824503
2016-05-16,CA,9.782505655975346
2016-05-17,CA,9.689675328650802
2016-05-18,CA,9.660013734748668
2016-05-19,CA,9.69873632077599
2016-05-20,CA,9.765948138514066
2016-05-21,CA,10.04771775820736
2016-05-22,CA,10.112288742134462
"""
      )
)