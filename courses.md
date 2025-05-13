---
layout: default
title: Course Information
nav_order: 4
has_children: false
---

# Course Information
{: .no_toc }

1. TOC
{:toc}

## CS Course Prerequisite Chart

![Prerequisite Chart]({{ site.data.externallinks.prereq_chart }})

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

__UPDATES__

* As of the 2024-2025 AY, APMA 3120 != STAT 3120 (per information from Jesse Rogers)

### Other SEAS Courses

* MAE 2300 == CE 2300
* MAE 2310 == CE 2310
* MAE 2320 == CE 2320

### Courses That ARE NOT Equivalent

* STAT 3080 - From Data to Knowledge cannot be used in place of APMA 3150 due to differences in content.


## Transferring Courses to UVA

[See our dedicated page on transferring courses](/transfer.html)

## Which CS1 Course Should I Take

If you have never programmed before, take CS 1110, 1112, 1113, or 1120. If you have programmed a little, take CS 1111 (or 1110 or 1113 if you can't get into 1111). If you have programmed a fair amount, you can probably get transfer credit or test out of CS 111x. More details follow.

* CS 1110 - A basic introductory course that focuses on learning the basics of programming and computational thinking. No prerequisite required. Language: Python. Requires a lecture section and a lab.
* CS 1111 - Only students with some programming experience may take this course. This programming experience can be in any language. CS 1111 has the same assignments and tests as CS 1110, but does not require lab and moves slightly faster through some material since students are expected to have some exposure to basic concepts. Language: Python.
* CS 1112 - Only students with no programming experience may take this course. Offered as a lecture + lab combination that meets three times a week. Language: Python.
* CS 1113 - CS1 special topics and can vary from semester to semester. In the past we have offered a version focused on a mathematical approach to computing and a version emphasizing uses of computing in engineering disciplines.
* CS 1120 - A course designed as an introductory course for the BACS, it now counts the same for all majors and schools.

Note - You can only receive credit for 1 CS 111X or 1120 course.

## AP/IB/Dual Enrollment Credit

### Advanced Placement
{: .no_toc }

* For Computer Science - 4 or 5 gives credit for CS 1110
* For CS Principles - 4 or 5 gives credit for CS 1000T and the student is encouraged to take the CS 1110 Place-Out Test

### International Baccalaureate
{: .no_toc }

For Computer Science:

* 5 on High Level gives credit for CS 1110
* 6 or 7 on High Level gives credit for CS 1110 and CS 2100

### Dual Enrollment
{: .no_toc }

Please discuss with a CS advisor or the SEAS dean's office.

### UVA AP Credit Information

Please see the [undergraduate record]({{site.data.externallinks.ap_credit}}) for information about what AP credit UVA accepts.

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