#!/bin/sh

cd native
bazel build _meds_reader.so
cd ..

rm -f src/meds_reader/*.so
cp native/bazel-bin/_meds_reader.so src/meds_reader/_meds_reader.so
