import meds_reader
import collections
import time
import pickle

meds_reader.convert_to_patient_database("/home/ethanid/health_research/mimic-iv-demo-meds", '/home/ethanid/health_research/mimic-iv-demo-meds-temp2', 4)

database = meds_reader.PatientDatabase('/home/ethanid/health_research/mimic-iv-demo-meds-temp2')


print(database.properties)

counter = collections.defaultdict(int)

print("Running", len(database))

patient_ids = list(database)

start = time.time()

for patient_id in patient_ids:
    patient = database[patient_id]
    patient_codes = set()
    for event in patient.events:
        patient_codes.add(event.code)
    
    for code in patient_codes:
        counter[code] += 1

end = time.time()

final = pickle.dumps(database)

print(final)

other = pickle.loads(final)

print(other, len(other))


print(sum(counter.values()), end-start)
print(max(counter.values()))
items = list(counter.items())
items.sort(key=lambda a:-a[1])
print(items[:10])
print(counter['MIMIC_IV_Gender/M'])
print(counter['MIMIC_IV_Gender/F'])
