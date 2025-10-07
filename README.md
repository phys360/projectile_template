# Projectile Motion

Template for Projectile Motion Project using Agile and Scrum Methodology, see Chapter 1.

A projectile of mass $m$ is launched with speed $v0$ at an angle $\theta$. 

## Functions

`convert_speed(v0,theta)` returns x- and y-components: $v_x$ and $v_y$, where $v_x = v_0 \cos \theta$ and $v_y = v_0 \sin \theta$.

`dvdt(m,g,beta, vx,vy)` returns $a=\frac{dv}{dt}$ as vector with $a_x$ and $a_y$ using: $a_x = -\beta v v_x$ and $a_y = -g - \beta v v_y$

`solver(v0, theta, m, beta, dt)` returns a tuple, time $t$, position $x$ and $y$. Using Euler algorithm.

`plot_theta(v0, theta_vec)` returns a graph with all the projectiles for a list of starting angles
