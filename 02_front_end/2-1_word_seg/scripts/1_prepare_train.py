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
    word_list = line.strip().split()
    for word in word_list:
        if len(word) == 1:
            output_file.write(word + "\tS\n")
        else:
            output_file.write(word[0] + "\tB\n")
            for w in word[1:len(word)-1]:
                output_file.write(w + "\tM\n")
            output_file.write(word[len(word)-1] + "\tE\n")
    output_file.write("\n")
    schedule = count*100//int(total_lines)
    p.update(schedule)
p.finish()

input_file.close()
output_file.close()
