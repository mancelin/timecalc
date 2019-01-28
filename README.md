# timecalc
Console utility to perform time operations in Python.

## Operators supported :
* **\+** : Addition
* **\-** : Substraction
* **->** , also noted **v** : time elapsed between two times

## timeformat
A valid timeformat is a string with numbers and the character **h** as the separator between hours and minutes:
  * hours and minutes : **10h05**
  * just hours : **7h**
  * just minutes : **23**

**timecalc** output is allways in hours and minutes

## Example

```
timecalc 8h20 + 2h55
```
11h05

```
timecalc 2h41 - 1h10
```
1h31


```
timecalc 2h41 - 301
```
-2h20


```
timecalc 1h20 + 0h55 + 1h - 3h27
```
-0h12

```
timecalc 14h11 '->' 19h02
```
4h51

```
timecalc 14h11 v 19h02
```
4h51


## Installation

* Clone or download this repository
```
    $ git clone git@github.com:mancelin/timecalc.git
```
* Add timecalc to your PATH, for example by editing ~/.bashrc
```
    $ cd timecalc
    $ echo "export PATH=`pwd`:$PATH" >> ~/.bashrc
```


## Licence
GNU GENERAL PUBLIC LICENSE v3
