# Loops and Orbits &mdash; README.md

* [Syllabus (with References)](http://physics.stmarys-ca.edu/faculty/brianhill/courses/Jan033/20J/index.html) (on physics.stmarys-ca.edu)
* [Weekly Schedule](#weekly-schedule)
* [Daily Schedule](#daily-schedule)
  * [Week 1 Daily Schedule](#week-1-daily-schedule)
  * [Week 2 Daily Schedule](#week-2-daily-schedule)
  * [Week 3 Daily Schedule](#week-3-daily-schedule)
  * [Week 4 Daily Schedule](#week-4-daily-schedule)

## Weekly Schedule

### Week 1

* Physics &amp; Math: The Description of Motions of Objects in 1-D including Coordinates, Units, Speed, Velocity, and Acceleration.
* Computer Science: Jupyter Notebooks. Documentation in Markdown. Elements of Python including Expressions, Statements, Variables and Assignments, Types (Lists, Tuples, and Ranges), Control Flow (While and For loops), and introducing Functions.

### Week 2

* Physics &amp; Math: The Description of Motions of Objects in 2-D. Projectile Motion. Circular Motion. Two-Dimensional Acceleration.
* Computer Science: Continue Discussion of Functions, Scope and Lifetime of Variables. Packages. Objects. Methods. Graphics. Version Control.

### Week 3

* Physics &amp; Math: The Problem of Motion in Two-Dimensions in Newton's Universal Theory of Gravitation (Circular and Elliptical Orbits).
* Applications: Selection and Formulation of Final Project.
* Computer Science: Testing. Capturing Input from Files or from Users.
	
### Week 4

* Physics &amp; Math: Rockets Burns.
* Applications: Implementation and Presentation of Final Project.
* Computer Science: Display of Program Output.

## Daily Schedule

### Week 1 Daily Schedule

#### Week 1 Physics &amp; Math

* [Physics and Math Notes 1-1](./physics_and_math/lao-1-1-pm.pdf): Speed. Velocity. Definitiions. Coordinates. Units of Position and Velocity. Velocity from Position.
* [Physics and Math Notes 1-2](./physics_and_math/lao-1-2-pm.pdf): Position from Velocity. Indices. Summations. Relationship to Derivatives and Integrals.
* [Physics and Math Notes 1-3](./physics_and_math/lao-1-3-pm.pdf): Physics Laws. Acceleration. Newton's Three Laws. Units of Acceleration. Constant Acceleration.
* [Physics and Math Notes 1-4](./physics_and_math/lao-1-4-pm.pdf): Air Glider on Spring Demonstration. Amplitude. Period. Frequency. Spring Constant. Mass. Sign of Acceleration. Comparing Position, Velocity, and Acceleration Graphs. Adding Damping to Air Glider. Adding Wind Resistance to Drag Racer.

#### Week 1 Worksheets and Homework

* [Worksheet 1 (2020-01-06)](./worksheets/lao-1-1-ws1.pdf): Velocity from Position (Lionel Messi Run).
* [Worksheet 2 (2020-01-07)](./worksheets/lao-1-2-ws2.pdf): Position from Velocity (Lionel Messi Run).
* [Worksheet 3 (2020-01-09)](./worksheets/lao-1-3-ws3.pdf): Steady Acceleration with Graphs (Drag Racer).
* [Homework 1 (2020-01-10)](./homework/lao-hw1.pdf): Adding Damping to the Air Glider. Adding Wind Resistance to the Drag Racer.
	
#### Week 1 Computer Science

* [Computer Science Notes 1-1](./computer_science/lao-1-1-cs.pdf): Markdown. Statements. Expressions. Variables and Assignments. Types.
* [Computer Science Notes 1-2](./computer_science/lao-1-2-cs.pdf): Comparisons. While Loops. Lists. Lists vs. Arrays.
* [Computer Science Notes 1-3](./computer_science/lao-1-3-cs.pdf): Tuples. Unpacking Tuples. Ranges. For Loops. Compare and Contrast Lists, Tuples, and Ranges.
* [Computer Science Notes 1-4](./computer_science/lao-1-4-cs.pdf): Introduce Function Definitions (Power-of-Two Implementation), Function Usage (Call Sites), Scope of Variables. Lifetime of Variables. Pass-by-Value Example (Alternate Power-of-Two Implementation). Pass-by-Reference Example (Add-to-Roster).<sup>[1](#footnote1)</sup>

#### Week 1 Python Coding Lab

* Jupyter [Notebook 1-1](https://mybinder.org/v2/gh/observatree/loops-and-orbits/master?filepath=notebooks%2Flao-1-1.ipynb) (online version &mdash; uses Binder)
* Jupyter [Notebook 1-2](https://mybinder.org/v2/gh/observatree/loops-and-orbits/master?filepath=notebooks%2Flao-1-2.ipynb): Lionel Messi Run (online version &mdash; uses Binder)
* Jupyter [Notebook 1-3](https://mybinder.org/v2/gh/observatree/loops-and-orbits/master?filepath=notebooks%2Flao-1-3.ipynb): Drag Racer (online version &mdash; uses Binder)
* Jupyter [Notebook 1-4](https://mybinder.org/v2/gh/observatree/loops-and-orbits/master?filepath=notebooks%2Flao-1-4.ipynb): Air Glider on Spring (online version &mdash; uses Binder)
	
### Week 2 Daily Schedule

#### Week 2 Physics &amp; Math

#### Week 2 Worksheets and Homework
	
#### Week 2 Computer Science

* [Computer Science Notes 2-1](./computer_science/lao-2-1-cs.pdf): Using Jupyter on the lab iMacs.

#### Week 2 Python Coding Lab
	
* Jupyter [Notebook 2-1](https://github.com/observatree/loops-and-orbits/blob/master/notebooks/lao-2-1.ipynb): Knocking it out of the Park (download to your machine per these notes [Computer Science Notes 2-1](./computer_science/lao-2-1-cs.pdf))

### Week 3 Daily Schedule

#### Week 3 Physics &amp; Math

#### Week 3 Worksheets and Homework
	
#### Week 3 Computer Science

#### Week 3 Python Coding Lab

### Week 4 Daily Schedule

#### Week 4 Physics &amp; Math

#### Week 4 Worksheets and Homework
	
#### Week 4 Computer Science

#### Week 4 Python Coding Lab

### Footnotes

<a name="footnote1">1</a>: For students who had an easy time accepting the pass-by-value and pass-by-reference rules, here is a good-quality and patient explanation of how those somewhat contradictory rules are actually highly compatible: [Is Python pass-by-reference or pass-by-value?](https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/) The bottom line is Python is indeed pass-by-value, but a list is an object &mdash; we haven't learned about objects yet! &mdash; and for objects the variable and the function argument are references to the object, not the object itself. This means that the function body gets a copy of the reference to the list, and the copy of the reference still refers to the original list.
