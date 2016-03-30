import parse as par
import mdpmodel as mod
import mdpsolve as sol

#make results class

# takes 3d list of observations & reward list(if step-wise rewards not included in observations)
#[obs,gamma, max_iter, verbose, eps]
def learn(obs,gamma=1,max_iter=1000,verbose=True,eps=1e-3):
  obs_ = obs
  parsed = par.parse(obs_)

  stateMap = parsed[0]
  actMap = parsed[1]
  obs = parsed[2]
  model = mod.model(len(stateMap),len(actMap),obs)

  P = model[0]
  R = model[1]
  policy = sol.policy(P,gamma,R,max_iter,verbose,eps)
  print actMap
  print policy
  print stateMap
  #map integer policy and action back to
  strat = {}
  for i in range(0,len(policy)):
    strat[stateMap[i]] = actMap[policy[i]]

  #return strategy
  return strat
