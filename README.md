# euler-edo

Temos um sistema de equações diferenciais da seguinte forma:

$$\cases{ \dot x = v \cr \dot v = \frac{1}{m}F(x) }$$

Seja $t_0$ um ponto inicial dado tal que $x_0 = x(t_0)$ e $v_0 = v(t_0)$. Seja também o intervalo $I = \[t_0, t_f\]$ cuja trajetória que quer obter a partir dos dados iniciais.

Discretizando o intervalo em $n$ partições, obtém-se um fator $h = \frac{| t_f - t_0 |}{n}$, de forma que qualquer $t_{k+1} \in I$, com $k = 0, 1, ..., n$, é da forma $t_{k+1} = t_k + h$.

Expadindo $x$ via Taylor a partir de um ponto $t_{k}$ para encontrar um ponto $t_{k+1}$, tem-se:

$$
x(t_{k+1}) = t_k + \dot x(t_k)(t_{k+1}-t_k) + O(h^2)
$$

e como $t_{k+1} = t_k + h$, é possível substituir:

$$
x(t_{k+1}) = t_k + \dot x(t_k)(t_k + h - t_k) + O(h^2) = t_k + h \dot x(t_k) + O(h^2) = t_k + h v(t_k) + O(h^2)
$$

Abrindo mão do erro e definindo

$$
x(t_{k+1}) \approx x_{k+1} = x_k + h v_k
$$

Analogamente para o $v$:

$$
v_{k+1} = v_k + \dfrac{h}{m}F(x_k)
$$

Então, para qualquer $t_{k+1}$, com $k=0,...,n$, se obtém a aproximação de $x(t_{k+1}$ e $v(t_{k+1})$ de forma recursiva:

$$
\begin{equation}
  \begin{cases}
    x_{k+1} = x_k + h v_k \\
    v_{k+1} = v_k + \frac{h}{m}F(x_k)
  \end{cases}
\end{equation}
$$
