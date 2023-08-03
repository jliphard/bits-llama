---
title: "Week 8 Problem Set"
permalink: /docs/w8ps/
2018: Week 4
---

**PSET #7**

ASSIGNED: Friday 29 May 2020

DUE: Friday 05 June 2020  5:00 PM Pacific

**NOTES:**

- Given the unique circumstance of Spring 2020, we ask you to do your best to maximize your learning. Each problem set is an opportunity to assess your learning, identify gaps, reflect on what you have learned, and determine what you wish to learn next.
- You can discuss the PSET questions with other students. But your answers should be your own work. Please let us know if you collaborated with other students working on the PSET.
- Please turn in your completed problem sets as an electronic copy via Gradescope. Please make sure to clearly indicate the starting and ending boundaries of your answers to each question on Gradescope.
- Please do not go over any word limits.
- Please **type** your answers.
- Please **label** and provide descriptions for the figures.
- **Please show your work and include units.**

## (Q1) Evolution Fundamentals & Misconceptions (20 points)

True / False questions, please select the best answer.  If **False** please explain why (1-2 sentences).
Please see preclass materials for background material.

**Q.1.a.** Individual mutations occur at random (True /  False)

**Q.1.b.** Evolution of living matter is independent of the environment (True /  False)

**Q.1.c.** Selection is random and unbiased (True /  False)

**Q.1.d.** Evolution works on the scale of individuals, not on populations (True /  False)

**Q.1.e.** Engineers, including bioengineers, can use evolution to optimize human-designed systems  (True /  False)

## (Q2) Understanding the "Search Space" of Evolution (30 points)

In class, we talked about thinking of evolution as an algorithm. In this problem we will try and make some elements of this metaphor more concrete. We can think of evolution as a type of [optimization algorithm](https://en.wikipedia.org/wiki/Mathematical_optimization#Optimization_algorithms). In lecture we talked about so called "evolutionary algorithms," which are a type of optimization algorithm in the field of computer science that borrows heavily from biological evolution.

These optimization algorithms seek to find the best solution, or at least a really good one, from a set of possible choices. What is defined as "really good" depends on the particular problem being optimized, but generally engineers deal with systems where an input choice maps to an output number. The goal then becomes to maximize or minimize the output number over all possible choices. This output number could be something like a "cost of production," or an "energy consumption," or the "mass of product". For example, a manufacturing engineer may wish to maximize the number of Foldscopes that can be made with $1M. The set of all possible input choices defines a "search space" over which the evolutionary algorithm seeks to find the best set of outputs.

In biological evolution, the search space is the space of all possible genomes (the **"genotype space"**) and the output is biological fitness.

**Q.2.a.** Recall that there are 4 nucleotides / letters in the DNA alphabet (A, C, T, G). If asked to make a genome that is one base long, how many possible genomes could you make? As in, how many unique genomes of length 1 could exist? How many unique genomes of length 2 could exist? Of length 3?

Note: it may be very helpful to write out all the possible genomes by hand.

**Q.2.b.** How does the number of unique genomes grow as you increased the length of the genome? Given a genome length of _n_, how many unique genome of length _n_ could exist?

**Q.2.c.** A microbial genome is approximately _n_ ~ 10<sup>7</sup>. How many unique microbial genomes could be made of this length? We will use this number for the rest of the problem set as an approximation for the number of possible microbial genomes.

**Q.2.d.** Physicists estimate that there are 10<sup>80</sup> atoms in the known Universe ([link to popular science article describing how this number was estimated](https://www.universetoday.com/36302/atoms-in-the-universe/)). How does the number of atoms in the known Universe compare to the number of possible microbial genomes?  

Note: Use a calculator that can handle large numbers. Or use Log to compare the exponents of large numbers.  

## Question 3: Evolution vs Random Searching (35 points)
To illustrate just how powerful evolution is as an "algorithm" for optimization, let's consider the following toy system. Imagine a species with a **genome of 100 genes**. Suppose that each of these 100 genes has **one of two forms: 0 or 1**. We can describe the genome of one of these imaginary organisms as a list of a hundred 0s and 1s (e.g., "0110001...010").

In general, it is difficult or impossible to quantitatively predict the fitness of an organism from the organism's *genotype*. This is because the fitness of an organism depends only indirectly on genotype. Fitness depends directly on how the organism looks and acts (its *phenotype*) in the context of a given *environment*, which is difficult to predict. In order to avoid some of these complications, let's make our toy system have the following properties:
- the total population of our system remains constant throughout (e.g., if 4 organisms die, 4 new ones will be born)
- the 1 form of each gene is more fit than the 0 form of the same gene
- genes can only change form by "mutation"; a gene in the 0 form mutates to 1 form and vice versa
- each time an organism reproduces, it's offspring will have a random mutation in exactly one of its genes (e.g., an organism with genome "010" may give rise to an offspring with genome "110", "000", or "011" with equal probability)
- the fitness of a given organism is equal to the number of genes in its genome in the 1 form (e.g., an organism with genome "011" has a fitness of 2)

Suppose that we wish find the most fit genome "111...111" in the space of all genomes, but we don't know ahead of time which genome is the most fit. That is to say, we don't know that the 1 form is more fit than the 0 form.

**3.a.** Let's first try and guess how long it will take to find the most fit genome by randomly searching the space of all genomes. How big is the space of possible genomes of 100 genes if each gene has 2 forms?

HINT: this problem uses the same math you used for Question 2a and 2b. Instead of considering n nucleotides (of which there are 4 types), we are considering 100 genes (of which there are 2 types)

**3.b.** Let's now try and get a better sense of how long it takes evolution to find the fittest genome in our toy system. Check out [this cloud notebook](https://colab.research.google.com/drive/1w57b1R19w49yTg4b9Gat8v9ygWNjdxhm?usp=sharing), which simulates the evolution of a population of ten thousand (1e4) organisms in our toy system. To run this notebook, go to the toolbar at the top of the page and click Runtime > Run all.

How many generations does it take for our simulated population to evolve a genome of fitness 100? How many genome-generations does it take? How does the size of the genome space (from 3.a) compare to the number of genome generations it took for our simulation to find the most fit genome?

HINT: genome-generations is a unit that combines the number of individuals in a population and the number of generations over which that population evolves. You can derive the number of genome-generations by multiplying the number of genomes and the number of generations (e.g., a population of 10 individuals over 4 generations represent 40 genome-generations)

**3.c.** Let's try and see how sensitive our evolving system is to the parameters we chose for our simulation. We may have just gotten lucky! First, let's try changing the size of our population, which is represented by the parameter named "NUM_GENOMES".

Repeat the simulation using a population size of one thousand (1e3) individuals. Run the simulation by clicking Runtime > Run all, otherwise the code will run using the default parameters instead of the updated ones. Does this simulation to converge to a genome of fitness 100? If so, how many genome-generations does it take?

Repeat the simulation again using a population size of one hundred thousand (1e5) individuals. Does this simulation to converge to a genome of fitness 100? If so, how many genome-generations does it take? Given the answers you got in this problem, how sensitive is our model to the population size?

**3.d.** Now, let's try and change the strength of selection that we impose on our system, which is represented by the parameter named "SELECTION". SELECTION represents the percentage of the population that dies within each generation and is replaced by newborn individuals. With SELECTION = 0.5, which is the default setting we've used thusfar, half of the population is replaced every generation!

Repeat the simulation using a population size of ten thousand (1e4) individuals, like we did in 3.b, but set the selective pressure to 0.2. Does this simulation to converge to a genome of fitness 100? If so, how many genome-generations does it take?

Repeat the simulation using a population size of ten thousand (1e4) individuals and a selective pressure of 0.9. Does this simulation to converge to a genome of fitness 100? If so, how many genome-generations does it take? Given the answers you got in this problem, how sensitive is our model to the selective pressure?

EXTRA INFORMATION: In making our toy system, we made some implicit assumptions in order for the properties listed above to hold. Below, we highlight some of these assumptions.
- the fitness that any given gene contributes to the organism is only determined by the form of that gene (there is no [epistasis](https://en.wikipedia.org/wiki/Epistasis) in this system)
- the fitness of one organism does not affect the fitness of any other organism (there is no [density dependence](https://en.wikipedia.org/wiki/Density_dependence) or [frequency dependence](https://en.wikipedia.org/wiki/Frequency-dependent_selection))
- the organisms reproduce asexually and cannot perform [recombination](https://en.wikipedia.org/wiki/Genetic_recombination)
- the Environment does not change over time
In general, these assumptions do not apply. However, scientists have made great headway in describing evolution using simple models that make some or all of these assumptions.

## (Q4) Paper reading activity (15 points)

Read the following paper, [Fail-safe genetic codes designed to intrinsically contain engineered organisms](https://academic.oup.com/nar/article/47/19/10439/5568210)

**Q.4.a** In your own words, what is the primary claim of the paper? What are the primary evidence in support of the claim? (2-3 Bullet points)

**Q.4.b** What are the paper’s strengths and significance? What are the paper’s shortcomings and deficiencies?  (Bullet points)? How can the paper improve? (3-4 Bullet points)


Read the following pre-print, [Content-based similarity search in large-scale DNA data storage systems](https://www.biorxiv.org/content/10.1101/2020.05.25.115477v1.full.pdf+html)

**Q.4.c** In your own words, what is the primary claim of the paper? What are the primary evidence in support of the claim? (2-3 Bullet points)

**Q.4.d** What are the paper’s strengths and significance? What are the paper’s shortcomings and deficiencies?  (Bullet points)? How can the paper improve? (3-4 Bullet points)

## Extra Credit - Design and solve a question (20 points)

Design your own BIOE\ENGR 80 question based on any of the material that we have covered so far in the class.  A student successfully finishing BIOE\ENGR 80 should be able to answer your question.  

- Start by thinking about your learning goals.  What do you expect the learners to gain after engaging your question?

- Next, provide your question. Your questions can have multiple parts.  Make sure to include references if you draw inspiration from a source.
- Finally, provide an answer to the question. (Optional: you can also include potential mistakes and misunderstandings.)

<sub><sup> [github source code](https://github.com/Stanford-BioE80/Stanford-BioE80.github.io/edit/master/_docs/w8ps.md) for teaching staff <sub><sup>
