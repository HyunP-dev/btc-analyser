from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/XML"


@dataclass
class SdnList:
    class Meta:
        name = "sdnList"
        namespace = "https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/XML"

    publsh_information: Optional["SdnList.PublshInformation"] = field(
        default=None,
        metadata={
            "name": "publshInformation",
            "type": "Element",
            "required": True,
        },
    )
    sdn_entry: List["SdnList.SdnEntry"] = field(
        default_factory=list,
        metadata={
            "name": "sdnEntry",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class PublshInformation:
        publish_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "Publish_Date",
                "type": "Element",
            },
        )
        record_count: Optional[int] = field(
            default=None,
            metadata={
                "name": "Record_Count",
                "type": "Element",
            },
        )

    @dataclass
    class SdnEntry:
        uid: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        first_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "firstName",
                "type": "Element",
            },
        )
        last_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "lastName",
                "type": "Element",
                "required": True,
            },
        )
        title: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        sdn_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "sdnType",
                "type": "Element",
                "required": True,
            },
        )
        remarks: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        program_list: Optional["SdnList.SdnEntry.ProgramList"] = field(
            default=None,
            metadata={
                "name": "programList",
                "type": "Element",
                "required": True,
            },
        )
        id_list: Optional["SdnList.SdnEntry.IdList"] = field(
            default=None,
            metadata={
                "name": "idList",
                "type": "Element",
            },
        )
        aka_list: Optional["SdnList.SdnEntry.AkaList"] = field(
            default=None,
            metadata={
                "name": "akaList",
                "type": "Element",
            },
        )
        address_list: Optional["SdnList.SdnEntry.AddressList"] = field(
            default=None,
            metadata={
                "name": "addressList",
                "type": "Element",
            },
        )
        nationality_list: Optional["SdnList.SdnEntry.NationalityList"] = field(
            default=None,
            metadata={
                "name": "nationalityList",
                "type": "Element",
            },
        )
        citizenship_list: Optional["SdnList.SdnEntry.CitizenshipList"] = field(
            default=None,
            metadata={
                "name": "citizenshipList",
                "type": "Element",
            },
        )
        date_of_birth_list: Optional["SdnList.SdnEntry.DateOfBirthList"] = (
            field(
                default=None,
                metadata={
                    "name": "dateOfBirthList",
                    "type": "Element",
                },
            )
        )
        place_of_birth_list: Optional["SdnList.SdnEntry.PlaceOfBirthList"] = (
            field(
                default=None,
                metadata={
                    "name": "placeOfBirthList",
                    "type": "Element",
                },
            )
        )
        vessel_info: Optional["SdnList.SdnEntry.VesselInfo"] = field(
            default=None,
            metadata={
                "name": "vesselInfo",
                "type": "Element",
            },
        )

        @dataclass
        class ProgramList:
            program: List[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

        @dataclass
        class IdList:
            id: List["SdnList.SdnEntry.IdList.Id"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass
            class Id:
                uid: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                id_type: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "idType",
                        "type": "Element",
                    },
                )
                id_number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "idNumber",
                        "type": "Element",
                    },
                )
                id_country: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "idCountry",
                        "type": "Element",
                    },
                )
                issue_date: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "issueDate",
                        "type": "Element",
                    },
                )
                expiration_date: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "expirationDate",
                        "type": "Element",
                    },
                )

        @dataclass
        class AkaList:
            aka: List["SdnList.SdnEntry.AkaList.Aka"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass
            class Aka:
                uid: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                type_value: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "type",
                        "type": "Element",
                        "required": True,
                    },
                )
                category: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                last_name: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "lastName",
                        "type": "Element",
                    },
                )
                first_name: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "firstName",
                        "type": "Element",
                    },
                )

        @dataclass
        class AddressList:
            address: List["SdnList.SdnEntry.AddressList.Address"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass
            class Address:
                uid: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                address1: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                address2: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                address3: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                city: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                state_or_province: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "stateOrProvince",
                        "type": "Element",
                    },
                )
                postal_code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "postalCode",
                        "type": "Element",
                    },
                )
                country: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                region: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

        @dataclass
        class NationalityList:
            nationality: List[
                "SdnList.SdnEntry.NationalityList.Nationality"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass
            class Nationality:
                uid: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                country: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                main_entry: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "mainEntry",
                        "type": "Element",
                        "required": True,
                    },
                )

        @dataclass
        class CitizenshipList:
            citizenship: List[
                "SdnList.SdnEntry.CitizenshipList.Citizenship"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

            @dataclass
            class Citizenship:
                uid: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                country: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                main_entry: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "mainEntry",
                        "type": "Element",
                        "required": True,
                    },
                )

        @dataclass
        class DateOfBirthList:
            date_of_birth_item: List[
                "SdnList.SdnEntry.DateOfBirthList.DateOfBirthItem"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "dateOfBirthItem",
                    "type": "Element",
                },
            )

            @dataclass
            class DateOfBirthItem:
                uid: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                date_of_birth: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "dateOfBirth",
                        "type": "Element",
                        "required": True,
                    },
                )
                main_entry: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "mainEntry",
                        "type": "Element",
                        "required": True,
                    },
                )

        @dataclass
        class PlaceOfBirthList:
            place_of_birth_item: List[
                "SdnList.SdnEntry.PlaceOfBirthList.PlaceOfBirthItem"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "placeOfBirthItem",
                    "type": "Element",
                },
            )

            @dataclass
            class PlaceOfBirthItem:
                uid: Optional[int] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                place_of_birth: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "placeOfBirth",
                        "type": "Element",
                        "required": True,
                    },
                )
                main_entry: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "mainEntry",
                        "type": "Element",
                        "required": True,
                    },
                )

        @dataclass
        class VesselInfo:
            call_sign: Optional[str] = field(
                default=None,
                metadata={
                    "name": "callSign",
                    "type": "Element",
                },
            )
            vessel_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vesselType",
                    "type": "Element",
                },
            )
            vessel_flag: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vesselFlag",
                    "type": "Element",
                },
            )
            vessel_owner: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vesselOwner",
                    "type": "Element",
                },
            )
            tonnage: Optional[int] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            gross_registered_tonnage: Optional[int] = field(
                default=None,
                metadata={
                    "name": "grossRegisteredTonnage",
                    "type": "Element",
                },
            )
