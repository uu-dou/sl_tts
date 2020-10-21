#!/bin/bash

echo "Prepare test data [people_daliy_$1]"
python ../scripts/2_prepare_test.py people_daliy_$1/test.raw people_daliy_$1/test.data
python ../scripts/1_prepare_train.py people_daliy_$1/test.raw people_daliy_$1/reference.data

../tools/CRF++-0.58/build/bin/crf_test -m people_daliy_$1/model.demo people_daliy_$1/test.data > people_daliy_$1/test.out

python measure_performance.py people_daliy_$1/reference.data people_daliy_$1/test.out
