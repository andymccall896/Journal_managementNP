
print(glob.glob("/home/adam/*.txt"))
os.chdir("C:/Users/andym/Desktop/Datafancy/Journal_managementNP/01-Raw_data/all_data")
# get data file names
path =r'C:\Users\andym\Desktop\Datafancy\Knowledge Discovery -DL\01-Raw_data\all_data'
all_files = glob.glob(path + "/*.csv")

### set an empty list?
li = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df['file_name'] = filename
    li.append(df)
    
frame = pd.concat(li, axis=0, ignore_index=True)
dframe = pd.DataFrame(data = frame)
dframe['Publication Year'] = dframe['Publication Year'].astype('int') 

#### Covert the publication year to integer 
dframe['Publication Year'] = dframe['Publication Year'].astype('int') 

#### Filter out the null values in the Abstract
#### Meaning this is a dataframe of only Scientific Papers
dframetrim = dframe[dframe.Abstract.notnull()]
test = re.sub('[^A-Za-z0-9]+', ' ', dframetrim['Abstract'].values[0].lower())
text = test.split(' ')
#text
filtered_words = [word for word in text if word not in stopwords.words('english')] 

dframetrim['Abstract_trim_2'] = dframetrim['Abstract']
for i in range(len(dframetrim['Abstract'])):
    dframetrim['Abstract_trim_2'].values[i]  = re.sub('[^A-Za-z0-9]+', ' ', dframetrim['Abstract_trim_2'].values[i].lower()) ## Lower case and special characters removed
    dframetrim['Abstract_trim_2'].values[i]  = dframetrim['Abstract_trim_2'].values[i].split(' ') ## tokenise
##### I might need to look up lambda
dframetrim['Abstract_trim_2'] = dframetrim['Abstract_trim_2'].apply(lambda x: [item for item in x if item not in stopwords.words('english')]) ## Stopwords
dframetrim['Abstract_trim_2'] =  dframetrim['Abstract_trim_2'].apply(lambda x: [porter.stem(item) for item in x ]) ## Stemming 
#dframetrim

word_remove_list = ['knowledg','classif','inform','use','www','good','','organ'
                    ,'paper','subject','term','studi','develop','term','librari'
                    ,'differ','index','approach','work','base','scienc','field'
                    ,'user','structure','ko','www','present','ko','also','p',
                    'two','one','provid','author','need','tag','within','way','well','includ',
                   'part','three','may','2','e','ddc','1','3','4','5','6','7','8','9','10','li',
                    'would','non','de','four','ir','thu','frbr','737','g',
                    'etc','av','br','co','th','o','sg','nr','per','1087',
                   'six','j','via','miss','r','et','dan','bia','niac','sch','17525900'
                   'u','lcc','c','ii','la','n','dc','aat' ,'24','TRUE','keep','220','le','po','stw',
                   'kdc','oto','gsc','gsp','k','pt','dr','go','100','cc','il','nt','280','b','l','v',
                   '20','kr','sp','ave','se','12','0','23','33','157','iv','rd','am','mid','34','be','iii','fid'
                    ,'lc','met','20th' ,'ste','axi','dsi','axi','200','230','223','hlt','sur','du','mesh'
                    ,'lcsh','oclc','eu','atn','2nd','bc2','di','76','500','get','http','sdss','crg'
                    ,'esp','sab','lay','11','37','cs','urg','17525000','ot','fo','hn','em','ncft','48',
                    '40','168','dec','pc','fix','ccq','lrt','ic','fix','owe','120th','87','510','94','49',
                    '6n','mit','rev','int','32','136','144','cr','119','148','wall','120','ckm','cd','rom',
                    'ata','nest','sdoc','soli','istei','tct','shl','ana','asp','dk5','240','292','299','f','ég','222'
                    ,'229','59','pin','sen','twelv','bbk','14','28','180','192','cle','150','ec','np','ifla','ey','dea',
                    'cpcl','nl','601','178','215','iskoi','htm','i','ref','31','92','97','çmf','ibn','vo','inv','un','kop','cen','21st'
                    ,'659','ph','229','26','va','oc','ufpr','80060000','ena','od','fu','3d','dog','ear','vi','saa','vi','62',
                    'ed','43hing','kno','pubm','39','268','275','els','fac','nd','ek','oth','er','cep','ia','iti','38','114',
                   '122','35','lam','liu','ru','16','403','41','311','318','ga','eas','gri','tgn','cut','off','add','lrm','cm','ric','collat',
                    'stop','unlik','die','sdi','90','379','1a','1b','rda','riv','hj','pac','hoc','rid','rio','ssn','real',
                   'ccp','iht','edm','today','lie','point','bcc']

dframetrim['Abstract_trim_2'] = dframetrim['Abstract_trim_2'].apply(lambda x: [item for item in x if item not in word_remove_list]) 

####### using this CSV file to check which words to remove from the Abstract_trim_2 col
pd.DataFrame(dframetrim['Lens ID'],)

test = dframetrim['Abstract_trim_2'].to_list()

flat_list = []
wordfreq = []
for sublist in test:
    for item in sublist:
        flat_list.append(item)


#### Please see Def)pivot_func.py script for more details
testsmall = word_count_df(testing_loop =  dframetrim.iloc[0:9])

#test = word_count_df(testing_loop =  dframetrim)
##total_counts = Counter(flat_list)
##unique_counts = total_counts.items()
##dsa = total_counts.most_common()
##dsalist = pd.DataFrame(list(dsa))
##dsalist = dsalist.rename(columns = {0: "Word", 1: "Count"})
##dsalist.to_csv(r'C:\Users\andym\Desktop\Datafancy\Journal_managementNP\03-test_datasets\wordcount.csv')




