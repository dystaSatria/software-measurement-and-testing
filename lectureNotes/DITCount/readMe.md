# DIT Count

<br>

## DIT Count Method

![DIT](https://github.com/dystaSatria/software-measurement-and-testing/blob/main/lectureNotes/DITCount/Screenshot%202024-01-15%20at%2022.17.43.png)

DIT -> Choose the longest way to main section (at the top / at the bottom)

Example : 
 * Taşıt section DIT score : 0.
 * Roket section DIT score : 0.
 * Kara Taşıtı section DIT score : 1.
 * Deniz Taşıtı section DIT score : 1.
 * Tank section DIT score : 2.

___ _____ ___ ____


## DIT Count Code

```python

def dit(yolcu):
    return sum(i for i in range(1, yolcu+1) if yolcu % i == 0)

```
