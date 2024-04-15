---
layout: default
title: Transferring Courses
nav_order: 4
---

# Transferring Courses to UVA
{: .no_toc }

1. TOC
{:toc}

## General Information

Current UVA students taking course work at other institutions may need to secure permission prior to enrolling in courses at another institution -- see more about this below. After completing such work, students must have official transcripts from the institution in which the courses were taken sent to the appropriate dean’s office at the University. Here are links to policies and procedures:

* [General University Policies]({{ site.data.externallinks.ureg_transfer_credit }}) from the UG Record
* [SEAS process and policies](https://engineering.virginia.edu/current-students/current-undergraduate-students/transferring-uva-engineering/transfer-credit) (for BSCS and CpE majors)
* [College process and policies](https://college.as.virginia.edu/transfer-credit) (for BACS majors)

The College and SEAS pages have their own list of courses each has pre-approved. If a course is pre-approved, College students must submit a form before they take it (see the instructions on their website). SEAS does not require anything in advance if the course is pre-approved, but see their page for what you need to do after you complete the course. 

## Approved Transfer Courses

The pages above have links to school's pre-approved list of courses, but here are direct links:

* [SEAS List of Approved Transfer Courses](https://engineering.virginia.edu/undergraduate-study/future-undergrads/transferring-uva-engineering/transfer-credit-equivalency)
* [College Transfer Credit Equivalencies for U.S. Colleges and Universities](http://ascs8.eservices.virginia.edu/AsEquivs)

### Quick Reference for VCCS Courses

| VCCS Course | VCCS Credits | UVA CS Course | UVA Credits |
| ----------- | ------------ | ------------- | ----------- |
| CSC 205: Computer Organization | 3 | CS 2000T | 3 (unrestricted elective) |
| CSC 208: Intro to Discrete Structures | 3 | CS 2120 | 3 |
| CSC 215: Computer Systems | 3 | CS 2130 | 3 out of 4 _(See note below)_ |
| CSC 221: Intro to Problem Solving & Programming | 3 | CS 1110 | 3 |
| CSC 223: Data Structures & Analysis of Algorithms | 4 | CS 2100 | 4 |

__NOTE:__
- CS 215 will only transfer 3 of 4 credits required for CS 2130.  Students must make up the remaining credit with another CS course level 2000 or higher.  Transfer students are _highly recommended_ to take CS 205 as part of their VCCS program to make up this credit.  [See below for more information about CS 215 at VCCS transferring to UVA.](/transfer.html#important-information-about-csc-215-from-a-virginia-community-college)

## What if the course I want to transfer is not listed?

If the course is not on the pre-approved list for your school, approval is required before you take the course. First email the following to your program director ([bacsdirector@virginia.edu](mailto:bacsdirector@virginia.edu) or [bscsdirector@virginia.edu](mailto:bscsdirector@virginia.edu)):

* Where you want to take the course from
* Course Number / Title
* Link to course syllabus or a PDF of the course syllabus
* Why you believe the course is a match

We will then look at the course and inform you of the CS department's decision as soon as possible, and then you will have to follow your school's procedures for the paperwork approval.

## Transferring a course that is a prerequisite to CS courses

The courses taken at another institution cannot apply toward prerequisites at UVA until it has been completed and the grade is shown in SIS.  For example, if you plan to take a course to replace CS 2100 over the summer, SIS will not let you register for CS 3140 for the following fall until the course you are taking over the summer has been successfully completed AND is in SIS.  There is no good way to put in exceptions in SIS based on what a student "plans to do."  You can always reach out to the professors of the course you want to get in to, but they will generally let the registration process proceed normally.


## Important Information about taking CSC 223 from a Virginia Community College

If you have taken all the courses in the VCCS three-course sequence CSC 221, CSC 222, and CSC 223 at a Virginia community college, none of what is discussed next applies to you.

If a UVA student who has taken CS111x at UVA (or the equivalent) and wants to only take CSC 223 at a community college, there are some issues that make this challenging.

The CSC 223 course is the third in the community college's sequence of three courses - CSC 221, 222, and 223, all of which are in Java.  Here at UVA, we have a two-course sequence (CS 1110 and CS 2100).  Before taking CSC 223 at a Virginia community college, you must have taken their CSC 222 course, in addition to a first programming course (like their CSC 221 or UVA's CS111x).  CSC 222 is a strict prerequisite to take CSC 223 at the community college.  Also, they require you have a discrete math class as a co-requisite for CSC 223, so if you haven't had our CS 2120 class here at UVA, they'd require you to take CSC 208: Introduction to Discrete Structures while or before you take CSC 223.  (CSC 208 will transfer here CS 2120).

The transfer credit rule about CSC 223 is more about how a student how transfers from a community college gets credit for the three CS courses they take there before coming to UVA.  The fact that their three-course sequence is different than how we teach things makes it a challenge (but not impossible) for a student who takes CS111x at UVA to go pick up one course, such as CSC 223, in the summer. You may need to take one or two more courses in addition to CSC 223.

## Important Information about CSC 215 from a Virginia Community College

If you have taken CSC 215 at one of Virginia's community colleges or are planning to, read the following carefully.

CSC 215 is listed as an approved transfer course for UVA's CS 2130. A few years ago when we evaluated this course, the community colleges told us that CSC 205 was a pre-requisite for CSC 215. Our evaluation determined that students who take both CSC 205 and CSC 215 would be ready to take UVA's CS 3130.  But it appears that the community colleges made a change, and it's possible for a student to take CSC 215 without taking CSC 205.

This is unfortunate. It's important that we honor our agreement with students and allow CSC 215 to count for CS 2130, especially for those who took it before being admitted to UVA. But this doesn't change the fact that students who only take CSC 215 will not be fully prepared for CS 3130.  Therefore we recommend the following:

* If you are a student at UVA, we recommend you take CS 2130 here, or take both CSC 205 and CSC 215 at a community college.  If you don't do this, you'll need to learn some things outside of the normal classes or you won't be prepared for CS 3130.
* You need to know how to read simple assembly language programs, be comfortable with common assembly instructions, and be able to understand how function calls are done in assembly language.
* Students use x86-64 assembly (in AT&T syntax) in CS 2130; if you learn a different assembly language, you should be prepared for the names and syntax (e.g. order of operands) being slightly different. 
* You should also have been introduced to the idea that assembly code is translated to machine code for the processor to run, including the fetch/execute cycle.

BACS students at UVA who submit the transfer credit form before they register for CSC 215 will be warned about this issue and asked to acknowledge that they understand these issues and that they'll need to do some "outside learning" to prepared for CS 3130.  (BSCS students do not need department approval before taking the course, so we have no way to provide this information to them directly. We'll have to hope BSCS students will have read the information here!)

Students who do transfer CSC 215, because CSC 215 is three credits and CS 2130 is four credits, will need one additional 2000+ level CS credit to make up the difference.

Finally, note that you won't be able to sign up for CS3130 or other courses that require CS2130 as a prerequisite until the grade from the community college has been transferred  and credit appears in SIS for CS2130.  This often means that you can't sign up for such courses until the start of the term after you complete the course at the community college.  This is due to how SIS and UVA handle credits and pre-requisites, and unfortunately it is not something that the CS department can help you overcome.
