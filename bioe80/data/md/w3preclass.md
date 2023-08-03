---
title: "Week 3 Analysis & Design of Molecules & Genetic Systems"
permalink: /docs/w3preclass/
last_modified_at: 
2018: "Week 6"
---
## Analysis & Design of Molecules & Genetic Systems
Please read and consider the below before the start of each class.
The questions are study-questions and not homework to be graded.
Talk about anything you find interesting with your classmates, friends, or TAs, as you like, using Piazza or email the instructors!

## Optional On-Ramping
We recognize this is an introductory class and many may be unfamiliar with some molecular and cellular biology terms (DNA, protein, transcription, translation, etc.). Those who would like a bit of "on-ramping" to the molecular biology jargon we will be using in class from Week 3 onwards should feel free to look over.
- [Slides](https://stanford-bioe80.github.io/docs/200419_biomolecules_deck.pdf)
 from on-ramping office hours
- [Recording](https://canvas.stanford.edu/courses/115648/files/folder/Optional%20On-Ramping%20-%20Biomolecules%20-%20Audio%20Video) of on-ramping office hours

## Preclass for Monday

### Activity – Tools for seeing biology (Foldscope)

"If you want to know how nature works, (you) looked at it, carefully. Looking at it, that's the way it looks.  You don't like it? Go somewhere else, to another universe where the rules are simpler..." - Richard Feynman [source](https://www.youtube.com/watch?v=eLQ2atfqk2c&t=24m2s)

### Self-Assessment: 

Imagine that you spend hours assembling a device (a box) that, once finished, is supposed to power a light bulb when a button is pushed. You place your finished construction on your workshop table and press the button... POOF! 
Smoke pours from the device but the bulb remains dark. 

Do you exclaim (choose one):

          DARN!!! 	COOL!!!

Why did you pick your choice? Remember your answer for the class. 

### Microscopes

Microscopes are a fantastic tool for exploring the beauty of living systems.  
In week-1's reading, you encountered Van Leeuwenhoek's simple yet powerful microscope.  Since Van Leeuwenhoek's time, building microscopes - that enable us to observe living matter across various scales - have been ongoing and exciting area research. 
Microscopes are routinely used by bioengineers to test, quantify, and visualize natural and engineered organisms. For example, you, as part of BIOE.44 (Fundamentals for Engineering Biology Lab), could build a genetic circuit in *E. coli* that produces green fluorescent proteins in response to environmental toxins such as lead or arsenic. Or you can build a genetic clock (oscillator) that expresses fluorescent proteins at predefined time frequencies. For both examples, you can use a fluorescent microscope to see, quantify, and test the operation of your engineered organisms.  

*Optional reading: Nobel prize in chemistry 2014, for the development of super-resolved fluorescence microscopy [How the optical microscope became a nanoscope](https://www.nobelprize.org/uploads/2018/06/popular-chemistryprize2014.pdf), and [Scientifc Background ](https://www.nobelprize.org/uploads/2018/06/advanced-chemistryprize2014.pdf).*

*Optional reading: Nobel prize in chemistry 2017, for developing cryo-electron microscopy for the high-resolution structure determination of biomolecules in solution [They captured life in atomic detail](https://www.nobelprize.org/uploads/2018/06/popular-chemistryprize2017.pdf), and [Scientifc Background ](https://www.nobelprize.org/uploads/2018/06/advanced-chemistryprize2017.pdf)*

Despite the tremendous progress in microscopy, modern microscopes (for the most part) are expensive lab instruments that cannot easily be used or shared outside of labs. 

**Q.1. But what if you do not have access to a lab with a microscope?  
(Wouldn't it be nice to take your microscope with you wherever you go and explore the living matter?**  

**Q.2. How can we -as Bioengineers- enable all learners, explorers, and makers to have access to tools such as microscopes?**

### Foldscope

[Foldscope](https://journals.plos.org/plosone/article%3Fid=10.1371/journal.pone.0098781) is a field-deployable paper origami microscope designed and built here at Stanford by Manu Prakash and his team. 

First, spend 10' and watch the Manu's TED talk on Foldscopes, [here](https://www.ted.com/talks/manu_prakash_a_50_cent_microscope_that_folds_like_origami#t-545437)

**Q.3. According to Manu, what are the problems with modern microscopes?**

**Q.4. According to Manu, what is the relationship between hands on science education tools and global health?**

Next, familiarize yourself with the global community of Foldscope users from [Microcosmos](https://microcosmos.foldscope.com/)

**Putting your Foldscope together**

*We will do this together in class on Monday.*

If you requested the BIOE.80 Education Kit and have received your Foldscopes follow the video instructions on [Foldscope Tutorials](https://www.foldscope.com/tutorials) or the written instruction inside the Foldscope kit to assemble your microscope. You can also find additional videos on how to use your Foldscope from the website.  

If you didn't ask for a Foldscope, don't worry.  You can still complete the problem set question without one.  

Make sure to remember your answer to the Self-Assessment.  
___________________________________________________________________________________________________
## Preclass for Wednesday

### Analysis and design of molecules 

On Monday, we discussed microscopes to visualize cells and organisms. You may have also encountered (cryo-electron) microscopes that enable visualization of [biomolecules](https://www.nobelprize.org/uploads/2018/06/advanced-chemistryprize2017.pdf). Here we discuss tools that will allow computer visualization, analysis, and design of molecules. First, read this case study: 

### Celiac Disease and KumaMax

Celiac disease is an autoimmune disease of the small intestine that is triggered by eating gluten - a protein found in wheat, barley, and rye - and causes damage to the fingerlike projections lining your small intestine (villi) necessary for nutrient absorption ([Celiac Disease](https://www.mayoclinic.org/diseases-conditions/celiac-disease/symptoms-causes/syc-20352220)). 

It is estimated that 1% of the US population has celiac disease. Still, despite increasing attention in the media, almost 83% of those 3 million people remain undiagnosed (NOTE:  Beyond Celiac: What is Celiac Disease?). While misdiagnosis is common, some postulate that this lack of diagnosis (and awareness) can be linked to the limited clinical treatment offerings. Currently, the only approved therapy is adherence to a strict gluten-free diet. Avoiding gluten can be difficult when hidden sources are lurking around us (NOTE:  Medivizor: 300 facts you didn't know about gluten). Further, many who do adhere to a strict gluten-free diet do not see a recovery of the small intestinal mucosa. [source-1](https://www.beyondceliac.org/celiac-disease/what-is-celiac-disease/),[source-2](https://www.mayoclinic.org/diseases-conditions/celiac-disease/symptoms-causes/syc-20352220),[source-3](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4596973/#ref1)
,and [source-4](https://celiac.org/celiac-disease/understanding-celiac-disease-2/what-is-celiac-disease/).


Recognizing the need for a true therapy, a 2011 undergraduate [iGEM](https://igem.org/Main_Page) team from the University of Washington began to design a drug that could potentially provide relief. Six years later, that drug (KumaMax) was funded to undergo phase I clinical trials to the tune of $35 million.  

To learn more skim the following two websites:

[iGEM Startup PvP Biologics Closes a $35 Million Agreement with Pharmaceutical Company Takeda](https://synbiobeta.com/igem-startup-pvp-biologics-closes-35-million-agreement-pharmaceutical-company-takeda/) 

[UW iGEM Wiki: Gluten Destruction](http://2011.igem.org/Team:Washington/Celiacs/Background)

**Q.1. According to the team's website, why had other approaches failed?**

**Q.2. What was unique about their approach?**

**Q.3. How did they choose their starting enzyme? What key design specification made this a great choice?**

**Q.4. How did they design their enzyme? What tools did they use?**

**Q.5. How did they test their enzyme?**

**Q.6. What would you have done differently?**

(You can also read the [paper](https://pubs-acs-org.stanford.idm.oclc.org/doi/10.1021/ja3094795) that they published in 2012)

### Design Tools

KumaMax example highlights the power of tools that enables us to visualize and design molecules. These tools can be used much like any traditional computer-aided design (CAD) application. For example, you may have used Onshape (as part of BIOE.123) to create, modify, and 3D print objects. Multiple design tools are available to Bioengineers.  For example, you can design and modify biomolecules via [PyMOL](https://pymol.org/2/). [FoldIt](http://fold.it/portal/) is another example that enables all learners to interact with protein folding and advance discovery via playing a game.  There are also tools such as [Cadnano](https://cadnano.org/) simplify the process of designing three-dimensional [DNA origami](https://www.sciencedirect.com/topics/neuroscience/dna-origami).  As design tools have improved, so has our ability to (rationally) modify and create molecules.   

**Q.7. What are the roles of design and analysis tools in the engineering of biology?**

(Note: The KumaMax example highlights the utility of the Design-Build-Test Cycle (DBT), a core process used across all disciplines of engineering, for living matter.)

___________________________________________________________________________________________________
## Preclass for Friday

### Analysis and design a genetic systems

Apply parse paper tool to this paper…

[A synthetic oscillatory network of transcriptional regulators](https://www.nature.com/articles/35002125)

**Q.1.  The living cells have been engineered with a synthetic genetic system that results in an oscillating dynamical system (biomolecule levels go up and down, repeatedly, over time).  At the level of biomolecules, what is causing the oscillation to occur?**

**Q.2. what is the most important claim and main evidence in support of this claim?**

**Q.3. Looking at Figure 2, are all cells oscillation together (i.e., turning bright in synch. with one another)?  Why not?**

Next, apply parse paper tool to this paper…

[Determination of cell fate selection during phage lambda infection](https://www.pnas.org/content/105/52/20705.full)

**Q.4. what is the most important claim and main evidence in support of this claim?**

Watch this [video](https://www.youtube.com/watch?v=sLkZ9FPHJGM&feature=youtu.be)

In the movie cells infected with virus turn green… 

**Q.5. According to the authors, why do some cells infected with virus break open, releasing new progeny virus into the environment, whereas other infected cells survive?**

**Q.6. How does your answer to the preceding question change or inform your thinking about why the “repressilator” goes out of phase with itself, at the single cell level?**

Additional reading,
- [Repressilator](https://en.wikipedia.org/wiki/Repressilator), 
- [Lambda phage](https://en.wikipedia.org/wiki/Lambda_phage)

_________________________________________________________________________________________________

**Additional Resources:**

- We strongly encourage you to check out this additional resource about creativity and design in the context of modernity titled: "Art, Critique, Design and Our World" by Alexandra Daisy Ginsberg [link](https://vimeo.com/225113974)

- Video lecture: [Synthetic Biology: Principles and Applications](https://www.ibiology.org/bioengineering/introduction-to-synthetic-biology/) by Jan van der Meer.

- Video lecture: [Synthetic Biology and Biological Circuits](https://www.ibiology.org/bioengineering/biological-circuits/) by Timothy Lu.

- Video lecture: [Programming Living Bacteria](https://www.ibiology.org/bioengineering/genetic-circuits/) by Chris Voigt.

- A comprehensive video series on microscopy (includes: fundmentals, tools, and techniques) from iBiology [resources](https://www.ibiology.org/online-biology-courses/microscopy-series/microscopy-series-table-contents/) 

<sub><sup> [github source code](https://github.com/Stanford-BioE80/Stanford-BioE80.github.io/edit/master/_docs/w3preclass.md) for teaching staff <sub><sup>

