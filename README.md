# Modul & Sub-modul
Ini masih plan sementara, tergantung nanti bentuk datasetnya dan kejadian tidak terduga lainnya<br/>
-Preprocessing<br/>
--loadData(filename)-->dataframe {baca file terus jadiin pandas dataframe}<br/>
--toOneHot(dataframe)-->dataframe {in case datanya multivalue, bikin one hot biar gampang kedepannya}<br/>
-Cleaning<br/>
--clearMissingValues(dataframe)-->dataframe {hapus missing value dari dataset}<br/>
-Apriori<br/>
--generateCombination(list_items,banlist,level)-->list_kombinasi (generate kombinasi berukuran level dari list items dengan pengecualian kombinasi yang berisi subset salah satu banlist)<br/>
--countItems(dataframe,list_kombinasi)-->list_kemunculan {hitung jumlah kemunculan member kombinasi pada dataframe}<br/>
--scanInfrequent(list_kemunculan,threshold)-->list_index_infrequent {return index elemen list yang tidak sampai threshold}<br/>
--getInfrequent(list_kombinasi,list_index_infrequent)-->list_infrequent {ambil kombinasi yang infrequent untuk banlist}<br/>
--dropItems(list_kombinasi,list_infrequent)-->list_kombinasi {hapus list infrequent dari list kombinasi}<br/>
--getUniqueItems(list_kombinasi)-->list_items {ambil unique items dari list kombinasi}<br/>
--mainApriori(dataframe,banlist,level,list_items)-->list_kombinasi {rekursif. pertama level=1. setelah scanInfrequent dicek, kalau list_index_infrequent kosong langsung return list_kombinasi, else return mainApriori dengan level selanjutnya}<br/>
-Association<br/>
--generateSubset(list_kombinasi)-->list_subset_kombinasi {Dibentuk subset yang mungkin dari list kombinasi}<br/>
--countSupport(dataframe,list_support)-->float {menghitung support untuk input list_support, list karena bisa saja lebih dari 1 item}<br/>
--countConfidence(suppport1,support2)-->float {menghitung confidence dengan masukan support dari dua set items}<br/>
--findAssociation(dataframe,list_kombinasi,threshold_support,threshold_confidence)-->list_association {looping list_subset, hitung support dan confidence, kalau memenuhi threshold tambah ke list}<br/>
