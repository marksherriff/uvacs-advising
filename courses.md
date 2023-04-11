---
layout: default
title: Course Information
nav_order: 4
has_children: true
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
* APMA 3120 == STAT 3120

### Other SEAS Courses

* MAE 2300 == CE 2300
* MAE 2310 == CE 2310
* MAE 2320 == CE 2320

### Courses That ARE NOT Equivalent

* STAT 3080 - From Data to Knowledge cannot be used in place of APMA 3150 due to differences in content.


## Transfering Courses to UVA

Current UVA students taking course work at other institutions may need to secure permission prior to enrolling in courses at another institution -- see more about this below. After completing such work, students must have official transcripts from the institution in which the courses were taken sent to the appropriate dean’s office at the University. Here are links to policies and procedures:

* [General University Policies](http://records.ureg.virginia.edu/content.php?catoid=54&navoid=4293#transer_credit) from the 2022-23 UG Record
* [SEAS process and policies](https://engineering.virginia.edu/current-students/current-undergraduate-students/transferring-uva-engineering/transfer-credit) (for BSCS and CpE majors)
* [College process and policies](https://college.as.virginia.edu/transfer-credit) (for BACS majors)

The College and SEAS pages have their own list of courses each has pre-approved. If a course is pre-approved, College students must submit a form before they take it (see the instructions on their website). SEAS does not require anything in advance if the course is pre-approved, but see their page for what you need to do after you complete the course. 

## Approved Transfer Courses

The pages above have links to school's pre-approved list of courses, but here are direct links:

* [SEAS List of Approved Transfer Courses](https://engineering.virginia.edu/current-students/current-undergraduate-students/transferring-uva-engineering/transfer-credit)
* [College Transfer Credit Equivalencies for U.S. Colleges and Universities](http://ascs8.eservices.virginia.edu/AsEquivs)

If the course is not on the pre-approved list for your school, approval is required before you take the course. First email the following to your program director ([bscsdirector@virginia.edu](mailto:bscsdirector@virginia.edu) or [bscsdirector@virginia.edu](mailto:bscsdirector@virginia.edu)):

* Where you want to take the course from
* Course Number / Title
* Link to course syllabus or a PDF of the course syllabus
* Why you believe the course is a match

We will then look at the course and inform you of the CS department's decision as soon as possible, and then you will have to follow your school's procedures for the paperwork approval.


### Transferring a course that is a prerequisite to CS courses

The courses taken at another institution cannot apply toward prerequisites at UVA until it has been completed and the grade is shown in SIS.  For example, if you plan to take a course to replace CS 2100 over the summer, SIS will not let you register for CS 3140 for the following fall until the course you are taking over the summer has been successfully completed AND is in SIS.  There is no good way to put in exceptions in SIS based on what a student "plans to do."  You can always reach out to the professors of the course you want to get in to, but they will generally let the registration process proceed normally.

### What if the course I want to transfer is not listed?

If there is a course that you believe would match one of our CS courses for transfer, email the following to your program director ([bscsdirector@virginia.edu](mailto:bscsdirector@virginia.edu) or [bscsdirector@virginia.edu](mailto:bscsdirector@virginia.edu)):

* Where you want to take the course from
* Course Number / Title
* Link to course syllabus or a PDF of the course syllabus
* Why you believe the course is a match

We will then look at the course and inform you of the decision as soon as possible.



## Which CS1 Course Should I Take

If you have never programmed before, take CS 1110, 1112, 1113, or 1120. If you have programmed a little, take CS 1111 (or 1110 or 1113 if you can't get into 1111). If you have programmed a fair amount, you can probably get transfer credit or test out of CS 111x. More details follow.

* CS 1110 - A basic introductory course that focuses on learning the basics of programming and computational thinking. No prerequisite required. Language: Python. Requires a lecture section and a lab.
* CS 1111 - Only students with some programming experience may take this course. This programming experience can be in any language. CS 1111 has the same assignments and tests as CS 1110, but does not require lab and moves slightly faster through some material since students are expected to have some exposure to basic concepts. Language: Python.
* CS 1112 - Only students with no programming experience may take this course. Offered as a lecture + lab combination that meets three times a week. Language: Python. Students must submit a permission of instructor request through SIS to request a seat in the course.
* CS 1113 - CS1 special topics and can vary from semester to semester. In the past we have offered a version focused on a mathematical approach to computing and a version emphasizing uses of computing in engineering disciplines.
* CS 1120 - A course designed as an introductory course for the BACS, it now counts the same for all majors and schools.

Note - You can only receive credit for 1 CS 111X or 1120 course.

## AP/IB/Dual Enrollment Credit

### Advanced Placement
{: .no_toc }

* For Computer Science - 4 or 5 gives credit for CS 1110
* For CS Principles - 4 or 5 gives credit for CS 1000T and the student is encouraged to take the CS 1110 Placement Test

### International Baccalaureate
{: .no_toc }

For Computer Science:

* 5 on High Level gives credit for CS 1110
* 6 or 7 on High Level gives credit for CS 1110 and CS 2110

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