---
title: Designing a Minimal Static Site Generator
date: 2026-01-15
description: Lorem ipsum dolor sit amet consectetur adipiscing elit. Consectetur adipiscing elit quisque faucibus ex sapien vitae.
thumbnail:/Assets/nn thumbnail.png
tags: web, static-sites, programming
readtime: 6 min
---
## Introduction

This post is a **test document** designed to exercise the full Markdown → HTML pipeline of a static site generator.

It includes *inline formatting*, block elements, math, code, and tables — the kinds of things a technical blog actually needs.



## Basic Text Formatting

You can write text in **bold**, *italic*, or even ***both at the same time***.

You can also include inline code like `git push -u origin main`, which should be rendered in a monospaced font.

Here’s a link to an external resource:  
[MDN Web Docs](https://developer.mozilla.org)



## Lists

### Unordered list

- Static site generators are fast
- They are secure
- They are easy to deploy
- They scale well for content-heavy sites

### Ordered list

1. Write content in Markdown
2. Parse metadata (frontmatter)
3. Convert Markdown to HTML
4. Apply templates
5. Output static files



## Code Blocks

### JavaScript example

```js
class PostCard {
  constructor(data) {
    this.title = data.title;
    this.date = data.date;
  }

  render() {
    console.log(this.title);
  }
}
```

### Python example

```python
def build_site(posts, templates):
    for post in posts:
        render_post(post, templates)
```

## Mathematics

### Inline math

When working with vectors, the dot product $a \cdot b$ gives a scalar value.

### Block math

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$$
​​

Another common expression:

$$\int_0^1 x^2 \, dx = \frac{1}{3}$$​

(Your generator will likely leave this untouched and let MathJax or KaTeX handle it.)

## Tables

| Feature             | Supported | Notes            |
| ------------------- | --------- | ---------------- |
| Markdown parsing    | ✅         | Core requirement |
| Syntax highlighting | ✅         | Nice to have     |
| Math rendering      | ⚠️        | Needs JS         |
| RSS generation      | ❌         | Future feature   |