---
layout: default
title: S24 Undergrad Courses
parent: Course Information
---

# CS Undergrad Courses for Spring 2024

__Last Updated: Wednesday, October 4__

__NOTE: These courses/days/times are subject to change!  Once SIS / Lou's List has updated on October 13, please refer there for the latest information.__

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


