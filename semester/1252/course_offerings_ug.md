---
layout: default
title: Undergrad - Spring 2025
parent: Course Information
---

# CS Undergrad Courses for Spring 2025

__Last Updated: Monday, February 15__

_NOTE: This is now very much out of date and will be updated in the coming weeks._

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


