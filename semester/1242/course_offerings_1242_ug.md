---
layout: default
title: S24 Undergrad Courses
parent: Course Information
---

# CS Undergrad Courses for Spring 2024

__Last Updated: Tuesday, October 10__

__NOTE: These courses/days/times are subject to change!  Once SIS / Lou's List has updated on October 13, please refer there for the latest information.__

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


