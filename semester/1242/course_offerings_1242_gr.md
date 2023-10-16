---
layout: default
title: S24 Graduate Courses
parent: Course Information
---

# CS Graduate Courses for Spring 2024

__Last Updated: Friday, October 13__

__NOTE: This page is now deprecated.  Please see Lou's List or SIS for the most up-to-date information.  This page will be retained for a short period.__

* [Lou's List for Spring 2024](https://louslist.org/page.php?Semester=1242&Type=Group&Group=CompSci)

## Graduate Courses

| Course        | Title          | Instructor |  Meeting |      
|:-------------|:------------------|:------|:-------|
{% for course in site.data.course_offerings_1242_gr -%}
{% if course.type == "LAB" -%}
| {{ course.course }} | {{ course.title }} (LAB) | {{ course.instructor }} | {{ course.day }} |
{% else -%}
| {{ course.course }} | {{ course.title }} | {{ course.instructor }} | {{ course.day }} |
{% endif -%}
{%- endfor -%}


