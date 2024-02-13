---
layout: default
title: Undergrad - Fall 2024
parent: Course Information
---

# CS Undergrad Courses for Fall 2024

__Last Updated: Monday, February 15__

_NOTE: The courses, days, times, and instructors are subject to change.  The official schedule will be released in SIS on Friday, March 15._

## Undergraduate Courses

| Course        | Title          | Instructor |  Meeting |      
|:-------------|:------------------|:------|:-------|
{% for course in site.data.course_offerings_1248_ug -%}
{% if course.type == "LAB" -%}
| {{ course.course }} | {{ course.title }} (LAB) | {{ course.instructor }} | {{ course.day }} |
{% else -%}
| {{ course.course }} | {{ course.title }} | {{ course.instructor }} | {{ course.day }} |
{% endif -%}
{%- endfor -%}


