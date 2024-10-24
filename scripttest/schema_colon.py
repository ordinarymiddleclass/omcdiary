from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class PTCategory(BaseModel):
    T1 = "T1"
    T2 = "T2"
    T3 = "T3"
    T4A = "T4a"
    T4B = "T4b"

class PNCategory(BaseModel):
    N0 = "N0"
    N1 = "N1"
    N1A = "N1a"
    N1B = "N1b"
    N1C = "N1c"
    N2 = "N2"
    N2A = "N2a"
    N2B = "N2b"
    
class PMCategory(BaseModel):
    M0 = "M0"
    M1A = "M1a"
    M1B = "M1b"
    M1C = "M1c"

class StageGroup(BaseModel):
    I = "I"
    IIA = "IIA"
    IIB = "IIB"
    IIC = "IIC"
    IIIA = "IIIA"
    IIIB = "IIIB"
    IIIC = "IIIC"
    IVA = "IVA"
    IVB = "IVB"
    IVC = "IVC"

class TNMDescriptors(BaseModel):
    POSTTREATMENT = "y"
    RECURRENT = "r"
    MULTIPLE = "m"

class StainIntensity(BaseModel):
    ABSENT = "absent"
    WEAK = "weak"
    MODERATE = "moderate"
    STRONG = "strong"

class TumorBudding(BaseModel):
    LOW = "low"
    INTERMEDIATE = "intermediate"
    HIGH = "high"

class HistologicFeatures(BaseModel):
    extracellular_mucin_production: bool
    signet_ring_cell_morphology: bool
    tumor_budding: TumorBudding
    other_histologic_features: Optional[Any]

class Margin(BaseModel):
    margin_involved: bool
    distance: Optional[int]

class Margins(BaseModel):
    proximal: Margin
    distal: Margin
    mesenteric: Margin
    circumferential_margin: Margin
    radial_margin: Optional[Margin]
    outmost_margin: Optional[Margin]
    bilateral_margin: Optional[List[Margin]]

class LymphNodeStatus(BaseModel):
    involved: int
    examined: int

class RegionalLymphNodes(BaseModel):
    pericolic_perirectal: LymphNodeStatus
    mesenteric_pedicle_site: Optional[LymphNodeStatus]
    others: Optional[List[LymphNodeStatus]]
    metastatic_tumor_size: Optional[float]
    extranodal_extension: bool

class ImmunohistochemistryResult(BaseModel):
    expression: bool
    percentage: int
    intensity: Optional[StainIntensity]

class Immunohistochemistry(BaseModel):
    MLH1: ImmunohistochemistryResult
    MSH2: ImmunohistochemistryResult
    MSH6: ImmunohistochemistryResult
    PMS2: ImmunohistochemistryResult
    others: Optional[List[ImmunohistochemistryResult]]
    interpretation: str

class AncillaryStudies(BaseModel):
    immunohistochemistry: Immunohistochemistry
    others: Optional[Any]

class CancerRegistry(BaseModel):
    primary_site: str
    surgery_type: str
    procedure: str
    laterality: str
    histology: str
    grade: int
    tumor_focality: int
    tumor_size: List[float]
    tumor_config: str
    tumor_perforation: bool
    tumor_intactness: str
    tumor_invasion: str
    list_of_adjacent_structures: Optional[Any]
    histologic_features: HistologicFeatures
    lymphovascular_invasion: bool
    perineural_invasion: bool
    margins: Margins
    treatment_effect: Optional[Any]
    tumor_deposits: int
    type_of_polyp: Optional[Any]
    regional_lymph_nodes: RegionalLymphNodes
    non_regional_lymph_nodes: Optional[List[LymphNodeStatus]]
    tnm_descriptors: Optional[TNMDescriptors]
    pt_category: PTCategory
    pn_category: PNCategory
    pm_category: Optional[PMCategory]
    stage_group: StageGroup
    ancillary_studies: AncillaryStudies

class CancerExcisionReport(BaseModel):
    cancer_excision_report: bool
    cancer_category: str
    cancer_registry: CancerRegistry


data = {
    "cancer_excision_report": True,
    "cancer_category": "colorectal",
    "cancer_registry": {
        "primary_site": "Rectosigmoid region",
        "surgery_type": "open",
        "procedure": "low anterior resection",
        "laterality": "not applicable",
        "histology": "adenocarcinoma",
        "grade": 2,
        "tumor_focality": 1,
        "tumor_size": [6.0, 6.0, 1.5],
        "tumor_config": "fungating",
        "tumor_perforation": False,
        "tumor_intactness": "not applicable",
        "tumor_invasion": "submucosa",
        "list_of_adjacent_structures": None,
        "histologic_features": {
            "extracellular_mucin_production": False,
            "signet_ring_cell_morphology": False,
            "tumor_budding": "low",
            "other_histologic_features": None
        },
        "lymphovascular_invasion": False,
        "perineural_invasion": False,
        "margins": {
            "proximal": {
                "margin_involved": False,
                "distance": 70
            },
            "distal": {
                "margin_involved": False,
                "distance": 15
            },
            "mesenteric": {
                "margin_involved": False,
                "distance": 40
            },
            "circumferential_margin": {
                "margin_involved": False,
                "distance": 10
            },
            "radial_margin": None,
            "outmost_margin": None,
            "bilateral_margin": None
        },
        "treatment_effect": None,
        "tumor_deposits": 0,
        "type_of_polyp": None,
        "regional_lymph_nodes": {
            "pericolic_perirectal": {
                "involved": 0,
                "examined": 16
            },
            "mesenteric_pedicle_site": None,
            "others": None,
            "metastatic_tumor_size": None,
            "extranodal_extension": False
        },
        "non_regional_lymph_nodes": None,
        "tnm_descriptors": None,
        "pt_category": "T1",
        "pn_category": "N0",
        "pm_category": None,
        "stage_group": "I",
        "ancillary_studies": {
            "immunohistochemistry": {
                "MLH1": {
                    "expression": True,
                    "percentage": 99
                },
                "MSH2": {
                    "expression": True,
                    "percentage": 99
                },
                "MSH6": {
                    "expression": True,
                    "percentage": 99
                },
                "PMS2": {
                    "expression": True,
                    "percentage": 70
                },
                "others": None,
                "interpretation": "low probability of MSI-H"
            }
        }
    }
}

report = CancerExcisionReport(**data)
print(report.cancer_registry.histologic_features.tumor_budding)
