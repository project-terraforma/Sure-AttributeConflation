# Objective 1: Explore, understand, and compare datasets
## Key Results
* Load and explore the datasets (Mayhem and Overture) to identify key attributes (name, phone number, website)
* Compare data quality (i.e. missing values and formatting differences)
* Analyze label distribution (i.e. “same” vs. “current”) and record structure (base_id grouping)

## Some Analysis
RAW DATA SAMPLE:
                                     names  ...                                           websites
0  {"primary":"Goin' Postal Jacksonville"}  ...         ["http://www.goinpostaljacksonville.com/"]
1        {"primary":"Valley Transmission"}  ...                      ["http://valleytransca.com/"]
2            {"primary":"Mazda Nelspruit"}  ...                   ["http://bit.ly/NelspruitMazda"]
3     {"primary":"Red Wing - Roswell, GA"}  ...     ["https://stores.redwingshoes.com/roswell-ga"]
4             {"primary":"Norauto España"}  ...  ["https://centro.norauto.es/alacant/finestrat/...
[5 rows x 3 columns]
GOLDEN DATA SIZE:
2000
FIRST 5 GOLDEN RECORDS:
{'id': '08f44f055a9a016e0390f050aa3c93c0', 'base_id': '1688849865669487', 'record_index': 0, 'labels': {'name': 'same'}}
{'id': '08f29a456e42e5830324637954145c50', 'base_id': '1125899907111860', 'record_index': 1, 'labels': {'name': 'same'}}
{'id': '08fbcd0030da5323031bcafa8c2fa0dc', 'base_id': '844424934845986', 'record_index': 2, 'labels': {'name': 'same'}}
{'id': '1407374885933937', 'base_id': '844424932146366', 'record_index': 3, 'labels': {'name': 'current'}}
{'id': '08f3956260b9e14003feca2bf0764d0c', 'base_id': '1407374887472291', 'record_index': 4, 'labels': {'name': 'current'}}
LABELS ONLY:
{'name': 'same'}
{'name': 'same'}
{'name': 'same'}
{'name': 'current'}
{'name': 'current'}
CLEAN NAMES:
Goin' Postal Jacksonville
Valley Transmission
Mazda Nelspruit
Red Wing - Roswell, GA
Norauto España
MISSING VALUES (OVERTURE):
names         0
phones      109
websites    288
>> Data Quality Insight (Overture): Names are the most complete values with 0 missing from Overture’s dataset. However, the labels with missing values are phone numbers and websites, with websites being the highest at 288 websites. This tell us that most places are missing websites.
dtype: int64
LABEL DISTRIBUTION (MAYHEM)
Counter({'same': 975, 'current': 519, 'base': 506})
>> Label Insight (Mayhem): Most records are labeled as “same,” meaning many entries do not have meaningful differences. However, a significant portion are labeled “current” or “base,” indicating cases where attribute selection is necessary.
BASE_ID GROUPING (OVERTURE):
base_id
1688849865669487            1
5e9050ceb5458f0008d83029    1
4c3e0a121ef0d13a88be9180    1
4cb0a433db32f04dca82c14d    1
52727d49498e547262e0ded9    1
>> Structure Insight (Overture): Each [base_id] is equal to 1, meaning it appears once in both datasets, which means that there are no multiple versions of the same place within the data. This shows that the data is already preprocessed. 
Name: count, dtype: int64
BASE_ID GROUPING (MAYHEM)
[('1688849865669487', 1), ('1125899907111860', 1), ('844424934845986', 1), ('844424932146366', 1), ('1407374887472291', 1)] << Structure Insight (Mayhem): Same as Overture – there are no multiple versions of the same place within the data. This shows that the data is already preprocessed. 

Final comments:
The Overture dataset contains raw and sometimes incomplete attribute data, while the Mayhem dataset gives structured labels for evaluation. This shows that Overture is useful for building models, while Mayhem is useful for validating results and comparing them.
The two datasets serve different purposes and have different data quality characteristics. The Overture dataset contains raw attribute data such as names, phone numbers, and websites, and includes missing values and formatting inconsistencies, particularly in the website field. In contrast, the Mayhem dataset is a labeled dataset with structured annotations such as “same,” “current,” and “base,” and does not contain missing label values. This indicates that Overture is used as the input data for analysis, while Mayhem acts as a ground truth reference for evaluation. Together, they complement each other by supporting both model development and performance assessment.
