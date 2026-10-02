layout: default
title: BSCS Senior Thesis Technical Report Information
permalink: /seniorthesis/
nav_exclude: true
---

# BSCS Senior Thesis Technical Report Guide

Default guidance for students and faculty

## 1 Using this guide

Your technical report explains a computing research or implementation project for the SEAS Senior Thesis portfolio. It should show what problem you addressed, what you contributed, how you examined the work, and what the evidence supports. A strong report makes your technical reasoning understandable to a reader who was not involved in the project.

Use this guide when your supervising faculty member has not provided more specific instructions. Faculty instructions govern the project scope, report content, format, and assessment; this guide fills gaps. Course requirements and current SEAS portfolio submission requirements also apply. If instructions conflict, resolve the conflict with the supervising faculty member or course instructor before submission.

### How the report fits your course

- **CS 4971** provides a course-based path to the technical report. Follow the course assignment and submission instructions.
- **CS 4980** involves independent research with a faculty member. That faculty member determines the paper’s content and format. This guide provides a starting point when additional guidance would help.
- **CS 4991** is a fallback for students in special circumstances. It carries no credit; students using this option take an additional CS elective. Follow the applicable CS 4991 instructions and confirm the arrangement with your advisor.

This guide addresses the technical report. It does not replace instructions for the STS paper, prospectus, or other portfolio components, and it does not determine eligibility for a course or thesis path.

### Start with a clear scope

Before drafting, identify the question or problem, the work you will report, your own contribution, and the evidence you can reasonably collect. Agree with your faculty member on the report’s scope, format, length, feedback schedule, and submission destination. A focused account of one substantial contribution is usually clearer than a survey of everything done in a lab, internship, or team project.

### Default presentation

When no other format is specified, use an ACM-style technical paper with a descriptive title, author name and affiliation, abstract, numbered body sections, and references. Word or LaTeX is suitable. A two-column layout is a useful default; preserve the chosen template’s margins, type size, and spacing. Remove sample text and publication metadata that do not apply, including invented conference names, copyright notices, and placeholder identifiers.

Use a default limit of **six pages of content, including figures and tables, plus up to one additional page containing only references**. References may begin within the first six pages; a seventh page, if needed, must contain only references. The faculty member may choose a different length or layout. This matches the CS 4971 report limit. In CS 4991, follow the applicable course limit. Use an editable document for feedback and a PDF for the final report unless the recipient specifies another format. Confirm portfolio packaging and submission instructions separately.


## 2 What the report should contain

These sections describe the report’s functions. You may rename, combine, or split sections to fit the project, provided the reader can find the information. Background and acknowledgments are optional. Methods, results, and limitations may be integrated into other sections, but their substance should remain explicit.

### Title and abstract

Choose a title that identifies the technical topic and contribution. Avoid generic titles such as “My Internship Project.” Include your name and affiliation; identify coauthors accurately when applicable. Follow any separate portfolio title-page requirements.

Write a single-paragraph abstract of roughly 150–250 words. Summarize the problem, approach, principal contribution, evaluation, and main finding or present status. State whether the work is implemented, partially implemented, or proposed. Write the abstract after the body so its claims match the report. It should stand alone, normally without citations or references to figures or sections.

### Introduction

Explain the problem, who encounters it, why it matters, and the specific scope of your work. Briefly introduce your approach and contribution. End with a clear research question, objective, or statement of what the project delivers. Give enough context for readers to understand why the following technical choices matter.

### Background and related work

Explain unfamiliar concepts only as needed. Discuss relevant research, systems, tools, or prior designs and compare them with your work. Show how earlier work informed your decisions and what you extend, adapt, investigate, or implement. A related-work section should synthesize connections rather than list summaries. Cite enough substantive sources to establish context; there is no default citation quota. Cite external factual claims wherever they occur, not only in this section.

### Technical approach or system design

Describe the research method, algorithm, architecture, implementation, or other technical artifact. Explain the important decisions, alternatives considered, and tradeoffs. Include relevant requirements, data flow, interfaces, dependencies, and constraints. Identify what you created and what came from existing systems or collaborators. An architecture diagram, worked example, or short pseudocode excerpt can make the explanation more precise. Avoid a feature list or a file-by-file tour of the code.

### Evaluation methods and results

Explain how you assessed the question or objective, then present what you observed. Describe the test conditions, data or participants, measures, comparisons, and procedures. Report failures and mixed findings as well as successes. Use labeled tables or figures when they clarify the evidence, and connect each important finding to the question it answers. See Section 3 for practical guidance.

### Discussion and limitations

Interpret the findings and explain their boundaries. Distinguish system limitations from limitations of the evaluation. Discuss plausible alternative explanations, restricted test conditions, missing evidence, and questions still unresolved. State how these limitations narrow your conclusions.

### Conclusion and future work

Summarize the contribution and what the evidence establishes. Do not introduce new results or promise benefits that were not examined. Identify concrete next steps, particularly those needed to address limitations or unfinished objectives. Acknowledgments may recognize assistance and resources. End with full references for the sources cited in the text.


## 3 Making the evaluation credible

Evaluation should fit the project’s objectives and available resources. It may involve experiments, benchmarks, correctness tests, a proof, structured user observations, analysis of an existing dataset, or comparison against defined requirements. A publishable discovery, successful deployment, or positive outcome is not necessary for a useful report. Honest analysis of an unsuccessful approach can demonstrate substantial technical work.

### Connect each claim to a measure

Identify what would count as evidence before collecting it. If you claim better performance, define the workload, comparison, and metric. If you claim improved usability, specify the tasks and observations. If you claim correctness, explain the specification and how the tests or analysis examine it. Functional testing can establish that a feature works under tested conditions; it does not by itself establish broad usability or long-term benefit.

For each major claim, a reader should be able to answer:

- What was evaluated, and against what criterion or baseline?
- What data, cases, workloads, or participants were included, and how were they selected?
- What procedure and environment were used, including relevant versions or settings?
- What was measured, how many observations were collected, and what happened?
- What remains uncertain, and how does that uncertainty affect the claim?

Include enough detail for another technically prepared reader to understand or repeat the evaluation. Provide appropriate aggregate data and avoid including identifying information about participants. Arrange any necessary research approvals with your faculty member before collecting data.

### Report results precisely

Use counts and denominators when reporting proportions: “Four of six participants completed the task without assistance” is more informative than “Most users succeeded.” Define units, success criteria, and any scoring scale. If you use an established instrument, describe its actual scoring method; if you adapt it, identify the adaptation. Describe how qualitative feedback was collected and summarized.

Keep tables, figures, and prose consistent. Explain missing observations, exclusions, and failures. When making a comparison, keep conditions comparable or discuss differences that could account for the result. Where relevant, report repeated trials and variation rather than a single favorable run. Statistical analysis is appropriate when the study supports it; it is not a default requirement for every project.

### Match the conclusion to the evidence

A small convenience sample can identify usability issues, but does not establish that the system works for every intended user. A short test can show task completion, but not a lasting change in behavior. Successful execution in one environment does not demonstrate reliability on every platform. Name these boundaries explicitly.

For example, a short evaluation of a planning tool might support the conclusion that participants could identify heavily scheduled weeks. Establishing that the tool reduces stress or improves grades would require additional evidence. A suitable report can explain the observed result and propose a longer study as future work.

### When the work is incomplete

Describe the implemented portion and evaluate it where possible. Label proposed components, expected benefits, and planned evaluations clearly. Never present anticipated results as observations. Explain what prevented completion, what you learned from the attempt, and what would be needed to answer the remaining question. Confirm with your faculty member that the resulting scope meets the expectations for your project.


## 4 Adapting the structure to your project

The same core questions apply across project types, but the evidence and technical explanation will differ. Choose a structure that makes the contribution visible.

### Independent research

State the research question or hypothesis and how it follows from prior work. Explain the experimental, analytical, or theoretical method; the data or assumptions; and the comparison used to interpret the result. Separate the contribution from the lab’s broader work. Report negative or inconclusive findings accurately. A theoretical project may use definitions, arguments, and proofs in place of empirical results; explain the assumptions and scope of the result.

### Software or system implementation

Define the requirements and intended use. Explain the architecture and technically significant design decisions, including alternatives and constraints. Describe the implemented state and assess it using appropriate tests, benchmarks, or user tasks. Distinguish requirements met, requirements partially met, and work deferred. Screenshots can illustrate behavior, but should accompany an explanation of the system’s design and evidence about its operation.

### Internship or collaborative project

Provide enough organizational context to explain the technical problem, then focus on your contribution. Identify what existed before you began, what you designed or implemented, and what other people contributed. Use “I” for your work and “we” for shared work, with a clear explanation of the roles. Agree on attribution and any shared text with your faculty member. Follow the applicable course rules for team reports and individual submissions.

Do not disclose confidential code, credentials, private records, or proprietary details. Work with the faculty member and project owner to identify a reportable scope or suitable abstraction. Resolve confidentiality and any archive restrictions before submission; do not assume that a private course submission will remain private in the portfolio.

### Technical design or proposal

A proposal is appropriate only when your faculty member or course instructor accepts it as the project scope. Define the problem and requirements, develop the design in enough technical detail to assess its feasibility, and explain the supporting literature or analysis. Describe the evaluation that would be needed to test the design. Clearly distinguish evidence from prior work, your design reasoning, and predicted outcomes. Approval of a proposal topic does not turn predicted outcomes into measured results.

### Literature based analysis

Use this approach only when agreed with the supervising faculty member or course instructor. State an analytical question, explain how sources were selected, compare them using meaningful technical dimensions, and develop a synthesis. The contribution should be an argued analysis, framework, comparison, or recommendation grounded in the sources. A collection of article summaries is not enough.

### Choosing section names

A research report might use Research Question, Methods, Results, and Discussion. A system report might use System Design, Implementation, Evaluation, and Limitations. A proposal might use Requirements, Proposed Design, Feasibility Analysis, and Evaluation Plan. The names may change; the distinction among what was done, what was observed, and what is expected should remain clear.


## 5 Writing and review

Write for a technically educated reader who does not know your particular project. Introduce specialized terms and expand acronyms on first use. Explain enough context for faculty outside the subfield to follow the argument while retaining the technical detail needed to assess the work. Prefer direct sentences and active voice when they clarify responsibility. First person is appropriate when it makes the contribution precise.

### Sources and figures

Use one consistent citation style, with ACM as the default. Cite prior ideas, algorithms, datasets, software, external claims, and borrowed or adapted figures where they appear. Use primary research and official technical documentation when available. Include complete reference entries and cite only sources actually used in the report. Check that every in-text citation resolves to an entry and every listed entry is cited.

Number figures and tables, refer to them in the prose, and provide captions that explain what readers should notice. Label axes and units, explain abbreviations, and make text legible at the final page size. Prefer diagrams that explain architecture or process over decorative images. Put essential reasoning and evidence in the report; repositories and appendices can provide supporting detail but should not be required to understand the contribution.

Follow the faculty member’s and course’s rules for AI assistance. If permitted, disclose its use as required and verify all facts, citations, code explanations, and analyses. You remain responsible for the report’s accuracy and for representing your contribution honestly.

### A practical drafting sequence

1. Agree on the project scope and write a short outline of the contribution and evaluation.
2. Draft the technical approach and evaluation methods while details are available.
3. Present results, then write the discussion, limitations, and conclusion.
4. Develop the introduction and related work so they frame the actual contribution.
5. Write or revise the abstract, obtain feedback, and check the final exported document.

Set dates with your faculty member for an outline, a complete draft, and the final report. Allow time to address feedback and prepare the portfolio submission. This sequence does not establish additional course deadlines.

### Student checklist

- The problem, objective, scope, and personal contribution are explicit.
- Technical choices are explained and connected to the objective and prior work.
- Evaluation methods are described, and important claims have evidence or citations.
- Implemented work, observed results, interpretations, and anticipated outcomes are distinguishable.
- Limitations explain what the report cannot establish; conclusions respect those limits.
- Figures, tables, references, and numerical claims are complete and consistent.
- Attribution, confidentiality, and permitted AI assistance are handled appropriately.
- The report follows faculty, course, and portfolio requirements; the final file is readable.

### Faculty review

Use the checklist as a shared basis for feedback. Consider whether the technical contribution is substantial for the agreed scope, the explanation permits informed assessment, the evaluation addresses the objectives, and the conclusions follow from the evidence. Identify specific gaps and the revisions needed to address them. Faculty determine assessment and acceptance; this guide does not impose a common grading rubric or require the same evaluation method for every project.


## 6 Learning from example reports

Read examples for how they explain a contribution and organize evidence. They illustrate different approaches rather than prescribing identical methods, section names, length, or formatting. Evaluate their claims critically, and follow your own applicable instructions.

### Implementation and evaluation examples

**Dream An AI Browser to Automate Sequential Web Actions with LLMs Enhancing Accessibility for Users with Disabilities** — Alexander Halpern and Ryland Birchmeier. The system section describes a Chromium-based implementation and a browser–backend separation. The methods and results sections compare manual and assisted task performance. Read it for the connection between architecture, a concrete task, and reported measures; check numerical statements against the results table.

**WahooWay An Accessible Navigation System for UVA** — Caitlin Fram, Ethan Nguyen, Karina Yakubisin, and Anissa Patel. The report moves from an accessibility need to routing and alert features, then to structured testing. Its limitations distinguish a small test area and peer participants from broader real-world use. Read it for the relationship between project scope and the boundaries of evaluation.

**Dynamic Schedule Planner Automated Workload Balancing via Syllabus and Canvas Extraction** — Chang Huang, Nathan Kim, Tapi Goredema, and Edward Cho-Jung. The report describes an ingestion pipeline and evaluates both extraction behavior and user workflows. Its limitations address document formats, participant selection, and the absence of long-term outcome evidence. Read it for evaluating separate system components and separating immediate feedback from longer-term impact.

**Reel It In** — supplied as BLUE_6__A_Gamified_Focus_Timer.pdf. The report describes focus and gameplay mechanisms, evaluates them through user tasks, and discusses the lack of long-term engagement testing. Read it for connecting implementation choices to intended user behavior and for recognizing what a brief test cannot demonstrate.

### Educational design examples

**Designing Coding Tutorials for STEM based Video Game Design Course** — Theodore Walsh. The report explains tutorial development and uses lab scores and message-board questions as evidence. Its limitations discuss incomplete visibility into student difficulties and platform dependencies. Read it for evaluating a technical educational artifact using available evidence and acknowledging alternative explanations.

**Improving Computer Science Curricula for Accessibility and Higher Engagement** — Sofia Alvarez. The report develops a curriculum from prior work, standards, resource choices, and design reasoning. Read it as an example of a design proposal and its feasibility considerations. Its proposed benefits should be distinguished from outcomes established through implementation or evaluation.

### A useful way to read any example

Identify the contribution in one sentence. Then trace one important claim from the introduction to the technical approach, evaluation, result, and limitation. If a link is missing, consider what additional information would make the claim assessable. Apply the same exercise to your own draft.

### Faculty starting statement

Faculty who wish to use this guide may give students the following direction and add any project-specific exceptions:

“Use the BSCS Senior Thesis Technical Report Guide as the default for your technical report. Follow the project-specific instructions I provide where they differ. Before drafting, we will agree on your contribution, evaluation, report length and format, feedback schedule, and submission requirements.”
