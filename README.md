- [BITS, a digital TA](#bits--a-digital-ta)
  * [What's the point of Tuning?](#what-s-the-point-of-tuning-)
  * [Technical Overview](#technical-overview)
  * [Usage](#usage)
  * [Methods](#methods)
  * [Unedited Question/Answer Pairs](#unedited-question-answer-pairs)
  * [Conversation example - unedited/raw output](#conversation-example---unedited-raw-output)
  * [Main impressions](#main-impressions)

# BITS: A rapidly re-tunable digital TA

BITS is a digital TA built on OpenAI's ChatGPT-3.5, `llama_index`, and `langchain`. 

The central premise is that educators seek great learning tools for their students but that educational chatbots trained on a generic, fixed corpus miss the mark. Rather, many educators wish to take materials specific to _their_ course, and which their reflect their unique point of view, and use that information to fine-tune the responses for their students. Tuning is not just about creating course-specific digital TAs, but also being able to respond to student needs/questions by quickly adding responsive materials to the tuning set, enabling BITs to within minutes provide great answers to common questions.

A desire for course-specific digital TAs is also shared by the students, since they generally care less about what Wikipedia says and more about what their instructors think (hopefully, at least).      

## What's the point of Tuning?

Consider ChatGPT's (initial) answer to simple question:

```text
INPUT: (Human) How can I synthesize DNA?

AgentExecutor> 

To synthesize DNA, you can use a four-key keyboard to input raw chemicals that 
are not derived from existing DNA. You can then play with the chemicals to get 
the desired DNA sequence. Additionally, you can optimize synthetic chemistry 
for accuracy to ensure that the DNA sequence is correct.
```

If you know anything about DNA, this is really funny but about as wrong as it could be. After tuning on Bioe80 course materials, 

```text
INPUT: (Human) How can I synthesize DNA?

AgentExecutor-Tuned> 

DNA can be synthesized by first designing the sequence, then synthesizing 
oligonucleotides (oligos) from the sequence, and finally assembling the oligos 
into double-stranded DNA (dsDNA) fragments. This process is known as artificial 
DNA synthesis and is a fundamental tool of synthetic biology. The oligos are 
synthesized using a process called phosphoramidite-based oligo synthesis, which 
involves building the oligo chain on a solid support through cycles of chemical 
reactions. The dsDNA fragments are then assembled using polymerase cycling 
assembly.
```

we end up with a useful, clear, and entirely correct answer. 

## Technical Overview

BITS uses [llama_index](https://github.com/jerryjliu/llama_index), a toolkit for augmenting LLMs with "private" data. Llama_index is used to structure your course data (e.g. lecture notes in `.txt` format to `indices`). The structured data can then be combined with an LLM input prompt, yielding knowledge-augmented outputs from generic LLMs such as GhatGPT-3.5.

The practical heart of the system is the `data` folder, which contains lecture notes, lecture transcriptions, papers, and other course materials. 

This repo contains as an example the course materials for BioE80, Stanford's flagship "Introduction to Bioengineering" class, but nothing in the code is specific to BioE80. 

The repo also contains various helper functions, such as code to download lecture videos from YouTube and then transcribe them with OpenAI's `Whisper`. 

The tuning data are used to create an `index`:

```python
required_exts = [".md", ".pdf", ".txt"]
reader = SimpleDirectoryReader(input_dir="./data", required_exts=required_exts, recursive=True)
```

The `index` can then be used directly as an input to ChatGPT. `llama_index` will handle the details in the background:

```python
query_engine = index.as_query_engine()
response = query_engine.query("What's the best way to synthesize DNA?")
print(response)
```

To build `BITS`, the chatbot, we define a `LlamaIndex tool`:

```python
tools = [
    Tool(
        name="LlamaIndex",
        func=lambda q: str(index.as_query_engine().query(q)),
        description="useful for when you want to answer questions about your class. The input to this tool should be a complete english sentence.",
        return_direct=True,
    ),
]
```

and use the tool and LLM to instantiate a `langchain` agent:

```python
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent

memory = ConversationBufferMemory(memory_key="chat_history")
llm = ChatOpenAI(temperature=0, max_tokens=512, model_name="gpt-3.5-turbo")
agent_executor = initialize_agent(
	tools, 
	llm, 
	agent="conversational-react-description", 
	memory=memory, 
	verbose=True)
```

This agent then responds to course-focused questions with tuned responses:

```shell
[tool/start] [1:chain:AgentExecutor > 4:tool:LlamaIndex] Entering Tool run with input:
"Please summarize the BioE80 course"
[tool/end] [1:chain:AgentExecutor > 4:tool:LlamaIndex] [3.01s] Exiting Tool run with output:
"BioE80 is an Introduction to Bioengineering (Engineering Living Matter) course that aims to help students learn ways of thinking about engineering living matter, empower them to explore and do bioengineering starting from DNA, and become more capable of learning and explaining bioengineering to themselves and others. Additionally, the course seeks to enable students to devise and express their wishes for bioengineering as might be made true by or before 2030, and to develop practical plans for making their wishes real."
```

## Usage

Install the following:

```shell
% pip3 install llama_index
% pip3 install torch transformers sentencepiece Pillow
% pip3 install pypdf
% pip3 install pytube
% pip3 install pydub
% brew install ffmpeg // assuming you are on Mac silicon, which everyone is...
```

Provide an OpenAI access token:

```shell
% export OPENAI_API_KEY=sk-.....
```

Populate the `/data` folder with your tuning data. For example, to download the audio for all BioE lectures from [BioE lectures-interviews](https://introbioe.stanford.edu/lectures-interviews), run

```shell
% python3 download_audio.py 
```

Some of these files will be too big for `OpenAI Whisper` to transcribe, so:

```shell
% python3 segment_audio.py 
```

Then, transcribe the audio:

```shell
% python3 transcribe.py 
```

Finally, run the indexer, if you have added new tuning data or if this is the first time you are running the system:

```shell
% cd bioe80
% python3 create_index.py

Generating new index
Loaded 964 docs. Please be patient...
```

Now, try it out....

```shell
% python3 query.py
```

## Methods

Downloaded all of [Stanford-BioE80.github.io](https://github.com/Stanford-BioE80/Stanford-BioE80.github.io)

Downloaded all of [introbioe.stanford.edu](https://introbioe.stanford.edu)

Indexed all `.md`, `.txt`, and `.pdf` files

## Unedited Question/Answer Pairs

These were not human-edited - this is raw output from the model.

*What is the goal of BioE80?*

The goal of BioE80 is to help students learn ways of thinking about engineering living matter, empower them to explore and do bioengineering starting from DNA, become more capable of learning and explaining bioengineering to themselves and others, and devise and express their wishes for bioengineering as might be made true by or before 2030, with the ultimate aim of benefiting all people and the planet.

*Help me to understand abstraction*

Abstraction is a way of simplifying complex systems by breaking them down into smaller, more manageable parts. It is a way of organizing information and ideas into categories and levels, allowing us to focus on the most important aspects of a system. Abstraction can be used to identify patterns and relationships between different parts of a system, and to make it easier to understand how the system works. Abstraction can also be used to create models of systems, which can be used to make predictions about how the system will behave in different situations.

*What is living matter?*

Living matter is any material composed of cells that are capable of growth, metabolism, response to stimuli, and reproduction. Living matter is distinguished from inert matter by its ability to self-organize, adapt, and evolve. Living matter is composed of complex molecules and structures that are organized on many orders of magnitude, from nanometers to meters. Living matter is capable of performing complex functions, such as sensing, responding, and self-repairing.

*Can living matter self-organize?*

Yes, living matter can self-organize. This is evidenced by the fact that living matter is intricately organized on multiple time and spatial scales, and is capable of self-mixing, self-healing, and self-replicating.

*How can I synthesize DNA? [BAD ANSWER before Tuning]*

To synthesize DNA, you can use a four-key keyboard to input raw chemicals that are not derived from existing DNA. You can then play with the chemicals to get the desired DNA sequence. Additionally, you can optimize synthetic chemistry for accuracy to ensure that the DNA sequence is correct.

*How can I synthesize DNA? [after Tuning]*

DNA can be synthesized by first designing the sequence, then synthesizing oligonucleotides (oligos) from the sequence, and finally assembling the oligos into double-stranded DNA (dsDNA) fragments. This process is known as artificial DNA synthesis and is a fundamental tool of synthetic biology. The oligos are synthesized using a process called phosphoramidite-based oligo synthesis, which involves building the oligo chain on a solid support through cycles of chemical reactions. The dsDNA fragments are then assembled using polymerase cycling assembly.

*Bioengineers will...*

One example of an impact of bioengineering today is the development of gene therapy. Gene therapy is a technique used to treat genetic diseases by introducing a gene into a person's cells to replace a mutated gene. This technique has been used to treat diseases such as cystic fibrosis, muscular dystrophy, and hemophilia. It has also been used to treat cancer, HIV, and other diseases. References: https://www.genome.gov/genetics-glossary/Gene-Therapy, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6111790/, https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/gene-therapy.

In the future, I wish to realize a world where bioengineering is used to improve the quality of life for all people. Bioengineering should be used to develop treatments and cures for diseases, create sustainable food sources, and develop renewable energy sources. Success would be defined as a world where everyone has access to the treatments and cures they need, where food is plentiful and sustainable, and where renewable energy sources are widely available. To realize this future, we need to focus on developing new technologies, such as gene editing, that can be used to create treatments and cures for diseases. We also need to focus on developing sustainable food sources and renewable energy sources. Finally, we need to create policies that ensure that everyone has access to the treatments and cures they need.

## Conversation example - unedited/raw output

*What's the best way to synthesize DNA?*

The best way to synthesize DNA is to use a combination of oligonucleotide synthesis and assembly techniques. Oligonucleotides can be synthesized using phosphoramidate chemistry, and then assembled into larger DNA fragments using overlap extension PCR. This method allows for the synthesis of DNA fragments up to 100 or 50 bases in length with high fidelity. However, it is not suitable for synthesizing repeated sequences. To overcome this limitation, it is possible to use templated DNA synthesis with a polymerase to fill in the gaps between the short synthesized regions. Additionally, the cost of DNA synthesis and sequencing is decreasing rapidly due to Moore's law, making it more accessible to researchers.

*Can you explain more about oligo assembly*

Oligo assembly is a process of joining short synthetic DNA fragments together to form longer DNA strands. This is done by using enzymes to join the fragments together in a specific order. The process is often used to create custom DNA strands for research or other applications. The process can be done manually or with automated systems. Automated systems are often used to increase the speed and accuracy of the assembly process.

## Main impressions

Training on the ~1000 RAW documents took 3 mins on my laptop. Some answers are great and some are _initially_ crazy/dumb (see e.g. "How can I synthesize DNA?[BAD ANSWER before Tuning]") and can be improved withing a few seconds by adding material relevant to the question (see e.g. "How can I synthesize DNA?[after Tuning]"). Tuning with relevant material immediately helps. The system does best when there is training material that is similar to the question/prompt. The system does best when trained with essays and question/answer pairs.
