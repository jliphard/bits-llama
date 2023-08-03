---
title: "Week 4 Preclass"
last_modified_at: Feb.20.2019
toc: true
---
## Engineering Abstraction in Biology

Please read and consider the below before the start of each class. The questions are study-questions and not homework to be graded. Talk about anything you find interesting with your classmates, friends, or TAs, as you like, using Piazza or email the instructors!

**Goal-1:** You will able to describe the role of abstraction as a tool for helping 
to manage complexity in biological systems.

**Goal-2:** You will also be able to apply abstraction (in the form of black box diagrams) to decompose 
or synthesize the designs systems that could then be implemented in living matter for example viaengineered 
(i.e., designer) DNA.

(Study note: previous BIOE/ENGR.80 students described Engineering Abstraction in Biology as challenging and time-consuming material.)

## Preclass for Monday

### Engineering abstraction in living matter – synthetic genetic logic

Read the first two parts from the following comic [Adventures in Synthetic Biology](http://web.mit.edu/endy/www/scraps/comic/AiSB.vol1.pdf) (**Programming DNA** and **Engineered Genetic Devices**)  where key ideas in designing and realizing biological circuits and systems are discussed
(Same comic book in other [languages](https://openwetware.org/wiki/Adventures))

Biology background, particularly  [Information Transfer in Cells](https://www.nature.com/scitable/ebooks/cntNm-14749010/122996756/) and [Regulation of Transcription and Translation](https://www.nature.com/scitable/ebooks/cntNm-14749010/122996928/) may help you have a richer understanding of the topic discussed in the comic. 

According to the comic,

**Q.1  what is a genetic device? for example, what is an inverter device?** 

**Q.2  What is the utility of using the Device abstraction to describe the DNA inverter?**

Next, briefly study the abstract and figures 1-3 from [Amplifying Genetic Logic Gates](https://science.sciencemag.org/content/340/6132/599/tab-pdf) (Alternative [link](https://science.sciencemag.org/content/340/6132/599.long)).

**Q.3  What is a the main claim of the paper?** 

**Q.4  What logic-gate devices were demonstrated in this paper?  How were the performances (and digital output) measured?**

Optional video-1 [Transcriptors & Boolean Integrase Logic (BIL) gates, explained](https://www.youtube.com/watch?v=ahYZBeP_r5U&t)

Next, read the following NYtimes article, [Taking Faster and Smarter to New Physical Frontiers](https://www.nytimes.com/2011/12/06/science/drew-endy-better-computing-for-the-things-we-care-about-most.html)

**Q.5 How can we better define and measure the intrinsic worth of computation?**

Extra resources:

- Khan Academy, [Central Dogma](https://www.khanacademy.org/science/biology/gene-expression-central-dogma)
- Bruce Alberts Molecular Biology of the Cell (2015)- Central Dogma  [Chapter 6](https://www.ncbi.nlm.nih.gov/books/NBK21054/) 
- Claude Shannon, [A symbolic analysis of relay and switching circuits](https://dspace.mit.edu/handle/1721.1/11173)
- [Principles of genetic circuit design](https://www.nature.com/articles/nmeth.2926)
- [Foundations for engineering biology](https://www.nature.com/articles/nature04342)

_______________________________________________

## Preclass for Wednesday

### Engineering abstraction in living matter – generic system architecture

Read the (**Common Signal Carriers**) part from this free comic book [Adventures in Synthetic Biology](https://openwetware.org/wiki/Adventures) before the class. 

**Q.1  What is the advantage of using a  common signal carrier to construct a system out of devices?  Specifically what common signal carrier is used in the comic?**

#### Bacterial Flash Mob

**Write down the DNA sequence** encoding a dynamic bacterial flash mob (see animation below in Figure.1 )

<figure>
<a href="/assets/images/w3_IEcolibratorMovie.gif"><img src="/assets/images/w3_IEcolibratorMovie.gif"></a>
</figure> 

**Figure-1** Bacterial flash mob. Credit to MIT students 2004: Polkadorks. 

**Q.2. What is the first base of your DNA program?  A, T, C, or G?  
(Hint: Do not spend more than 100 seconds pondering and answering this question.  Time’s up!).**  

*Figure 1.  Dynamic bacterial flash mob.* 
A collection of engineered bacteria (black dots)move randomly in two dimensions.One cell activates randomly, turns red, and secretes a diffusing attractant molecule (green circle). All other cells sense and move towards the source of the attractant.After a period of time all cells return to their original stateuntil the process repeats over and again.

**Q.3. Why is Q1 a difficult question to answer?**   
(Hint: Consider the difference between what you do and what must physically occur to use a smartphone to take a photograph and send an image to your best friend via text message.  Are you ever typing 0s and 1s into your phone?  What’s happening instead?)

One simple-but-powerful and general-purpose approach for organizing engineered systems is shown in figure-1.  For example, a computer has a keyboard that receives input via keys (sensors), performs logical operations (computation), and can output via a display, printer or other device (actuation).  As a second example, a pilot can control a Boeing 787 airplane by moving the yoke, whose inputs are combined with other inputs collected by additional sensors (e.g., air pressure), and then a flight computer determines what the actuated flight surfaces on the wings and tail physically do, as controlled by a “fly-by-wire” system.

Note that our thinking about such systems can quickly become complicated by the details of any one example, but that each example follows a similar pattern; inputs are received by one or more sensors; so-received information is computed upon as needed via an intermediate process; and finally some action is taken.  Please also note that in more complicated systems the output of a system can itself be an input, creating a “loop” or feedback to realize more sophisticated dynamics(e.g., repeating or other dynamically controlled behaviors, such as in the case of the looping bacterial flash mob).

<figure>
<a href="/assets/images/generic system arch.png"><img src="/assets/images/generic system arch.png"></a>
<figcaption><b>Figure 2</b>. Generic system architecture.</figcaption>
</figure>

A sensor measures environmental properties or inputs  (for example: a keyboard) and transfers this information to a computer (logic unit) to be processed. The results are then transferred to an actuator (e.g., a printer or a display) that can output these results.

This same framework can be applied to help manage the engineering of biological systems. Stated differently, the desired behavior of a complicated biological process can be represented at an intermediate level of abstraction via a simpler-to-understand  “Black box” diagram.

**Q.4. Revisit to the bacterial flash mob and develop a device-level block diagram that would result in the so-shownbehavior.  Label simple sensors, logic blocks, and actuators, as needed.  Connect outputs to inputs (i.e., connectboxes together via ines) where and as required.**  
(Hint: Only give simple device names (e.g., “coin flip,” “turn red,” etc.);do not describe any biology in any molecular detail).

**Key Concept:** What we are practicing via this generic system architecture is called **abstraction**. 
Abstraction is a tool that allows engineers (and others) to modularize and manage the complexity of a system. Abstraction establishes a level of simplicity at which a person interacts with the system, temporarily hiding more complex details for later consideration, only if and as such details must be considered.  

But, returning to the Bacterial Flash Mob example.

Now that you have thought about the above questions check out from [Here](https://2006.igem.org/wiki/index.php/IAP2004:Polkadorks)  MIT students solution. 

<figure>
<a href="/assets/images/w6pc_the laws of thought.png"><img src="/assets/images/w6pc_the laws of thought.png"></a>
</figure>

From a different perspective, note how George Boole observed ways in which human language results in a type of abstraction that can be used to organize and link our experiences to actions.  For example: if it is raining **AND** snowing then bundle up **OR** if it is warm **AND** sunny then go the beach.

**Q.5. When we go to actually implement any sensor, computer, or actuator, what exactly is inside the boxes?  Are there actually black boxes inside a cell?  What “wires” connect one box to another?**

These are challenging questions that we will resolve!

______________________________________________________

##  Preclass for Friday
### Team Project – "I like, I wish, What if" plus "Brainstorming"

Visit the following two resources to prepare for a productive in-class team activity:

First, examine [Brainstorming-Method](https://dschool-old.stanford.edu/sandbox/groups/dstudio/wiki/2fced/attachments/660d8/Brainstorming-Method.pdf?sessionID=d07c198d92501ebb3eee4ff3da193b387130fcbf)

Second, briefly examine [I like, I wish, What if](https://dschool-old.stanford.edu/wp-content/themes/dschool/method-cards/i-like-i-wish-what-if.pdf).  


<sub><sup> [github source code](https://github.com/Stanford-BioE80/Stanford-BioE80.github.io/edit/master/_docs/w4preclass.md) for teaching staff <sub><sup>
