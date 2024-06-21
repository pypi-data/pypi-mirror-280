import datetime

import imageio
import pydicom
from pydicom import uid
from pydicom.dataset import Dataset
from pydicom.encaps import encapsulate


def generate_uid(entropy_srcs=None):
    return pydicom.uid.generate_uid(prefix='1.2.826.0.1.3680043.10.918.', entropy_srcs=entropy_srcs)


def create_file_meta(transfer, sop):
    file_meta = pydicom.dataset.FileMetaDataset()
    file_meta.TransferSyntaxUID = transfer
    file_meta.MediaStorageSOPClassUID = sop
    file_meta.MediaStorageSOPInstanceUID = generate_uid()
    file_meta.ImplementationClassUID = '1.2.276.0.7230010.3.0.3.5.3'
    file_meta.ImplementationVersionName = '1.4'
    return file_meta


def generate_pdf_sc(img_data, study, page_no):
    sid = str(study.get('id'))
    ds = Dataset()
    ds.file_meta = create_file_meta(uid.JPEGBaseline8Bit, uid.SecondaryCaptureImageStorage)
    ds.SOPClassUID = uid.SecondaryCaptureImageStorage
    ds.InstanceNumber = 9900 + page_no + 1
    ds.SeriesNumber = 9900
    ds.Modality = "OT"
    ds.is_implicit_VR = False
    ds.is_little_endian = True
    ds.DerivationDescription = 'SmallPreview'
    ds.ImageType = 'DERIVED', 'SECONDARY', '', ''
    ds.PixelRepresentation = 0
    ds.PlanarConfiguration = 0
    ds.BitsStored = 8
    ds.BitsAllocated = 8
    ds.HighBit = 7
    ds.PhotometricInterpretation = 'YBR_FULL_422'
    ds.Rows, ds.Columns, ds.SamplesPerPixel = img_data.shape

    study_tags = study.get('tags', {})
    notes = study.get('notes')
    ds.SeriesDate = ds.SeriesTime = study.get('processedDate')
    ds.InstanceCreationDate = ds.InstanceCreationTime = datetime.datetime.utcnow()
    ds.InstanceCreatorUID = generate_uid()
    ds.SOPInstanceUID = generate_uid()
    ds.ContentDate = ds.StudyDate = ds.ContentTime = ds.StudyTime = study.get('ed')
    ds.StudyID = study_tags.get('StudyID', sid)[:16]
    ds.AccessionNumber = study_tags.get('AccessionNumber', '')
    ds.ReferringPhysician = study_tags.get('ReferringPhysician', '')
    ds.ReferringPhysicianName = study_tags.get('ReferringPhysicianName', '')
    ds.StudyInstanceUID = study_tags.get('StudyInstanceUID', generate_uid(['study', str(sid)]))
    ds.SeriesInstanceUID = study_tags.get('SeriesInstanceUID', generate_uid(['series', str(sid)]))
    ds.Manufacturer = ds.ManufacturerModelName = 'Us2.ai'
    ds.PatientName = study_tags.get('PatientName',
                                    f'{study.get("lastName") or ""}^{study.get("firstName") or ""}')
    ds.PatientID = study.get('patientID') or ''
    ds.PatientBirthDate = study.get('dob') or ''
    ds.PatientSex = study.get('gender') or ''
    ds.StudyDescription = notes and notes[:64]
    ds.SeriesDescription = notes and notes[:64]
    ds.CompletionFlag = 'COMPLETE' if study.get('reportCompleted') else 'PARTIAL'
    ds.VerificationFlag = 'VERIFIED' if study.get('approved') else 'UNVERIFIED'
    ds.SoftwareVersions = study.get('code_version')

    ds.ReferencedPerformedProcedureStepSequence = []
    ds.PerformedProcedureCodeSequence = []

    ds.file_meta.TransferSyntaxUID = uid.JPEGBaseline8Bit
    ds.PixelData = encapsulate([imageio.imwrite('<bytes>', img_data, format='jpg')])
    ds['PixelData'].is_undefined_length = True

    return ds
