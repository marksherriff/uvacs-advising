---
layout: default
title: Course Information
nav_order: 4
---

# Course Information
{: .no_toc }

1. TOC
{:toc}

## Course Descriptions

{% for course in site.data.courses %}

### {{ course.course }}: {{ course.title }}
{: .no_toc }
_({{ course.credits }} credits)_           
{{ course.description }} 

{% endfor %}

## Course Equivalencies

### CS Courses

These CS courses will count for each other in all cases.

* CS 2120 == CS 2102
* CS 3100 == CS 4102
* CS 3120 == CS 3102

### APMA Courses

* APMA 1090 == MATH 1310
* APMA 1110 == MATH 1320
* APMA 2120 == MATH 2310
* APMA 2130 == MATH 3250
* APMA 3080 == MATH 3351
* APMA 3100 == MATH 3100
* APMA 3120 == STAT 3120

### Other SEAS Courses

* MAE 2300 == CE 2300
* MAE 2310 == CE 2310
* MAE 2320 == CE 2320

### SEAS Approved Equivalencies outside UVA

[https://engineering.virginia.edu/current-students/current-undergraduate-students/transferring-uva-engineering/transfer-credit](https://engineering.virginia.edu/current-students/current-undergraduate-students/transferring-uva-engineering/transfer-credit)