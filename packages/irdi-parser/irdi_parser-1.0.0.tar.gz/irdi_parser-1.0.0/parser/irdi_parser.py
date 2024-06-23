import re


class IRDIParser:
    def __init__(self):
        self.pattern = re.compile(
            # International Code Designator (4 digits)
            r'^(?P<icd>\d{4})-'
            # Organization Identifier (4 safe characters)
            r'(?P<org_id>[a-zA-Z0-9]{4})'
            # Optional Additional Information (4 safe characters)
            r'(-(?P<add_info>[a-zA-Z0-9]{4}))?'
            # Separator Character
            r'#'
            # Code Space Identifier (2 safe characters)
            r'(?P<csi>[a-zA-Z0-9]{2})-'
            # Item Code (6 safe characters)
            r'(?P<item_code>[a-zA-Z0-9]{6})'
            # Separator Character
            r'#'
            # Version Identifier (1 digit)
            r'(?P<version>\d)$'
        )

    def parse(self, irdi):
        match = self.pattern.match(irdi)
        if match:
            return match.groupdict()
        else:
            raise ValueError(f"Invalid IRDI format: {irdi}")
