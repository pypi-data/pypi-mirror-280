## meds_reader: A Pythonic interface for working with MEDS

meds_reader is a fast and easy-to-use library for reading and processing patient data stored in MEDS (Medical Event Data Standard) format using a Python-native API.

Inspired by HuggingFace Datasets, meds_reader transforms MEDS datasets into collections of Python objects, that can then be processed using normal Python functions.

### Example

```python
import meds_reader

# Convert the source MEDS dataset into the meds_reader internal format
meds_reader.convert_to_patient_database("mimic_meds", "mimic_meds_reader")

# We can now construct a database
database = meds_reader.PatientDatabase("mimic_meds_reader")

# Databases are dict-like objects that store patient data

# We can iterate through all the patient ids in the database
for patient_id in database:

    # We can retrieve patient data given a patient_id
    patient = database[patient_id]

    # Patient data can be manipulated with normal Python operations
    print(patient.patient_id)
    for event in patient.events:
        print(event.time, event.code)
```


To learn more, see our the [full documentation](https://meds-reader.readthedocs.io/en/latest/).


### Installation

meds_reader can be installed using pip.

```bash
pip install meds_reader
```

### Interactive Demo

An interactive demo can be found at https://colab.research.google.com/ 
