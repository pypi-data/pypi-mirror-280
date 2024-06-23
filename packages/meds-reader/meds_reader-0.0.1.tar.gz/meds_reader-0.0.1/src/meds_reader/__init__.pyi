from __future__ import annotations

from typing import Mapping, Iterator, Sequence, Collection
from typing import Any, Optional
import meds
import datetime
import pyarrow as pa



def convert_to_patient_database(path_to_meds: str, path_to_destination: str, num_threads: int = 1) -> None:
    """Convert a MEDS dataset into a meds_reader PatientDatabase.
    
    This involves reading the entire MEDS dataset and reformating / indexing it.

    Args:
        path_to_meds: A path to a MEDS dataset
        path_to_destination: A path where to write the resulting PatientDatabase
        num_threads: The number of threads use
    """
    ...

class PatientDatabase:
    """A PatientDatabase is a read-only mapping from patient_id to Patient objects.
    
    It also stores metadata such as meds.DatasetMetadat and the custom per-event properties.
    """

    def __init__(self, path_to_database: str) -> None:
        """Open a PatientDatabase. The path must be from convert_to_patient_database."""
        ...

    metadata: meds.DatasetMetadata
    "The MEDS dataset metadata"

    properties: Mapping[str, pa.DataType]
    "The per-event properties for this dataset"

    def __len__(self) -> int:
        """The number of patients in the database"""
        ...

    def __getitem__(self, patient_id: int) -> Patient:
        """Retrieve a single patient from the database"""
        ...
        
    def __iter__(self) -> Iterator[int]:
        """Get all patient ids in the Database"""
        ...

class Patient:
    """A patient consists of a patient_id and a sequence of Events"""

    patient_id: int
    "The unique identifier for this patient"
    
    events: Sequence[Event]
    "Items that have happened to a patient"

class Event:
    """An event represents a single unit of information about a patient. It contains a time and code, and potentially more properties."""

    time: datetime.datetime
    "The time the event occurred"

    code: str
    "An identifier for the type of event that occured"

    def __getattr__(self, name: str) -> Any:
        """Events can contain arbitrary additional properties. This retrieves the specified property, or returns None"""
        ...


__all__ = ['PatientDatabase', 'Patient', 'Event', 'convert_to_patient_database']