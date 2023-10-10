---
layout: default
title: S24 Undergrad Courses
parent: Course Information
---

# CS Undergrad Courses for Spring 2024

__Last Updated: Saturday, October 7__

__NOTE: These courses/days/times are subject to change!  Once SIS / Lou's List has updated on October 13, please refer there for the latest information.__

_Update: Due to a lack of available rooms, CS 3140 will most likely be changing times to 9:30 AM TR and there may only be one large section.  This will be updated as soon as everything can be confirmed._

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


