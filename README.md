- [BITS, a digital TA](#bits--a-digital-ta)
  * [What's the point of Tuning?](#what-s-the-point-of-tuning-)
  * [Technical Overview](#technical-overview)
  * [Usage](#usage)
  * [Methods](#methods)
  * [Unedited Question/Answer Pairs](#unedited-question-answer-pairs)
  * [Conversation example - unedited/raw output](#conversation-example---unedited-raw-output)
  * [Main impressions](#main-impressions)


# BITS: A rapidly tunable digital TA using Retrieval augmented generation (RAG)

BITS is a digital TA built on OpenAI's GPT-3.5, `llama_index`, and `langchain`. 

The central premise that chatbots trained on a generic, fixed corpus leave much to be desired - see the problematic example below. Answers are either vague/general or the LLMs can hallucinate. In consequence, educators need a way to take materials specific to _their_ course, which reflect their unique point of view, and use that information to improve the answers from the models. 

Augmentation/tuning is not just about creating course-specific digital TAs, but also being able to respond to newly apparent student needs by adding additional materials to the LLM's context. BITS can be improved within a few minutes to provide better answers to common questions.

A desire for course-specific digital TAs is also shared by the students, since they generally care less about what Wikipedia says and more about what their instructors think (hopefully, at least).      

## What's the point of Augmentation?

Consider GPT-3.5's (initial) answer to a simple question:

*INPUT: (Human) How can I synthesize DNA?*

_AgentExecutor> To synthesize DNA, you can use a four-key keyboard to input raw chemicals that are not derived from existing DNA. You can then play with the chemicals to get the desired DNA sequence. Additionally, you can optimize synthetic chemistry for accuracy to ensure that the DNA sequence is correct._

If you know anything about DNA, this is really funny but about as wrong as it could be. However, after tuning on BioE80 course materials, we end up with a useful, clear, and technically correct answer: 

*INPUT: (Human) How can I synthesize DNA?*

_AgentExecutor-Tuned> DNA can be synthesized by first designing the sequence, then synthesizing oligonucleotides (oligos) from the sequence, and finally assembling the oligos into double-stranded DNA (dsDNA) fragments. This process is known as artificial DNA synthesis and is a fundamental tool of synthetic biology. The oligos are synthesized using a process called phosphoramidite-based oligo synthesis, which involves building the oligo chain on a solid support through cycles of chemical reactions. The dsDNA fragments are then assembled using polymerase cycling assembly._

## Technical Overview

BITS uses [llama_index](https://github.com/jerryjliu/llama_index), a toolkit for augmenting LLMs with "private" data. Llama_index uses Retrieval augmented generation (RAG); in this approach, data are indexed to generate a *knowledge base*. When the user generates a query, RAG pipeline retrieves the most relevant context for that query from knowledge base, and passes that context to the LLM (along with the query) to synthesize a response. The LLM has up-to-date knowledge that is generally not in its original training data and is less likely to hallucinate.

The practical heart of the system is the `data` folder, which contains lecture notes, lecture transcriptions, papers, and other course materials. `llama_index` is used to create an index (the knowledge base) from your course data (e.g. lecture notes in `.txt` format), 

```python
required_exts = [".md", ".pdf", ".txt"]
reader = SimpleDirectoryReader(input_dir="./data", required_exts=required_exts, recursive=True)
documents = reader.load_data()
index = VectorStoreIndex.from_documents(documents)
```

When interacting with ChatGPT, the custom tool can be provided to the LLM, yielding course specific knowledge-augmented outputs:

```python
tool = Tool(
        name="BITS",
        func=lambda q: str(index.as_query_engine().query(q)),
        description="useful for when you want to answer questions about BioE80. The input to this tool should be a complete english sentence.",
        return_direct=True,
    )

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, memory=memory, verbose=True)
```

The agent can then be queried: 

```python
agent.run("Summarize the BioE80 course") #simplfied pseudocode
```

*[tool/start] [1:chain:AgentExecutor > 4:tool:BITS] Entering Tool run with input:
"Please summarize the BioE80 course"*

_[tool/end] [1:chain:AgentExecutor > 4:tool:BITS] [3.01s] Exiting Tool run with output:
"BioE80 is an Introduction to Bioengineering (Engineering Living Matter) course that aims to help students learn ways of thinking about engineering living matter, empower them to explore and do bioengineering starting from DNA, and become more capable of learning and explaining bioengineering to themselves and others. Additionally, the course seeks to enable students to devise and express their wishes for bioengineering as might be made true by or before 2030, and to develop practical plans for making their wishes real."_

This repo contains as an example the course materials for BioE80, Stanford's flagship "Introduction to Bioengineering" class, but nothing in the code is specific to BioE80. The repo also contains various helper functions, such as code to download lecture videos from YouTube and then transcribe them with OpenAI's `Whisper`. 

## Usage

Install the following:

```shell
% pip3 install llama_index
% pip3 install torch transformers sentencepiece Pillow
% pip3 install pypdf pytube pydub
% pip3 install langchain streamlit watchdog
% pip3 install np pd # you probably have these anyway

% brew install ffmpeg
```

Provide an OpenAI access token:

```shell
% export OPENAI_API_KEY=sk-.....
```

Populate the `PROJECT/data` folder with your data. For example, to download the audio for all BioE lectures from [BioE lectures-interviews](https://introbioe.stanford.edu/lectures-interviews), run

```shell
% python3 1_download_audio.py --path ./bioe80
```

Some of these files will be too big for `OpenAI Whisper` to transcribe, so:

```shell
% python3 2_segment_audio.py --path ./bioe80 
```

Then, transcribe the audio:

```shell
% python3 3_transcribe.py --path ./bioe80
```

Finally, run the indexer, if you have added new data or if this is the first time you are running the system:

```shell
% python3 4_create_index.py --path ./bioe80

Generating new index
Loaded 964 docs. Please be patient...
```

Now, try it out....

```shell
% python3 5_query.py --path ./bioe80
```

## Streamlit UI

Streamlit handle the UI:

```shell
streamlit run bits_chat.py
```

## Jupyter notebook (BITS.ipynb)

Jupyter can be used to quickly try out 

```shell
jupyter notebook
```


## Methods

Downloaded all of [Stanford-BioE80.github.io](https://github.com/Stanford-BioE80/Stanford-BioE80.github.io) and [introbioe.stanford.edu](https://introbioe.stanford.edu). Indexed all `.md`, `.txt`, and `.pdf` files. Generated an index following the above instuctions. 

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

*How can I synthesize DNA? [BAD answer before Tuning]*

To synthesize DNA, you can use a four-key keyboard to input raw chemicals that are not derived from existing DNA. You can then play with the chemicals to get the desired DNA sequence. Additionally, you can optimize synthetic chemistry for accuracy to ensure that the DNA sequence is correct.

*How can I synthesize DNA? [GOOD answer after Tuning]*

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
