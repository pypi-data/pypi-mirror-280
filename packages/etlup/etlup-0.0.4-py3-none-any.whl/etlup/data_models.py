"""
Contains the code for ensuring data follows a predifined format and uses Pydantic

--------------------CONSTRUCTION DATA---------------------
- ConstructionBase
    - all assembly and test types inherit from this base class, contains the needed and shared fields and validation for every assembly/test (user, measurement date, etc...)

- Subclasses of ConstructionBase (assembly and test types!)
    - type field overwritten to ensure it is the correct assembly or test type
    - data field so the data can be of a defined format as well
    * data_cache method takes the data field and trims any fat to put in the database for fast lookup (code to visualize the data will use this)

----------------OTHER DATA NOT IMPLMEMENTED----------------
"""

from typing import Union, List
from typing_extensions import Literal
from pydantic import BaseModel, field_validator, model_validator, Field, AwareDatetime, AliasChoices, RootModel, ConfigDict
import numpy as np
import json
from _ctypes import PyObj_FromPtr
import re
import json
from datetime import datetime
import pytz
from typing import get_args

#-----------------------------------------------------------#
def get_constr_model(constr_type: str):
    """
    Returns a single construction model class based on type
    """
    #loop through all subclasses of ConstructionBase
    for ConstrSubclass in ConstructionBase.get_subclasses():
        #get all the types the construction class is defined for
        model_constr_types = get_args(ConstrSubclass.model_fields['type'].annotation)   
        #check if the supplied type is part of it 
        if constr_type in model_constr_types:
            return ConstrSubclass



def validate_datetime(meas_date: datetime) -> datetime:
    #if measurement date has tz information, convert from that TZ to UTC time!
    if not isinstance(meas_date, datetime):
        raise ValueError(f"Inputted date is not a datetime object it is {type(meas_date)}")
    #is a datetime object...
    if meas_date.tzinfo is None:
        #need to do this otherwise it has a default for no timezone given!
        raise ValueError("Measurement data has no time zone information, see https://en.wikipedia.org/wiki/ISO_8601")

    #converts time to UTC time
    return meas_date.astimezone(pytz.utc)

class NoIndent(object):
    """ Value wrapper. """
    def __init__(self, value, max_length=None):
        self.value = value
        self.max_length = max_length


class DocumentationEncoder(json.JSONEncoder):
    FORMAT_SPEC = '@@{}@@'
    regex = re.compile(FORMAT_SPEC.format(r'(\d+)'))

    def __init__(self, **kwargs):
        # Save copy of any keyword argument values needed for use here.
        self.__sort_keys = kwargs.get('sort_keys', None)
        super(DocumentationEncoder, self).__init__(**kwargs)

    def default(self, obj):
        return (self.FORMAT_SPEC.format(id(obj)) if isinstance(obj, NoIndent)
                else super(DocumentationEncoder, self).default(obj))

    def encode(self, obj):
        format_spec = self.FORMAT_SPEC  # Local var to expedite access.
        json_repr = super(DocumentationEncoder, self).encode(obj)  # Default JSON.

        # Replace any marked-up object ids in the JSON repr with the
        # value returned from the json.dumps() of the corresponding
        # wrapped Python object.
        for match in self.regex.finditer(json_repr):
            # see https://stackoverflow.com/a/15012814/355230
            _id = int(match.group(1))
            no_indent = PyObj_FromPtr(_id)
            if no_indent.max_length is not None and isinstance(no_indent.value, list) and len(str(no_indent.value)) > no_indent.max_length:
                truncated_value = str(no_indent.value)[0:no_indent.max_length]
                json_obj_repr = truncated_value + '...'
            else:
                json_obj_repr = json.dumps(no_indent.value, sort_keys=self.__sort_keys)

            # Replace the matched id string with json formatted representation
            # of the corresponding Python object.
            json_repr = json_repr.replace(
                            '"{}"'.format(format_spec.format(_id)), json_obj_repr)

        return '\n'+json_repr #\n to get rid of weird indent in html :)

#----------------------SUBMODELS------------------------#
class SensorVendorTestData(BaseModel):
    vendor_leakage_current_uA: Union[None,float] = Field(validation_alias=AliasChoices('vendor_leakage_current_uA','Vendor Leakage Current [uA]'))
    vendor_breakdown_voltage_V: Union[None,float] = Field(validation_alias=AliasChoices('vendor_breakdown_voltage_V','Vendor Breakdown Voltage [V]'))
    vendor_category: Union[None,Literal["BAD", "GOOD", "MEDIUM"]] = Field(validation_alias=AliasChoices('vendor_category','Vendor Category'))
    current: Union[None,List] = Field(validation_alias=AliasChoices('current','Current'))
    voltage: Union[None,List] = Field(validation_alias=AliasChoices('voltage','Voltage'))


class GantryPickAndPlaceData(BaseModel):
    target: List[float]
    actual: List[float]
    delta: List[float]

    @field_validator('*')
    @classmethod
    def length_check(cls, v):
        if len(v) != 4:
            raise ValueError("The required length is 4 for target, actual and delta. It is [x, y, z, rot]")
        return v
    

#---------------------------------------- BASE CONSTRUCTION MODELS ---------------------------------------#
class ConstrHelperMixin:
    @classmethod
    def get_examples(cls):
        json_schema = cls.model_config.get("json_schema_extra")
        return [json.dumps(examp, cls=DocumentationEncoder, indent=2) for examp in json_schema.get("examples", []) if json_schema]

class ConstructionBase(BaseModel, ConstrHelperMixin):
    measurement_date: AwareDatetime #force times to have timezone
    location: str
    user_created: str

    @field_validator('*')
    @classmethod
    def empty_str_to_none(cls, v):
        if isinstance(v, str) and v.strip() == '':
            return None
        return v

    @classmethod
    def get_subclasses(cls):
        return tuple(cls.__subclasses__())

    @field_validator("measurement_date")
    @classmethod
    def validate_measurement_date(cls, v):
        return validate_datetime(v)

#------------------------------------------------------#

class SensorVendorTest(ConstructionBase):
    model_config = ConfigDict(json_schema_extra={
        'examples': [
            {
                "component": "TYL4U001",
                "type": "Sensor Vendor Test",
                "measurement_date": "2023-01-01T12:00:00+01:00",
                "location": "FBK",
                "user_created": "fsiviero",
                "data": {
                    "vendor_leakage_current_uA": 158.176,
                    "vendor_breakdown_voltage_V": 282.0,
                    "vendor_category": "BAD",
                    "current": NoIndent([1.7981099942332435e-9, 2.1325199384136795e-9,2.3892399170222234e-9,2.6674600306364482e-9,2.9917699428949618e-9,3.3739500082674567e-9,3.8820999748168106e-9,4.47047021623348e-9,5.163700134147575e-9,5.982729867071157e-9,6.888820180961375e-9,7.861340023396224e-9,8.972140363994185e-9,9.177109738800482e-9,1.1357499829500739e-8,1.3345699656497345e-8,1.591829956737456e-8,1.9567799824926624e-8,2.4187400526898273e-8,2.9501000753384687e-8,4.2371500086346714e-8,5.5717400755384006e-6,0.000025144199753412977,0.000034218599466839805,0.000040536098822485656,0.00004414160139276646,0.000045468401367543265,0.00005196220081415959,0.00006523320189444348,0.00007574760093120858,0.00008891220204532146,0.00011379199713701382,0.00013335900439415127,0.00015114799316506833,0.0001657230022829026,0.00018318099319003522,0.00020124799630139023,0.00021330300660338253,0.00022421199537348002,0.00023484700068365782,0.00024567899527028203,0.00025691199698485434,0.0002710630069486797,0.00028676798683591187,0.0003011419903486967,0.00031354298698715866,0.0003255319898016751,0.00033718798658810556,0.00034998898627236485,0.00037184200482442975,0.0003914310073014349,0.0004061759973410517,0.00042100698919966817,0.0004358369915280491,0.0004506719997152686,0.00046582298818975687,0.0004808040102943778,0.0004961600061506033,0.0005116279935464263,0.0005280390032567084,0.000550133001524955,0.000574567005969584], max_length=40),
                    "voltage": NoIndent([0.0,2.0,4.0,6.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,23.0,25.0,26.0,28.0,30.0,32.0,34.0,36.0,38.0,40.0,41.0,43.0,45.0,47.0,49.0,50.0,55.0,60.0,65.0,70.0,75.0,80.0,85.0,90.0,95.0,100.0,105.0,110.0,115.0,120.0,125.0,130.0,135.0,140.0,145.0,150.0,155.0,160.0,165.0,170.0,175.0,180.0,185.0,190.0,195.0,200.0,205.0,210.0,215.0,220.0,225.0,230.0,235.0,240.0,245.0,250.0,255.0,260.0,265.0,270.0,275.0,280.0], max_length=40)
                }
            }
        ],
    })

    type: Literal['Sensor Vendor Test']
    component: str
    data: SensorVendorTestData

    def calc_data_cache(self):
        return self.data


class ModuleETROCStatus(ConstructionBase):
    model_config = ConfigDict(json_schema_extra={
        'examples': [
            {
                "component": "PE0001",
                "type": "etroc_status",
                "measurement_date": "2023-01-01T12:00:00+01:00",
                "location": "BU",
                "user_created": "hayden",
                "data": NoIndent(np.ones((16,16), dtype=int).tolist(), max_length=60)
            }
        ],
    })
    type: Literal['etroc_status']
    component: str
    data: List[List[int]]

    @field_validator('data')
    @classmethod
    def length_check(cls, v):
        v_arr = np.array(v)
        if v_arr.shape != (16,16):
            raise ValueError(f"Your array is not the correct shape, it should be 16x16, you gave: {v_arr.shape}")
        
    def calc_data_cache(self):
        return self.data
    

#---------------------ASSEMBLY----------------------#   

class SubassemblyAlignment(ConstructionBase):
    model_config = ConfigDict(json_schema_extra={
        'examples': [
            {
                "compoenent": "PS0001",
                "type": "subassembly alignment",
                "measurement_date": "2023-01-01T12:00:00+01:00",
                "location": "BU",
                "user_created": "hayden",
                "data": {
                    "target": NoIndent([639.141118, 287.244992, 64.009534,-0.048954]),
                    "actual": NoIndent([639.141118, 287.244992, 64.009534,-0.048954]),
                    "delta": NoIndent([639.141118, 287.244992, 64.009534,-0.048954])
                }
            },
        ],
    })
    type: Literal['subassembly alignment']
    component: str
    data: GantryPickAndPlaceData  

    def calc_data_cache(self):
        return self.data

class GantryPickPlace(ConstructionBase):
    model_config = ConfigDict(json_schema_extra={
        'examples': [
            {
                "module": "PBU0001",
                "compoenent": "PE0001",
                "component_pos": 1, 
                "type": "pick and place survey precure",
                "measurement_date": "2023-01-01T12:00:00+01:00",
                "location": "BU",
                "user_created": "hayden",
                "data": {
                    "target": NoIndent([639.141118, 287.244992, 64.009534,-0.048954]),
                    "actual": NoIndent([639.141118, 287.244992, 64.009534,-0.048954]),
                    "delta": NoIndent([639.141118, 287.244992, 64.009534,-0.048954])
                }
            },
            {
                "module": "PBU0001",
                "compoenent": "PE0001",
                "component_pos": 1, 
                "type": "pick and place survey postcure",
                "measurement_date": "2023-01-01T12:00:00+01:00",
                "location": "BU",
                "user_created": "hayden",
                "data": {
                    "target": NoIndent([639.141118, 287.244992, 64.009534,-0.048954]),
                    "actual": NoIndent([639.141118, 287.244992, 64.009534,-0.048954]),
                    "delta": NoIndent([639.141118, 287.244992, 64.009534,-0.048954])
                }
            }
        ],
    })
    type: Literal['pick and place survey precure', 'pick and place survey postcure']
    module: str
    component: str
    component_pos: int
    data: GantryPickAndPlaceData

    def calc_data_cache(self):
        print("whoops")
        return self.data
    
    def display_data(self):
        #take the data and make a plot or calculation
        pass

    def as_html_card(self):
        pass

#-------------------------Model for list of construction objects-------------------------------#
class ConstructionCong(RootModel): #cong for conglomerate
    #https://github.com/pydantic/pydantic/issues/3947
    root: List[Union[ConstructionBase.get_subclasses()]] = Field(..., discriminator='type') #could try Union[Type[ConstructionBase]] later