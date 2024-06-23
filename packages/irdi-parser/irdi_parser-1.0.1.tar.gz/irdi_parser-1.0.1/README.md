# IRDI Parser

## Overview

The IRDI Parser is a Python program designed to parse IRDI (International Registration Data Identifier) strings based on the international standards ISO/IEC 11179-6, ISO 29002 and ISO/IEC 6523. It is used in the [ECLASS](https://eclass.eu/support/technical-specification/structure-and-elements/irdi) standard. The program uses regular expressions to extract various components of an IRDI string and returns them in a structured format.

## Usage

Here's a basic example of how to use the `IRDIParser` class:

```python
from parser.irdi_parser import IRDIParser

parser = IRDIParser()
irdi = '1234-ABCD-#12-ABCDEF#1'
result = parser.parse(irdi)
print(result)
```
This will output:

```python
{
    'icd': '1234',
    'org_id': 'ABCD',
    'add_info': None,
    'csi': '12',
    'item_code': 'ABCDEF',
    'version': '1'
}
```

## EBNF Specification

The following is the EBNF (Extended Backus-Naur Form) representation of the IRDI format:

```ebnf
IRDI            ::= ICD '-' ORG_ID [ '-' ADD_INFO ] '#' CSI '-' ITEM_CODE '#' VERSION

ICD             ::= DIGIT DIGIT DIGIT DIGIT
ORG_ID          ::= SAFE_CHAR SAFE_CHAR SAFE_CHAR SAFE_CHAR
ADD_INFO        ::= SAFE_CHAR SAFE_CHAR SAFE_CHAR SAFE_CHAR
CSI             ::= SAFE_CHAR SAFE_CHAR
ITEM_CODE       ::= SAFE_CHAR SAFE_CHAR SAFE_CHAR SAFE_CHAR SAFE_CHAR SAFE_CHAR
VERSION         ::= DIGIT

DIGIT           ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
SAFE_CHAR       ::= DIGIT | ALPHA
ALPHA           ::= 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
                  | 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'
```

For this parser, a safe character is interpreted as a character that can be either a digit (0-9) or an alphanumeric character (a-z, A-Z). 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.