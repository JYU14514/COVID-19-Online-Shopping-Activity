import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import json
from weasyprint import HTML

# 1. Macro JSON Data
macro_data = [
    {"pandemic_phase": "1_Pre-COVID", "review_count": "34255890", "avg_rating": "4.2621996392445105", "avg_sentiment_score": "0.631099819622262", "avg_review_length": "157.43689111565894", "pct_shipping_keyword": "2.5825077088932735", "pct_verified_purchase": "92.522553055839452", "avg_helpful_votes": "1.2082837725132762", "unique_products": "2624063", "unique_users": "13422339"},
    {"pandemic_phase": "2_Lockdown", "review_count": "10577552", "avg_rating": "4.1258146497412662", "avg_sentiment_score": "0.56290732487063244", "avg_review_length": "175.91012003533584", "pct_shipping_keyword": "3.0616063149583193", "pct_verified_purchase": "93.542456704538068", "avg_helpful_votes": "0.9661817781656854", "unique_products": "1176919", "unique_users": "6289950"},
    {"pandemic_phase": "3_New Normal", "review_count": "18029421", "avg_rating": "4.0064380325912952", "avg_sentiment_score": "0.50321901629564281", "avg_review_length": "179.97679315381239", "pct_shipping_keyword": "2.614021825770223", "pct_verified_purchase": "91.343870665619264", "avg_helpful_votes": "0.73734902524046531", "unique_products": "1690219", "unique_users": "9157710"}
]
df_macro = pd.DataFrame(macro_data)
for col in df_macro.columns[1:]:
    df_macro[col] = pd.to_numeric(df_macro[col])
df_macro['Phase_Label'] = df_macro['pandemic_phase'].apply(lambda x: x.split('_', 1)[-1])

# 2. Category JSON Data
cat_data = [
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Health & Personal Care", "review_count": "6178244", "category_share_pct": "18.035567022196766", "avg_rating": "4.2960375148666685"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Sports & Outdoors", "review_count": "5641932", "category_share_pct": "16.469961808027758", "avg_rating": "4.2983451413452043"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Prime Video", "review_count": "5185423", "category_share_pct": "15.137317991154223", "avg_rating": "4.1872375696254638"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Grocery", "review_count": "5086234", "category_share_pct": "14.847764866129593", "avg_rating": "4.2692748701691583"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "AMAZON FASHION", "review_count": "2823091", "category_share_pct": "8.2411842167872447", "avg_rating": "4.15432942119119"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Movies & TV", "review_count": "2034966", "category_share_pct": "5.9404849793714307", "avg_rating": "4.48414371542326"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Amazon Home", "review_count": "1714175", "category_share_pct": "5.0040299638981791", "avg_rating": "4.2964347280761892"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": None, "review_count": "1092880", "category_share_pct": "3.1903418652967419", "avg_rating": "4.2945327940853568"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "All Beauty", "review_count": "1068383", "category_share_pct": "3.1188300756453855", "avg_rating": "4.1851845265227716"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Video Games", "review_count": "1055006", "category_share_pct": "3.0797798568362986", "avg_rating": "4.1261044960881685"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Industrial & Scientific", "review_count": "437793", "category_share_pct": "1.2780079571717446", "avg_rating": "4.2825604794960208"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Computers", "review_count": "384270", "category_share_pct": "1.1217632938452338", "avg_rating": "4.040913940718764"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Tools & Home Improvement", "review_count": "365073", "category_share_pct": "1.0657232960521532", "avg_rating": "4.2956367630583463"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "All Electronics", "review_count": "349587", "category_share_pct": "1.0205164717658775", "avg_rating": "4.2775160403561907"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Automotive", "review_count": "230550", "category_share_pct": "0.67302294583500821", "avg_rating": "4.34849273476469"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Toys & Games", "review_count": "174893", "category_share_pct": "0.51054869688103277", "avg_rating": "4.25097059344857"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Cell Phones & Accessories", "review_count": "129559", "category_share_pct": "0.37820941157856358", "avg_rating": "4.00875276900871"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Office Products", "review_count": "74820", "category_share_pct": "0.21841499374268192", "avg_rating": "4.3122828120823291"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Pet Supplies", "review_count": "66293", "category_share_pct": "0.19352292408692345", "avg_rating": "4.2372497850451776"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Arts, Crafts & Sewing", "review_count": "35943", "category_share_pct": "0.10492502165321059", "avg_rating": "4.38750243441004"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Baby", "review_count": "33618", "category_share_pct": "0.0981378676776461", "avg_rating": "4.0461062526027725"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Home Audio & Theater", "review_count": "28424", "category_share_pct": "0.082975511656535564", "avg_rating": "4.1832958063608192"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Camera & Photo", "review_count": "22576", "category_share_pct": "0.065903994904233987", "avg_rating": "4.2888465627214716"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Books", "review_count": "8376", "category_share_pct": "0.024451269548098151", "avg_rating": "4.4998806112702958"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Musical Instruments", "review_count": "7189", "category_share_pct": "0.020986172013046516", "avg_rating": "4.2922520517457228"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Premium Beauty", "review_count": "6834", "category_share_pct": "0.019949853879143119", "avg_rating": "4.2074919520046814"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Software", "review_count": "5106", "category_share_pct": "0.014905465892142927", "avg_rating": "3.93654524089307"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Appliances", "review_count": "3417", "category_share_pct": "0.00997492693957156", "avg_rating": "4.0869183494293226"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Amazon Elements", "review_count": "3218", "category_share_pct": "0.0093940049433834591", "avg_rating": "4.2467371037911743"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Buy a Kindle", "review_count": "2165", "category_share_pct": "0.0063200810138052173", "avg_rating": "4.4618937644341816"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Digital Music", "review_count": "1679", "category_share_pct": "0.0049013468924614129", "avg_rating": "4.5723645026801671"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Sports Collectibles", "review_count": "773", "category_share_pct": "0.0022565462464995069", "avg_rating": "4.4618369987063389"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "GPS & Navigation", "review_count": "721", "category_share_pct": "0.002104747533927742", "avg_rating": "3.9528432732316228"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "SUBSCRIPTION BOXES", "review_count": "552", "category_share_pct": "0.0016114017180695057", "avg_rating": "3.7989130434782608"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Handmade", "review_count": "478", "category_share_pct": "0.00139538047325584", "avg_rating": "4.62970711297071"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Car Electronics", "review_count": "429", "category_share_pct": "0.0012523393787170615", "avg_rating": "4.088578088578088"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Portable Audio & Accessories", "review_count": "427", "category_share_pct": "0.0012465009666950706", "avg_rating": "3.9414519906323195"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Collectibles & Fine Art", "review_count": "272", "category_share_pct": "0.000794024034990771", "avg_rating": "4.3235294117647056"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Entertainment", "review_count": "166", "category_share_pct": "0.00048458819782524988", "avg_rating": "4.4518072289156621"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Amazon Devices", "review_count": "165", "category_share_pct": "0.00048166899181425441", "avg_rating": "4.4060606060606062"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Collectible Coins", "review_count": "62", "category_share_pct": "0.00018099077268171984", "avg_rating": "4.790322580645161"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Unique Finds", "review_count": "45", "category_share_pct": "0.00013136427049479667", "avg_rating": "4.2666666666666666"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Amazon Fire TV", "review_count": "35", "category_share_pct": "0.00010217221038484184", "avg_rating": "4.9428571428571439"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Gift Cards", "review_count": "32", "category_share_pct": "9.34145923518554e-05", "avg_rating": "3.90625"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Audible Audiobooks", "review_count": "14", "category_share_pct": "4.0868884153936739e-05", "avg_rating": "3.9285714285714284"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "Fire Phone", "review_count": "1", "category_share_pct": "2.9192060109954813e-06", "avg_rating": "4.0"},
    {"pandemic_phase": "1_Pre-COVID", "main_category": "", "review_count": "1", "category_share_pct": "2.9192060109954813e-06", "avg_rating": "5.0"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Health & Personal Care", "review_count": "2641152", "category_share_pct": "24.969406910029846", "avg_rating": "4.2474064347678526"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Grocery", "review_count": "2227486", "category_share_pct": "21.058615452800421", "avg_rating": "4.0321636140474206"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Sports & Outdoors", "review_count": "1696721", "category_share_pct": "16.040772004713379", "avg_rating": "4.1567847630812551"},
    {"pandemic_phase": "2_Lockdown", "main_category": "AMAZON FASHION", "review_count": "708787", "category_share_pct": "6.7008604637443527", "avg_rating": "4.1092387416811995"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Amazon Home", "review_count": "684489", "category_share_pct": "6.4711475774356861", "avg_rating": "4.17709269250492"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Prime Video", "review_count": "515311", "category_share_pct": "4.8717415901146124", "avg_rating": "3.8918323109733746"},
    {"pandemic_phase": "2_Lockdown", "main_category": "All Beauty", "review_count": "370901", "category_share_pct": "3.5064918612548541", "avg_rating": "4.0583632829245655"},
    {"pandemic_phase": "2_Lockdown", "main_category": None, "review_count": "311639", "category_share_pct": "2.9462299027222931", "avg_rating": "4.1605736124169326"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Movies & TV", "review_count": "233934", "category_share_pct": "2.2116081301231136", "avg_rating": "4.2580086691118071"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Industrial & Scientific", "review_count": "206942", "category_share_pct": "1.956426212794794", "avg_rating": "4.1088372587488244"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Video Games", "review_count": "205345", "category_share_pct": "1.9413282014590898", "avg_rating": "3.8707151379385891"},
    {"pandemic_phase": "2_Lockdown", "main_category": "All Electronics", "review_count": "186166", "category_share_pct": "1.7600102556810877", "avg_rating": "4.081260810244614"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Computers", "review_count": "165373", "category_share_pct": "1.5634335808512214", "avg_rating": "3.9545330858120722"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Tools & Home Improvement", "review_count": "165321", "category_share_pct": "1.562941973719439", "avg_rating": "4.1792452259543529"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Automotive", "review_count": "71311", "category_share_pct": "0.67417300335654229", "avg_rating": "4.1596107192438749"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Toys & Games", "review_count": "55212", "category_share_pct": "0.52197332615334813", "avg_rating": "4.0869013982467584"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Cell Phones & Accessories", "review_count": "41204", "category_share_pct": "0.38954192803779175", "avg_rating": "3.9835452868653562"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Office Products", "review_count": "27377", "category_share_pct": "0.25882170090017048", "avg_rating": "4.2151806260729767"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Pet Supplies", "review_count": "17658", "category_share_pct": "0.16693843717336487", "avg_rating": "4.1461094121644591"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Camera & Photo", "review_count": "12746", "category_share_pct": "0.12050047118652785", "avg_rating": "4.2950729640671605"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Arts, Crafts & Sewing", "review_count": "9777", "category_share_pct": "0.092431594758409119", "avg_rating": "4.2301319423135917"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Baby", "review_count": "7284", "category_share_pct": "0.068862814382760776", "avg_rating": "4.1188907193849547"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Home Audio & Theater", "review_count": "5754", "category_share_pct": "0.05439821992839175", "avg_rating": "3.9787973583594018"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Premium Beauty", "review_count": "2864", "category_share_pct": "0.027076208181250255", "avg_rating": "3.8596368715083829"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Musical Instruments", "review_count": "2081", "category_share_pct": "0.019673739254602578", "avg_rating": "4.233061028351754"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Appliances", "review_count": "1185", "category_share_pct": "0.011202970214658362", "avg_rating": "4.0506329113924044"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Software", "review_count": "680", "category_share_pct": "0.0064287086463862327", "avg_rating": "4.0132352941176466"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Books", "review_count": "531", "category_share_pct": "0.0050200651341633677", "avg_rating": "4.3804143126177042"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Handmade", "review_count": "494", "category_share_pct": "0.004670267751933529", "avg_rating": "4.2914979757085012"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Buy a Kindle", "review_count": "428", "category_share_pct": "0.0040463048539019237", "avg_rating": "4.4626168224299061"},
    {"pandemic_phase": "2_Lockdown", "main_category": "SUBSCRIPTION BOXES", "review_count": "280", "category_share_pct": "0.0026471153249825671", "avg_rating": "3.871428571428571"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Portable Audio & Accessories", "review_count": "233", "category_share_pct": "0.0022027781097176359", "avg_rating": "4.0343347639484977"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Digital Music", "review_count": "227", "category_share_pct": "0.0021460542098965807", "avg_rating": "4.4008810572687214"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Sports Collectibles", "review_count": "223", "category_share_pct": "0.0021082382766825442", "avg_rating": "4.331838565022422"},
    {"pandemic_phase": "2_Lockdown", "main_category": "GPS & Navigation", "review_count": "180", "category_share_pct": "0.00170171699463165", "avg_rating": "4.1944444444444464"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Collectibles & Fine Art", "review_count": "116", "category_share_pct": "0.0010966620632070635", "avg_rating": "3.5431034482758617"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Car Electronics", "review_count": "69", "category_share_pct": "0.00065232484794213255", "avg_rating": "3.5072463768115938"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Amazon Fire TV", "review_count": "17", "category_share_pct": "0.00016071771615965583", "avg_rating": "4.5294117647058814"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Entertainment", "review_count": "16", "category_share_pct": "0.00015126373285614668", "avg_rating": "4.5"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Unique Finds", "review_count": "9", "category_share_pct": "8.5085849731582518e-05", "avg_rating": "4.0"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Collectible Coins", "review_count": "9", "category_share_pct": "8.5085849731582518e-05", "avg_rating": "5.0"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Amazon Elements", "review_count": "7", "category_share_pct": "6.6177883124564173e-05", "avg_rating": "5.0"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Amazon Devices", "review_count": "6", "category_share_pct": "5.6723899821055e-05", "avg_rating": "5.0"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Gift Cards", "review_count": "5", "category_share_pct": "4.7269916517545835e-05", "avg_rating": "2.4"},
    {"pandemic_phase": "2_Lockdown", "main_category": "Audible Audiobooks", "review_count": "1", "category_share_pct": "9.4539833035091673e-06", "avg_rating": "5.0"},
    {"pandemic_phase": "2_Lockdown", "main_category": "", "review_count": "1", "category_share_pct": "9.4539833035091673e-06", "avg_rating": "5.0"},
    {"pandemic_phase": "3_New Normal", "main_category": "Health & Personal Care", "review_count": "4494038", "category_share_pct": "24.926136008471929", "avg_rating": "4.0851243358422877"},
    {"pandemic_phase": "3_New Normal", "main_category": "Grocery", "review_count": "4033733", "category_share_pct": "22.373059012821322", "avg_rating": "3.9214018379501132"},
    {"pandemic_phase": "3_New Normal", "main_category": "Sports & Outdoors", "review_count": "2679156", "category_share_pct": "14.859911474694613", "avg_rating": "4.0608165407314791"},
    {"pandemic_phase": "3_New Normal", "main_category": "Amazon Home", "review_count": "1306241", "category_share_pct": "7.2450524062863693", "avg_rating": "4.0148058436383511"},
    {"pandemic_phase": "3_New Normal", "main_category": "AMAZON FASHION", "review_count": "1099673", "category_share_pct": "6.0993250975724624", "avg_rating": "3.9732620515371422"},
    {"pandemic_phase": "3_New Normal", "main_category": "Prime Video", "review_count": "860518", "category_share_pct": "4.77285432516108", "avg_rating": "3.8381288944565943"},
    {"pandemic_phase": "3_New Normal", "main_category": None, "review_count": "574830", "category_share_pct": "3.1882887420511175", "avg_rating": "4.0787224048849211"},
    {"pandemic_phase": "3_New Normal", "main_category": "All Beauty", "review_count": "571675", "category_share_pct": "3.1707895666754906", "avg_rating": "3.9469016486639981"},
    {"pandemic_phase": "3_New Normal", "main_category": "Movies & TV", "review_count": "407304", "category_share_pct": "2.259107488809541", "avg_rating": "4.2672156423703136"},
    {"pandemic_phase": "3_New Normal", "main_category": "Industrial & Scientific", "review_count": "362618", "category_share_pct": "2.0112570448047111", "avg_rating": "4.0245271883910858"},
    {"pandemic_phase": "3_New Normal", "main_category": "All Electronics", "review_count": "318565", "category_share_pct": "1.7669175288546426", "avg_rating": "3.9103919137381662"},
    {"pandemic_phase": "3_New Normal", "main_category": "Tools & Home Improvement", "review_count": "306808", "category_share_pct": "1.7017074480650267", "avg_rating": "4.0114534171208058"},
    {"pandemic_phase": "3_New Normal", "main_category": "Video Games", "review_count": "296151", "category_share_pct": "1.6425985060751536", "avg_rating": "3.8567723897606152"},
    {"pandemic_phase": "3_New Normal", "main_category": "Computers", "review_count": "231869", "category_share_pct": "1.2860590475978124", "avg_rating": "3.8739417515924903"},
    {"pandemic_phase": "3_New Normal", "main_category": "Automotive", "review_count": "143134", "category_share_pct": "0.79389127360218614", "avg_rating": "4.0520281694076878"},
    {"pandemic_phase": "3_New Normal", "main_category": "Toys & Games", "review_count": "109484", "category_share_pct": "0.60725189122823187", "avg_rating": "3.9881261188849506"},
    {"pandemic_phase": "3_New Normal", "main_category": "Cell Phones & Accessories", "review_count": "83023", "category_share_pct": "0.46048622415550672", "avg_rating": "3.7837105380436764"},
    {"pandemic_phase": "3_New Normal", "main_category": "Office Products", "review_count": "46236", "category_share_pct": "0.25644750322264925", "avg_rating": "4.1504455402716447"},
    {"pandemic_phase": "3_New Normal", "main_category": "Pet Supplies", "review_count": "29586", "category_share_pct": "0.16409844775381308", "avg_rating": "4.0444804975326134"},
    {"pandemic_phase": "3_New Normal", "main_category": "Camera & Photo", "review_count": "20931", "category_share_pct": "0.11609357837947208", "avg_rating": "4.1074960584778557"},
    {"pandemic_phase": "3_New Normal", "main_category": "Arts, Crafts & Sewing", "review_count": "13463", "category_share_pct": "0.074672392419035533", "avg_rating": "4.0651414989229737"},
    {"pandemic_phase": "3_New Normal", "main_category": "Baby", "review_count": "12452", "category_share_pct": "0.06906489121309", "avg_rating": "4.0883392226148416"},
    {"pandemic_phase": "3_New Normal", "main_category": "Home Audio & Theater", "review_count": "7983", "category_share_pct": "0.04427762821667984", "avg_rating": "3.9352373794312911"},
    {"pandemic_phase": "3_New Normal", "main_category": "Premium Beauty", "review_count": "5290", "category_share_pct": "0.029340931136945553", "avg_rating": "3.8175803402646533"},
    {"pandemic_phase": "3_New Normal", "main_category": "Appliances", "review_count": "4619", "category_share_pct": "0.025619236469102361", "avg_rating": "4.12210435159125"},
    {"pandemic_phase": "3_New Normal", "main_category": "Musical Instruments", "review_count": "3478", "category_share_pct": "0.019290691586823561", "avg_rating": "4.2050028752156408"},
    {"pandemic_phase": "3_New Normal", "main_category": "Software", "review_count": "1511", "category_share_pct": "0.0083807461149196082", "avg_rating": "3.99536730641959"},
    {"pandemic_phase": "3_New Normal", "main_category": "Sports Collectibles", "review_count": "1008", "category_share_pct": "0.0055908617364917043", "avg_rating": "4.2390873015873005"},
    {"pandemic_phase": "3_New Normal", "main_category": "Books", "review_count": "914", "category_share_pct": "0.0050694916936045806", "avg_rating": "4.2516411378555778"},
    {"pandemic_phase": "3_New Normal", "main_category": "Handmade", "review_count": "767", "category_share_pct": "0.0042541576903662075", "avg_rating": "4.0925684485006517"},
    {"pandemic_phase": "3_New Normal", "main_category": "SUBSCRIPTION BOXES", "review_count": "563", "category_share_pct": "0.0031226737675047913", "avg_rating": "3.5133214920071048"},
    {"pandemic_phase": "3_New Normal", "main_category": "Portable Audio & Accessories", "review_count": "474", "category_share_pct": "0.0026290361737074087", "avg_rating": "3.9894514767932483"},
    {"pandemic_phase": "3_New Normal", "main_category": "Digital Music", "review_count": "442", "category_share_pct": "0.002451548499533069", "avg_rating": "4.3076923076923057"},
    {"pandemic_phase": "3_New Normal", "main_category": "Buy a Kindle", "review_count": "352", "category_share_pct": "0.001952364415917738", "avg_rating": "4.3380681818181817"},
    {"pandemic_phase": "3_New Normal", "main_category": "Collectibles & Fine Art", "review_count": "188", "category_share_pct": "0.0010427400857742463", "avg_rating": "4.0585106382978706"},
    {"pandemic_phase": "3_New Normal", "main_category": "GPS & Navigation", "review_count": "181", "category_share_pct": "0.0010039146570486096", "avg_rating": "4.05524861878453"},
    {"pandemic_phase": "3_New Normal", "main_category": "Car Electronics", "review_count": "95", "category_share_pct": "0.00052691653270507135", "avg_rating": "3.957894736842106"},
    {"pandemic_phase": "3_New Normal", "main_category": "Entertainment", "review_count": "42", "category_share_pct": "0.000232952572353821", "avg_rating": "4.57142857142857"},
    {"pandemic_phase": "3_New Normal", "main_category": "Collectible Coins", "review_count": "12", "category_share_pct": "6.6557877815377428e-05", "avg_rating": "3.7500000000000004"},
    {"pandemic_phase": "3_New Normal", "main_category": "Audible Audiobooks", "review_count": "7", "category_share_pct": "3.8825428725636835e-05", "avg_rating": "4.2857142857142856"},
    {"pandemic_phase": "3_New Normal", "main_category": "Amazon Devices", "review_count": "4", "category_share_pct": "2.2185959271792478e-05", "avg_rating": "4.75"},
    {"pandemic_phase": "3_New Normal", "main_category": "Amazon Elements", "review_count": "1", "category_share_pct": "5.5464898179481195e-06", "avg_rating": "2.0"},
    {"pandemic_phase": "3_New Normal", "main_category": "Gift Cards", "review_count": "1", "category_share_pct": "5.5464898179481195e-06", "avg_rating": "1.0"},
    {"pandemic_phase": "3_New Normal", "main_category": "", "review_count": "1", "category_share_pct": "5.5464898179481195e-06", "avg_rating": "5.0"}
]

df_cat = pd.DataFrame(cat_data)
# Clean up null/empty categories
df_cat['main_category'] = df_cat['main_category'].fillna('Uncategorized').replace('', 'Uncategorized')
df_cat['category_share_pct'] = pd.to_numeric(df_cat['category_share_pct'])
df_cat['review_count'] = pd.to_numeric(df_cat['review_count'])
df_cat['avg_rating'] = pd.to_numeric(df_cat['avg_rating'])
df_cat['Phase_Label'] = df_cat['pandemic_phase'].apply(lambda x: x.split('_', 1)[-1])

# Calculate Category Share Shifts
pivot_share = df_cat.pivot(index='main_category', columns='Phase_Label', values='category_share_pct').fillna(0)
pivot_share['Shift_COVID'] = pivot_share['Lockdown'] - pivot_share['Pre-COVID']

inc_cats = pivot_share[pivot_share['Shift_COVID'] > 0].sort_values(by='Shift_COVID', ascending=False)
dec_cats = pivot_share[pivot_share['Shift_COVID'] < 0].sort_values(by='Shift_COVID', ascending=True)

def get_base64_img(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', dpi=150)
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

images = {}

# Tone Chart
fig, ax1 = plt.subplots(figsize=(6, 3.5))
ax2 = ax1.twinx()
ax1.plot(df_macro['Phase_Label'], df_macro['avg_rating'], marker='o', color='#27ae60', label='Rating', linewidth=2)
ax2.plot(df_macro['Phase_Label'], df_macro['avg_sentiment_score'], marker='s', color='#2980b9', label='Sentiment', linewidth=2)
ax1.set_ylabel('Avg Rating (1-5)', color='#27ae60')
ax2.set_ylabel('Avg Sentiment', color='#2980b9')
ax1.set_title('Emotional Tone Trajectory')
images['tone'] = get_base64_img(fig)

# Supply Chain Chart
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.bar(df_macro['Phase_Label'], df_macro['pct_shipping_keyword'], color='#e74c3c')
ax.set_title('Supply Chain Friction (Shipping Keywords %)')
ax.set_ylabel('% of Reviews')
images['shipping'] = get_base64_img(fig)

# Helpful Votes
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(df_macro['Phase_Label'], df_macro['avg_helpful_votes'], marker='D', color='#8e44ad', linewidth=2)
ax.set_title('Community Reliance (Helpful Votes)')
ax.set_ylabel('Average Votes per Review')
images['helpful'] = get_base64_img(fig)

# Category Shift Chart
fig, ax = plt.subplots(figsize=(7, 4))
top_cats = ["Health & Personal Care", "Grocery", "Sports & Outdoors", "Prime Video", "AMAZON FASHION", "Amazon Home"]
colors = ['#e74c3c', '#27ae60', '#f39c12', '#9b59b6', '#3498db', '#34495e']
for i, cat in enumerate(top_cats):
    subset = df_cat[df_cat['main_category'] == cat]
    ax.plot(subset['Phase_Label'], subset['category_share_pct'], marker='o', label=cat, linewidth=2, color=colors[i])
ax.set_title('Category Mix Shift (Top 6 Categories)')
ax.set_ylabel('Share of Total Reviews (%)')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
images['category'] = get_base64_img(fig)

html_content = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    @page {{ size: A4; margin: 15mm 15mm; }}
    body {{ font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #2c3e50; line-height: 1.5; font-size: 9pt; }}
    h1 {{ color: #1a252f; font-size: 16pt; border-bottom: 2px solid #34495e; padding-bottom: 5px; }}
    h2 {{ color: #2980b9; font-size: 12pt; margin-top: 15px; page-break-after: avoid; }}
    table {{ width: 100%; border-collapse: collapse; margin-bottom: 10px; font-size: 8pt; }}
    th, td {{ border: 1px solid #bdc3c7; padding: 4px; text-align: center; }}
    th {{ background-color: #ecf0f1; font-weight: bold; }}
    td:first-child, th:first-child {{ text-align: left; }}
    .section {{ page-break-inside: avoid; margin-bottom: 20px; border: 1px solid #e0e0e0; padding: 10px; border-radius: 4px; }}
    .img-container {{ text-align: center; margin-bottom: 10px; }}
    .img-container img {{ max-width: 85%; height: auto; }}
    .inference {{ background-color: #f8f9fa; border-left: 4px solid #e74c3c; padding: 8px 12px; margin-top: 8px; font-style: italic; font-size: 8.5pt; }}
</style>
</head>
<body>

<h1>Amazon Review Dynamics: Multi-Phase Impact Report</h1>

<div class="section">
    <h2>Master Dataset (Macro Metrics)</h2>
    <table>
        <tr>
            <th>Phase</th><th>Reviews</th><th>Users</th><th>Products</th><th>Rating</th><th>Sentiment</th><th>Length</th><th>Shipping %</th><th>Verified %</th><th>Helpful</th>
        </tr>
        {"".join([f"<tr><td>{r['Phase_Label']}</td><td>{r['review_count']:,.0f}</td><td>{r['unique_users']:,.0f}</td><td>{r['unique_products']:,.0f}</td><td>{r['avg_rating']:.2f}</td><td>{r['avg_sentiment_score']:.2f}</td><td>{r['avg_review_length']:.1f}</td><td>{r['pct_shipping_keyword']:.2f}%</td><td>{r['pct_verified_purchase']:.2f}%</td><td>{r['avg_helpful_votes']:.2f}</td></tr>" for _, r in df_macro.iterrows()])}
    </table>
</div>

<div class="section">
    <h2>Market Activity Mix Shift by Category</h2>
    <div class="img-container"><img src="data:image/png;base64,{images['category']}" /></div>
    <table>
        <tr>
            <th>Category</th><th>Pre-COVID Share</th><th>Lockdown Share</th><th>New Normal Share</th>
        </tr>
        {"".join([f"<tr><td>{cat}</td><td>{df_cat[(df_cat['main_category']==cat) & (df_cat['Phase_Label']=='Pre-COVID')]['category_share_pct'].values[0]:.2f}%</td><td>{df_cat[(df_cat['main_category']==cat) & (df_cat['Phase_Label']=='Lockdown')]['category_share_pct'].values[0]:.2f}%</td><td>{df_cat[(df_cat['main_category']==cat) & (df_cat['Phase_Label']=='New Normal')]['category_share_pct'].values[0]:.2f}%</td></tr>" for cat in top_cats])}
    </table>
    <div class="inference">
        <strong>Inference:</strong> During the lockdown, essential goods like Health & Personal Care (up to 24.97%) and Grocery (up to 21.06%) saw a massive surge in category share, while digital entertainment like Prime Video plummeted. These shifts largely solidified rather than reverting to pre-COVID baselines, indicating a permanent shift in consumer priorities.
    </div>
</div>

<div class="section">
    <h2>Emotional Tone & Customer Effort</h2>
    <div class="img-container"><img src="data:image/png;base64,{images['tone']}" /></div>
    <div class="inference">
        <strong>Inference:</strong> There is a distinct erosion of consumer goodwill. Ratings and sentiment scores continued to steadily decline into the New Normal phase (reaching an average rating of 4.01). Post-pandemic consumers are measurably more critical and less forgiving than they were in the 2016-2019 baseline years.
    </div>
</div>

<div class="section">
    <h2>Supply Chain Friction</h2>
    <div class="img-container"><img src="data:image/png;base64,{images['shipping']}" /></div>
    <div class="inference">
        <strong>Inference:</strong> Supply chain friction was a temporary shock. Shipping-related complaints spiked to 3.06% during lockdowns but returned to pre-COVID normalcy in the New Normal phase (2.61%). Verified Purchases spiked to over 93% during lockdowns, confirming a rapid shift of the transaction pipeline online.
    </div>
</div>

<div class="section">
    <h2>Community Reliance & Validation</h2>
    <div class="img-container"><img src="data:image/png;base64,{images['helpful']}" /></div>
    <div class="inference">
        <strong>Inference:</strong> Community reliance has drastically dropped. Pre-COVID reviews generated an average of 1.21 helpful votes, which plummeted to just 0.74 in the New Normal phase. This suggests consumers are utilizing reviews primarily for rapid, individual purchase validation.
    </div>
</div>

<div style="page-break-before: always;"></div>
<h2>Complete Category Data (All Records)</h2>
<table>
    <tr><th>Phase</th><th>Category</th><th>Review Count</th><th>Share %</th><th>Avg Rating</th></tr>
    {"".join([f"<tr><td>{r['Phase_Label']}</td><td>{r['main_category']}</td><td>{r['review_count']:,.0f}</td><td>{r['category_share_pct']:.4f}%</td><td>{r['avg_rating']:.2f}</td></tr>" for _, r in df_cat.iterrows()])}
</table>

<div style="page-break-before: always;"></div>
<h2>Categories that INCREASED Share during COVID (Lockdown > Pre-COVID)</h2>
<table>
    <tr><th>Category</th><th>Pre-COVID Share %</th><th>Lockdown Share %</th><th>Net Shift %</th></tr>
    {"".join([f"<tr><td>{cat}</td><td>{row['Pre-COVID']:.4f}%</td><td>{row['Lockdown']:.4f}%</td><td style='color:green;'>+{row['Shift_COVID']:.4f}%</td></tr>" for cat, row in inc_cats.iterrows()])}
</table>

<h2>Categories that DECREASED Share during COVID (Lockdown < Pre-COVID)</h2>
<table>
    <tr><th>Category</th><th>Pre-COVID Share %</th><th>Lockdown Share %</th><th>Net Shift %</th></tr>
    {"".join([f"<tr><td>{cat}</td><td>{row['Pre-COVID']:.4f}%</td><td>{row['Lockdown']:.4f}%</td><td style='color:red;'>{row['Shift_COVID']:.4f}%</td></tr>" for cat, row in dec_cats.iterrows()])}
</table>

</body>
</html>
"""

HTML(string=html_content).write_pdf("amazon_review_impact_report_updated.pdf")
print("Report generated successfully.")