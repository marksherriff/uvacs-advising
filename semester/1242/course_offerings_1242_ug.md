---
layout: default
title: S24 Undergrad Courses
parent: Course Information
---

# CS Undergrad Courses for Spring 2024

__Last Updated: Friday, October 13__

__NOTE: This page is now deprecated.  Please see Lou's List or SIS for the most up-to-date information.  This page will be retained for a short period.__

* [Lou's List for Spring 2024](https://louslist.org/page.php?Semester=1242&Type=Group&Group=CompSci)

_Updates:_

- _CS 3120 has been moved to TuTh 11:00-12:15._
- _CS 3140 has been moved to TuTh 09:30-10:45.  The second section has been canceled._
- _CS 5501 has been added and will count as a CS elective for undergrads._

## Undergraduate Courses

| Course        | Title          | Instructor |  Meeting |      
|:-------------|:------------------|:------|:-------|
{% for course in site.data.course_offerings_1242_ug -%}
{% if course.type == "LAB" -%}
| {{ course.course }} | {{ course.title }} (LAB) | {{ course.instructor }} | {{ course.day }} |
{% else -%}
| {{ course.course }} | {{ course.title }} | {{ course.instructor }} | {{ course.day }} |
{% endif -%}
{%- endfor -%}


