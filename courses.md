---
layout: default
title: Course Information
nav_order: 4
---

# Course Information
{: .no_toc }

1. TOC
{:toc}

## CS Course Prerequisite Chart

![Prerequisite Chart]({{ site.data.externallinks.prereq_chart }})

## CS Course Descriptions

{% for course in site.data.courses %}

### {{ course.course }}: {{ course.title }}
{: .no_toc }
{% if course.flag == "foundation" %}
Foundation
{: .label .label-green .float-right}
{% elsif course.flag == "elective" %}
CS Elective
{: .label .label-purple .float-right}
{% elsif course.flag == "deprecated" %}
Deprecated
{: .label .label-red .float-right}
{% elsif course.flag != NULL %}
{{ course.flag }}
{: .label .float-right}
{% endif %}
_({{ course.credits }} credits  / Prerequisites: {{ course.prereqs }})_     
{{ course.description }}

{% endfor %}

## UVA Course Equivalencies

These courses have been approved and entered into SIS to count for each other in all cases.  If you find a discrepancy in your academic record, please [email cs-office@virginia.edu](mailto:cs-office@virginia.edu).

### CS Courses

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

## Approved Transfer Courses

[SEAS List of Approved Transfer Courses](https://engineering.virginia.edu/current-students/current-undergraduate-students/transferring-uva-engineering/transfer-credit)

[College Transfer Credit Equivalencies for U.S. Colleges and Universities](http://ascs8.eservices.virginia.edu/AsEquivs)