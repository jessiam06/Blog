---
title: Advanced Mechanics
subtitle: Notes from HRK Physics
date: 2026-01-15
description: Lorem ipsum dolor sit amet consectetur adipiscing elit. Consectetur adipiscing elit quisque faucibus ex sapien vitae.
thumbnail:/Assets/nn thumbnail.png
tags: web, static-sites, programming
readtime: 6 min
---
# Work Done
The work done of a force vector $\overrightarrow f$  moving along a displacement vector $\overrightarrow r$ , the Work Done by the force is defined by:

$$W = \overrightarrow f \cdot \overrightarrow r = fr\cos\theta \tag{1}$$ 
where $\theta$ is the angle between the vectors.

**The change in kinetic energy of a body is equal to the work done by the force on the body**

Proof:
Consider a body of mass $m$ moving under the influence of a constant force $f$. By $f = ma$, the acceleration must also be constant. Consider the constant acceleration formula:
$$v^2-u^2 = 2as$$
if we multiply both sides by $\frac{m}{2}$:
$$\frac{1}{2}mv^2 - \frac{1}{2}mu^2 = mas$$
$$\frac{1}{2}mv^2 - \frac{1}{2}mu^2 = fs$$
Thus the change in kinetic energy is equal to the work done by the force on the body.

This theorem is valid for 1D motion with varying force as well
Proof:

$$ m\frac{dv}{dt} = f $$By Multiplying both sides by $v = \frac{dx}{dt}$ 
![[Advanced Mechanics Notes.excalidraw]]
Where $W(x_1 \rightarrow x_2)$  is the work done by the varying force acting on the body during the displacement from $x_1$ to $x_2$. 

# Conservative and Non-conservative Forces

When the work done by a force depends only on the starting and ending positions of the body, the force is said to be **conservative**. 
![[Conservative forves.excalidraw]]
Since $x_3$ is an arbitrary point, it's implied that the work done is determined only by its starting and ending points, and thus are conservative. The **gravitational** and **elastic** forces are examples of this.

The opposite of this is a **non-conservative force**. I.e a force that depends on the path of motion as well as the end points. An example of this is the frictional force. The frictional force is always opposite to the direction of motion. Therefore from (1), the angle between the force and displacement vectors is 180 degrees, and therefore the work done is negative. Following the same process as above, it can be shown that the work done depends on the path travelled.

# Potential Energy

A **potential energy function** can be defined for a conservative force. Consider a body that moves from point $P$ to $O$ under the action of a force $\overrightarrow f$ , then we know that the work done by the force $W(P \rightarrow O)$ is determined by the positions of $P$ and $O$. The **potential energy** possessed by the body at $P$, $U(P)$ is defined as:
$$U(P) = W(P \rightarrow O )$$
This of course depends on teh point O, which is called the **reference point**. 

Since non-conservative forces depend on the path taken, we cannot define a potential energy function in this way for non-conservative forces.

Some examples of Potential Energy:
## Gravitational Potential Energy

We usually choose the **ground** as the reference point for GPE, so that its value at height $h_0$ is equal to the work done by gravity as the body moves from its initial height to the ground.

