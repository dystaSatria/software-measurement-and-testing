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

## Usage in NOC Project

In our NOC project, monitoring NOC values can assist in assessing the design structure of our components. It can guide decisions on refactoring, optimizing, or restructuring the class hierarchy for improved maintainability and understanding.

- - - - - -

## Example Scenario

* Suppose we have a class Router in our NOC project with NOC equal to 5. It means there are 5 immediate subclasses extending the Router class.

```c#
// Kelas dasar Router
public class Router {
  // Implementasi
}

public class Subclass1 extends Router {
  // Implementasi khusus untuk Subclass1
}

public class Subclass2 extends Router {
  // Implementasi khusus untuk Subclass2
}

public class Subclass3 extends Router {
  // Implementasi khusus untuk Subclass3
}

public class Subclass4 extends Router {
  // Implementasi khusus untuk Subclass4
}

public class Subclass5 extends Router {
  // Implementasi khusus untuk Subclass5
}


```

* [gambar](https://github.com/dystaSatria/software-measurement-and-testing/blob/main/lectureNotes/NOC%20Matrix/Screenshot%202024-01-15%20at%2022.17.43.png)

- - - - - -

## Recommendations

* Regularly review NOC values to ensure a balanced and maintainable class hierarchy.
* Consider refactoring if NOC is excessively high, potentially indicating a need for a more streamlined design.


- - - - - -
