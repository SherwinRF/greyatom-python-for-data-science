# --------------
# Importing header files
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record = np.asarray(new_record)

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate( (new_record, data) )
print(census.shape)

# Operations on Country's Age
age = census[:,0]
max_age = age.max()
min_age = age.min()
age_mean = np.mean(age)
age_std = np.std(age)
print( max_age, min_age, age_mean, age_std )

# Finding Minority Race
race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = 0
if len_0 == min(len_0,len_1,len_2,len_3,len_4): minority_race = 0
elif len_1 == min(len_0,len_1,len_2,len_3,len_4): minority_race = 1
elif len_2 == min(len_0,len_1,len_2,len_3,len_4): minority_race = 2
elif len_3 == min(len_0,len_1,len_2,len_3,len_4): minority_race = 3
elif len_4 == min(len_0,len_1,len_2,len_3,len_4): minority_race = 4
print(minority_race)

# Finding work hours of senoir citizens
senior_citizens = census[age > 60]
working_hours_sum = np.sum( senior_citizens[:,6] )
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(working_hours_sum, avg_working_hours)

# Finding avg. high & low pay & income
high = census[ census[:,1] > 10 ]
low = census[ census[:,1] <= 10 ]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(avg_pay_high, avg_pay_low)
