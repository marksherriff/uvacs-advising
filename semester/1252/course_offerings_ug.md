---
layout: default
title: Undergrad - Spring 2025
parent: Course Information
---

# CS Undergrad Courses for Spring 2025

__Last Updated: Monday, February 15__

_NOTE: Below is the current predicted courses for Spring 2025.  This is subject to change, but is being provided to help students plan their next academic year as best as possible._

## Undergraduate Courses

| Course        | Title          | Instructor |  Meeting |      
|:-------------|:------------------|:------|:-------|
{% for course in site.data.course_offerings_1252_ug -%}
{% if course.type == "LAB" -%}
| {{ course.course }} | {{ course.title }} (LAB) | {{ course.instructor }} | {{ course.day }} |
{% else -%}
| {{ course.course }} | {{ course.title }} | {{ course.instructor }} | {{ course.day }} |
{% endif -%}
{%- endfor -%}


