#!/bin/bash

echo "Prepare train data [people_daliy_$1]"
python ../scripts/1_prepare_train.py people_daliy_$1/train.raw people_daliy_$1/train.data

echo "Start training the model"
../tools/CRF++-0.58/build/bin/crf_learn -f 3 -c 4.0 ../config/template people_daliy_$1/train.data people_daliy_$1/model.demo
