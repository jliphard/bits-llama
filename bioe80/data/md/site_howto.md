---
title: "Markdown and GitHub"
permalink: /docs/site_howto/
last_modified_at: 2018-11-25T22:21:33-05:00
toc: true
---

### Introduction to Markdown: How to edit files and add new materials

You can use the [editor on GitHub](https://github.com/Stanford-BioE80/Stanford-BioE80.github.io/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown - Basics

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

Here are some examples of what a post with images might look like. If you want to display two or three images next to each other responsively use `figure` with the appropriate `class`. Each instance of `figure` is auto-numbered and displayed in the caption.


### Markdown - Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Stanford-BioE80/Stanford-BioE80.github.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Markdown - Figures (for images or video)

#### One Up

Here is an example of a figure with a caption and links to the sources. Where possible, please use permalinks, or link directly to the source, as opposed to linking to Google searches. 

```html
<figure>
<a href="/assets/images/w1pc_microscope.png"><img src="/assets/images/w1pc_microscope.png"></a>
<figcaption><b>Figure 1</b>. 
<b>Left</b>. Van Leeuwenhoek's simple yet powerful microscope 1670s (arrow points at the lens,  
<a href="http://www.physics.umd.edu/courses/Phys106/rolston/Lectures/Lec28.pdf">History of the microscope</a>). 
<b>Right</b>. An artist etching of a person’s reaction to a magnified drop of Thames water (monster soup), revealing the impurity of London drinking water 1828. <a href="https://wellcomecollection.org/works/qqcx38hr">Source</a>
source.
</figcaption>
</figure>
```

And you'll get something that looks like this:

<figure>
<a href="/assets/images/w1pc_microscope.png"><img src="/assets/images/w1pc_microscope.png"></a>
<figcaption><b>Figure 1</b>. 
<b>Left</b>. Van Leeuwenhoek's simple yet powerful microscope 1670s (arrow points at the lens,  
<a href="http://www.physics.umd.edu/courses/Phys106/rolston/Lectures/Lec28.pdf">History of the microscope</a>). 
<b>Right</b>. An artist etching of a person’s reaction to a magnified drop of Thames water (monster soup), revealing the impurity of London drinking water 1828. <a href="https://wellcomecollection.org/works/qqcx38hr">Source</a>
</figcaption>
</figure>

#### Two Up

Apply the `half` class like so to display two images side by side that share the same caption.

```html
<figure class="half">
    <a href="/assets/images/image-filename-1-large.jpg"><img src="/assets/images/image-filename-1.jpg"></a>
    <a href="/assets/images/image-filename-2-large.jpg"><img src="/assets/images/image-filename-2.jpg"></a>
    <figcaption>Caption describing these two images.</figcaption>
</figure>
```

And you'll get something that looks like this:

<figure class="half">
	<a href="http://placehold.it/1200x600.JPG"><img src="http://placehold.it/600x300.jpg"></a>
	<a href="http://placehold.it/1200x600.jpeg"><img src="http://placehold.it/600x300.jpg"></a>
	<figcaption>Two images.</figcaption>
</figure>

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
