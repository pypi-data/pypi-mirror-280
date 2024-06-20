from typing import Any, Dict, List


class ValidationError(Exception):
    def __init__(self, error_messages: List[str]) -> None:
        super().__init__(
            "\n".join(
                [
                    f"Validation failed ({len(error_messages)} issues)",
                    *[f"- {message}" for message in error_messages],
                ],
            ),
        )
        self.error_messages = error_messages


class SeqMetadataKeys:
    MELDETATBESTAND = "MELDETATBESTAND"
    SPECIES = "SPECIES"
    LAB_SEQUENCE_ID = "LAB_SEQUENCE_ID"
    DEMIS_NOTIFICATION_ID = "DEMIS_NOTIFICATION_ID"
    STATUS = "STATUS"
    VERSION = "VERSION"
    IGS_ID = "IGS_ID"
    DATE_OF_RECEIVING = "DATE_OF_RECEIVING"
    DATE_OF_SAMPLING = "DATE_OF_SAMPLING"
    DATE_OF_SEQUENCING = "DATE_OF_SEQUENCING"
    DATE_OF_SUBMISSION = "DATE_OF_SUBMISSION"
    DATE_OF_DELETION = "DATE_OF_DELETION"
    SEQUENCING_INSTRUMENT = "SEQUENCING_INSTRUMENT"
    SEQUENCING_PLATFORM = "SEQUENCING_PLATFORM"
    ADAPTER = "ADAPTER"
    SEQUENCING_STRATEGY = "SEQUENCING_STRATEGY"
    ISOLATION_SOURCE = "ISOLATION_SOURCE"
    HOST = "HOST"
    HOST_SEX = "HOST_SEX"
    HOST_BIRTH_MONTH = "HOST_BIRTH_MONTH"
    HOST_BIRTH_YEAR = "HOST_BIRTH_YEAR"
    SEQUENCING_REASON = "SEQUENCING_REASON"
    GEOGRAPHIC_LOCATION = "GEOGRAPHIC_LOCATION"
    ISOLATE = "ISOLATE"
    AUTHOR = "AUTHOR"
    NAME_AMP_PROTOCOL = "NAME_AMP_PROTOCOL"
    PRIMER_SCHEME = "PRIMER_SCHEME"
    METADATA_QC = "METADATA_QC"
    METADATA_QC_REASON = "METADATA_QC_REASON"
    PRIME_DIAGNOSTIC_LAB_DEMIS_LAB_ID = "PRIME_DIAGNOSTIC_LAB.DEMIS_LAB_ID"
    PRIME_DIAGNOSTIC_LAB_NAME = "PRIME_DIAGNOSTIC_LAB.NAME"
    PRIME_DIAGNOSTIC_LAB_ADDRESS = "PRIME_DIAGNOSTIC_LAB.ADDRESS"
    PRIME_DIAGNOSTIC_LAB_POSTAL_CODE = "PRIME_DIAGNOSTIC_LAB.POSTAL_CODE"
    PRIME_DIAGNOSTIC_LAB_FEDERAL_STATE = "PRIME_DIAGNOSTIC_LAB.FEDERAL_STATE"
    SEQUENCING_LAB_DEMIS_LAB_ID = "SEQUENCING_LAB.DEMIS_LAB_ID"
    SEQUENCING_LAB_NAME = "SEQUENCING_LAB.NAME"
    SEQUENCING_LAB_ADDRESS = "SEQUENCING_LAB.ADDRESS"
    SEQUENCING_LAB_POSTAL_CODE = "SEQUENCING_LAB.POSTAL_CODE"
    SEQUENCING_LAB_FEDERAL_STATE = "SEQUENCING_LAB.FEDERAL_STATE"
    UPLOADS = "Uploads"
    REPOSITORY_NAME = "REPOSITORY_NAME"
    REPOSITORY_LINK = "REPOSITORY_LINK"
    REPOSITORY_ID = "REPOSITORY_ID"
    UPLOAD_DATE = "UPLOAD_DATE"
    UPLOAD_STATUS = "UPLOAD_STATUS"
    UPLOAD_SUBMITTER = "UPLOAD_SUBMITTER"
    FILES = "Files"
    FILE_NAME = "FILE_NAME"
    FILE_SHA256SUM = "FILE_SHA256SUM"


seq_metadata_schema = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        SeqMetadataKeys.MELDETATBESTAND: {
            "enum": [
                "EHCP",
                "LISP",
                "SALP",
                "STYP",
                "INVP",
                "NEIP",
                "MSVP",
                "MYTP",
                "CVDP",
                "HIVP",
                "NEGP",
                "EBCP",
                "ACBP",
                "CDFP",
                "MRAP",
                "SALP",
                "HEVP",
                "HAVP",
                "LEGP",
                "SPNP",
                "WNVP",
            ],
        },
        SeqMetadataKeys.SPECIES: {
            "type": "string",
            "minLength": 1,
        },
        SeqMetadataKeys.LAB_SEQUENCE_ID: {
            "type": "string",
            "pattern": "^[A-Za-z0-9-_]+$",
        },
        SeqMetadataKeys.DEMIS_NOTIFICATION_ID: {
            "type": "string",
            "minLength": 1,
        },
        SeqMetadataKeys.STATUS: {"enum": ["preliminary", "amended", "final", ""]},
        SeqMetadataKeys.VERSION: {"$ref": "#/$defs/int"},
        SeqMetadataKeys.IGS_ID: {
            "type": "string",
            "pattern": (
                "^(IMS|IGS)-[0-9]{5}-[A-Z]{3}P-"
                "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
                "|"
                "^(IMS|IGS)-[0-9]{5}-[A-Z]{3}P-[0-9]{2,6}$"  # for migration of old sequences
            ),
        },
        SeqMetadataKeys.DATE_OF_RECEIVING: {"$ref": "#/$defs/date"},
        SeqMetadataKeys.DATE_OF_SAMPLING: {"$ref": "#/$defs/date"},
        SeqMetadataKeys.DATE_OF_SEQUENCING: {"$ref": "#/$defs/date"},
        SeqMetadataKeys.DATE_OF_SUBMISSION: {"$ref": "#/$defs/date"},
        SeqMetadataKeys.DATE_OF_DELETION: {"$ref": "#/$defs/date"},
        SeqMetadataKeys.SEQUENCING_INSTRUMENT: {
            "enum": [
                "454_GS",
                "454_GS_20",
                "454_GS_FLX",
                "454_GS_FLX+",
                "454_GS_FLX_Titanium",
                "454_GS_Junior",
                "HiSeq_X_Five",
                "HiSeq_X_Ten",
                "Illumina_Genome_Analyzer",
                "Illumina_Genome_Analyzer_II",
                "Illumina_Genome_Analyzer_IIx",
                "Illumina_HiScanSQ",
                "Illumina_HiSeq_1000",
                "Illumina_HiSeq_1500",
                "Illumina_HiSeq_2000",
                "Illumina_HiSeq_2500",
                "Illumina_HiSeq_3000",
                "Illumina_HiSeq_4000",
                "Illumina_iSeq_100",
                "Illumina_MiSeq",
                "Illumina_MiniSeq",
                "Illumina_NovaSeq_6000",
                "NextSeq_500",
                "NextSeq_550",
                "PacBio_RS",
                "PacBio_RS_II",
                "Sequel",
                "Ion_Torrent_PGM",
                "Ion_Torrent_Proton",
                "Ion_Torrent_S5",
                "Ion_Torrent_S5_XL",
                "AB_3730xL_Genetic_Analyzer",
                "AB_3730_Genetic_Analyzer",
                "AB_3500xL_Genetic_Analyzer",
                "AB_3500_Genetic_Analyzer",
                "AB_3130xL_Genetic_Analyzer",
                "AB_3130_Genetic_Analyzer",
                "AB_310_Genetic_Analyzer",
                "MinION",
                "GridION",
                "PromethION",
                "BGISEQ-500",
                "DNBSEQ-T7",
                "DNBSEQ-G400",
                "DNBSEQ-G50",
                "DNBSEQ-G400_FAST",
                "Illumina_NextSeq_1000",
                "Illumina_NextSeq_2000",
                "Illumina_NovaSeq_X",
                "Illumina_NovaSeq_X_PLUS",
                "Sequel_II",
                "Sequel_IIe",
                "Flongle",
                "DNBSEQ-T10",
                "DNBSEQ-T20",
                "DNBSEQ-G99",
                "Ion_Torrent_Genexus",
                "Onso",
                "Revio",
                "UG_100",
                "G4",
                "PX",
                "unspecified",
            ],
        },
        SeqMetadataKeys.SEQUENCING_PLATFORM: {
            "enum": [
                "LS454",
                "ILLUMINA",
                "PACBIO_SMRT",
                "ION_TORRENT",
                "CAPILLARY",
                "OXFORD_NANOPORE",
                "BGISEQ",
                "DNBSEQ",
                "OTHER",
            ],
        },
        SeqMetadataKeys.ADAPTER: {
            "type": "string",
            "pattern": "^[\\+a-zA-Z0-9_ ,-]+$",
        },
        SeqMetadataKeys.SEQUENCING_STRATEGY: {
            "enum": [
                "WGS",
                "WGA",
                "WXS",
                "RNA-Seq",
                "ssRNA-seq",
                "miRNA-Seq",
                "ncRNA-Seq",
                "FL-cDNA",
                "EST",
                "Hi-C",
                "ATAC-seq",
                "WCS",
                "RAD-Seq",
                "CLONE",
                "POOLCLONE",
                "AMPLICON",
                "CLONEEND",
                "FINISHING",
                "ChIP-Seq",
                "MNase-Seq",
                "DNase-Hypersensitivity",
                "Bisulfite-Seq",
                "CTS",
                "MRE-Seq",
                "MeDIP-Seq",
                "MBD-Seq",
                "Tn-Seq",
                "VALIDATION",
                "FAIRE-seq",
                "SELEX",
                "RIP-Seq",
                "ChIA-PET",
                "Synthetic-Long-Read",
                "Targeted-Capture",
                "Tethered Chromatin Conformation Capture",
                "OTHER",
            ],
        },
        SeqMetadataKeys.ISOLATION_SOURCE: {
            "type": "string",
            "minLength": 1,
        },
        SeqMetadataKeys.HOST: {"enum": ["Homo sapiens"]},
        SeqMetadataKeys.HOST_SEX: {"enum": ["male", "female", "diverse"]},
        SeqMetadataKeys.HOST_BIRTH_MONTH: {
            "type": "string",
            "pattern": "^(0?[1-9]|1[012])$",
        },
        SeqMetadataKeys.HOST_BIRTH_YEAR: {
            "type": "string",
            "pattern": "^\\d{4}$",
        },
        SeqMetadataKeys.SEQUENCING_REASON: {"enum": ["random", "requested", "other", "clinical"]},
        SeqMetadataKeys.GEOGRAPHIC_LOCATION: {
            "type": "string",
            "pattern": "^[0-9]{3}$",
        },
        SeqMetadataKeys.ISOLATE: {
            "type": "string",
        },
        SeqMetadataKeys.AUTHOR: {
            "type": "string",
            "minLength": 1,
        },
        SeqMetadataKeys.NAME_AMP_PROTOCOL: {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_ ,-]+$",
        },
        SeqMetadataKeys.PRIME_DIAGNOSTIC_LAB_DEMIS_LAB_ID: {
            "type": "string",
            "pattern": "^DEMIS-[0-9]{5}$",
        },
        SeqMetadataKeys.PRIME_DIAGNOSTIC_LAB_NAME: {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_ ,-äöüÄÖÜß]+$",
        },
        SeqMetadataKeys.PRIME_DIAGNOSTIC_LAB_ADDRESS: {
            "type": "string",
        },
        SeqMetadataKeys.PRIME_DIAGNOSTIC_LAB_POSTAL_CODE: {
            "type": "string",
            "pattern": "^[0-9]{5}$",
        },
        SeqMetadataKeys.PRIME_DIAGNOSTIC_LAB_FEDERAL_STATE: {"$ref": "#/$defs/federalStates"},
        SeqMetadataKeys.PRIMER_SCHEME: {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_ ,-\\.]+$",
        },
        SeqMetadataKeys.METADATA_QC: {
            "$ref": "#/$defs/bool",
        },
        SeqMetadataKeys.METADATA_QC_REASON: {
            "type": "string",
            "pattern": "^([a-zA-Z0-9_:-]|; (?!$))+$",
        },
        SeqMetadataKeys.SEQUENCING_LAB_DEMIS_LAB_ID: {
            "type": "string",
            "pattern": "^DEMIS-[0-9]{5}$",
        },
        SeqMetadataKeys.SEQUENCING_LAB_NAME: {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_ ,-äöüÄÖÜß]+$",
        },
        SeqMetadataKeys.SEQUENCING_LAB_ADDRESS: {
            "type": "string",
            "minLength": 1,
        },
        SeqMetadataKeys.SEQUENCING_LAB_POSTAL_CODE: {
            "type": "string",
            "pattern": "^[0-9]{5}$",
        },
        SeqMetadataKeys.SEQUENCING_LAB_FEDERAL_STATE: {"$ref": "#/$defs/federalStates"},
        SeqMetadataKeys.UPLOADS: {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    SeqMetadataKeys.REPOSITORY_NAME: {"enum": ["GISAID", "ENA", "SRA", "PubMLST", "GenBank", "Other"]},
                    SeqMetadataKeys.REPOSITORY_LINK: {"type": "string"},
                    SeqMetadataKeys.REPOSITORY_ID: {"type": "string"},
                    SeqMetadataKeys.UPLOAD_DATE: {"$ref": "#/$defs/date"},
                    SeqMetadataKeys.UPLOAD_STATUS: {"enum": ["Accepted", "Planned", "Denied", "Other"]},
                    SeqMetadataKeys.UPLOAD_SUBMITTER: {"type": "string"},
                },
                "additionalProperties": False,
                "required": [
                    SeqMetadataKeys.REPOSITORY_NAME,
                    SeqMetadataKeys.REPOSITORY_ID,
                    SeqMetadataKeys.UPLOAD_STATUS,
                ],
            },
        },
        SeqMetadataKeys.FILES: {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    SeqMetadataKeys.FILE_NAME: {
                        "type": "string",
                        "pattern": "^[a-zA-Z0-9_-]+\\.(fasta|fa|fastq|fq)(\\.gz)?$",
                    },
                    SeqMetadataKeys.FILE_SHA256SUM: {
                        "type": "string",
                        "pattern": "^[A-Fa-f0-9]{64}$",
                    },
                },
                "required": ["FILE_NAME", "FILE_SHA256SUM"],
                "additionalProperties": False,
            },
            "minItems": 1,
            "uniqueItems": True,
        },
    },
    "$defs": {
        "bool": {
            "type": "string",
            "pattern": "^(true)|(false)$",
        },
        "int": {
            "type": "string",
            "pattern": "^-?[0-9]+$",
        },
        "date": {
            "type": "string",
            "format": "date",
        },
        "federalStates": {
            "enum": [
                "Baden-Württemberg",
                "Bayern",
                "Berlin",
                "Brandenburg",
                "Bremen",
                "Hamburg",
                "Hessen",
                "Mecklenburg-Vorpommern",
                "Niedersachsen",
                "Nordrhein-Westfalen",
                "Rheinland-Pfalz",
                "Saarland",
                "Sachsen",
                "Sachsen-Anhalt",
                "Schleswig-Holstein",
                "Thüringen",
            ],
        },
    },
    "required": [
        SeqMetadataKeys.MELDETATBESTAND,
        SeqMetadataKeys.LAB_SEQUENCE_ID,
        SeqMetadataKeys.DATE_OF_SUBMISSION,
        SeqMetadataKeys.SEQUENCING_INSTRUMENT,
        SeqMetadataKeys.SEQUENCING_PLATFORM,
        SeqMetadataKeys.HOST,
        SeqMetadataKeys.SEQUENCING_REASON,
        SeqMetadataKeys.SEQUENCING_LAB_DEMIS_LAB_ID,
    ],
}


def loose_schema(schema: Dict[str, Any]) -> Dict[str, Any]:
    new_schema = schema.copy()
    # Allows extra fields to the schema
    new_schema["additionalProperties"] = True
    # Remove requirement for HOST
    new_schema["required"].remove(SeqMetadataKeys.HOST)
    # Accept code in addition to display for deferal states https://simplifier.net/packages/de.basisprofil.r4/1.4.0/files/656722
    new_schema["$defs"]["federalStates"]["enum"].extend(
        [
            "DE-BW",
            "DE-BY",
            "DE-BE",
            "DE-BB",
            "DE-HB",
            "DE-HH",
            "DE-HE",
            "DE-MV",
            "DE-NI",
            "DE-NW",
            "DE-RP",
            "DE-SL",
            "DE-SN",
            "DE-ST",
            "DE-SH",
            "DE-TH",
        ],
    )
    return new_schema
