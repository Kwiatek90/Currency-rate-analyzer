# Currency Rate Analyzer

## Contents
* [Introduction](#introduction)
* [Setup](#setup)
* [Applied technologies and libraries](#applied-technologies-and-libraries)
* [License](#license)

## Introduction

This script allows you to download currency exchange rate data from the NBP API and save it to a file. Script also allows you to download data from a file, display selected currency rates and analyze their average, minimum and maximum values. There is also a program that downloads currency rates every day at 12 p.m. and adds them to all records saved in the file.

## Setup

You only need the appropriate version of python and its libraries, running in your IDLE environment (I recommend Visual studio code or PyCharm)
```
pip install requests=2.31.0
pip install pandas=2.1.4
pip install schedule=1.2.1
```

## Applied technologies and libraries

* Environment
    * Pyhton 3.11.4
    * Visual Studio Code 1.79

* Libraries
    * schedule 1.2.1
    * pandas 2.1.4
    * requests 2.31.0

## License

This project is open-source and available under the MIT License.




