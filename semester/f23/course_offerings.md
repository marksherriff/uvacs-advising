---
layout: default
title: Course Offerings for F23
parent: Course Information
---

# Course Offerings for Fall 2023

__Last Updated: Thursday, March 8__

| Course        | Title          | Instructor |  Meeting |      
|:-------------|:------------------|:------|:-------|
{% for course in site.data.course_offerings_1238 -%}
{% if course.type == "LAB" -%}
| {{ course.course }} | {{ course.title }} (LAB) | {{ course.instructor }} | {{ course.day }} |
{% else -%}
| {{ course.course }} | {{ course.title }} | {{ course.instructor }} | {{ course.day }} |
{% endif -%}
{%- endfor -%}