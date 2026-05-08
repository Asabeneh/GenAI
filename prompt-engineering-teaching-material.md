# Prompt Engineering 
## 0) How to Use This Material

This is designed as a full module you can use in three ways:

- **Self-study**: Work section by section and complete all exercises.
- **Facilitated workshop**: Deliver as a 2-4 hour session.
- **Team training pack**: Use templates, rubrics, and capstone tasks for ongoing practice.

### Estimated Duration

- Core lesson: 90 minutes
- Guided practice: 45 minutes
- Capstone project: 45-60 minutes
- Total: 3 hours (recommended)

### Prerequisites

- None. Suitable for a generic audience (students, professionals, creators, and beginners).

---

## 1) Learning Outcomes

By the end of this module, learners will be able to:

1. Explain prompt engineering and why it matters.
2. Diagnose weak prompts and improve them systematically.
3. Use multiple prompting patterns (instructional, few-shot, rubric-driven, and iterative).
4. Build prompts for real-world tasks across learning, work, business, and creativity.
5. Evaluate AI output quality using a practical scoring rubric.
6. Run an end-to-end prompt workflow: define objective -> craft prompt -> evaluate -> iterate.

---

## 2) What Prompt Engineering Really Is

Prompt engineering is the discipline of designing inputs that reliably produce useful outputs from AI systems.

It is not about secret words. It is about:

- Clear goals
- Clear constraints
- Clear context
- Clear evaluation criteria

### Mental Model

Treat the AI like a highly capable but literal collaborator:

- It can reason over what you provide.
- It cannot reliably infer what you forgot to specify.
- It performs best when requirements are explicit and structured.

### Why This Skill Matters

Prompt engineering improves:

- **Quality**: More accurate and relevant responses
- **Speed**: Fewer retries, faster completion
- **Consistency**: Repeatable outputs across users and teams
- **Control**: Better formatting, tone, and scope

---

## 3) Prompt Anatomy: The RTFCC Framework

Use this framework as your default:

1. **R - Role**: Who the AI should act as
2. **T - Task**: The specific job to do
3. **F - Facts/Context**: Domain background and input data
4. **C - Constraints**: Limits, tone, audience, exclusions
5. **C - Criteria/Output Contract**: What "good" looks like and output format

### Base Template

```text
You are a [role].
Task: [clear objective].
Context:
- [fact 1]
- [fact 2]
- [fact 3]
Constraints:
- [tone/length/reading level]
- [must include]
- [must avoid]
Output contract:
- [format]
- [sections]
- [quality criteria]
If needed, ask [N] clarifying questions before answering.
```

### Filled Example (Ready to Reuse)

```text
You are a study coach for beginners.
Task: Create a 7-day study plan to help me prepare for an introductory biology exam.
Context:
- I am a first-year university student.
- I have 2 hours per day available.
- My weak areas are cell division and genetics.
Constraints:
- Use simple, non-technical language.
- Include short daily revision and quiz tasks.
- Do not suggest more than 2 hours of work per day.
Output contract:
- Format: day-by-day plan
- Sections: daily goal, topics, 2 activities, and quick self-check
- Quality criteria: realistic workload, clear progression, and practical actions
If needed, ask 3 clarifying questions before answering.
```

### Why "Output Contract" Is Powerful

An output contract converts vague expectations into measurable requirements.
Example:

- Vague: "Give me a good summary."
- Structured (Improved): "Provide a 120-word summary, 5 bullet key points, 3 risks, and 2 next actions."

---

## 4) Levels of Prompt Quality

### Level 1: Request

```text
Write about remote work.
```

Problem: vague task, no audience, no structure, no constraints.

### Level 2: Directed Request

```text
Write a short explanation of remote work benefits and challenges.
```

Better, but still under-specified.

### Level 3: Structured Prompt

```text
You are an HR advisor.
Explain remote work to new managers.
Include 4 benefits, 4 challenges, and 5 practical policies.
Keep it under 350 words in simple language.
Output as headings + bullet points.
```

Clear and usable.

### Level 4: Production-Ready Prompt

```text
You are an HR advisor with policy-writing experience.
Task: Draft a manager guide for hybrid work onboarding.
Context:
- Company size: 80 employees
- Teams: engineering, sales, support
- Current issue: inconsistent work-from-home expectations
Constraints:
- Audience: first-time managers
- Tone: practical and supportive
- Length: 450-550 words
- Avoid legal claims and country-specific legal advice
Output contract:
- Section 1: Policy principles (5 bullets)
- Section 2: Team agreement template (checklist)
- Section 3: First 30-day rollout plan (week-by-week)
- Section 4: 3 risks and mitigations
Before drafting, ask 3 clarifying questions about local policies and team schedules.
```

---

## 5) Prompting Patterns You Should Know

## Pattern A: Direct Instruction

Best for straightforward tasks.

```text
Generate 10 customer service email subject lines for delayed delivery notices.
Tone: empathetic and professional.
Max 8 words each.
```

## Pattern B: Role + Audience Alignment

Best when tone and depth depend on audience.

```text
You are a cybersecurity trainer.
Explain phishing to office staff with no technical background.
Use everyday examples and a 5-item safety checklist.
```

## Pattern C: Few-Shot Prompting (Learning from Examples)

Best for style consistency.

```text
Convert informal sentences into professional tone.

Example 1:
Input: "Can you send this fast?"
Output: "Could you please prioritize sending this at your earliest convenience?"

Example 2:
Input: "This report is late."
Output: "The report timeline has slipped; please share an updated delivery date."

Now transform:
Input: "We need this now."
Output:
```

## Pattern D: Critique-and-Revise Loop

Best for quality improvement.

```text
Draft a project update email.
Then self-critique for clarity, tone, and actionability.
Revise once based on your critique.
```

## Pattern E: Ask-Then-Answer

Best when requirements are unclear.

```text
Before answering, ask me 5 clarifying questions.
Only after I answer, produce the final plan.
```

## Pattern F: Rubric-Guided Generation

Best for reliable quality.

```text
Write a training summary and score it from 1-5 on:
1) Accuracy
2) Clarity
3) Completeness
4) Actionability
If any score is below 4, revise.
```

Example

```
Role: Act as an expert Corporate Trainer and Technical Writer.

Task: Please write a concise training summary regarding [INSERT TOPIC, e.g., Phishing Awareness] for office staff with no technical background.

Rubric: After drafting the content, evaluate your own work on a scale of 1-5 based on these criteria:

Accuracy: Does it align with standard security best practices?  

Clarity: Is it written in plain English, avoiding complex technical jargon?  

Completeness: Does it include a clear definition, examples, and a checklist?  

Actionability: Can an employee immediately apply this to their daily workflow?  

Instructions for Revision:

If any category scores below a 4, you must identify the weakness and rewrite the summary to improve it.  

Present your final output in this order:

The Final Polished Summary.

A brief table showing your self-evaluation scores.

A one-sentence explanation of any improvements made during the revision process.

```

---

## 6) Advanced Prompt Design Principles

### 6.1 Specify the Decision Context

Outputs improve when the model knows where the answer will be used.

Bad:

```text
Suggest marketing ideas.
```

Better:

```text
Suggest marketing ideas for a small local bakery launching weekend breakfast boxes.
Budget: low.
Audience: nearby working professionals and parents.
Goal: increase Saturday pre-orders by 20% in 2 months.
```

### 6.2 Separate Facts from Instructions

Keep user-provided facts cleanly separated from instructions to avoid confusion.

### 6.3 Constrain Scope

If the AI returns broad or generic output, scope it by:

- geography
- user segment
- timeframe
- budget
- objective metric

### 6.4 Request Verification Behavior

For uncertain tasks:

```text
If you are uncertain, state assumptions explicitly.
Do not invent specific statistics.
```

### 6.5 Force Structured Output

If output must be reused downstream, request JSON, tables, or fixed headings.

---

## 7) Real-World Use Cases with Deep Examples

## Use Case 1: Learning Complex Topics

### Goal

Understand unfamiliar content quickly and retain it.

### Prompt

```text
You are a learning strategist and tutor.
Task: Teach me the concept of opportunity cost.
Context:
- I am a beginner in economics.
- I learn best with analogies and examples.
Constraints:
- Use plain language.
- Max 300 words.
- Avoid formulas unless essential.
Output contract:
- Part A: 1-paragraph explanation
- Part B: 2 everyday analogies
- Part C: 5-question mini quiz with answers
- Part D: one practical exercise I can do today
```

### Why This Works

- Matches explanation style to learner needs
- Includes retrieval practice (quiz)
- Ends with behavior-focused action

---

## Use Case 2: Professional Email Writing

### Goal

Draft sensitive communication clearly and diplomatically.

### Prompt

```text
You are a communications advisor.
Task: Draft an email to a vendor who missed two milestones.
Context:
- We want to keep the relationship.
- Delay impacts a client launch date.
Constraints:
- Tone: firm but respectful
- Length: 140-180 words
- Avoid blame language
Output contract:
- Subject line
- Email body
- 3 optional closing lines with different tones
```

### Extension

Ask for alternatives:

```text
Provide 3 versions: conservative, neutral, and assertive.
```

---

## Use Case 3: Job Search and CV Improvement

### Goal

Tailor applications for specific roles.

### Prompt

```text
You are a career coach and recruiter.
Task: Improve my CV summary for a junior data analyst role.
Context:
- Background: economics graduate
- Experience: internship in operations
- Skills: Excel, SQL basics, dashboard reporting
Constraints:
- Keep summary 90-110 words
- Emphasize measurable outcomes
- Keep language truthful and realistic
Output contract:
- Version 1: formal
- Version 2: modern concise
- 6 bullet improvements for my full CV
```

---

## Use Case 4: Small Business Planning

### Goal

Turn a rough business idea into actionable steps.

### Prompt

```text
You are a small business advisor.
Task: Build a 30-day launch plan for a home-based fresh juice service.
Context:
- Target market: office workers in one neighborhood
- Starting budget: $400
- Capacity: one person operation
Constraints:
- Prioritize low-cost actions
- Include risk controls for hygiene and delivery delays
Output contract:
- Week-by-week plan
- Budget allocation table
- Top 5 risks and mitigations
- Daily KPI checklist
Before answering, ask 4 clarifying questions.
```

---

## Use Case 5: Content Creation

### Goal

Maintain style consistency and usefulness.

### Prompt

```text
You are a content strategist.
Task: Create a 2-week LinkedIn content calendar for a personal finance educator.
Context:
- Audience: early-career professionals
- Objective: build trust and newsletter signups
Constraints:
- 5 posts per week
- Mix of educational, story-based, and actionable posts
- Keep each post idea under 35 words
Output contract:
- Table with columns: Day, Post Hook, Format, CTA, Topic Goal
```

---

## 8) Prompt Evaluation Rubric (Scoring Guide)

Use this rubric to evaluate any AI output from 1 (poor) to 5 (excellent).

### Criteria

1. **Task Alignment**: Does it answer the exact request?
2. **Accuracy**: Is information plausible and non-fabricated?
3. **Completeness**: Are required components included?
4. **Clarity**: Is it easy to understand?
5. **Actionability**: Can the learner/user do something with it immediately?
6. **Format Compliance**: Did it follow the requested structure?

### Interpretation

- 26-30: production-ready
- 20-25: useful with minor edits
- 14-19: partially useful, needs rewrite
- <=13: reprompt from scratch

### Evaluation Prompt

```text
Evaluate the previous answer using this 6-criteria rubric (1-5 each).
Return:
1) table of scores,
2) top 3 weaknesses,
3) revised version that fixes them.
```

---

## 9) Common Failure Modes and Fixes

## Failure Mode A: Generic Output

Cause: task too broad.  
Fix: add audience, goal, and constraints.

## Failure Mode B: Wrong Tone

Cause: tone not specified.  
Fix: define tone and include do/don't examples.

## Failure Mode C: Missing Sections

Cause: no output contract.  
Fix: specify required sections explicitly.

## Failure Mode D: Hallucinated Facts

Cause: asks for unavailable specifics.  
Fix: require assumptions and uncertainty statements.

## Failure Mode E: Verbose, Unfocused Responses

Cause: no length bound.  
Fix: add max words and expected structure.

---

## 10) Iterative Prompt Workflow (Professional Practice)

### Step 1: Define Success

Write one sentence:
"A successful output will help me _**by**_."

### Step 2: Draft Prompt v1

Use RTFCC.

### Step 3: Run and Evaluate

Score with rubric.

### Step 4: Diagnose Gaps

Identify one of:

- task mismatch
- missing context
- weak constraints
- weak format contract

### Step 5: Revise to v2

Only change 1-2 variables at a time so you can learn cause and effect.

### Step 6: Save Reusable Prompt

Store final prompt as a team template.

---

## 11) Teaching Plan (For Instructors)

### Session Flow (3 Hours)

1. **Concept Lecture (35 min)**  
   Foundations, frameworks, patterns, and examples.
2. **Live Demonstration (20 min)**  
   Weak -> strong prompt transformation.
3. **Guided Practice (35 min)**  
   Learners do mini tasks in pairs.
4. **Break (10 min)**
5. **Use-Case Labs (35 min)**  
   Different domains: education, business, productivity.
6. **Capstone Challenge (35 min)**  
   End-to-end prompt design and peer review.
7. **Debrief (10 min)**  
   Lessons learned and next practice plan.

### Materials Needed

- This module
- Any AI assistant tool
- Rubric sheet (included in section 8)
- Peer feedback form (simple: strengths, gaps, improvements)

---

## 12) Mini Tasks (Short Drills)

## Task 1: Prompt Diagnosis

Given prompt:

```text
Help me market my product.
```

Identify at least 5 missing elements and rewrite.

## Task 2: Audience Shift

Write two prompts for the same topic ("cybersecurity basics"):

- version A for children (age 12)
- version B for executives

## Task 3: Format Control

Prompt topic: "how to prepare for an interview."  
Request output in:

- checklist
- 7-day plan
- FAQ format

## Task 4: Clarification Gate

Write a prompt that forces the AI to ask questions before drafting:

- a business proposal
- a trip plan

## Task 5: Reliability Guardrails

Rewrite a prompt to include:

- "state assumptions"
- "don't invent data"
- "mark uncertain claims clearly"

---

## 13) Scenario-Based Exercises (Medium Difficulty)

## Exercise A: Student Support

### Brief

A student struggles with exam anxiety and poor study structure.

### Task

Design a prompt that outputs:

- 14-day study plan
- daily focus blocks
- stress management strategy
- progress tracker table

### Constraint

Must be realistic for someone with 2 hours/day.

---

## Exercise B: Team Productivity

### Brief

A small team has unclear meeting outcomes.

### Task

Design a prompt that creates:

- meeting agenda template
- decision log format
- action item tracker with owners and due dates

### Constraint

Output should fit one page and be immediately usable.

---

## Exercise C: Freelance Business Growth

### Brief

A freelancer wants more clients in 60 days.

### Task

Design a prompt to generate:

- positioning statement
- outreach strategy
- weekly KPI dashboard
- risk register

### Constraint

Budget under $150.

---

## 14) Capstone Project (End-to-End)

## Capstone Objective

Create one production-ready prompt system for a real use case you care about.

### Required Deliverables

1. Problem statement (max 120 words)
2. Prompt v1
3. Output sample
4. Rubric scoring
5. Prompt v2 (improved)
6. Reflection: what changed and why (max 150 words)

### Capstone Evaluation (100 points)

- Problem clarity (15)
- Prompt structure quality (25)
- Output usefulness (20)
- Iteration quality (20)
- Reflection depth (10)
- Format discipline (10)

---

## 15) Answer Key (Selected Examples)

## Example Answer for Task 1 (Diagnosis + Rewrite)

```text
You are a growth marketer for small businesses.
Task: Create a 4-week marketing plan for my handmade soap brand.
Context:
- Business age: 6 months
- Current sales channel: Instagram and word of mouth
- Monthly budget: $120
Constraints:
- Focus on low-cost, high-impact actions
- Audience: women and men aged 20-40 interested in natural products
- Avoid paid ads above $3/day
Output contract:
- Week-by-week action plan
- Daily content ideas (3 per week)
- KPI table with target metrics
- Top 5 risks and mitigation actions
```

## Example Answer for Task 3 (Format Control)

```text
You are a career coach.
Teach interview preparation for entry-level candidates.
Output in three parts:
1) 15-item checklist
2) 7-day preparation plan
3) FAQ with 8 common interview questions and model answer strategy
Keep language concise and practical.
```

---

## 16) One-Page Prompt Cheat Sheet

```text
[ROLE]
You are a [specific role].

[TASK]
Do [specific objective] for [specific audience].

[CONTEXT]
- Situation:
- Inputs/data:
- Constraints of environment (time, budget, tools):

[CONSTRAINTS]
- Tone/style:
- Length:
- Must include:
- Must avoid:

[OUTPUT CONTRACT]
- Format:
- Required sections:
- Quality criteria:

[SAFETY/RELIABILITY]
- State assumptions.
- Mark uncertainty.
- Do not fabricate specific data.

[INTERACTION RULE]
Ask [N] clarifying questions first when requirements are unclear.
```

---

## 17) Final Notes

Prompt engineering is an applied thinking skill.  
Your results improve when you:

- define success before prompting,
- structure instructions carefully,
- evaluate output with a rubric,
- iterate deliberately.

If learners complete all drills and capstone activities in this module, they will have practical, transferable prompt engineering ability for everyday and professional use.
