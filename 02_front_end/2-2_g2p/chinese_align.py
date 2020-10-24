import codecs
import sys
import os
import progressbar

input_file  = codecs.open(sys.argv[1], 'r', 'utf-8')
output_file = codecs.open(sys.argv[2], 'w', 'utf-8')

total_lines=os.popen('wc -l %s' % (sys.argv[1])).read().split()[0]
p = progressbar.ProgressBar(maxval=100).start()

count = 0
for line in input_file.readlines():
    count += 1
    word_list = line.split('\t' , 1 )
    cn_sentense_list  = word_list[0]
    en_sentense_list = word_list[1]

    cn_word_list = [i for i in cn_sentense_list]
    en_word_list = en_sentense_list.strip().split()
    for i in range(0, len(cn_word_list)):
        cn = cn_word_list[i]
        en = en_word_list[i]
        output_file.write(cn +'}'+ en + ' ')
    output_file.write("\n")
    schedule = count*100//int(total_lines)
    p.update(schedule)
p.finish()

input_file.close()
output_file.close()
