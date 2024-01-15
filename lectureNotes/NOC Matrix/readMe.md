# NOC Matrix (Chidamber & Kemerer)


## Overview

The "Number of Children" (NOC) is one of the Chidamber and Kemerer (CK) metrics used in software engineering to evaluate the complexity of object-oriented software. In the context of our NOC (Network on Chip) project, this metric provides insights into the inheritance hierarchy of our classes.

_ _ _ _ _ _

## Calculation

NOC is calculated by counting the number of immediate subclasses (children) that inherit from a specific class. In the context of our NOC project, this metric helps us understand how many classes directly inherit from a particular class, indicating the level of specialization and complexity in the hierarchy.


_ _ _ _ _ _

## Interpretation

* Low NOC Values: A low number of children suggests a more focused and less complex class hierarchy. It might indicate a design where each class has a specific responsibility and is not extensively extended.

* High NOC Values: A high number of children may suggest a more intricate hierarchy with multiple levels of specialization. While this can lead to a flexible design, it might also increase the complexity and maintenance challenges.

_ _ _ _ _ _

