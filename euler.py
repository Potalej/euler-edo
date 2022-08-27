def euler (intervalo:tuple, x0:float, v0:float, v_:"function", n:int)->list:
  '''
    Aplica o método de Euler, conforme descrito no README, para aproximar cada
    `x(t_{k+1})` e `v(t_{k+1})`, onde `t_{k+1} ∈ I` e `k=0,1,...,n`.

    Parâmetros
    ----------
    intervalo : tuple
        Tupla `(t_0, t_f)`. 
    x0 : float
        Ponto `x(t_0)`
    v0 : float
        Ponto `v(t_0)`
    v_ : function
        Função v'(x) = F(x)/m 
    n : float
        Quantidade de partições do intervalo.

    Retorna
    ----------
    list
        Uma lista `[X, V]`, onde `X` contém os pontos `t_k` aplicados em `x`
        e `V` contém os pontos `t_k` aplicados em `v`.
  '''
  # separa o intervalo em duas variáveis
  t0, tf = intervalo

  # calcula o fator h
  h = abs(tf - t0) / n

  # lista de pontos xk e vk, iniciados com x0 e v0
  X, V = [x0], [v0]

  # calcula recursivamente os pontos x_{k+1} e v_{k+1} para cada partição
  for i in range(n):
    # captura os pontos anteriores
    xk, vk = X[-1], V[-1]
    
    # calcula conforme o sistema descrito
    xk1 = xk + h*vk
    vk1 = vk + h*v_(xk)

    # salva os pontos
    X.append(xk1)
    V.append(vk1)
  
  return X,V
