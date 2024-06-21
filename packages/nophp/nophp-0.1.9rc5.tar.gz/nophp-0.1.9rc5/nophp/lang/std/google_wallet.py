import os
from GoogleWalletPassGenerator.eventticket import EventTicketManager
from GoogleWalletPassGenerator.types import TranslatedString, LocalizedString, EventTicketClass, EventTicketClassId, EventTicketObject, EventTicketObjectId, Barcode, ObjectsToAddToWallet, EventTicketIdentifier
from GoogleWalletPassGenerator.enums import ReviewStatus, State, BarcodeType, BarcodeRenderEncoding
from GoogleWalletPassGenerator.serializer import serialize_to_json
from ..exceptions import TranspilerExceptions, Warn
from ..module import Module
from ..types import *

class CommonResendMod(Module):
    name="COMMONRESEND"
    type = Module.MODULE_TYPES.FUNCTION

    def __init__(self, compiler_instance):
        super().__init__()
        self.compiler_instance = compiler_instance

    def base(self, tree, ref=False):
        values = []

        if 'FUNCTION_ARGUMENTS' not in tree:
            # Advanced handling
            for var in tree:
                value = self.ref_resolve(var) if ref else self.safely_resolve(var)
                values.append(value)
        else:
            if 'POSITIONAL_ARGS' in tree['FUNCTION_ARGUMENTS']:
                for var in tree['FUNCTION_ARGUMENTS']['POSITIONAL_ARGS']:

                    value = self.ref_resolve(var) if ref else self.safely_resolve(var)

                    values.append(value)

        return values


# create_gpass($value) -> Bool
class CreateGpassMod(CommonResendMod):
    name="create_gpass"
    type = Module.MODULE_TYPES.FUNCTION

    def __init__(self, compiler_instance):
        super().__init__(compiler_instance)
        self.compiler_instance = compiler_instance

    def proc_tree(self, tree):
        values = self.base(tree)

        items = values[0]

        service_account_json = os.path.expanduser('~/key.json')
        manager = EventTicketManager(service_account_json)

        issuerId = items['ISSUER_ID']
        uniqueClassId = items['UNIQUE_CLASS_ID']
        uniqueObjectId = items['UNIQUE_OBJECT_ID']
        event_name = items['EVENT_NAME']
        issuerName = items["ISSUER_NAME"]
        qr_code = items['QR_CODE_DATA']

        eventTicketClass = serialize_to_json(
            EventTicketClass(
                id=EventTicketClassId(
                    issuerId=issuerId,
                    uniqueId=uniqueClassId
                ),
                issuerName=issuerName,
                eventName=LocalizedString(
                    defaultValue=TranslatedString(
                        "en-US", event_name
                    ),
                ),
                reviewStatus=ReviewStatus.APPROVED,  # Or any other status from the enum
            )
        )

        manager.create_class(eventTicketClass)     

        eventTicketObject = serialize_to_json(
            EventTicketObject(
                id=EventTicketObjectId(
                    issuerId=issuerId,
                    uniqueId=uniqueObjectId
                ),
                classId=EventTicketClassId(
                    issuerId=issuerId,
                    uniqueId=uniqueClassId
                ),
                state=State.ACTIVE,  # Or any other state from the enum
                barcode=Barcode(
                    type=BarcodeType.QR_CODE,  # Or any other barcode from the enum
                    renderEncoding=BarcodeRenderEncoding.UTF_8,  # Or any other render encoding from the enum
                    value=qr_code,
                )
            )
        )

        manager.create_object(eventTicketObject)   

        objectsToAdd = serialize_to_json(
            ObjectsToAddToWallet(
                [
                    EventTicketIdentifier(
                        id=EventTicketObjectId(
                            issuerId=issuerId,
                            uniqueId=uniqueObjectId
                        ),
                        classId=EventTicketClassId(
                            issuerId=issuerId,
                            uniqueId=uniqueClassId
                        ),
                    )
                ]
            )
        )

        walletUrls = manager.create_add_event_ticket_urls(objectsToAdd)

        return String(walletUrls)
    
_MODS = {
    "create_gpass": CreateGpassMod,
}

def build_funcs(c):
    functions = {}
    for f in _MODS:
        functions[f] = {
                "run_func": _MODS[f](c)
            }
    return functions