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
    for word in line.strip():
        word = word.strip()
        if word:
            output_file.write(word.strip() + "\n")
    output_file.write("\n")
    schedule = count*100//int(total_lines)
    p.update(schedule)
p.finish()

input_file.close()
output_file.close()
