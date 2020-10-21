
import codecs
import sys
import pandas
import os
import progressbar

reference_file = codecs.open(sys.argv[1], 'r', 'utf-8')
test_file  = codecs.open(sys.argv[2], 'r', 'utf-8')

print('Read reference data:')
total_lines=os.popen('wc -l %s' % (sys.argv[1])).read().split()[0]
p = progressbar.ProgressBar(maxval=100).start()
line=[]
count=0
for i in reference_file.readlines():
    count+=1
    i=i[0:-1]
    if len(i)!=0 and len(i)!=1:
        line.append(i.split('\t'))
        schedule = count*100//int(total_lines)
    p.update(schedule)
p.finish()
reference_df = pandas.DataFrame(line,columns=['character','reference'])

print('Read test data:')
total_lines=os.popen('wc -l %s' % (sys.argv[1])).read().split()[0]
p = progressbar.ProgressBar(maxval=100).start()
line=[]
count = 0
for i in test_file.readlines():
    count+=1
    i=i[0:-1]
    if len(i)!=0 and len(i)!=1:
        line.append(i.split('\t'))
        schedule = count*100//int(total_lines)
    p.update(schedule)
p.finish()
test_df = pandas.DataFrame(line,columns=['character','test'])

concat_df = pandas.concat([reference_df, test_df.test], axis=1)
correct = concat_df[concat_df.reference==concat_df.test]

for i in ('B','S','M','E'):
    R=sum(correct.test==i)/sum(concat_df.reference==i)
    P=sum(correct.test==i)/sum(concat_df.test==i)
    F=R*P*2/(R+P)
    print(i,':\n','R=',R,' P=',P,' F=',F)


