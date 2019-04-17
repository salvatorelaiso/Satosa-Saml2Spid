EDUCOURSE_OID = 'urn:oid:1.3.6.1.4.1.5923.1.6.1.'
EDUPERSON_OID = 'urn:oid:1.3.6.1.4.1.5923.1.1.1.'
EDUMEMBER1_OID = 'urn:oid:1.3.6.1.4.1.5923.1.5.1.'

# ldap.gv.at definitions as specified in:
# http://www.ref.gv.at/AG-IZ-PVP2-Version-2-1-0-2.2754.0.html
LDAPGVAT_OID = 'urn:oid:1.2.40.0.10.2.1.1.'

UCL_DIR_PILOT = 'urn:oid:0.9.2342.19200300.100.1.'
X500ATTR_OID = 'urn:oid:2.5.4.'
LDAPGVAT_UCL_DIR_PILOT = UCL_DIR_PILOT
LDAPGVAT_X500ATTR_OID = X500ATTR_OID
NETSCAPE_LDAP = 'urn:oid:2.16.840.1.113730.3.1.'
NOREDUPERSON_OID = 'urn:oid:1.3.6.1.4.1.2428.90.1.'
PKCS_9 = 'urn:oid:1.2.840.113549.1.9.1.'
SCHAC = 'urn:oid:1.3.6.1.4.1.25178.1.2.'
SIS = 'urn:oid:1.2.752.194.10.2.'
UMICH = 'urn:oid:1.3.6.1.4.1.250.1.57.'

# openosi-0.82.schema http://www.openosi.org/osi/display/ldap/Home
OPENOSI_OID = 'urn:oid:1.3.6.1.4.1.27630.2.1.1.'

EIDAS_NATURALPERSON = 'http://eidas.europa.eu/attributes/naturalperson/'
EIDAS_LEGALPERSON = 'http://eidas.europa.eu/attributes/legalperson/'


_MAP = {
        # R&S federation and eIDAS
        EIDAS_LEGALPERSON+'LegalPersonIdentifier': 'LegalPersonIdentifier',
        EIDAS_LEGALPERSON+'LegalAddress': 'LegalAddress',
        EIDAS_LEGALPERSON+'LegalName': 'LegalName',
        EIDAS_LEGALPERSON+'VATRegistration': 'VATRegistration',
        EIDAS_LEGALPERSON+'TaxReference': 'TaxReference',
        EIDAS_LEGALPERSON+'BusinessCodes': 'BusinessCodes',
        EIDAS_LEGALPERSON+'LEI': 'LEI',
        EIDAS_LEGALPERSON+'EORI': 'EORI',
        EIDAS_LEGALPERSON+'SEED': 'SEED',
        EIDAS_LEGALPERSON+'SIC': 'SIC',
        EIDAS_LEGALPERSON+'D-2012-17-EUIdentifier': 'D-2012-17-EUIdentifier',
        EIDAS_NATURALPERSON+'PersonIdentifier': 'PersonIdentifier',
        EIDAS_NATURALPERSON+'CurrentFamilyName': 'FamilyName',
        EIDAS_NATURALPERSON+'CurrentGivenName': 'FirstName',
        EIDAS_NATURALPERSON+'DateOfBirth': 'DateOfBirth',
        EIDAS_NATURALPERSON+'BirthName': 'BirthName',
        EIDAS_NATURALPERSON+'PlaceOfBirth': 'PlaceOfBirth',
        EIDAS_NATURALPERSON+'CurrentAddress': 'CurrentAddress',
        EIDAS_NATURALPERSON+'Gender': 'Gender',
        EDUCOURSE_OID+'1': 'eduCourseOffering',
        EDUCOURSE_OID+'2': 'eduCourseMember',
        EDUMEMBER1_OID+'1': 'isMemberOf',
        EDUPERSON_OID+'1': 'eduPersonAffiliation',
        EDUPERSON_OID+'2': 'eduPersonNickname',
        EDUPERSON_OID+'3': 'eduPersonOrgDN',
        EDUPERSON_OID+'4': 'eduPersonOrgUnitDN',
        EDUPERSON_OID+'5': 'eduPersonPrimaryAffiliation',
        EDUPERSON_OID+'6': 'eduPersonPrincipalName',
        EDUPERSON_OID+'7': 'eduPersonEntitlement',
        EDUPERSON_OID+'8': 'eduPersonPrimaryOrgUnitDN',
        EDUPERSON_OID+'9': 'eduPersonScopedAffiliation',
        EDUPERSON_OID+'10': 'eduPersonTargetedID',
        EDUPERSON_OID+'11': 'eduPersonAssurance',
        EDUPERSON_OID+'12': 'eduPersonPrincipalNamePrior',
        EDUPERSON_OID+'13': 'eduPersonUniqueId',
        EDUPERSON_OID+'16': 'eduPersonOrcid',
        LDAPGVAT_OID+'1': 'PVP-GID',
        LDAPGVAT_OID+'149': 'PVP-BPK',
        LDAPGVAT_OID+'153': 'PVP-OU-OKZ',
        LDAPGVAT_OID+'261.10': 'PVP-VERSION',
        LDAPGVAT_OID+'261.20': 'PVP-PRINCIPAL-NAME',
        LDAPGVAT_OID+'261.24': 'PVP-PARTICIPANT-OKZ',
        LDAPGVAT_OID+'261.30': 'PVP-ROLES',
        LDAPGVAT_OID+'261.40': 'PVP-INVOICE-RECPT-ID',
        LDAPGVAT_OID+'261.50': 'PVP-COST-CENTER-ID',
        LDAPGVAT_OID+'261.60': 'PVP-CHARGE-CODE',
        LDAPGVAT_OID+'3': 'PVP-OU-GV-OU-ID',
        LDAPGVAT_OID+'33': 'PVP-FUNCTION',
        LDAPGVAT_OID+'55': 'PVP-BIRTHDATE',
        LDAPGVAT_OID+'71': 'PVP-PARTICIPANT-ID',
        LDAPGVAT_UCL_DIR_PILOT+'1': 'PVP-USERID',
        LDAPGVAT_UCL_DIR_PILOT+'3': 'PVP-MAIL',
        LDAPGVAT_X500ATTR_OID+'11': 'PVP-OU',
        LDAPGVAT_X500ATTR_OID+'20': 'PVP-TEL',
        LDAPGVAT_X500ATTR_OID+'42': 'PVP-GIVENNAME',
        NETSCAPE_LDAP+'1': 'carLicense',
        NETSCAPE_LDAP+'2': 'departmentNumber',
        NETSCAPE_LDAP+'3': 'employeeNumber',
        NETSCAPE_LDAP+'4': 'employeeType',
        NETSCAPE_LDAP+'39': 'preferredLanguage',
        NETSCAPE_LDAP+'40': 'userSMIMECertificate',
        NETSCAPE_LDAP+'216': 'userPKCS12',
        NETSCAPE_LDAP+'241': 'displayName',
        NOREDUPERSON_OID+'1': 'norEduOrgUniqueNumber',
        NOREDUPERSON_OID+'2': 'norEduOrgUnitUniqueNumber',
        NOREDUPERSON_OID+'3': 'norEduPersonBirthDate',
        NOREDUPERSON_OID+'4': 'norEduPersonLIN',
        NOREDUPERSON_OID+'5': 'norEduPersonNIN',
        NOREDUPERSON_OID+'6': 'norEduOrgAcronym',
        NOREDUPERSON_OID+'7': 'norEduOrgUniqueIdentifier',
        NOREDUPERSON_OID+'8': 'norEduOrgUnitUniqueIdentifier',
        NOREDUPERSON_OID+'9': 'federationFeideSchemaVersion',
        NOREDUPERSON_OID+'10': 'norEduPersonLegalName',
        NOREDUPERSON_OID+'11': 'norEduOrgSchemaVersion',
        NOREDUPERSON_OID+'12': 'norEduOrgNIN',
        OPENOSI_OID+'17': 'osiHomeUrl',
        OPENOSI_OID+'19': 'osiPreferredTZ',
        OPENOSI_OID+'72': 'osiICardTimeLastUpdated',
        OPENOSI_OID+'104': 'osiMiddleName',
        OPENOSI_OID+'107': 'osiOtherEmail',
        OPENOSI_OID+'109': 'osiOtherHomePhone',
        OPENOSI_OID+'120': 'osiWorkURL',
        PKCS_9+'1': 'email',
        SCHAC+'1': 'schacMotherTongue',
        SCHAC+'2': 'schacGender',
        SCHAC+'3': 'schacDateOfBirth',
        SCHAC+'4': 'schacPlaceOfBirth',
        SCHAC+'5': 'schacCountryOfCitizenship',
        SCHAC+'6': 'schacSn1',
        SCHAC+'7': 'schacSn2',
        SCHAC+'8': 'schacPersonalTitle',
        SCHAC+'9': 'schacHomeOrganization',
        SCHAC+'10': 'schacHomeOrganizationType',
        SCHAC+'11': 'schacCountryOfResidence',
        SCHAC+'12': 'schacUserPresenceID',
        SCHAC+'13': 'schacPersonalPosition',
        SCHAC+'14': 'schacPersonalUniqueCode',
        SCHAC+'15': 'schacPersonalUniqueID',
        SCHAC+'17': 'schacExpiryDate',
        SCHAC+'18': 'schacUserPrivateAttribute',
        SCHAC+'19': 'schacUserStatus',
        SCHAC+'20': 'schacProjectMembership',
        SCHAC+'21': 'schacProjectSpecificRole',
        SIS+'1': 'sisLegalGuardianFor',
        SIS+'2': 'sisSchoolGrade',
        UCL_DIR_PILOT+'1': 'uid',
        UCL_DIR_PILOT+'3': 'mail',
        UCL_DIR_PILOT+'25': 'dc',
        UCL_DIR_PILOT+'37': 'associatedDomain',
        UCL_DIR_PILOT+'43': 'co',
        UCL_DIR_PILOT+'60': 'jpegPhoto',
        UMICH+'57': 'labeledURI',
        X500ATTR_OID+'2': 'knowledgeInformation',
        X500ATTR_OID+'3': 'cn',
        X500ATTR_OID+'4': 'sn',
        X500ATTR_OID+'5': 'serialNumber',
        X500ATTR_OID+'6': 'c',
        X500ATTR_OID+'7': 'l',
        X500ATTR_OID+'8': 'st',
        X500ATTR_OID+'9': 'street',
        X500ATTR_OID+'10': 'o',
        X500ATTR_OID+'11': 'ou',
        X500ATTR_OID+'12': 'title',
        X500ATTR_OID+'14': 'searchGuide',
        X500ATTR_OID+'15': 'businessCategory',
        X500ATTR_OID+'16': 'postalAddress',
        X500ATTR_OID+'17': 'postalCode',
        X500ATTR_OID+'18': 'postOfficeBox',
        X500ATTR_OID+'19': 'physicalDeliveryOfficeName',
        X500ATTR_OID+'20': 'telephoneNumber',
        X500ATTR_OID+'21': 'telexNumber',
        X500ATTR_OID+'22': 'teletexTerminalIdentifier',
        X500ATTR_OID+'23': 'facsimileTelephoneNumber',
        X500ATTR_OID+'24': 'x121Address',
        X500ATTR_OID+'25': 'internationaliSDNNumber',
        X500ATTR_OID+'26': 'registeredAddress',
        X500ATTR_OID+'27': 'destinationIndicator',
        X500ATTR_OID+'28': 'preferredDeliveryMethod',
        X500ATTR_OID+'29': 'presentationAddress',
        X500ATTR_OID+'30': 'supportedApplicationContext',
        X500ATTR_OID+'31': 'member',
        X500ATTR_OID+'32': 'owner',
        X500ATTR_OID+'33': 'roleOccupant',
        X500ATTR_OID+'36': 'userCertificate',
        X500ATTR_OID+'37': 'cACertificate',
        X500ATTR_OID+'38': 'authorityRevocationList',
        X500ATTR_OID+'39': 'certificateRevocationList',
        X500ATTR_OID+'40': 'crossCertificatePair',
        X500ATTR_OID+'42': 'givenName',
        X500ATTR_OID+'43': 'initials',
        X500ATTR_OID+'44': 'generationQualifier',
        X500ATTR_OID+'45': 'x500UniqueIdentifier',
        X500ATTR_OID+'46': 'dnQualifier',
        X500ATTR_OID+'47': 'enhancedSearchGuide',
        X500ATTR_OID+'48': 'protocolInformation',
        X500ATTR_OID+'50': 'uniqueMember',
        X500ATTR_OID+'51': 'houseIdentifier',
        X500ATTR_OID+'52': 'supportedAlgorithms',
        X500ATTR_OID+'53': 'deltaRevocationList',
        X500ATTR_OID+'54': 'dmdName',
        X500ATTR_OID+'65': 'pseudonym',

        # Spid related
        "spidCode": "spidCode",
        "name": "name",
        "familyName": "familyName",
        "placeOfBirth": "placeOfBirth",
        "countyOfBirth": "countyOfBirth",
        "dateOfBirth": "dateOfBirth",
        "gender": "gender",
        "companyName": "companyName",
        "registeredOffice": "registeredOffice",
        "fiscalNumber": "fiscalNumber",
        "ivaCode": "ivaCode",
        "idCard": "idCard",
        "mobilePhone": "mobilePhone",
        "email": "email",
        "address": "address",
        "expirationDate": "expirationDate",
        "digitalAddress": "digitalAddress",
    }


MAP = {
    "identifier":  'urn:oasis:names:tc:SAML:2.0:attrname-format:uri',
    "fro": _MAP,
    "to": {v:k for k,v in _MAP.items()}
}
